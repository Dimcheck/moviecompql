from ariadne import gql


movie_defs = gql("""
    input CreateMovieCompilationInput {
        name: String!
    }

    input AppendMovieToCompilationInput {
        movie_id: Int!
        compilation_id: Int!
    }

    type MovieCompilationCreationResult {
        compilation: MovieCompilation
        success: Boolean!
        error: String
    }

    type MovieCreationResult {
        movie: Movie
        success: Boolean!
        error: String
    }

    type Movie {
        name: String
        release_date: String
        director: String!
        cast: String!
        compilations: [MovieCompilation]
    }

    type MovieCompilation {
        name: String!
        enjoyer_id: Int
        movies: [Movie]
    }


""")

