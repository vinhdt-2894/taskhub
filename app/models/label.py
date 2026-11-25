from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.constants import LABEL_COLOR_MAX_LENGTH, NAME_MAX_LENGTH
from app.db.base import Base


class Label(Base):
    __tablename__ = "labels"
    __table_args__ = (
        UniqueConstraint("project_id", "name", name="uq_labels_project_id_name"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id", ondelete="CASCADE")
    )
    name: Mapped[str] = mapped_column(String(NAME_MAX_LENGTH))
    color: Mapped[str] = mapped_column(String(LABEL_COLOR_MAX_LENGTH))
