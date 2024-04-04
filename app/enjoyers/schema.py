from ariadne import gql


enjoyer_defs = gql("""
    input CreateUserInput {
        id: Int
        username: String!
        password: String!
    }

    type UserCreationResult {
        user: Enjoyer
        success: Boolean!
        error: String
    }

    type Enjoyer {
        id: Int
        username: String!
        password: String
        compilations: [MovieCompilation]
    }
""")
