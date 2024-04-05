from ariadne import ObjectType

from app.db.session import Session
from app.movies.models import Movie, MovieCompilation
from app.movies.utils import get_random_movie

mutation_movie = ObjectType('Mutation')


@mutation_movie.field("SaveMovie")
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


@mutation_movie.field("CreateMovieCompilation")
def mutate_create_compilation(_, info, input) -> dict:
    request = info.context["request"]

    try:
        with Session() as session:
            db_compilation = MovieCompilation(
                name=input["name"],
                enjoyer_id=input["enjoyer_id"],
            )
            session.add(db_compilation)
            session.commit()
            session.refresh(db_compilation)
        return {"success": True, "compilation": db_compilation.__dict__}
    except Exception as error:
        return {
            "success": False,
            "error": str(error)
        }


@mutation_movie.field("AppendMovieToCompilation")
def mutate_movie_to_compilation(_, info, input) -> dict:
    request = info.context["request"]

    try:
        with Session() as session:
            movie = session.query(Movie).get(input["movie_id"])
            compilation = session.query(MovieCompilation).get(input["compilation_id"])

            if movie and compilation:
                compilation.movies.append(movie)
                session.add(compilation)
                session.commit()
                session.refresh(compilation)
                return {"success": True, "compilation": compilation.__dict__}

        return {"success": False, "error": "movie or compilation does not exist"}

    except Exception as error:
        return {
            "success": False,
            "error": str(error)
        }

