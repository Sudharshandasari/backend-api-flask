from db.database import get_connection
from utils.jwt_handler import generate_token
import bcrypt


def create_user(data):
    conn = get_connection()
    cursor = conn.cursor()


    password = data["password"]
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    print("original:", password)
    print("hashed:", hashed_password)

    cursor.execute(

        """
        INSERT INTO users(name, email, password, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (
            data["name"],
            data["email"],
            hashed_password,
            data["created_at"]
        )
    )
    conn.commit()
    conn.close()

def email_exists(email):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        return user is not None
         
    finally:
        conn.close()

def get_user_by_email(email):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        return cursor.fetchone()
    finally:
        conn.close()

def login_user(email,password):
    user = get_user_by_email(email)
    if not user:
        return None
    
    if not bcrypt.checkpw(password.encode(), user["password"].encode()):
        return None
    
    token = generate_token(user)
    
    return{
        "user": user,
        "token": token
    }

