# VideoMaker

## Description
VideoMaker is a project that allows you to generate a short-content video for platforms such as Youtube Shorts or Tiktok based on a text prompt using Bing Copilot, OpenAI Whisper and DALL-E 2 and Google Text to Speech.

## Installation
1. Clone the repository
2. Install the required dependencies: `pip install -r requirements.txt`
3. Replace in `main.py` the 19th line of code `api_key = ` with your own OpenAI API Key

## Usage
1. Run the script: `python main.py`
2. You will be asked to give the title of the video based on which the video will be themed on
3. Your video will be generated and saved in the specified output directory.

## Features
- Video editing
- Image and text overlays
- OpenAI API integration
  - Whisper for subtitles
  - DALL-E 2 for images
- Google Text to Speech voice
- Audio synchronization