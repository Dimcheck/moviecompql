from ariadne import gql


query_defs = gql("""
    type Query {
        hello: String!

        user(id: Int): Enjoyer!
        users: [Enjoyer]!

        random_movie: Movie!
        movie(id: Int): Movie!
        movies: [Movie]!

        compilation(id: Int): MovieCompilation!
        compilations: [MovieCompilation]!
    }


    type Mutation {
        SaveMovie: MovieCreationResult
        CreateUser(input: CreateUserInput!): UserCreationResult!
        CreateMovieCompilation(input: CreateMovieCompilationInput!): MovieCompilationCreationResult!
        AppendMovieToCompilation(input: AppendMovieToCompilationInput!): MovieCompilationCreationResult!
    }



""")
