"""
Template HTTP API server that exposes endpoints:
1. POST /user/{user_id}/order {order_items: OrderItems}
    - creates an order
2. GET /users/{user_id}/orders
    - gets all orders
"""

import logging
from fastapi import FastAPI
from .datatype import Order
from .data_store import MemoryStore
from .utils import config_logging

# section: globals

app = FastAPI()
store = MemoryStore()
config_logging()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/user/{user_id}/order")
def post_order(user_id: int, order: Order):
    """
    Receives order and returns order_id.
    Order_id is generated by the datastore
    """
    logging.info(f"In post_order, received user_id: {user_id}, order: {order}")
    order_id = store.new_order(user_id, order)
    return {"order_id": order_id}


@app.get("/user/{user_id}/orders")
def get_orders(user_id: int):
    return store.get_orders(user_id)


