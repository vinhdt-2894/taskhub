from enum import Enum

from sqlalchemy import Enum as SqlEnum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class WorkspaceRole(str, Enum):
    OWNER = "OWNER"
    EDITOR = "EDITOR"
    VIEWER = "VIEWER"


class WorkspaceMember(Base):
    __tablename__ = "workspace_members"

    workspace_id: Mapped[int] = mapped_column(
        ForeignKey("workspaces.id"), primary_key=True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), primary_key=True
    )
    role: Mapped[WorkspaceRole] = mapped_column(
        SqlEnum(
            WorkspaceRole,
            name="workspace_member_role",
            native_enum=False,
            create_constraint=True,
            validate_strings=True,
        )
    )