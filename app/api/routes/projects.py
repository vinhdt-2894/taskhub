from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import projects
from app.db.session import get_db
from app.schemas.project import ProjectResponse

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


@router.get("/ping", summary="Check projects API availability")
def ping_projects():
    return {"module": "projects", "status": "ok"}


@router.get("", response_model=list[ProjectResponse])
async def list_projects(db: Annotated[AsyncSession, Depends(get_db)]):
    return await projects.list_projects(db)


@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(
    project_id: int, db: Annotated[AsyncSession, Depends(get_db)]
):
    project = await projects.get_project(db, project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project
