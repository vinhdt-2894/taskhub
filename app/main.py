from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import api_router
from app.db.session import engine


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    try:
        yield
    finally:
        await engine.dispose()


app = FastAPI(
    title="TaskHub API",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/health", tags=["Health"], summary="Check TaskHub API health")
def health():
    return {"status": "ok"}


app.include_router(api_router)
