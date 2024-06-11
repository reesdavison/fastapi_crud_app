from pydantic import BaseModel, ConfigDict

from .notebook_step import NotebookStep


class NotebookBase(BaseModel):
    name: str


class NotebookCreate(NotebookBase):
    pass


class Notebook(NotebookBase):
    model_config = ConfigDict(from_attributes=True, use_enum_values=True)

    id: int
    steps: list[NotebookStep] = []
