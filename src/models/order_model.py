class Order:
    def __init__(self, order_id: int, user_id: int, item: str):
        self.order_id = order_id
        self.user_id = user_id
        self.item = item

    def to_dict(self):
        return {"order_id": self.order_id, "user_id": self.user_id, "item": self.item}
