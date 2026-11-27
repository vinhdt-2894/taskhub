from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import ProjectNotFoundError
from app.crud import projects
from app.db.session import get_db
from app.models.project import Project


async def get_project_detail(
    project_id: int, db: Annotated[AsyncSession, Depends(get_db)]
) -> Project:
    project = await projects.get_project(db, project_id)
    if project is None:
        raise ProjectNotFoundError()
    return project


async def get_project_with_tasks(
    project_id: int, db: Annotated[AsyncSession, Depends(get_db)]
) -> Project:
    project = await projects.get_project_with_tasks(db, project_id)
    if project is None:
        raise ProjectNotFoundError()
    return project
