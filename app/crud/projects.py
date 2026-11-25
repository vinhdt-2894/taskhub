from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.project import Project


async def list_projects(db: AsyncSession) -> Sequence[Project]:
    result = await db.scalars(select(Project).order_by(Project.id))
    return result.all()


async def get_project(db: AsyncSession, project_id: int) -> Project | None:
    return await db.get(Project, project_id)
