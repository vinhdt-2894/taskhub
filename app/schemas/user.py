from datetime import datetime

from app.schemas.base import BaseSchema


class UserProfileResponse(BaseSchema):
    id: int
    username: str
    full_name: str
    created_at: datetime
