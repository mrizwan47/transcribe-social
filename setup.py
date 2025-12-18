from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="transcribe-social",
    version="1.0.0",
    description="Transcribe social media videos using OpenAI Whisper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Rizwan",
    author_email="hi@iamrizwan.me",
    url="https://github.com/mrizwan47/transcribe-social",
    project_urls={
        "Bug Tracker": "https://github.com/mrizwan47/transcribe-social/issues",
        "Source Code": "https://github.com/mrizwan47/transcribe-social",
    },
    scripts=["bin/transcribe-social"],
    install_requires=[
        "yt-dlp>=2023.1.6",
        "openai-whisper>=20231117",
    ],
    python_requires=">=3.11",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Video",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    keywords="transcription whisper video audio youtube instagram tiktok",
)
