from pydantic import BaseModel, Field

from app.enums import StepType


class NotebookStepBase(BaseModel):
    name: str
    type: StepType
    content: str


class NotebookStepCreate(NotebookStepBase):
    prev_step_index: int | None = Field(default=None)


class NotebookStep(NotebookStepBase):
    id: int
    index: int
    notebook_id: int

    class Config:
        orm_mode = True
