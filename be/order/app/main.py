from fastapi import FastAPI
from app.api.v1.endpoints import orders

app = FastAPI()

app.include_router(orders.router, prefix="/api/v1/orders", tags=["orders"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Order Management API"}