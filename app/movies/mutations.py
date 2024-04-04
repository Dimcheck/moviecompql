from ariadne import ObjectType

from app.db.session import Session
from app.movies.models import Movie
from app.movies.utils import get_random_movie

mutation_movie = ObjectType('Mutation')


@mutation_movie.field('SaveMovie')
def mutate_random_movie(_, info) -> dict:
    movie = get_random_movie()
    request = info.context["request"]

    try:
        with Session() as session:
            db_movie = Movie(
                name=movie['name'],
                director=movie['director'],
                release_date=movie['release_date'],
                cast=movie['cast'],
            )
            session.add(db_movie)
            session.commit()
        return {"success": True, "movie": movie}
    except Exception as error:
        return {
            "success": False,
            "error": str(error)
        }

