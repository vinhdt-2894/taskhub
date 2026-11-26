from app.schemas.base import BaseSchema


class LabelResponse(BaseSchema):
    id: int
    project_id: int
    name: str
    color: str
