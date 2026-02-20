import speech_recognition as sr

_recognizer = sr.Recognizer()


def speech_input():
    """Listen for speech and return the recognized text as a lowercase string.

    Retries indefinitely on recognition errors until valid input is received.
    Returns an empty string if no speech could be understood (should be
    handled by the caller).
    """
    while True:
        try:
            with sr.Microphone() as source:
                _recognizer.adjust_for_ambient_noise(source, duration=0.2)
                print("\033[93m Listening... \033[0m")

                audio = _recognizer.listen(source)
                text = _recognizer.recognize_google(audio)
                return text.lower()

        except sr.RequestError as e:
            print(f"\033[91m Could not request results: {e} \033[0m")

        except sr.UnknownValueError:
            print("\033[91m Could not understand audio \033[0m")
