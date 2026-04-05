from flask import Flask
from flask_cors import CORS

from views.user_view import user_blueprint
from views.order_view import order_blueprint

app = Flask(__name__)

CORS(
    app,
    resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE"]}},
)

app.register_blueprint(user_blueprint, url_prefix="/users")
app.register_blueprint(order_blueprint, url_prefix="/orders")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
