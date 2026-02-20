from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def _get_volume_interface():
    """Return the system IAudioEndpointVolume COM interface."""
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    return cast(interface, POINTER(IAudioEndpointVolume))


def set_volume(change):
    """Adjust the master volume by `change` dB, clamped to the valid range."""
    volume = _get_volume_interface()
    current_db = volume.GetMasterVolumeLevel()
    vol_min, vol_max, _ = volume.GetVolumeRange()
    new_db = max(min(current_db + change, vol_max), vol_min)
    volume.SetMasterVolumeLevel(new_db, None)


def increase_volume():
    """Increase system volume by ~4 dB."""
    set_volume(4.0)


def decrease_volume():
    """Decrease system volume by ~4 dB."""
    set_volume(-4.0)


def mute_volume():
    """Mute system audio."""
    volume = _get_volume_interface()
    volume.SetMute(1, None)


def unmute_volume():
    """Unmute system audio."""
    volume = _get_volume_interface()
    volume.SetMute(0, None)
