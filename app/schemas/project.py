from datetime import datetime

from app.enums import ProjectStatus
from app.schemas.base import BaseSchema


class ProjectResponse(BaseSchema):
    id: int
    workspace_id: int
    name: str
    description: str | None
    status: ProjectStatus
    created_at: datetime
