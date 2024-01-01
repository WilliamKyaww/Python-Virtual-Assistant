import subprocess
import os

def open_app(app_name):
    switch_dict = {
        'terminal': r'C:\WINDOWS\system32\cmd.exe',
        'discord': r'C:\Users\D E L L\\AppData\Roaming\\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk',
        'chrome': r'C:\Program Files\Google\Chrome\Application\chrome.exe' ,
        'spotify': r'C:\Users\D E L L\AppData\Roaming\Spotify\Spotify.exe' ,
        'zoom': r'C:\Users\D E L L\AppData\Roaming\Zoom\bin\Zoom.exe',
        'vs code': r'C:\Users\D E L L\AppData\Local\Programs\Microsoft VS Code\Code.exe',
        'trello': r'C:\Program Files\WindowsApps\45273LiamForsyth.PawsforTrello_2.14.5.0_x64__7pb5ddty8z1pa\app\Trello.exe',
        'notion': r'C:\Users\D E L L\AppData\Local\Programs\Notion\Notion.exe',
        'photoshop': r'C:\Program Files\Adobe\Adobe Photoshop CS6 (64 Bit)\Photoshop.exe',
    }

    app_path = switch_dict.get(app_name)
    if app_path:
        if app_name == 'terminal':
            subprocess.run(['start', 'cmd.exe', '/k'], shell=True)  # '/k' keeps the command prompt window open
        else:
            subprocess.run(app_path, shell=True)
    else:
        print('\033[91m Application not found \033[0m')
        


def close_app(app_name):
    process_names = {
        'terminal': 'cmd.exe',
        'discord': 'Discord.exe',
        'chrome': 'chrome.exe',
        'spotify': 'Spotify.exe',
        'zoom': 'Zoom.exe',
        'vs code': 'Code.exe',
        'trello': 'Trello.exe',
        'notion': 'Notion.exe',
        'photoshop': 'Photoshop.exe',
    }

    process_name = process_names.get(app_name.lower())
    
    if process_name:
        try:
            os.system(f"taskkill /f /im {process_name}")
        except Exception as e:
            print(f"Failed to close {app_name}: {e}")
    else:
        print(f"Process name for {app_name} not found.")



