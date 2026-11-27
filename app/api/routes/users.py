from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from app.constants import USERNAME_MAX_LENGTH
from app.core.exceptions import UserNotFoundError
from app.core.messages import USER_NOT_FOUND
from app.crud import users
from app.db.session import get_db
from app.schemas.error import ErrorResponse
from app.schemas.user import UserProfileResponse

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/ping", summary="Check users API availability")
def ping_users():
    return {
        "module": "users",
        "status": "ok",
    }


@router.get(
    "/{username}/profile",
    summary="Get a user profile by username",
    response_model=UserProfileResponse,
    responses={
        HTTPStatus.NOT_FOUND: {"model": ErrorResponse, "description": USER_NOT_FOUND},
    },
)
async def get_user_profile(
    username: Annotated[str, Path(min_length=1, max_length=USERNAME_MAX_LENGTH)],
    db: Annotated[AsyncSession, Depends(get_db)],
):
    user = await users.get_user_by_username(db, username)
    if user is None:
        raise UserNotFoundError()
    return user
