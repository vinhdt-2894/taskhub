from fastapi import APIRouter

router = APIRouter(
    prefix="/api/users",
    tags=["Users"],
)


@router.get("/ping")
def ping_users():
    return {
        "module": "users",
        "status": "ok",
    }