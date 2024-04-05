import json
import requests

from random import randint
from datetime import datetime
from ariadne import ObjectType

from app.movies.models import Movie, MovieCompilation
from app.core.config import settings
from app.db.session import Session
from sqlalchemy.orm import joinedload



query_movie = ObjectType('Query')


@query_movie.field("random_movie")
def resolve_random_movie(_, info) -> dict:
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


@query_movie.field("movies")
def resolve_movies(_, info):
    with Session() as session:
        for movie in session.query(Movie).all():
            yield movie.__dict__


@query_movie.field("movie")
def resolve_movie(_, info, id):
    with Session() as session:
        movie = session.query(Movie).options(
            joinedload(Movie.compilations)
        ).get(id)
        return movie.__dict__


@query_movie.field("compilations")
def resolve_compilations(_, info):
    with Session() as session:
        for compilation in session.query(MovieCompilation).all():
            yield compilation.__dict__


@query_movie.field("compilation")
def resolve_compilation(_, info, id):
    with Session() as session:
        compilation = session.query(MovieCompilation).options(
            joinedload(MovieCompilation.movies)
        ).get(id)
        return compilation.__dict__
