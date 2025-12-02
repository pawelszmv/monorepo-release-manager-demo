from fastapi import APIRouter, HTTPException
from app.schemas.order import OrderCreate, OrderRead, OrderUpdate
from app.services.order_service import OrderService

router = APIRouter()
order_service = OrderService()

@router.post("/", response_model=OrderRead)
async def create_order(order: OrderCreate):
    return await order_service.create_order(order)

@router.get("/{order_id}", response_model=OrderRead)
async def get_order(order_id: int):
    order = await order_service.get_order(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.put("/{order_id}", response_model=OrderRead)
async def update_order(order_id: int, order: OrderUpdate):
    updated_order = await order_service.update_order(order_id, order)
    if updated_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated_order

@router.delete("/{order_id}", response_model=dict)
async def delete_order(order_id: int):
    success = await order_service.delete_order(order_id)
    if not success:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"detail": "Order deleted successfully"}