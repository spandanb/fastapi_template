from typing import List

from .datatype import DBResponse, Order


class MemoryStore:
    """
    In-memory datastore.
    """
    def __init__(self):
        # user_id -> {order_id: Order}
        self.users = {}
        # globally auto-increment pk generator
        self.order_id_autoincr = 1

    def next_order_id(self) -> int:
        """
        Increments order_id and returns id
        """
        order_id = self.order_id_autoincr
        self.order_id_autoincr += 1
        return order_id

    def get_user(self, user_id: int):
        if user_id not in self.users:
            self.users[user_id] = {}
        return self.users[user_id]

    def new_order(self, user_id: int, order: Order) -> DBResponse[int]:
        """
        Create a new order and return order_id
        """
        order_id = self.next_order_id()
        user_orders = self.get_user(user_id)
        user_orders[order_id] = order
        print("user_orders_map", self.users)
        return DBResponse(data=order_id)

    def get_orders(self, user_id: int) -> DBResponse[List[Order]]:
        return DBResponse(data=list(self.get_user(user_id).values()))
