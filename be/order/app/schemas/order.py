from pydantic import BaseModel
from typing import Optional

class OrderBase(BaseModel):
    customer_id: int
    product_id: int
    quantity: int

class OrderCreate(OrderBase):
    pass

class OrderUpdate(OrderBase):
    status: Optional[str] = None

class Order(OrderBase):
    id: int
    status: str

    class Config:
        orm_mode = True