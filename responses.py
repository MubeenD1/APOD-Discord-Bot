from typing import Final
import os
from dotenv import load_dotenv
import requests
from random import choice

#Load Nasa Token
load_dotenv()
NTOKEN: Final[str] = os.getenv("NASA_TOKEN")

def get_apod(NTOKEN):
    url = f"https://api.nasa.gov/planetary/apod?api_key={NTOKEN}"
    response = requests.get(url)
    data = response.json()
    return data

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == "~":
        return "What do you want from me...?"
    elif "~hello" in lowered or "~hey" in lowered:
        greet = ["Hello there cowboy!", "Hey there cowboy!", "Hiya!", "Heyo!", "Heyy!", "Hello!"]
        return choice(greet)
    elif "~apod" in lowered and "~explanation" not in lowered:
        data = get_apod(NTOKEN)
        image_url = data.get("url")
        explanation = data.get("explanation")

        if image_url:
            return f"\nHere is Nasa's Astronomy Picture of the Day!\n{image_url}"
        else:
            return "Could not retrieve image"    
    elif "~apod" in lowered and "~explanation" in lowered:
        data = get_apod(NTOKEN)
        image_url = data.get("url")
        explanation = data.get("explanation")

        if image_url:
            return f"\nHere is Nasa's Astronomy Picture of the Day!\n{image_url}\nHere's their explanation:\n{explanation}"
        else:
            return "Could not retrieve image"
