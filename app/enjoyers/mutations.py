from ariadne import ObjectType

from app.enjoyers.models import Enjoyer
from app.db.session import Session
from time import time, sleep

mutation_user = ObjectType('Mutation')


@mutation_user.field('CreateUser')
def mutate_create_user(_, info, input):
    request = info.context["request"]

    try:
        with Session() as session:
            db_enjoyer = Enjoyer(
                username=input["username"],
                password=input["password"],
            )
            session.add(db_enjoyer)
            session.commit()
            session.refresh(db_enjoyer, ['username', 'id'])
        return {"success": True, "user": db_enjoyer.__dict__}

    except Exception as error:
        return {
            "success": False,
            "error": str(error)
        }

