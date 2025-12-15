# Transcribe Reel

Transcribe social media videos using OpenAI Whisper.

**Tested and working with:**
- YouTube (both shorts and regular videos)
- Instagram Reels
- TikTok videos
- X/Twitter videos
- Facebook videos
- Reddit videos

### Prerequisites

You need `ffmpeg` and `cmake` installed on your system:

```bash
# macOS
brew install ffmpeg cmake

# Ubuntu/Debian
sudo apt install ffmpeg cmake

# Windows (with chocolatey)
choco install ffmpeg cmake
```

## Installation

```bash
git clone https://github.com/mrizwan47/transcribe-reel.git
cd transcribe-reel
pip3 install .
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

Then paste any supported video URL when prompted.

### Commands

- `/model <name>` - Set model (tiny, base, small, medium, large, turbo)
- `/lang <code>` - Set language (en, ur, es, fr, de, zh, ar, hi, etc.)
- `/status` - Show current settings
- `/help` - Show help
- `exit` - Quit

## Author

[Rizwan](https://riz.codes/)
