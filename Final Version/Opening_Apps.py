import subprocess

terminal_path = r'C:\WINDOWS\system32\cmd.exe'
spotify_path = r'C:\Users\D E L L\AppData\Roaming\Spotify\Spotify.exe' 
discord_path = r'C:\Users\D E L L\\AppData\Roaming\\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk'
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe' 
zoom_path = r'C:\Users\D E L L\AppData\Roaming\Zoom\bin\Zoom.exe'
vscode_path = r'C:\Users\D E L L\AppData\Local\Programs\Microsoft VS Code\Code.exe'
trello_path = r'C:\Program Files\WindowsApps\45273LiamForsyth.PawsforTrello_2.14.5.0_x64__7pb5ddty8z1pa\app\Trello.exe'
notion_path = r'C:\Users\D E L L\AppData\Local\Programs\Notion\Notion.exe'
photoshop_path = r'C:\Program Files\Adobe\Adobe Photoshop CS6 (64 Bit)\Photoshop.exe'

def open_apps(value):
    switch_dict = {
        'terminal': terminal_path,
        'discord': discord_path,
        'chrome': chrome_path,
        'spotify': spotify_path,
        'zoom': zoom_path,
        'vscode': vscode_path,
        'trello': trello_path,
        'notion': notion_path,
        'photoshop': photoshop_path,
    }

    app_path = switch_dict.get(value)
    if app_path:
        if value == 'terminal':
            subprocess.run(['start', 'cmd.exe', '/k'], shell=True)  # '/k' keeps the command prompt window open
        else:
            subprocess.run(app_path, shell=True)
    else:
        print('\033[91m Application not found \033[0m')

