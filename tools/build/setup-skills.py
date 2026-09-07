#!/usr/bin/env python3
"""Transactional PBAW installer: project a v6 flat source onto one project root.

The source is one directory carrying `runtime-manifest.json` (the graph) plus the files it
names. The projection is: every non-build-only entry -> `.pbaw/<path>`; the four harness
overlays -> `.claude/skills/<op>` and `.agents/skills/<op>` (ownership markers on both hosts);
the product rules -> `.claude/rules/<name>` and `rules/reference/*` -> `.claude/rules-reference/`
(managed files listed in one marker; everything else in those folders is unmanaged and never
touched). The installed manifest carries opaque ids; `.pbaw/install-manifest.json` is the
install ledger; `.pbaw/sync-receipt.json` is the persisted pre/post receipt.
"""
from __future__ import annotations
import argparse, hashlib, json, os, shutil, sys, tempfile
from datetime import datetime
from pathlib import Path, PurePosixPath

OPS=frozenset({"audit","context-harvest","pbaw","plan"})
MARKER=".pbaw-managed.json"; GEN="setup-skills.py"; JOURNAL=".setup-skills-journal.json"
RUNTIME_DIRS=("agents","skills","knowledge","rules","tools","harness")
CLASS_ROOT={"agent":"agents","capability":"skills","team-route":"skills","knowledge":"knowledge","rule":"rules","tool":"tools"}
RUNTIME_MANIFEST="runtime-manifest.json"; LEDGER="install-manifest.json"; RECEIPT="sync-receipt.json"
HOSTS=(".claude/skills",".agents/skills",".claude/rules",".claude/rules-reference")
LEGACY_SCHEMA="pbaw-legacy-managed/v1"; LEDGER_SCHEMA=3

class WorkspaceConfig:
    def __init__(self, base_dir: Path, legacy_allowlist: frozenset[str]=frozenset(), source: Path|None=None,
                 legacy_managed: dict|None=None):
        self.base_dir=Path(base_dir).resolve()
        self.legacy_allowlist=frozenset(legacy_allowlist)
        self.source=Path(source).resolve() if source else self.p()
        declared=dict(legacy_managed or {})
        if set(declared)-set(HOSTS): raise ValueError("legacy_managed names an unknown host")
        self.legacy_managed={h:frozenset(declared.get(h,())) for h in HOSTS}
        for names in self.legacy_managed.values():
            for n in names:
                if not n or "/" in n or "\\" in n or n in (".",".."): raise ValueError("unsafe legacy_managed name "+n)
    def p(self,*parts): return self.base_dir.joinpath(*parts)
    @property
    def claude_skills(self): return self.p(".claude","skills")
    @property
    def codex_skills(self): return self.p(".agents","skills")
    @property
    def rules(self): return self.p(".claude","rules")
    @property
    def rules_reference(self): return self.p(".claude","rules-reference")
    @property
    def pbaw(self): return self.p(".pbaw")
    @property
    def manifest(self): return self.pbaw/LEDGER
    @property
    def runtime_manifest(self): return self.pbaw/RUNTIME_MANIFEST
    @property
    def receipt(self): return self.pbaw/RECEIPT
    @property
    def journal(self): return self.claude_skills/JOURNAL
    def host(self,key): return self.p(*key.split("/"))

def _hash(path,skip_marker=False,skip=()):
    d=hashlib.sha256()
    if not path.exists(): return "<absent>"
    for p in sorted(x for x in path.rglob("*") if x.is_file()):
        if (skip_marker and p.name==MARKER) or p.relative_to(path).as_posix() in skip: continue
        d.update(p.relative_to(path).as_posix().encode()); d.update(bytes([0]))
        d.update(hashlib.sha256(p.read_bytes()).digest())
    return d.hexdigest()
