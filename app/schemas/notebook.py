from pydantic import BaseModel

from .notebook_step import NotebookStep


class NotebookBase(BaseModel):
    name: str


class NotebookCreate(NotebookBase):
    pass


class Notebook(NotebookBase):
    id: int
    steps: list[NotebookStep] = []

    class Config:
        orm_mode = True
        orm_mode = True
