import os


def open_bluetooth_settings():
    """Open the Windows Bluetooth settings panel."""
    os.startfile("ms-settings:bluetooth")