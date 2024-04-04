from fastapi import FastAPI
from ariadne.asgi import GraphQL
from ariadne import make_executable_schema

from app.movies.resolvers import query_movie
from app.movies.schema import movie_defs
from app.movies.mutations import mutation_movie

from app.enjoyers.resolvers import query_user, user
from app.enjoyers.mutations import mutation_user
from app.enjoyers.schema import enjoyer_defs

from app.schema import query_defs
from app.core import tasks


app = FastAPI()
app.add_event_handler("startup", tasks.create_start_app_handler(app))
app.add_event_handler("shutdown", tasks.create_stop_app_handler(app))

app.mount(
    "/graphql/",
    GraphQL(
        make_executable_schema(
            [enjoyer_defs, movie_defs, query_defs],
            [query_user, user, mutation_user, query_movie, mutation_movie,]
        ),
        debug=True,
    )
)
