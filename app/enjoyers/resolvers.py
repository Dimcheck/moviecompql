from ariadne import ObjectType

from app.enjoyers.models import Enjoyer
from app.db.session import Session


query_user = ObjectType('Query')
user = ObjectType('Enjoyer')


@query_user.field('hello')
def resolve_hello(_, info):
    request = info.context['request']
    user_agent = request.headers.get('user-agent', 'guest')
    return f'Hello {user_agent}!'


@query_user.field('users')
def resolve_users(_, info):
    with Session() as session:
        for user in session.query(Enjoyer).all():
            yield user.__dict__


@query_user.field('user')
def resolve_user(_, info, id):
    with Session() as session:
        user = session.query(Enjoyer).get(id)
        return user.__dict__

