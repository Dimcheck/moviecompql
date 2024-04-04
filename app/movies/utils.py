import json
import requests

from random import randint
from datetime import datetime

from app.core.config import settings


def get_random_movie() -> dict:
    imdb_id = randint(1000000, 2000000)

    try:
        movie = requests.get(url=f'https://www.omdbapi.com/?i=tt{imdb_id}&apikey={settings.OMDB_KEY}')
        movie = json.loads(movie.content)
        result = {
            "name": movie.get("Title"),
            "release_date": datetime.strptime(movie.get("Year"), "%Y"),
            "director": movie.get("Director"),
            "cast": movie.get("Actors"),
        }
    except (TypeError, ValueError):
        return {
            "name": movie.get("Title"),
            "director": movie.get("Director"),
            "cast": movie.get("Actors"),
        }

    return result

