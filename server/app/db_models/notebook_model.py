from typing import List

from app.db_models.base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Notebook(Base):
    __tablename__ = "notebook"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    steps: Mapped[List["Step"]] = relationship(
        back_populates="notebook", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Notebook(id={self.id!r}, " f"name={self.name!r})"
