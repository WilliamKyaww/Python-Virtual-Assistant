import speech_recognition as sr
import pyttsx3
from Opening_Apps import open_apps
from Opening_Chrome import open_chrome

r = sr.Recognizer()

def record_text():
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print("\033[93m Active \033[0m")
                
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower() 
                
                return MyText
        
        except sr.RequestError as e:
            print("\033[91m Could not request results; {0} \033[0m".format(e))
            print()
            
        except sr.UnknownValueError:
            print("\033[91m Unknown error occurred \033[0m")
            print()
            
while True:
    text = record_text()
    print("\033[92m", text, "\033[0m")
    print()
    
    if text.split()[0] == "open":
        text = ' '.join(text.split()[1:])
        open_apps(text)

    elif text.split()[0] == "search":
        text = ' '.join(text.split()[1:])
        open_chrome(text)