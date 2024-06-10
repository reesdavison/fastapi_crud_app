from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db_models.base import Base

from .notebook_step_model import NotebookStepModel


class NotebookModel(Base):
    __tablename__ = "notebook"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    steps: Mapped[List["NotebookStepModel"]] = relationship(
        back_populates="notebook", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"NotebookModel(id={self.id!r}, " f"name={self.name!r})"
