from app.db.session import Base

from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Table, Column


movie_comp_association_table = Table(
    "movie_comp_association_table",
    Base.metadata,
    Column("compilation_id", ForeignKey("movie_compilation.id"), primary_key=True),
    Column("movie_id", ForeignKey("movie.id"), primary_key=True),
)


class MovieCompilation(Base):
    __tablename__ = "movie_compilation"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150))

    enjoyer_id: Mapped[Optional[int]] = mapped_column(ForeignKey("enjoyer.id"))
    enjoyer: Mapped["Enjoyer"] = relationship(back_populates="compilations")

    movies: Mapped[List["Movie"]] = relationship(
        secondary=movie_comp_association_table,
        back_populates="compilations",
    )

    def __repr__(self) -> str:
        return f"MovieCompilation(id={self.id!r}, name={self.name!r},)"


class Movie(Base):
    __tablename__ = "movie"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150))
    release_date: Mapped[str] = mapped_column(String(25), nullable=True)
    director: Mapped[str] = mapped_column(String(100))
    cast: Mapped[str] = mapped_column(String(300))

    compilations: Mapped[Optional["MovieCompilation"]] = relationship(
        secondary=movie_comp_association_table,
        back_populates="movies",
    )

    def __repr__(self) -> str:
        return f"Movie(id={self.id!r}, name={self.name!r},)"

