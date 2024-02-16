import os
import asyncio
import pydub
from openai import OpenAI
from pydub.silence import detect_silence, split_on_silence, detect_nonsilent
from sydney import SydneyClient
import gtts
from pydub import AudioSegment
import numpy
import apikey
import openai
import requests
from PIL import Image
import json
import convert_json


#here you need to put your OpenAI api key
client = OpenAI(
    api_key = apikey.apiKey().get(),
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
# text = '''What is the capital of France?
#
# If you are curious about the capital of France, you might be surprised to learn that it has not always been Paris. Paris is the current and most populous capital of France, with more than 2 million residents in an area of 105 square kilometres. It is also one of the world's major centres of culture, fashion, and gastronomy, and it is known as the City of Light for its role in the Enlightenment and its early street lighting system.
#
# But Paris was not always the seat of power in France. In fact, throughout history, the capital has changed several times, depending on the political and religious circumstances of the time. Some of the other cities that have served as the capital of France include:
#
# - Reims: The city where most of the French kings were crowned, Reims was the capital during the Merovingian dynasty (5th-8th centuries) and again during World War I, when Paris was threatened by German invasion.
# - Aachen: The city where Charlemagne, the first emperor of the Holy Roman Empire, established his court, Aachen was the capital of the Carolingian dynasty (8th-10th centuries).
# - Orléans: The city where Joan of Arc lifted the siege by the English during the Hundred Years' War, Orléans was the capital of the Valois dynasty (14th-16th centuries).
# - Versailles: The city where Louis XIV built his magnificent palace, Versailles was the capital of the Bourbon dynasty (17th-18th centuries) until the French Revolution.
# - Vichy: The city where Marshal Pétain established his collaborationist regime, Vichy was the capital of France during World War II, while Paris was occupied by Nazi Germany.
#
# As you can see, Paris has not always been the undisputed capital of France. However, since 1871, after the end of the Franco-Prussian War and the Paris Commune, Paris has remained the official and permanent capital of France. It is also one of the most visited and admired cities in the world, with many iconic landmarks such as the Eiffel Tower, Notre-Dame Cathedral, and the Louvre Museum.
# '''

#AUDIO GENERATION

# print("read file sound1.wav")
# audio = AudioSegment.from_file("sound1.wav", format="wav")
# print("changing playback speed")
# audio = audio.speedup(playback_speed=1.25)
# print("changed playback speed, exporting")
# audio.export("sound2.wav", format="wav")
# print("exported")

#remove the silent parts from audio using pydub

#IMAGE GENERATION

def generate_image(text):
    for i in range(1):
        response = openai.Image.create(
            prompt = text,
            n = 1,
            size = "1920x1080",
            response_format="b64_json",
        )
        json_file = f"{text[:10]}--{response['created']}.json"
        with open(json_file, mode="w", encoding="utf-8") as file:
            json.dump(response, file, ensure_ascii=False, indent=2)
        print(f"Image saved to {json_file}")
        convert_json.convert(json_file)

generate_image(title)



