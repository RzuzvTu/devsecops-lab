from flask import Flask, request, jsonify
from app.database import get_user
from app.config import DEBUG

app = Flask(__name__)


@app.route("/user")
def user():
    username = request.args.get("username")
    result = get_user(username)
    return jsonify({"user": result})


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=DEBUG)
