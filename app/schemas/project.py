from datetime import datetime

from app.enums import ProjectStatus
from app.schemas.base import BaseSchema
from app.schemas.task import TaskResponse


class ProjectResponse(BaseSchema):
    id: int
    workspace_id: int
    name: str
    description: str | None
    status: ProjectStatus
    created_at: datetime


class ProjectDetailResponse(ProjectResponse):
    tasks: list[TaskResponse]
