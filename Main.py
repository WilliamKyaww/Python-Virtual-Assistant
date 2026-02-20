from Opening_Apps import open_app, close_app
from Opening_Chrome import open_chrome
from Speech_to_Text import speech_input
from Volume import increase_volume, decrease_volume, mute_volume, unmute_volume
from Bluetooth import open_bluetooth_settings


def handle_command(text):
    """Route a voice command to the appropriate handler.

    Returns False if the user requested to exit, True otherwise.
    """
    words = text.split()

    if not words:
        return True

    keyword = words[0]
    argument = " ".join(words[1:])

    if keyword == "open":
        open_app(argument)

    elif keyword == "close":
        close_app(argument)

    elif keyword == "search":
        open_chrome(argument)

    elif "volume" in text:
        if "increase" in text or "up" in text:
            increase_volume()
        elif "decrease" in text or "down" in text:
            decrease_volume()

    elif "unmute" in text:
        unmute_volume()

    elif "mute" in text:
        mute_volume()

    elif "bluetooth" in text:
        open_bluetooth_settings()

    elif text in ("stop", "exit", "quit", "goodbye"):
        print("\033[94m Goodbye! \033[0m")
        return False

    else:
        print(f"\033[91m Command not recognized: '{text}' \033[0m")

    return True


def main():
    """Main loop — listen for voice commands and execute them."""
    print("\033[96m JARVIS is starting up... \033[0m")
    print("\033[96m Say 'stop', 'exit', or 'quit' to shut down. \033[0m")
    print()

    while True:
        text = speech_input()
        print("\033[92m", text, "\033[0m")
        print()

        if not handle_command(text):
            break


if __name__ == "__main__":
    main()
