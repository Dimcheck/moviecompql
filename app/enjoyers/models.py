from app.db.session import Base

from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String


class Enjoyer(Base):
    __tablename__ = "enjoyer"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(30), unique=True)
    password: Mapped[str] = mapped_column(String(30))

    compilations: Mapped[List["MovieCompilation"]] = relationship(back_populates="enjoyer")

    def __repr__(self) -> str:
        return f"Enjoyer(id={self.id!r}, username={self.username!r},)"


