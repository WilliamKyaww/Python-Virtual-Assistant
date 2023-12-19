from Opening_Apps import open_apps
from Opening_Chrome import open_chrome
from Speech_to_Text import speech_input

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
        open_apps(text)

    elif text.split()[0] == "search":
        text = ' '.join(text.split()[1:])
        open_chrome(text)