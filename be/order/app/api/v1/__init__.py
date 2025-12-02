from fastapi import APIRouter

router = APIRouter()

from .endpoints import orders

router.include_router(orders.router, prefix="/orders", tags=["orders"])