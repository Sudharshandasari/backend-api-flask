from flask import Blueprint, request
from services.user_service import (
    create_user,
    login_user
)

from validations.user_validation import validate_user
from utils.response import (
    success_response,
    error_response
)

user_bp = Blueprint("user_bp", __name__)
@user_bp.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    errors = validate_user(data)
    if errors:
        return error_response(errors), 400
    create_user(data)
    return success_response("User created successfully")


@user_bp.route("/login_user", methods=["POST"])
def login():

    data = request.get_json()

    result = login_user(
        data.get("email"),
        data.get("password")
    )

    if not result:
        return error_response(
            "Invalid email or password"
        ), 401

    return success_response(
        {
            "user": {
                "id": result["user"]["id"],
                "name": result["user"]["name"],
                "email": result["user"]["email"]
            },
            "token": result["token"]
        },
        "login successful"
    )




