import json
import random

def generate_playlist(city, mood):
    with open("data/city_moods.json", "r") as file:
        data = json.load(file)

    mood_key = f"{city.lower()}_{mood.lower()}"
    return data.get(mood_key, random.sample(data.get("default", []), 5))
