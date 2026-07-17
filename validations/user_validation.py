


from services.user_service import  email_exists



def validate_user(data):
    errors = []

    if not data.get("username"):
        errors.append("Username is required")

    email = data.get("email")
    if not email:
        errors.append("Email is required")

    elif email_exists(email):
        errors.append("email already exists")

    if not data.get("password"):
        errors.append("Password is required")


    return errors

