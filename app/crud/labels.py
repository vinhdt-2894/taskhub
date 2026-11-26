from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.label import Label


async def list_labels(db: AsyncSession, project_id: int) -> Sequence[Label]:
    statement = select(Label).where(Label.project_id == project_id).order_by(Label.id)
    result = await db.scalars(statement)
    return result.all()
