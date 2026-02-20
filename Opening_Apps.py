import subprocess
import os

# Resolve the current user's home directory dynamically
_HOME = os.path.expanduser("~")


def _resolve(relative_path):
    """Join a relative path with the user's home directory."""
    return os.path.join(_HOME, relative_path)


# Application paths — relative to the current user's home directory where possible
APP_PATHS = {
    "terminal": r"C:\WINDOWS\system32\cmd.exe",
    "discord": _resolve(r"AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk"),
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "spotify": _resolve(r"AppData\Roaming\Spotify\Spotify.exe"),
    "zoom": _resolve(r"AppData\Roaming\Zoom\bin\Zoom.exe"),
    "vs code": _resolve(r"AppData\Local\Programs\Microsoft VS Code\Code.exe"),
    "notion": _resolve(r"AppData\Local\Programs\Notion\Notion.exe"),
    "photoshop": r"C:\Program Files\Adobe\Adobe Photoshop CS6 (64 Bit)\Photoshop.exe",
}

# Process names used by taskkill to close applications
PROCESS_NAMES = {
    "terminal": "cmd.exe",
    "discord": "Discord.exe",
    "chrome": "chrome.exe",
    "spotify": "Spotify.exe",
    "zoom": "Zoom.exe",
    "vs code": "Code.exe",
    "notion": "Notion.exe",
    "photoshop": "Photoshop.exe",
}


def open_app(app_name):
    """Open a desktop application by its friendly name."""
    app_path = APP_PATHS.get(app_name)

    if not app_path:
        print("\033[91m Application not found \033[0m")
        return

    if app_name == "terminal":
        subprocess.run(["start", "cmd.exe", "/k"], shell=True)
    else:
        subprocess.Popen(app_path, shell=True)


def close_app(app_name):
    """Close a running application by its friendly name."""
    process_name = PROCESS_NAMES.get(app_name.lower())

    if not process_name:
        print(f"\033[91m Process name for '{app_name}' not found. \033[0m")
        return

    try:
        subprocess.run(
            ["taskkill", "/f", "/im", process_name],
            check=True,
            capture_output=True,
        )
    except subprocess.CalledProcessError:
        print(f"\033[91m Failed to close {app_name} (it may not be running). \033[0m")
