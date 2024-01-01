import subprocess

def open_apps(value):
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

    app_path = switch_dict.get(value)
    if app_path:
        if value == 'terminal':
            subprocess.run(['start', 'cmd.exe', '/k'], shell=True)  # '/k' keeps the command prompt window open
        else:
            subprocess.run(app_path, shell=True)
    else:
        print('\033[91m Application not found \033[0m')

