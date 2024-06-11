from pydantic import BaseModel, ConfigDict, Field

from app.enums import StepType


class NotebookStepBase(BaseModel):
    name: str
    type: StepType
    content: str


class NotebookStepCreate(NotebookStepBase):
    prev_step_id: int | None = Field(default=None)


class NotebookStep(NotebookStepBase):
    model_config = ConfigDict(from_attributes=True, use_enum_values=True)

    id: int
    index: int
    notebook_id: int
