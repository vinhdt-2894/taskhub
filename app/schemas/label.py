from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StringConstraints, field_validator

from app.constants import NAME_MAX_LENGTH

LabelName = Annotated[
    str,
    StringConstraints(strip_whitespace=True, min_length=1, max_length=NAME_MAX_LENGTH),
]
LabelColor = Annotated[str, Field(pattern=r"^#[0-9A-Fa-f]{6}$")]


class LabelCreate(BaseModel):
    project_id: Annotated[int, Field(gt=0)]
    name: LabelName
    color: LabelColor


class LabelUpdate(BaseModel):
    name: LabelName | None = None
    color: LabelColor | None = None

    @field_validator("name", "color")
    @classmethod
    def reject_null(cls, value: str | None) -> str:
        if value is None:
            raise ValueError("field cannot be null")
        return value


class LabelResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    project_id: int
    name: str
    color: str
