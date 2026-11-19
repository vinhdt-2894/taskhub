from fastapi import APIRouter

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


@router.get("/ping", summary="Check projects API availability")
def ping_projects():
    return {"module": "projects", "status": "ok"}
