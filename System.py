from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Get default audio device
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

# Get volume
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Control and get current volume 
currentVolumeDb = volume.GetMasterVolumeLevel()

# Increase volume by 2 dB
def increase_volume(value):
    volume.SetMasterVolumeLevel(currentVolumeDb + 2.0, None)

# Increase volume by 2 dB
def decrease_volume(value):
    volume.SetMasterVolumeLevel(currentVolumeDb + 2.0, None)