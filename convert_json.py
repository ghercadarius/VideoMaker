#source: https://realpython.com/generate-images-with-dalle-openai-api/#call-the-api-from-a-python-script

import json
from base64 import b64decode
from pathlib import Path

def convert(json_file):
    JSON_FILE = Path(json_file)

    with open(JSON_FILE, mode="r", encoding="utf-8") as file:
        response = json.load(file)

    for index, image_dict in enumerate(response["data"]):
        image_data = b64decode(image_dict["b64_json"])
        image_file = f"{JSON_FILE.stem}-{index}.png"
        with open(image_file, mode="wb") as png:
            png.write(image_data)