def _sha(data): return hashlib.sha256(data).hexdigest()
def _jb(v): return (json.dumps(v,indent=2,sort_keys=True,ensure_ascii=False)+"\n").encode()
def _write(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("wb") as f: f.write(data); f.flush(); os.fsync(f.fileno())
def _fault(got,want):
    if got==want: raise RuntimeError("injected failure at "+want)
def _is_reparse(path):
    return path.is_symlink() or bool(getattr(path,"is_junction",lambda:False)())
def _opaque(target_id):
    if len(target_id)==16 and all(ch in "0123456789abcdef" for ch in target_id): return target_id
    return hashlib.sha256(target_id.encode()).hexdigest()[:16]
def _safe_rel(rel):
    posix=PurePosixPath(rel.replace("\\","/"))
    if posix.is_absolute() or not posix.parts or any(p in ("..",".","") for p in posix.parts) or ":" in rel:
        raise ValueError("unsafe manifest path "+rel)
    return posix

def _read_manifest(c):
    try: text=c.source.joinpath(RUNTIME_MANIFEST).read_text(encoding="utf-8")
    except FileNotFoundError as e: raise ValueError("runtime manifest is absent: "+str(c.source)) from e
    except UnicodeDecodeError as e: raise ValueError("runtime manifest is not UTF-8") from e
    try: m=json.loads(text)
    except json.JSONDecodeError as e: raise ValueError("runtime manifest is malformed JSON") from e
    if not isinstance(m,dict) or not isinstance(m.get("entries"),list) or not isinstance(m.get("overlays",[]),list):
        raise ValueError("runtime manifest shape")
    for row in m["entries"]+m.get("overlays",[]):
        if not isinstance(row,dict) or not all(isinstance(row.get(k),str) and row.get(k) for k in ("target_id","path","sha256")):
            raise ValueError("manifest row lacks id/path/digest")
        for k in ("requires","optional"):
            if not isinstance(row.get(k,[]),list) or not all(isinstance(x,str) and x for x in row.get(k,[])):
                raise ValueError("manifest row has malformed edges: "+row["path"])
    return m

def installed_manifest(m):
    """The installed shape shared by every install (OD-7.5-1): build-only rows dropped, the
    harness overlays kept, ids opaque (`sha256(id)[:16]`). Returns (installed, id_map, dropped)."""
    dropped={r["target_id"] for r in m["entries"] if r.get("conveyance")=="build-only"}
    keep=[r for r in m["entries"] if r.get("conveyance")!="build-only"]
    overlays=[r for r in m.get("overlays",[]) if r.get("overlay_class")=="harness"]
    ids={r["target_id"] for r in keep+overlays}
    id_map={t:_opaque(t) for t in sorted(ids|dropped)}
    if len({id_map[t] for t in ids})!=len(ids): raise ValueError("opaque id collision")
    warnings=[]
    def row(r,extra):
        for e in r.get("requires",[]):
            if e in dropped: raise ValueError("required edge to a build-only row: "+r["path"]+" -> "+e)
            if e not in ids: raise ValueError("unresolved required dependency "+r["path"]+" -> "+e)
        optional=[]
        for e in r.get("optional",[]):
            if e in ids: optional.append(id_map[e])
            else: warnings.append("optional dependency unresolved "+r["path"]+" -> "+e)
        out={"target_id":id_map[r["target_id"]],"path":r["path"],"distribution":r.get("distribution"),
             "sha256":r["sha256"],"source_sha256":r.get("source_sha256"),
             "requires":sorted(id_map[e] for e in r.get("requires",[])),"optional":sorted(optional)}
        out.update(extra(r)); return out
    entries=[row(r,lambda r:{"resource_class":r.get("resource_class"),**({"conveyance":r["conveyance"]} if r.get("conveyance") else {})}) for r in keep]
    harness=[row(r,lambda r:{"overlay_class":"harness"}) for r in overlays]
    installed={"schema":m.get("schema"),"loader":m.get("loader"),"discovery_order":m.get("discovery_order",[".pbaw/"+RUNTIME_MANIFEST]),
               "id_scheme":"sha256(target_id)[:16]","entries":sorted(entries,key=lambda r:r["path"]),
               "overlays":sorted(harness,key=lambda r:r["path"]),"warnings":sorted(warnings)}
    return installed,{t:o for t,o in id_map.items() if t!=o},sorted(dropped)

def _sources(c):
    """Validate the source against its manifest; nothing is written. Returns the projection."""
    if not c.source.is_dir(): raise ValueError("source root is absent: "+str(c.source))
    m=_read_manifest(c); installed,id_map,dropped=installed_manifest(m)
    runtime={}; fold={}
    for r in m["entries"]:
        if r.get("conveyance")=="build-only": continue
        posix=_safe_rel(r["path"]); rel=posix.as_posix()
        root=CLASS_ROOT.get(r.get("resource_class"))
        if root is None: raise ValueError("unknown resource class: "+rel)
        if posix.parts[0]!=root: raise ValueError("resource class/path mismatch: "+rel)
        if rel.casefold() in fold: raise ValueError("duplicate destination "+rel)
        fold[rel.casefold()]=rel
        src=c.source.joinpath(*posix.parts)
        if not src.is_file(): raise ValueError("source file is absent: "+rel)
        data=src.read_bytes()
        if _sha(data)!=r["sha256"]: raise ValueError("source digest mismatch: "+rel)
        runtime[rel]=data
    harness={}
    for r in m.get("overlays",[]):
        if r.get("overlay_class")!="harness": continue
        posix=_safe_rel(r["path"])
        if len(posix.parts)!=3 or posix.parts[0]!="harness" or posix.parts[1] not in OPS: raise ValueError("operator source mismatch")
        src=c.source.joinpath(*posix.parts)
        if not src.is_file(): raise ValueError("source file is absent: "+r["path"])
        data=src.read_bytes()
        if _sha(data)!=r["sha256"]: raise ValueError("source digest mismatch: "+r["path"])
        harness.setdefault(posix.parts[1],{})[posix.parts[2]]=data
    if set(harness)!=OPS or any("SKILL.md" not in files for files in harness.values()): raise ValueError("operator source mismatch")
    rules={}; reference={}
    for rel,data in runtime.items():
        parts=PurePosixPath(rel).parts
        if parts[0]!="rules" or not rel.endswith(".md"): continue
        if len(parts)==2: rules[parts[1]]=data
        elif len(parts)==3 and parts[1]=="reference": reference[parts[2]]=data
    for name in list(rules)+list(reference):
        if name.casefold() in {MARKER.casefold()}: raise ValueError("rule name collides with the marker")
    return {"manifest":m,"installed":installed,"id_map":id_map,"dropped":dropped,"runtime":runtime,"harness":harness,
            "rules":rules,"reference":reference,"manifest_sha256":_sha(c.source.joinpath(RUNTIME_MANIFEST).read_bytes())}

def build_runtime_manifest(c):
    """Validate the source and return the installed manifest without mutating the workspace."""
    return _sources(c)["installed"]

def _legacy(c):
    if not c.claude_skills.exists(): return []
    a=sorted(x for x in c.claude_skills.iterdir() if x.is_dir() and x.name.startswith("pmtk-")); names=[x.name for x in a]
    if len({x.casefold() for x in names})!=len(names) or not set(names).issubset(set(c.legacy_allowlist)): raise ValueError("legacy allowlist mismatch")
    for p in a:
        if p.resolve().parent!=c.claude_skills.resolve() or p.is_symlink() or bool(getattr(p,"is_junction",lambda:False)()): raise ValueError("unsafe legacy target")
    return a
def _marker(path):
    if _is_reparse(path): raise ValueError("destination is a reparse point: "+path.name)
    p=path/MARKER
    if not p.exists(): return None
    try: v=json.loads(p.read_text(encoding="utf-8"))
    except Exception as e: raise ValueError("malformed marker") from e
    if v.get("generator")!=GEN or v.get("source")!="shell" or not isinstance(v.get("content_hash"),str): raise ValueError("forged marker")
    if v["content_hash"]!=_hash(path,True): raise ValueError("managed marker content hash mismatch")
    return v
def _files_marker(root):
    p=root/MARKER
    if not root.exists() or not p.exists(): return {}
    if _is_reparse(root): raise ValueError("destination is a reparse point: "+root.name)
    try: v=json.loads(p.read_text(encoding="utf-8"))
    except Exception as e: raise ValueError("malformed marker") from e
    if v.get("generator")!=GEN or v.get("source")!="shell" or v.get("kind")!="files" or not isinstance(v.get("files"),dict): raise ValueError("forged marker")
    for name,digest in v["files"].items():
        f=root/name
        if "/" in name or "\\" in name or not f.is_file() or _sha(f.read_bytes())!=digest: raise ValueError("managed marker content hash mismatch: "+name)
    return v["files"]

def _classify_dirs(c,key):
    """One host root: (managed marked dirs, declared-legacy dirs, unmanaged names). Refuses an
    unmarked, undeclared collision on a harness name; never reads inside an unmanaged reparse dir."""
    root=c.host(key); managed={}; legacy=[]; unmanaged={}
    if not root.exists(): return managed,legacy,unmanaged
    if _is_reparse(root): raise ValueError("host root is a reparse point: "+key)
    dirs=sorted(x for x in root.iterdir() if x.is_dir()); fold={}
    for d in dirs:
        if d.name.casefold() in fold: raise ValueError("deployed case collision "+fold[d.name.casefold()]+" / "+d.name)
        fold[d.name.casefold()]=d.name
    for d in dirs:
        if d.name.startswith("pmtk-") and key==".claude/skills": continue
        declared=d.name in c.legacy_managed[key]
        if _is_reparse(d):
            if d.name in OPS or declared: raise ValueError("destination is a reparse point: "+d.name)
            unmanaged[d.name]=d; continue
        if _marker(d): managed[d.name]=d
        elif declared: legacy.append(d)
        elif d.name in OPS: raise ValueError("unmanaged destination collision "+key+"/"+d.name)
        else: unmanaged[d.name]=d
    return managed,legacy,unmanaged
def _classify_files(c,key,product):
    root=c.host(key); managed=_files_marker(root); legacy=[]; unmanaged={}
    if root.exists():
        for f in sorted(x for x in root.iterdir() if x.is_file() and x.name!=MARKER):
            if f.name in managed: continue
            if f.name in c.legacy_managed[key]: legacy.append(f.name)
            elif f.name in product: raise ValueError("unmanaged rule collision "+key+"/"+f.name)
            else: unmanaged[f.name]=f
    return managed,legacy,unmanaged

def recover_incomplete_transaction(c):
    if not c.journal.exists(): return
    try: j=json.loads(c.journal.read_text(encoding="utf-8"))
    except Exception as e: raise RuntimeError("journal unreadable; restore backups") from e
    ops=j.get("operations")
    if not isinstance(ops,list) or any("target" not in x for x in ops): raise RuntimeError("journal lacks recovery paths; restore backups")
    for op in reversed(ops):
        target=Path(op["target"]); backup=Path(op["backup"]) if op.get("backup") else None
        if backup and backup.exists():
            if target.exists(): shutil.rmtree(target) if target.is_dir() else target.unlink()
            backup.rename(target)
        elif target.exists() and (op.get("applied") or (op.get("staged") and not Path(op["staged"]).exists())):
            shutil.rmtree(target) if target.is_dir() else target.unlink()
    c.journal.unlink(missing_ok=True)

def _snapshot(c,unmanaged):
    snap={"hosts":{},"pbaw_tree_sha256":_hash(c.pbaw,skip=(RECEIPT,)),"context_tree_sha256":_hash(c.p("context"))}
    for key in HOSTS:
        root=c.host(key); items=sorted(x.name for x in root.iterdir()) if root.is_dir() else []
        snap["hosts"][key]={"tree_sha256":_hash(root),"listing":items,
                            "unmanaged":{n:(_hash(p) if p.is_dir() else _sha(p.read_bytes())) for n,p in sorted(unmanaged.get(key,{}).items())}}
    return snap

def sync_workspace(c,*,fail_at=None,preview=False,backup_to=None):
    if c.journal.exists(): recover_incomplete_transaction(c)
    s=_sources(c); legacy=_legacy(c)
    if c.pbaw.exists() and (not c.pbaw.is_dir() or _is_reparse(c.pbaw)): raise ValueError("runtime destination is a reparse point")
    dirs={key:_classify_dirs(c,key) for key in (".claude/skills",".agents/skills")}
    files={".claude/rules":_classify_files(c,".claude/rules",set(s["rules"])),
           ".claude/rules-reference":_classify_files(c,".claude/rules-reference",set(s["reference"]))}
    unmanaged={key:dirs[key][2] for key in dirs}; unmanaged.update({key:files[key][2] for key in files})
    backup_root=Path(backup_to).resolve() if backup_to else None
    if backup_root is not None and backup_root.exists(): raise ValueError("--backup-to must name an absent directory")
    pre=_snapshot(c,unmanaged); created_roots=[r for r in (c.pbaw,c.claude_skills,c.codex_skills,c.rules,c.rules_reference) if not r.exists()]
    staging_root=c.p(".setup-skills-staging")
    if staging_root.exists() and (not staging_root.is_dir() or _is_reparse(staging_root)):
        raise ValueError("unsafe workspace staging root")
    staging_root.mkdir(parents=False,exist_ok=True)
    if staging_root.resolve().parent!=c.base_dir.resolve(): raise ValueError("staging root containment failure")
    stage=Path(tempfile.mkdtemp(prefix="setup-skills-stage-",dir=staging_root))
    rb=Path(tempfile.mkdtemp(prefix="setup-skills-rollback-",dir=staging_root))
    operations=[]; report={"copied":0,"updated":0,"deleted":0}; ledger_tmp=None; manifest_tmp=None
    try:
        # ---- staging: everything is materialised before any live byte moves ----
        for rel,data in sorted(s["runtime"].items()): _write(stage/"pbaw"/PurePosixPath(rel),data)
        for op,files_ in sorted(s["harness"].items()):  # the canonical harness copy lives in .pbaw too; the hosts get projections
            for name,data in sorted(files_.items()): _write(stage/"pbaw"/"harness"/op/name,data)
        _fault(fail_at,"staging-copy")
        hosts={}
        for key in (".claude/skills",".agents/skills"):
            for op in sorted(OPS):
                d=stage/"hosts"/key.replace("/","_")/op
                for name,data in sorted(s["harness"][op].items()): _write(d/name,data)
                _write(d/MARKER,_jb({"generator":GEN,"source":"shell","content_hash":_hash(d,True)})); _fault(fail_at,"marker-write")
                hosts[(key,op)]=d
        rule_sets={".claude/rules":s["rules"],".claude/rules-reference":s["reference"]}
        for key,product in rule_sets.items():
            for name,data in sorted(product.items()): _write(stage/"files"/key.replace("/","_")/name,data)
            _write(stage/"files"/key.replace("/","_")/MARKER,_jb({"generator":GEN,"source":"shell","kind":"files","files":{n:_sha(d) for n,d in sorted(product.items())}}))
        mb_runtime=_jb(s["installed"]); json.loads(mb_runtime.decode("utf-8"))
        old=json.loads(c.manifest.read_text(encoding="utf-8")) if c.manifest.exists() else {}
        target_map={rel:_sha(data) for rel,data in sorted(s["runtime"].items())}
        target_map.update({"harness/%s/%s"%(op,name):_sha(data) for op,files_ in s["harness"].items() for name,data in files_.items()})
        target_map=dict(sorted(target_map.items()))
        core={"schema_version":LEDGER_SCHEMA,"generator":GEN,"source_manifest_sha256":s["manifest_sha256"],
              "installed_manifest_sha256":_sha(mb_runtime),"target_map_sha256":_sha(_jb(target_map)),
              "runtime_files":target_map,"operator_skills":sorted(OPS),
              "hosts":{".claude/skills":sorted(OPS),".agents/skills":sorted(OPS)},
              "rules":{".claude/rules":sorted(s["rules"]),".claude/rules-reference":sorted(s["reference"])},
              "dropped_build_only":s["dropped"],
              "counts":{"entries":len(s["installed"]["entries"]),"overlays":len(s["installed"]["overlays"]),
                        "runtime_files":len(target_map),"rules":len(s["rules"]),"rules_reference":len(s["reference"]),
                        "opaque_ids":len(s["id_map"]),"warnings":len(s["installed"]["warnings"])},
              "validation":{"errors":[],"warnings":s["installed"]["warnings"]}}
        gh=_sha(json.dumps(core,sort_keys=True,separators=(",",":")).encode())
        man={"generated":old.get("generated") if old.get("content_hash")==gh else datetime.now().isoformat(),**core,"content_hash":gh}
        mb=_jb(man); _fault(fail_at,"manifest-serialize")
        if fail_at=="permission-denied": raise PermissionError("injected")
        if fail_at=="short-write": raise OSError("injected short write")
        # ---- the plan (apply order == recovery order reversed) ----
        plan=[]
        def want(kind,target,source,existed=None):
            plan.append({"kind":kind,"target":target,"source":source,"existed":target.exists() if existed is None else existed})
        for key in (".claude/skills",".agents/skills"):
            managed,legacy_dirs,_=dirs[key]; root=c.host(key)
            for op in sorted(OPS):
                target=root/op
                if _hash(target)!=_hash(hosts[(key,op)]): want("operator",target,hosts[(key,op)])
            for n,p in sorted(managed.items()):
                if n not in OPS: want("stale",p,None)
            for p in legacy_dirs:
                if p.name not in OPS: want("legacy-managed",p,None)
        for p in legacy: want("legacy",p,None)
        for root in RUNTIME_DIRS:
            target=c.pbaw/root; staged=stage/"pbaw"/root
            if staged.exists():
                if _hash(target)!=_hash(staged): want("runtime",target,staged)
            elif target.exists(): want("runtime-remove",target,None)
        for key,product in rule_sets.items():
            root=c.host(key); managed_files,legacy_files,_=files[key]; sdir=stage/"files"/key.replace("/","_")
            for name in sorted(product):
                target=root/name
                if not target.exists() or target.read_bytes()!=product[name]: want("rule",target,sdir/name)
            for name in sorted(set(managed_files)|set(legacy_files)):
                if name not in product: want("rule-remove",root/name,None)
            marker=root/MARKER
            if not marker.exists() or marker.read_bytes()!=(sdir/MARKER).read_bytes(): want("rule-marker",marker,sdir/MARKER)
        if not c.runtime_manifest.exists() or c.runtime_manifest.read_bytes()!=mb_runtime: want("manifest",c.runtime_manifest,None)
        if not c.manifest.exists() or c.manifest.read_bytes()!=mb: want("ledger",c.manifest,None)
        if preview:
            return {"preview":True,"operations":[{"kind":o["kind"],"target":str(o["target"]),"existed":o["existed"]} for o in plan],
                    "copied":0,"updated":0,"deleted":0}
        # ---- durable backup, then the journalled apply ----
        backup_map=None
        if backup_root is not None:
            backup_map={}
            for key in HOSTS:
                root=c.host(key)
                if root.exists():
                    dst=backup_root/key.replace("/","_"); shutil.copytree(root,dst,symlinks=True)
                    if _hash(dst)!=_hash(root): raise RuntimeError("backup copy hash mismatch: "+key)
                    backup_map[key]={"path":str(dst),"tree_sha256":_hash(dst)}
        def prepare(target,source,kind):
            backup=rb/str(len(operations)); op={"kind":kind,"target":str(target),"staged":str(source) if source else None,"backup":str(backup) if target.exists() else None,"applied":False}
            operations.append(op); _write(c.journal,_jb({"schema_version":1,"state":"incomplete","operations":operations})); return op
        def apply(op,source):
            target=Path(op["target"]); target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists(): target.rename(Path(op["backup"])); _fault(fail_at,"live-to-rollback")
            if source: source.rename(target); _fault(fail_at,"staged-to-live")
            op["applied"]=True; _write(c.journal,_jb({"schema_version":1,"state":"incomplete","operations":operations}))
        for o in plan:
            kind,target,source=o["kind"],o["target"],o["source"]
            if kind in ("manifest","ledger"):
                data=mb_runtime if kind=="manifest" else mb
                c.pbaw.mkdir(parents=True,exist_ok=True)
                fd,name=tempfile.mkstemp(prefix=".manifest-stage-",suffix=".json",dir=c.pbaw); os.close(fd)
                tmp=Path(name); _write(tmp,data); json.loads(tmp.read_text(encoding="utf-8"))
                if kind=="manifest": manifest_tmp=tmp
                else: ledger_tmp=tmp
                op=prepare(target,tmp,kind)
                if target.exists(): target.rename(Path(op["backup"]))
                os.replace(tmp,target); _fault(fail_at,"manifest-replace"); op["applied"]=True
                _write(c.journal,_jb({"schema_version":1,"state":"incomplete","operations":operations}))
                report["updated" if o["existed"] else "copied"]+=1; continue
            apply(prepare(target,source,kind),source)
            if kind=="legacy": _fault(fail_at,"legacy-remove")
            if source is None: report["deleted"]+=1
            else: report["updated" if o["existed"] else "copied"]+=1
        c.journal.unlink(missing_ok=True)
        # ---- the persisted receipt (outside the journal: evidence, not state) ----
        post=_snapshot(c,unmanaged)
        preserved=all(pre["hosts"][k]["unmanaged"]==post["hosts"][k]["unmanaged"] for k in HOSTS) and pre["context_tree_sha256"]==post["context_tree_sha256"]
        receipt={"schema":"pbaw-sync-receipt/v1","generator":GEN,"completed_at":datetime.now().isoformat(),
                 "project_root":str(c.base_dir),"source":{"root":str(c.source),"runtime_manifest_sha256":s["manifest_sha256"]},
                 "installed_manifest_sha256":_sha(mb_runtime),"ledger_content_hash":gh,"target_map_sha256":core["target_map_sha256"],
                 "frozen_unmanaged":{k:sorted(unmanaged.get(k,{})) for k in HOSTS},
                 "legacy_removed":{key:sorted(p.name for p in dirs[key][1] if p.name not in OPS) for key in dirs},
                 "legacy_adopted":{key:sorted(p.name for p in dirs[key][1] if p.name in OPS) for key in dirs},
                 "legacy_rules_adopted":{key:sorted(files[key][1]) for key in files},
                 "pmtk_removed":[p.name for p in legacy],"declared_legacy_counts":{k:len(v) for k,v in c.legacy_managed.items()},
                 "pre":pre,"post":{**post,"pbaw_map":target_map},"unmanaged_and_context_preserved":preserved,
                 "backup":backup_map,"operations":[{"kind":o["kind"],"target":str(o["target"]),"existed":o["existed"]} for o in plan],"report":report}
        _write(c.receipt,_jb(receipt))
        if not preserved: raise RuntimeError("unmanaged or context bytes changed during sync; see "+str(c.receipt))
        return report
    except Exception:
        if c.journal.exists(): recover_incomplete_transaction(c)
        for r in created_roots:
            if r.is_dir() and not any(r.iterdir()): r.rmdir()
        raise
    finally:
        for tmp in (manifest_tmp,ledger_tmp):
            if tmp: tmp.unlink(missing_ok=True)
        shutil.rmtree(stage,ignore_errors=True); shutil.rmtree(rb,ignore_errors=True)
        if staging_root.exists() and not any(staging_root.iterdir()): staging_root.rmdir()

def uninstall_workspace(c,*,fail_at=None):
    """Remove exactly what this tool manages (the marked harness dirs on both hosts, the managed rule
    files and their markers, `.pbaw/`) inside one journalled transaction; unmanaged content and
    `context/` are never touched. Refuses an unmarked harness-named directory."""
    if c.journal.exists(): recover_incomplete_transaction(c)
    dirs={key:_classify_dirs(c,key) for key in (".claude/skills",".agents/skills")}
    rule_hosts={".claude/rules":_files_marker(c.rules),".claude/rules-reference":_files_marker(c.rules_reference)}
    for key,(managed,legacy_dirs,_) in dirs.items():
        for p in legacy_dirs:
            if p.name in OPS: raise ValueError("unmanaged destination collision "+key+"/"+p.name)
    unmanaged={key:dirs[key][2] for key in dirs}
    for key,managed_files in rule_hosts.items():
        root=c.host(key); unmanaged[key]={f.name:f for f in sorted(root.iterdir()) if root.is_dir() and f.is_file() and f.name!=MARKER and f.name not in managed_files} if root.exists() else {}
    pre=_snapshot(c,unmanaged)
    staging_root=c.p(".setup-skills-staging"); staging_root.mkdir(parents=False,exist_ok=True)
    rb=Path(tempfile.mkdtemp(prefix="setup-skills-rollback-",dir=staging_root)); operations=[]; report={"copied":0,"updated":0,"deleted":0}
    plan=[]
    for key,(managed,_l,_u) in dirs.items():
        for n,p in sorted(managed.items()): plan.append(("managed",p))
    for key,managed_files in rule_hosts.items():
        root=c.host(key)
        for name in sorted(managed_files): plan.append(("rule",root/name))
        if (root/MARKER).exists(): plan.append(("rule-marker",root/MARKER))
    if c.pbaw.exists():
        for child in sorted(c.pbaw.iterdir()):
            if child.name!=JOURNAL: plan.append(("runtime",child))
    try:
        def prepare(target,kind):
            backup=rb/str(len(operations)); op={"kind":kind,"target":str(target),"staged":None,"backup":str(backup),"applied":False}
            operations.append(op); _write(c.journal,_jb({"schema_version":1,"state":"incomplete","operations":operations})); return op
        for kind,target in plan:
            op=prepare(target,kind); target.rename(Path(op["backup"])); _fault(fail_at,"live-to-rollback")
            op["applied"]=True; _write(c.journal,_jb({"schema_version":1,"state":"incomplete","operations":operations})); report["deleted"]+=1
        c.journal.unlink(missing_ok=True)
        if c.pbaw.is_dir() and not any(c.pbaw.iterdir()): c.pbaw.rmdir()
        post=_snapshot(c,unmanaged)
        preserved=all(pre["hosts"][k]["unmanaged"]==post["hosts"][k]["unmanaged"] for k in HOSTS) and pre["context_tree_sha256"]==post["context_tree_sha256"]
        receipt={"schema":"pbaw-uninstall-receipt/v1","generator":GEN,"completed_at":datetime.now().isoformat(),"project_root":str(c.base_dir),
                 "removed":[{"kind":k,"target":str(t)} for k,t in plan],"frozen_unmanaged":{k:sorted(unmanaged.get(k,{})) for k in HOSTS},
                 "pre":pre,"post":post,"unmanaged_and_context_preserved":preserved,"report":report}
        _write(c.p(".pbaw-uninstall-receipt.json"),_jb(receipt))
        if not preserved: raise RuntimeError("unmanaged or context bytes changed during uninstall")
        return report
    except Exception:
        if c.journal.exists(): recover_incomplete_transaction(c)
        raise
    finally:
        shutil.rmtree(rb,ignore_errors=True)
        if staging_root.exists() and not any(staging_root.iterdir()): staging_root.rmdir()

def default_allowlist(source):
    p=Path(source)/"tools"/"build"/"fixtures"/"pmtk-legacy-allowlist-baseline.md"; tick=chr(96)
    if not p.is_file(): return frozenset()
    names={line.split(tick,2)[1] for line in p.read_text(encoding="utf-8").splitlines() if line.startswith("| "+tick+"pmtk-")}
    if len(names)!=56: raise RuntimeError("frozen legacy denominator is not 56")
    return frozenset(names)
def load_legacy_managed(path):
    """Declared legacy data (never derived from the tree under test): {host: [names]} with pinned denominators."""
    v=json.loads(Path(path).read_text(encoding="utf-8"))
    if v.get("schema")!=LEGACY_SCHEMA or not isinstance(v.get("hosts"),dict) or not isinstance(v.get("denominators"),dict): raise ValueError("legacy-managed schema")
    out={}
    for host,names in v["hosts"].items():
        if host not in HOSTS or not isinstance(names,list) or len(set(names))!=len(names): raise ValueError("legacy-managed host "+str(host))
        if v["denominators"].get(host)!=len(names): raise ValueError("legacy-managed denominator "+host)
        out[host]=frozenset(names)
    return out

def _argument_parser():
    parser=argparse.ArgumentParser(description="Transactional PBAW installer (project a v6 flat source onto one project root)")
    parser.add_argument("--check",action="store_true",help="validate the source and the installed manifest without writing")
    parser.add_argument("--preview",action="store_true",help="stage, print the operation list, roll back; writes nothing live")
    parser.add_argument("--backup-to",metavar="DIR",help="durable copy of both host roots and the rules folders into an ABSENT directory before the sync")
    parser.add_argument("--source",metavar="DIR",help="the flat source root (default: the project root)")
    parser.add_argument("--project-root",metavar="DIR",help="the project root (default: this file's directory)")
    parser.add_argument("--legacy-managed",metavar="JSON",help="declared legacy-managed directories/files to shrink once (never inferred)")
    parser.add_argument("action",nargs="?",choices=("sync","uninstall"),help="explicitly run the sync, or remove exactly what this tool manages")
    return parser

def main(argv=None):
    parser=_argument_parser(); args=parser.parse_args(argv)
    if (args.check or args.preview) and args.action is not None: parser.error("--check/--preview cannot be combined with sync")
    if args.check and args.preview: parser.error("--check and --preview are exclusive")
    if not (args.check or args.preview) and args.action is None: parser.error("an explicit action is required: sync, uninstall, --check or --preview")
    if args.backup_to and args.action!="sync": parser.error("--backup-to only applies to sync")
    base=Path(args.project_root).resolve() if args.project_root else Path(__file__).resolve().parent
    source=Path(args.source).resolve() if args.source else base
    legacy=load_legacy_managed(args.legacy_managed) if args.legacy_managed else None
    c=WorkspaceConfig(base,default_allowlist(source),source=source,legacy_managed=legacy)
    if args.check:
        installed=build_runtime_manifest(c)
        print("Check: OK"); print("Source:",c.source); print("Target:",c.claude_skills)
        print("Entries:",len(installed["entries"]),"Overlays:",len(installed["overlays"])); return 0
    if args.preview:
        r=sync_workspace(c,preview=True)
        print("Preview (nothing written):",len(r["operations"]),"operations"); print("Target:",c.claude_skills)
        for o in r["operations"]: print(" ",o["kind"],o["target"],"(existing)" if o["existed"] else "(new)")
        return 0
    if args.action=="uninstall":
        print("setup-skills.py - transactional PBAW uninstall"); print("Target:",c.claude_skills)
        r=uninstall_workspace(c); print("Deleted:",r["deleted"]); print("Receipt:",c.p(".pbaw-uninstall-receipt.json")); return 0
    print("setup-skills.py - transactional PBAW sync"); print("Source:",c.source); print("Target:",c.claude_skills)
    r=sync_workspace(c,backup_to=args.backup_to)
    print("Copied:",r["copied"],"Updated:",r["updated"],"Deleted:",r["deleted"]); print("Manifest:",c.manifest); print("Receipt:",c.receipt); return 0
if __name__=="__main__": sys.exit(main())
