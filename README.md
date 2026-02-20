# JARVIS — Python Virtual Assistant

A voice-controlled desktop assistant for Windows that listens for spoken commands and performs system actions.

## Features

- **Open / Close apps** — Launch or kill desktop applications by name
- **Web search** — Open bookmarked sites or Google anything
- **Volume control** — Increase, decrease, mute, or unmute system audio
- **Bluetooth** — Open Windows Bluetooth settings
- **Speech recognition** — Hands-free control via Google Speech Recognition

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure environment variables

Copy the `.env.example` and fill in your API keys (optional for core features):

```bash
cp .env.example .env
```

### 3. Run

```bash
python Main.py
```

## Voice Commands

| Command | Example | Action |
|---------|---------|--------|
| `open <app>` | "open chrome" | Launch an application |
| `close <app>` | "close spotify" | Kill a running application |
| `search <query>` | "search Python tutorials" | Google search or open bookmarked site |
| `increase volume` | "increase volume" | Turn volume up |
| `decrease volume` | "decrease volume" | Turn volume down |
| `mute` | "mute" | Mute system audio |
| `unmute` | "unmute" | Unmute system audio |
| `bluetooth` | "bluetooth" | Open Bluetooth settings |
| `stop` / `exit` / `quit` | "stop" | Shut down JARVIS |

### Supported Apps

`terminal` · `discord` · `chrome` · `spotify` · `zoom` · `vs code` · `notion` · `photoshop`

### Bookmarked Sites

`learn` · `email` · `outlook` · `github` · `jira` · `chat gpt` · `drive` · `hostinger`

Any unrecognized search term is sent to Google.

## Project Structure

```
JARVIS/
├── Main.py              # Entry point — command loop
├── Speech_to_Text.py    # Microphone input → text
├── Opening_Apps.py      # Open/close desktop applications
├── Opening_Chrome.py    # Web bookmarks and Google search
├── Volume.py            # System volume control
├── Bluetooth.py         # Bluetooth settings
├── Spotify_Commands.py  # Spotify integration (WIP)
├── requirements.txt     # Python dependencies
└── .env                 # API keys (not committed)
```

## Requirements

- Python 3.8+
- Windows 10/11
- A working microphone
