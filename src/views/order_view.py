from flask import Blueprint
from controllers import order_controller

order_blueprint = Blueprint("orders", __name__)

order_blueprint.route("/", methods=["GET"])(order_controller.get_orders)
order_blueprint.route("/", methods=["POST"])(order_controller.add_order)
