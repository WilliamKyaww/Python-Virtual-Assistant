from Opening_Apps import *
from Opening_Chrome import *
from Speech_to_Text import *
from Volume import *

from dotenv import load_dotenv
import os

load_dotenv()

spotify_client_id = os.getenv('SPOTIFY_CLIENT_ID')
spotify_client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
openai_api_key = os.getenv('OPENAI_API_KEY')
discord_bot_token = os.getenv('DISCORD_BOT_TOKEN')
wikipedia_api_key = os.getenv('WIKIPEDIA_API_KEY')


while True:
    text = speech_input()
    print("\033[92m", text, "\033[0m")
    print()
    
    if text.split()[0] == "open":
        text = ' '.join(text.split()[1:])
        open_app(text)

    if text.split()[0] == "close":
        text = ' '.join(text.split()[1:])
        close_app(text)

    elif text.split()[0] == "search":
        text = ' '.join(text.split()[1:])
        open_chrome(text)
        
    elif "volume" in text:
        if "increase" in text:
            increase_volume()
        elif "decrease" in text:
            decrease_volume()
            
    elif "bluetooth" in text:
        open_bluetooth_settings()
    
    elif "unmute" in text:
        unmute_volume()
        
    elif "mute" in text:
        print("testing")
        mute_volume()
        

