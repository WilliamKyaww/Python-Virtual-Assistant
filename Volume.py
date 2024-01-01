from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

import os

def set_volume(change):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    currentVolumeDb = volume.GetMasterVolumeLevel()
    newVolumeDb = max(min(currentVolumeDb + change, volume.GetVolumeRange()[1]), volume.GetVolumeRange()[0])
    volume.SetMasterVolumeLevel(newVolumeDb, None)

def increase_volume():
    set_volume(4.0)  # Increase volume by 4 dB

def decrease_volume():
    set_volume(-4.0)  # Decrease volume by 4 dB
    
def mute_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(1, None)  # 1 to mute

def unmute_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(0, None)  # 0 to unmute

def open_bluetooth_settings(): 
    command = "start ms-settings:bluetooth"
    os.system(command)
    
    



    
