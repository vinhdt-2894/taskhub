from datetime import date, datetime
from typing import Annotated

from pydantic import Field, PositiveInt

from app.constants import TASK_TITLE_MAX_LENGTH
from app.enums import TaskPriority, TaskStatus
from app.schemas.base import BaseSchema
from app.schemas.label import LabelResponse


class TaskCreate(BaseSchema):
    title: Annotated[str, Field(min_length=1, max_length=TASK_TITLE_MAX_LENGTH)]
    description: str | None = None
    status: TaskStatus = TaskStatus.TODO
    priority: TaskPriority = TaskPriority.MEDIUM
    due_date: date | None = None
    created_by: PositiveInt
    assignee_id: PositiveInt | None = None
    label_ids: list[PositiveInt] = Field(default_factory=list)


class TaskResponse(BaseSchema):
    id: int
    project_id: int
    title: str
    description: str | None
    status: TaskStatus
    priority: TaskPriority
    due_date: date | None
    created_by: int
    assignee_id: int | None
    created_at: datetime
    labels: list[LabelResponse]
