from setuptools import setup

setup(
    name="transcribe-reel",
    version="1.0.0",
    description="Transcribe Instagram/TikTok reels and YouTube shorts using Whisper",
    author="Rizwan (riz.codes)",
    author_email="hi@iamrizwan.me",
    url="https://github.com/mrizwan47/transcribe-reel",
    scripts=["bin/transcribe-reel"],
    install_requires=[
        "yt-dlp",
        "openai-whisper",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
