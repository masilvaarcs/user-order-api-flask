from flask import Blueprint
from controllers import user_controller

user_blueprint = Blueprint("users", __name__)

user_blueprint.route("/", methods=["GET"])(user_controller.get_users)
user_blueprint.route("/<int:user_id>", methods=["GET"])(user_controller.get_user_by_id)
user_blueprint.route("/", methods=["POST"])(user_controller.add_user)
user_blueprint.route("/<int:user_id>", methods=["PUT"])(user_controller.update_user)
user_blueprint.route("/<int:user_id>", methods=["DELETE"])(user_controller.delete_user)
