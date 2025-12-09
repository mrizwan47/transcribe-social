# Transcribe Reel

Transcribe Instagram/TikTok reels and YouTube shorts using OpenAI Whisper.

### Prerequisites

You need `ffmpeg` installed on your system:

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg

# Windows (with chocolatey)
choco install ffmpeg
```

## Installation

```bash
git clone https://github.com/mrizwan47/transcribe-reel.git
cd transcribe-reel
pip install .
```

This will install:
- `yt-dlp` - for downloading audio from URLs
- `openai-whisper` - for transcription
- `transcribe-reel` command

## Usage

Run the command:

```bash
transcribe-reel
```

Then paste any reel/short URL when prompted.

### Commands

- `/model <name>` - Set model (tiny, base, small, medium, large, turbo)
- `/lang <code>` - Set language (en, ur, es, fr, de, zh, ar, hi, etc.)
- `/status` - Show current settings
- `/help` - Show help
- `exit` - Quit

## Author

[Rizwan](https://riz.codes/)
