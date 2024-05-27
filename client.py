"""
Emulates a client to app/main.py.
"""
import requests
from app.datatype import Order, OrderItem

base_url = "http://127.0.0.1:8000"


def get_orders():
    resp = requests.get(base_url + "/user/1/orders")
    print("Getting orders")
    print(resp.status_code)
    print(resp.json())


def post_order():
    order = Order(
        items=[OrderItem(item_id=100, quantity=1), OrderItem(item_id=101, quantity=2)]
    )
    data = order.dict()
    print(f"posting data: {data}")
    # note:  requests.post(data=DICT_OBJECT) will form encode the the dict; to send json, use `json` param
    resp = requests.post(base_url + "/user/1/order", json=data)
    print(resp.status_code)
    print(resp.json())


post_order()
get_orders()


