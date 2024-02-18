import os
import asyncio
import pydub
import moviepy
from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.audio.fx.volumex import volumex
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip
import moviepy.editor
from openai import OpenAI
from pydub.silence import detect_silence, split_on_silence, detect_nonsilent
from sydney import SydneyClient
import gtts
from pydub import AudioSegment
import numpy
import openai
import requests
from PIL import Image
import json
import convert_json
import base64
from io import BytesIO
import cv2
import os
from ffmpeg import FFmpeg


#here you need to put your OpenAI api key
client = OpenAI(
    api_key = os.getenv('OPENAI_API_KEY'),
)

def query_sydney(prompt):
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(get_result(prompt))
    return result

async def get_result(prompt):
    print("entered get_result")
    sydney = SydneyClient()
    #start conversation
    await sydney.start_conversation()
    print("started conversation")
    #give prompt
    response = await sydney.compose(prompt, format = "blogpost", tone = "informational", length = "short")
    print(response)
    #close conversation
    await sydney.close_conversation()
    print("closed conversation")
    return response

title = "What is the capital of France?"

# text = query_sydney(title)
text = '''What is the capital of France?

Paris, with its timeless elegance and rich cultural heritage, stands as one of the world’s most captivating cities. Nestled along the Seine River, it exudes an irresistible allure that has drawn artists, poets, and dreamers for centuries.

Gastronomy: Imagine savoring a flaky croissant at a cozy café, the aroma of freshly brewed coffee mingling with the morning mist. Parisians take their culinary art seriously, and every meal is a celebration of flavor. From Michelin-starred restaurants to bustling street markets, the city is a gastronomic paradise.

Fashion and Haute Couture: Paris is the birthplace of haute couture, where fashion becomes poetry. The elegant boulevards showcase designer boutiques, and the Champs-Élysées sparkles with luxury. Here, style is not just clothing; it’s an expression of individuality.

Art and Literature: Wander through the Louvre, where the Mona Lisa smiles mysteriously, or lose yourself in the pages of a book at Shakespeare and Company. Paris breathes art—its streets adorned with sculptures, its walls echoing the footsteps of Hemingway and Proust.

The Eiffel Tower: An iconic silhouette against the sky, the Eiffel Tower stands tall, a testament to human ingenuity. Climb its iron lattice steps, and as the city unfolds beneath you, feel the heartbeat of Paris.

Romance: Paris whispers love stories. Stroll along the Seine at sunset, hand in hand, the river reflecting the city’s golden hues. The Pont des Arts, adorned with love locks, bears witness to countless promises made.

Intellectual Hub: Paris reverberates with ideas. Cafés host spirited debates, and the Sorbonne nurtures brilliant minds. The City of Light has illuminated the works of Voltaire, Sartre, and Camus.

Nightfall: As twilight descends, the city transforms. The Eiffel Tower shimmers, the Sacré-Cœur glows atop Montmartre, and the streets come alive with laughter. Parisians embrace joie de vivre—the joy of living.

In this timeless tapestry, Paris weaves together history, passion, and dreams. It’s more than a city; it’s a symphony—a melody that lingers long after you’ve bid it “au revoir.”'''

# AUDIO GENERATION
# sound1 = gtts.gTTS(text, slow = False)
# sound1.save("sound1.wav")

# AUDIO MANIPULATION

# print("read file sound1.wav")
# audio = AudioSegment.from_file("sound1.wav", format="wav")
# print("changing playback speed")
# audio = audio.speedup(playback_speed=1.25)
# print("changed playback speed, exporting")
# audio.export("sound2.wav", format="wav")
# print("exported")

#remove the silent parts from audio using pydub

#IMAGE GENERATION

# def generate_image(text):
#         response = client.images.generate(prompt = text, model="dall-e-2", n = 5, response_format="b64_json", size="1024x1024", user = "user123")
#         json_file = "image_json.json"
#         image_data_list = []
#         result = []
#         for image in response.data:
#             image_data_list.append(image.model_dump()["b64_json"])
#         image_objects = []
#         for i, data in enumerate(image_data_list):
#             image_objects.append(Image.open(BytesIO(base64.b64decode(data))))
#             image_objects[i].save(f"image{i}.png")
#             result.append(f"image{i}.png")
#             print("saved image")

# images_names = generate_image(title)
# images_names = ["image0.png", "image1.png", "image2.png", "image3.png", "image4.png"]

#modify image sizes

# for image in images_names:
#     with Image.open(image) as img:
#         img = img.resize((1080, 1920))
#         img.save(image)
#         print(f"resized image {image} successfully")

# VIDEO GENERATION

# frame_width, frame_height = 1080, 1920
# fps = 30
# num_frames = fps * 12
# video_title = "video.mp4"
# video_writer = cv2.VideoWriter(video_title, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))
# print(f"made video file {video_title}")
#
# for image in images_names:
#     frame = cv2.imread(image)
#     for x in range(num_frames):
#         video_writer.write(frame)
#     print(f"added image {image} to video for {num_frames} frames")
#     # video_writer.write(frame)
#
# video_writer.release()
# cv2.destroyAllWindows()

# LINK AUDIO SPEECH TO VIDEO

# clip the sound2.wav to match the length of the video
print("read file sound2.wav")
audio = AudioSegment.from_file("sound2.wav", format="wav")
audio = audio[: 60 * 1000]
audio.export("sound2.wav", format="wav")
print("exported sound2.wav")

print("read file background_audio.wav")
audio = AudioSegment.from_file("background_audio.wav", format="wav")
audio = audio[: 60 * 1000]
audio.export("background_audio.wav", format="wav")
print("exported background_audio.wav")

# create the subtitles for the sound2.wav file based on text
print("opened sound2.wav for subtitles")
audioSub = open("sound2.wav", "rb")
transcript = client.audio.transcriptions.create(
    file=audioSub,
    model="whisper-1",
    response_format="srt"
)
#write transcript in a srt file
with open("subtitles.srt", "w") as file:
    file.write(transcript)
print("created subtitles")
audioSub.close()
# print(transcript)

# load video and audio

video_clip = VideoFileClip("video.mp4")
audio_clip = AudioFileClip("sound2.wav")
background_audio = AudioFileClip("background_audio.wav")
#
volume_factor = 1
# bigger -> louder, smaller -> quieter
audio_clip = volumex(audio_clip, volume_factor)
volume_factor = 0.2
background_audio = volumex(background_audio, volume_factor)
final_audio = CompositeAudioClip([audio_clip, background_audio])
print("added audio")
final_clip = video_clip.set_audio(final_audio)
print("set audio")
final_clip.write_videofile("final_video.mp4", codec="libx264", audio_codec="aac")
print("exported successfully without subtitles")
final_clip.close()

# add subtitles to the video
ffmpeg = (
    FFmpeg()
    .input("final_video.mp4")
    .input("subtitles.srt")
    .output("final_video_with_subtitles.mp4", vf="subtitles=subtitles.srt")
)
ffmpeg.execute()
print("exported successfully with subtitles")







