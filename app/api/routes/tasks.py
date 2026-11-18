from fastapi import APIRouter

router = APIRouter(
    prefix="/api/tasks",
    tags=["Tasks"],
)


@router.get("/ping")
def ping_tasks():
    return {"module": "tasks", "status": "ok"}