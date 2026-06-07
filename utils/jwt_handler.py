import jwt
def generate_token(user):

    payload = {
        "user_id": user["id"],
        "email": user["email"]
    }
