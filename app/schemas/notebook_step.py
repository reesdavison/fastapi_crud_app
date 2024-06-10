from pydantic import BaseModel

from app.enums import StepType


class NotebookStepBase(BaseModel):
    name: str
    type: StepType
    content: str
    notebook_id: int


class NotebookStepCreate(NotebookStepBase):
    pass


class NotebookStep(NotebookStepBase):
    id: int
    index: int

    class Config:
        orm_mode = True
