from fastapi import APIRouter

from app.api.routes import users, projects, tasks

api_router = APIRouter(prefix="/api")

api_router.include_router(users.router)
api_router.include_router(projects.router)
api_router.include_router(tasks.router)
