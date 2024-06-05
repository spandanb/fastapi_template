from fastapi.testclient import TestClient

from .main import app
from .datatype import Order, OrderItem

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_post_read_order():
    order = Order(
        items=[OrderItem(item_id=100, quantity=1), OrderItem(item_id=101, quantity=2)]
    )
    data = order.dict()
    print(f"posting data: {data}")
    response = client.post("/user/1/order", json=data)
    print("post response", response)
    assert len(response.json()) > 0

    resp = client.get("/user/1/orders")
    print("Getting orders")
    print(resp.status_code)
    assert len(resp.json()) > 0
