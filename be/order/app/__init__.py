from fastapi import FastAPI

app = FastAPI()

from .api.v1 import endpoints

app.include_router(endpoints.router, prefix="/api/v1", tags=["orders"])