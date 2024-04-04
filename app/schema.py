from ariadne import gql


query_defs = gql("""
    type Query {
        hello: String!
        user(id: Int): Enjoyer!
        users: [Enjoyer]!
        movie: Movie
    }


    type Mutation {
        SaveMovie: MovieCreationResult
        CreateUser(input: CreateUserInput!): UserCreationResult!
        CreateMovieCompilation(input: CreateMovieCompilationInput!): MovieCompilationCreationResult!
        AppendMovieToCompilation(input: AppendMovieToCompilationInput!): MovieCompilationCreationResult!
    }



""")
