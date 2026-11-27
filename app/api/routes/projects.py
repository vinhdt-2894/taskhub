from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_project_detail, get_project_with_tasks
from app.core.messages import PROJECT_NOT_FOUND
from app.crud import labels, projects, tasks
from app.db.session import get_db
from app.models.project import Project
from app.schemas.error import ErrorResponse
from app.schemas.label import LabelResponse
from app.schemas.project import ProjectDetailResponse, ProjectResponse
from app.schemas.task import TaskCreate, TaskResponse

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)

PROJECT_NOT_FOUND_RESPONSE = {
    HTTPStatus.NOT_FOUND: {"model": ErrorResponse, "description": PROJECT_NOT_FOUND},
}


@router.get("/ping", summary="Check projects API availability")
def ping_projects():
    return {"module": "projects", "status": "ok"}


@router.get("", summary="List projects", response_model=list[ProjectResponse])
async def list_projects(db: Annotated[AsyncSession, Depends(get_db)]):
    return await projects.list_projects(db)


@router.get(
    "/{project_id}",
    summary="Get project details",
    response_model=ProjectDetailResponse,
    responses=PROJECT_NOT_FOUND_RESPONSE,
)
async def get_project(project: Annotated[Project, Depends(get_project_with_tasks)]):
    return project


@router.get(
    "/{project_id}/labels",
    summary="List project labels",
    response_model=list[LabelResponse],
    responses=PROJECT_NOT_FOUND_RESPONSE,
)
async def list_project_labels(
    project: Annotated[Project, Depends(get_project_detail)],
    db: Annotated[AsyncSession, Depends(get_db)],
):
    return await labels.list_labels(db, project.id)


@router.get(
    "/{project_id}/tasks",
    summary="List project tasks",
    response_model=list[TaskResponse],
    responses=PROJECT_NOT_FOUND_RESPONSE,
)
async def list_project_tasks(
    project: Annotated[Project, Depends(get_project_with_tasks)],
):
    return project.tasks


@router.post(
    "/{project_id}/tasks",
    summary="Create a project task",
    response_model=TaskResponse,
    status_code=HTTPStatus.CREATED,
    responses={
        **PROJECT_NOT_FOUND_RESPONSE,
        HTTPStatus.UNPROCESSABLE_ENTITY: {
            "description": "Invalid request body, user, or project label",
        },
    },
)
async def create_project_task(
    project_id: int,
    data: TaskCreate,
    db: Annotated[AsyncSession, Depends(get_db)],
):
    return await tasks.create_task(db, project_id, data)
