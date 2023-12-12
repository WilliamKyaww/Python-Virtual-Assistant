import speech_recognition as sr
import pyttsx3

import os

r = sr.Recognizer()

def record_text():
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print("\033[92m Listening... \n \033[0m")
                
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                
                return MyText
        
        except sr.RequestError as e:
            print("\033[91m Could not request results; {0}\n \033[0m".format(e))
            
        except sr.UnknownValueError:
            print("\033[91m Unknown error occurred \n \033[0m")
            
            
while(1):
    text = record_text()
    print("User: \033[93m" , text , "\n \033[0m")
    

    discord_path = r"AppData\\Local\\Discord\\Update.exe"
    spotify_path = r"C:\\Users\\D E L L\\AppData\\Roaming\\Spotify\\Spotify.exe"
    os.startfile(spotify_path)


