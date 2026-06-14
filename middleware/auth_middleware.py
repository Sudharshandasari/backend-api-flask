from functools import wraps
from flask import request, g

from utils.jwt_handler import verify_token
from services.user_service import get_user_by_id
from utils.response import error_response

def login_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return error_response("Authorization header is missing"), 401
        
        token = auth_header.split(" ")[1] if " " in auth_header else auth_header
        payload = verify_token(token)
        if not payload:
            return error_response("Invalid or expired token"), 401
        user = get_user_by_id(payload["user_id"])

        if not user:
            return error_response("user not found"), 401
        g.user = user
        return f(*args, **kwargs)
    

    return decorated
