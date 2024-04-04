from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.core.config import settings


engine = create_engine(settings.DATABASE_URL)
Session = sessionmaker(engine)


class Base(DeclarativeBase):
    ...
