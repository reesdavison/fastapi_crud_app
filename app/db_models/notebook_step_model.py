from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db_models.base import Base
from app.enums import StepType


class NotebookStepModel(Base):
    __tablename__ = "notebook_step"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    index: Mapped[int] = mapped_column()
    type: Mapped[StepType] = mapped_column(String)
    content: Mapped[str] = mapped_column(String)
    notebook_id: Mapped[int] = mapped_column(ForeignKey("notebook.id"))
    notebook = relationship("NotebookModel", back_populates="steps")

    __table_args__ = (
        UniqueConstraint(
            "notebook_id", "index", name="_notebookd_id_index_uc", deferrable=True
        ),
    )

    def __repr__(self) -> str:
        return (
            f"Step(id={self.id!r}, "
            f"name={self.name!r}, "
            f"index={self.index!r}, "
            f"type={self.type!r}, "
            f"content={self.content!r}, "
            f"notebook_id={self.notebook_id!r})"
        )
