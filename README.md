# 🎙️ Transcribe Reel

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenAI Whisper](https://img.shields.io/badge/Powered%20by-OpenAI%20Whisper-412991.svg)](https://github.com/openai/whisper)

> Turn any social media video into text in seconds. Powered by OpenAI Whisper.

Stop wasting time manually transcribing videos. Whether you're repurposing content, analyzing competitors, or extracting insights—Transcribe Reel handles it instantly.

## ✨ Why Use This?

**Perfect for:**
- 📝 Content creators repurposing videos into blogs/threads
- 📊 Marketers analyzing competitor video content
- 🎓 Students transcribing lectures and tutorials
- 🔍 Researchers extracting insights from social media

**Works with:**
YouTube • Instagram • TikTok • Twitter/X • Facebook • Reddit

## 🚀 Features

- **One Command** - Paste URL, get transcript
- **6 Platforms** - Works with all major social media sites
- **Multi-language** - 50+ languages supported
- **Smart Models** - Choose speed vs accuracy (tiny to turbo)
- **No Clutter** - Clean CLI, no files saved unless you want them
- **Privacy First** - Everything runs locally on your machine

## 📦 Quick Start

**Requirements:** Python 3.11+ and FFmpeg

```bash
# Install FFmpeg (one-time setup)
brew install ffmpeg  # macOS
# sudo apt install ffmpeg  # Ubuntu/Debian

# Install Transcribe Reel
git clone https://github.com/mrizwan47/transcribe-reel.git
cd transcribe-reel
python3 -m pip install .

# Start transcribing!
transcribe-reel
```

## 💡 How It Works

**1. Start the CLI**
```bash
transcribe-reel
```

**2. Paste any video URL**
```
URL> https://www.youtube.com/shorts/xyz123
```

**3. Get your transcript**
```
Downloading audio...
Transcribing...

In this video, I'll show you three productivity hacks that 
changed my life. First, time blocking...
```

**That's it.** No accounts, no uploads, no waiting.

## 🎯 Real-World Use Cases

```bash
# Repurpose a viral YouTube Short into a Twitter thread
URL> https://youtube.com/shorts/xyz

# Extract quotes from competitor's Instagram Reel
URL> https://instagram.com/reel/abc

# Transcribe a TikTok tutorial in Spanish
/lang es
URL> https://tiktok.com/@user/video/123

# Analyze a trending Reddit video discussion
URL> https://reddit.com/r/videos/comments/xyz
```

### ⚙️ Commands

| Command | Description |
|---------|-------------|
| `/model tiny\|base\|small\|medium\|large\|turbo` | Switch AI model (tiny=fastest, large=most accurate) |
| `/lang <code>` | Change language (en, es, fr, de, zh, ar, hi, ur, etc.) |
| `/status` | Show current settings |
| `/help` | Show help |
| `exit` | Quit |

## 🔧 Need Help?

<details>
<summary><strong>Python version error?</strong></summary>

```bash
python3 --version  # Must be 3.11+
brew install python@3.11  # macOS
```
</details>

<details>
<summary><strong>YouTube 403 Forbidden error?</strong></summary>

```bash
python3 -m pip install -U yt-dlp
```
</details>

<details>
<summary><strong>FFmpeg not found?</strong></summary>

```bash
brew install ffmpeg  # macOS
sudo apt install ffmpeg  # Ubuntu/Debian
```
</details>

<details>
<summary><strong>How much disk space do models need?</strong></summary>

Models download automatically on first use:
- **tiny**: ~75MB (fastest, least accurate)
- **base**: ~150MB (default, balanced)
- **small**: ~500MB (good quality)
- **medium/turbo**: ~1.5GB (great quality)
- **large**: ~3GB (best quality)

Cached in `~/.cache/whisper/`
</details>

---

## 📝 License

MIT License - See [LICENSE](LICENSE)

## 👨‍💻 Author

Built by [Rizwan](https://riz.codes/)

**Found this useful?** Star the repo ⭐
