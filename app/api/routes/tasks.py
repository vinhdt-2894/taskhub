from fastapi import APIRouter

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.get("/ping", summary="Check tasks API availability")
def ping_tasks():
    return {"module": "tasks", "status": "ok"}
