from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="TaskHub API",
    version="0.1.0",
)


@app.get("/health", tags=["Health"], summary="Check TaskHub API health")
def health():
    return {"status": "ok"}


app.include_router(api_router)
