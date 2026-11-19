from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/ping", summary="Check users API availability")
def ping_users():
    return {
        "module": "users",
        "status": "ok",
    }
