from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.models.project import Project
from app.models.task import Task


async def list_projects(db: AsyncSession) -> Sequence[Project]:
    result = await db.scalars(select(Project).order_by(Project.id))
    return result.all()


async def get_project(db: AsyncSession, project_id: int) -> Project | None:
    return await db.get(Project, project_id)


async def get_project_with_tasks(db: AsyncSession, project_id: int) -> Project | None:
    statement = (
        select(Project)
        .where(Project.id == project_id)
        .options(joinedload(Project.tasks).joinedload(Task.labels))
    )
    result = await db.scalars(statement)
    return result.unique().one_or_none()
