from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.label import Label


async def list_labels(db: AsyncSession) -> Sequence[Label]:
    result = await db.scalars(select(Label).order_by(Label.id))
    return result.all()
