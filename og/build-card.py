"""
Social-preview card for the Product Org OS website (1200x630, og/product-org-os.png).

Rendered with Playwright headless Chromium from an inline HTML template that
uses the site's own tokens (bg #1a1a2e, primary #e94560, secondary #4ecca3,
Inter). Run from the site root:  python og/build-card.py
Bump the output filename when the card changes: LinkedIn caches by image URL.
"""

import base64
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).parent.parent
OUT = ROOT / "og" / "product-org-os.png"
ICON = ROOT / "brand-assets" / "product-org-os-icon.png"

icon_uri = "data:image/png;base64," + base64.b64encode(ICON.read_bytes()).decode("ascii")

HTML = f"""<!doctype html><html><head><meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body {{ width:1200px; height:630px; overflow:hidden; }}
body {{ font-family:'Inter',system-ui,sans-serif; background:#1a1a2e; color:#eaeaea; position:relative;
  padding:56px 72px; display:flex; flex-direction:column; justify-content:space-between; }}
body::before {{ content:''; position:absolute; top:0; left:0; right:0; height:6px;
  background:linear-gradient(90deg,#e94560 0%,#4ecca3 100%); }}
body::after {{ content:''; position:absolute; top:-260px; right:-240px; width:720px; height:720px; border-radius:50%;
  background:radial-gradient(circle, rgba(78,204,163,0.16), transparent 68%); pointer-events:none; }}
.brand {{ display:flex; align-items:center; gap:14px; font-family:'JetBrains Mono',monospace; font-size:16px; font-weight:700;
  letter-spacing:0.12em; text-transform:uppercase; color:#4ecca3; }}
.brand img {{ width:40px; height:40px; }}
.mid {{ position:relative; z-index:1; }}
h1 {{ font-size:66px; font-weight:800; line-height:1.05; letter-spacing:-0.025em; color:#ffffff; margin-bottom:20px; }}
h1 .os {{ color:#e94560; }}
.sub {{ font-size:26px; line-height:1.35; color:#c9c9d6; max-width:980px; }}
.stats {{ display:flex; gap:44px; margin-top:30px; }}
.stat b {{ display:block; font-size:44px; font-weight:800; letter-spacing:-0.02em; color:#4ecca3; line-height:1; }}
.stat span {{ display:block; font-size:14px; font-family:'JetBrains Mono',monospace; letter-spacing:0.08em;
  text-transform:uppercase; color:#a0a0a0; margin-top:8px; }}
.footer {{ display:flex; justify-content:space-between; align-items:flex-end; position:relative; z-index:1; }}
.byline {{ font-size:20px; font-weight:500; color:#eaeaea; }}
.byline-meta {{ display:block; font-size:15px; color:#a0a0a0; margin-top:4px; font-family:'JetBrains Mono',monospace; letter-spacing:0.04em; }}
.tag {{ display:inline-block; padding:8px 16px; background:rgba(233,69,96,0.12); border:1px solid rgba(233,69,96,0.5);
  border-radius:6px; font-family:'JetBrains Mono',monospace; font-size:14px; font-weight:500; color:#ff7a8f; letter-spacing:0.08em; }}
</style></head><body>
  <div class="brand"><img src="{icon_uri}" alt="">Product Org OS</div>
  <div class="mid">
    <h1>Product Org <span class="os">OS</span></h1>
    <p class="sub">Give your coding agent the product judgment, methods, and professional context behind serious product work. Works with Claude Code, Codex and Cursor.</p>
    <div class="stats">
      <div class="stat"><b>11</b><span>product roles</span></div>
      <div class="stat"><b>125</b><span>methods &amp; controls</span></div>
      <div class="stat"><b>117</b><span>knowledge files</span></div>
      <div class="stat"><b>4</b><span>governed workflows</span></div>
    </div>
  </div>
  <div class="footer">
    <div class="byline">Based on Vision to Value, by Yohay Etsion<span class="byline-meta">yohayetsion.github.io/product-org-os</span></div>
    <div class="tag">FREE · OPEN SOURCE · v6.2.0</div>
  </div>
</body></html>"""


def main():
    OUT.parent.mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=1)
        page.set_content(HTML, wait_until="networkidle")
        page.wait_for_timeout(900)
        page.screenshot(path=str(OUT), full_page=False, type="png")
        browser.close()
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
