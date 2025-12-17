from setuptools import setup

setup(
    name="transcribe-reel",
    version="1.0.0",
    description="Transcribe social media videos using OpenAI Whisper",
    author="Rizwan (riz.codes)",
    author_email="hi@iamrizwan.me",
    url="https://github.com/mrizwan47/transcribe-reel",
    scripts=["bin/transcribe-reel"],
    install_requires=[
        "yt-dlp>=2023.1.6",
        "openai-whisper>=20231117",
    ],
    python_requires=">=3.11",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
