import webbrowser

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe' 
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

def open_chrome(value):
    switch_dict = {
        'learn': 'https://learn.lboro.ac.uk/',
        'email': 'https://mail.google.com/mail/u/0/#inbox',
        'outlook': 'https://outlook.office365.com/mail/',
        'github': 'https://github.com/',
        'jira': 'https://alan-moss-inc.atlassian.net/jira/software/projects/KAN/boards/1',
        'chat gpt': 'https://chat.openai.com/',
        'drive': 'https://drive.google.com/drive/my-drive',
        'hostinger': 'https://hpanel.hostinger.com/',
    }

    tab_path = switch_dict.get(value)
    
    if tab_path:
        webbrowser.get('chrome').open_new_tab(tab_path)
    else:
        print('\033[91m Tab not programmed \033[0m')
        
