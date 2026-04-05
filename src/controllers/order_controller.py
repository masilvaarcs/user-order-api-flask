from flask import jsonify, request
from models.order_model import Order

orders_db = [
    Order(1, 1, "Laptop"),
    Order(2, 2, "Phone"),
    Order(3, 1, "Tablet"),
    Order(4, 3, "Keyboard"),
    Order(5, 2, "Mouse"),
    Order(6, 4, "Monitor"),
    Order(7, 5, "Printer"),
    Order(8, 3, "Webcam"),
    Order(9, 6, "Headphones"),
    Order(10, 7, "Smartwatch"),
]


def get_orders():
    return jsonify([order.to_dict() for order in orders_db])


def add_order():
    new_order_data = request.get_json()
    new_order = Order(
        len(orders_db) + 1, new_order_data["user_id"], new_order_data["item"]
    )
    orders_db.append(new_order)
    return jsonify(new_order.to_dict()), 201
