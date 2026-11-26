from datetime import datetime

from sqlalchemy import DateTime, Enum as SqlEnum, String, func, true
from sqlalchemy.orm import Mapped, mapped_column

from app.constants import EMAIL_MAX_LENGTH, NAME_MAX_LENGTH, PASSWORD_HASH_MAX_LENGTH
from app.db.base import Base
from app.enums import UserRole


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(EMAIL_MAX_LENGTH), unique=True)
    full_name: Mapped[str] = mapped_column(String(NAME_MAX_LENGTH))
    hashed_password: Mapped[str] = mapped_column(String(PASSWORD_HASH_MAX_LENGTH))
    role: Mapped[UserRole] = mapped_column(
        SqlEnum(
            UserRole,
            name="user_role",
            native_enum=False,
            create_constraint=True,
            validate_strings=True,
        ),
        server_default=UserRole.MEMBER.value,
    )
    is_active: Mapped[bool] = mapped_column(server_default=true())
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
