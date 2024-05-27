"""
Datatypes
"""
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List


class Item(BaseModel):
    item_id: int
    name: str


class OrderItem(BaseModel):
    item_id: int
    quantity: int


class Order(BaseModel):
    items: List[OrderItem]
    order_id: int = 0
    created_at: float = Field(default_factory=lambda: datetime.now().timestamp())
    status: str = None
