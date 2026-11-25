from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import labels
from app.db.session import get_db
from app.schemas.label import LabelResponse

router = APIRouter(prefix="/tags", tags=["Tags"])


@router.get("", response_model=list[LabelResponse])
async def list_tags(db: Annotated[AsyncSession, Depends(get_db)]):
    return await labels.list_labels(db)
