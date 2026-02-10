"""Audio device discovery and management."""

from dataclasses import dataclass
from typing import Optional

import pyaudio


@dataclass
class AudioDevice:
    """Represents an audio device."""

    index: int
    name: str
    max_input_channels: int
    max_output_channels: int
    default_sample_rate: float
    host_api: str
    is_loopback: bool = False

    @property
    def is_input(self) -> bool:
        """Check if device can capture audio."""
        return self.max_input_channels > 0

    @property
    def is_output(self) -> bool:
        """Check if device can play audio."""
        return self.max_output_channels > 0


def get_pyaudio() -> pyaudio.PyAudio:
    """Get a PyAudio instance."""
    return pyaudio.PyAudio()


def list_devices(input_only: bool = False, output_only: bool = False) -> list[AudioDevice]:
    """
    List available audio devices.

    Args:
        input_only: Only return input devices (microphones, loopback)
        output_only: Only return output devices (speakers)

    Returns:
        List of AudioDevice objects
    """
    p = get_pyaudio()
    devices = []

    try:
        # Get host API info for WASAPI detection
        host_apis = {}
        for i in range(p.get_host_api_count()):
            api_info = p.get_host_api_info_by_index(i)
            host_apis[i] = api_info["name"]

        for i in range(p.get_device_count()):
            try:
                info = p.get_device_info_by_index(i)
                host_api = host_apis.get(info["hostApi"], "Unknown")

                # Detect WASAPI loopback devices
                is_loopback = (
                    "WASAPI" in host_api and
                    info["maxInputChannels"] > 0 and
                    ("Loopback" in info["name"] or "loopback" in info["name"].lower())
                )

                # On Windows, stereo mix or similar can also capture system audio
                if not is_loopback:
                    is_loopback = any(
                        term in info["name"].lower()
                        for term in ["stereo mix", "what u hear", "wave out"]
                    )

                device = AudioDevice(
                    index=i,
                    name=info["name"],
                    max_input_channels=int(info["maxInputChannels"]),
                    max_output_channels=int(info["maxOutputChannels"]),
                    default_sample_rate=float(info["defaultSampleRate"]),
                    host_api=host_api,
                    is_loopback=is_loopback,
                )

                # Filter based on flags
                if input_only and not device.is_input:
                    continue
                if output_only and not device.is_output:
                    continue

                devices.append(device)

            except Exception:
                # Skip devices that can't be queried
                continue

    finally:
        p.terminate()

    return devices


def get_device_info(device_index: int) -> Optional[AudioDevice]:
    """
    Get detailed info for a specific device.

    Args:
        device_index: Index of the device

    Returns:
        AudioDevice object or None if not found
    """
    devices = list_devices()
    for device in devices:
        if device.index == device_index:
            return device
    return None


def find_loopback_device() -> Optional[AudioDevice]:
    """
    Find a WASAPI loopback device for capturing system audio.

    Returns:
        AudioDevice for loopback capture, or None if not found
    """
    devices = list_devices(input_only=True)

    # First, try to find explicit loopback devices
    for device in devices:
        if device.is_loopback:
            return device

    # Fallback: look for WASAPI devices that might work
    for device in devices:
        if "WASAPI" in device.host_api and device.is_input:
            return device

    return None


def find_microphone() -> Optional[AudioDevice]:
    """
    Find the default microphone device.

    Returns:
        AudioDevice for microphone, or None if not found
    """
    p = get_pyaudio()
    try:
        default_input = p.get_default_input_device_info()
        return get_device_info(int(default_input["index"]))
    except Exception:
        # No default input device
        devices = list_devices(input_only=True)
        # Return first non-loopback input device
        for device in devices:
            if not device.is_loopback:
                return device
        return None
    finally:
        p.terminate()


def print_devices() -> None:
    """Print a formatted list of all audio devices."""
    from rich.console import Console
    from rich.table import Table

    console = Console()
    devices = list_devices()

    table = Table(title="Audio Devices")
    table.add_column("Index", style="cyan")
    table.add_column("Name", style="green")
    table.add_column("Type", style="yellow")
    table.add_column("Channels", style="magenta")
    table.add_column("Sample Rate", style="blue")
    table.add_column("Host API", style="white")

    for device in devices:
        device_type = []
        if device.is_input:
            device_type.append("Input")
        if device.is_output:
            device_type.append("Output")
        if device.is_loopback:
            device_type.append("🔄 Loopback")

        table.add_row(
            str(device.index),
            device.name[:50],  # Truncate long names
            ", ".join(device_type),
            f"In: {device.max_input_channels}, Out: {device.max_output_channels}",
            f"{int(device.default_sample_rate)} Hz",
            device.host_api,
        )

    console.print(table)
