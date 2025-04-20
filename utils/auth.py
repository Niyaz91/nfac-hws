# utils/auth.py

from passlib.hash import bcrypt
from jose import jwt
from datetime import datetime, timedelta

SECRET = "your-secret-key"

def hash_password(password):
    return bcrypt.hash(password)

def verify_password(password, password_hash):
    return bcrypt.verify(password, password_hash)

def create_token(user_id: int):
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(days=1)
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return payload["user_id"]
    except:
        return None
