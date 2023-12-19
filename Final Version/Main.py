from Opening_Apps import open_apps
from Opening_Chrome import open_chrome
from Speech_to_Text import speech_input

while True:
    text = speech_input()
    print("\033[92m", text, "\033[0m")
    print()
    
    if text.split()[0] == "open":
        text = ' '.join(text.split()[1:])
        open_apps(text)

    elif text.split()[0] == "search":
        text = ' '.join(text.split()[1:])
        open_chrome(text)