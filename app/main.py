from fastapi import FastAPI
from pydantic import BaseModel

from app.config import settings

app = FastAPI(title=settings.app_name, version=settings.app_version)


class HealthResponse(BaseModel):
    status: str
    version: str


@app.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(status="ok", version=settings.app_version)
