from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Enum as SqlEnum, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.constants import NAME_MAX_LENGTH
from app.db.base import Base
from app.enums import ProjectStatus

if TYPE_CHECKING:
    from app.models.task import Task


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    workspace_id: Mapped[int] = mapped_column(
        ForeignKey("workspaces.id", ondelete="CASCADE"), index=True
    )
    name: Mapped[str] = mapped_column(String(NAME_MAX_LENGTH))
    description: Mapped[str | None] = mapped_column(Text)
    status: Mapped[ProjectStatus] = mapped_column(
        SqlEnum(
            ProjectStatus,
            name="project_status",
            native_enum=False,
            create_constraint=True,
            validate_strings=True,
        ),
        server_default=ProjectStatus.ACTIVE.value,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    tasks: Mapped[list["Task"]] = relationship(
        back_populates="project", order_by="Task.id", lazy="raise", passive_deletes="all"
    )
