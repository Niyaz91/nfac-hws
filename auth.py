# auth.py
import jwt
from fastapi import Request, HTTPException
from datetime import datetime, timedelta

SECRET = "supersecret"

def create_jwt(user_id: int):
    payload = {"user_id": user_id, "exp": datetime.utcnow() + timedelta(days=1)}
    return jwt.encode(payload, SECRET, algorithm="HS256")

def get_user_id_from_jwt(request: Request):
    token = request.cookies.get("token")
    if not token:
        raise HTTPException(status_code=401, detail="Unauthorized")
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return payload["user_id"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
