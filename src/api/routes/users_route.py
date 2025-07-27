from quart import Blueprint, request, jsonify, Response

from src.controllers import UsersController


users_bp = Blueprint("users/", __name__)


@users_bp.route("/", methods=["POST"])
async def create_user() -> tuple[Response, int]:
    data: dict = await request.get_json()
    response = await UsersController().create_user(data)

    body: dict = response["body"]
    status: int = response["status"]

    return jsonify(body), status
