from fastapi import FastAPI, UploadFile, Form, Depends, HTTPException, status
from repositories.users import UsersRepository
from auth import create_token, verify_token, oauth2_scheme
import hashlib

app = FastAPI()
users_repo = UsersRepository()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.post("/signup")
async def signup(username: str = Form(), password: str = Form()):
    try:
        users_repo.add_user(username, hash_password(password))
    except ValueError:
        raise HTTPException(status_code=400, detail="User already exists")
    return {"message": "Registered"}

@app.post("/login")
def login(username: str = Form(), password: str = Form()):
    user = users_repo.get_user(username)
    if not user or user.password_hash != hash_password(password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_token({"sub": username})
    return {"access_token": token, "type": "bearer"}

@app.get("/profile")
def profile(token: str = Depends(oauth2_scheme)):
    username = verify_token(token)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = users_repo.get_user(username)
    print("DEBUG: user object:", user)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "username": user.username,
    }

from repositories.flowers import FlowersRepository
from schemas import Flower
from fastapi import Form

flowers_repo = FlowersRepository()

@app.post("/flowers")
def add_flower(name: str = Form(), price: float = Form()):
    flower_id = flowers_repo.add_flower(name, price)
    return {"id": flower_id}

@app.get("/flowers", response_model=list[Flower])
def get_flowers():
    return flowers_repo.list_flowers()

from fastapi import Cookie, Response, Request
import json

def get_cart_from_cookie(cart_cookie: str | None) -> list[int]:
    if not cart_cookie:
        return []
    try:
        return json.loads(cart_cookie)
    except:
        return []

@app.post("/cart/items")
def add_to_cart(
    request: Request,
    response: Response,
    flower_id: int = Form(),
    cart: str = Cookie(default=None)
):
    cart_items = get_cart_from_cookie(cart)
    cart_items.append(flower_id)
    response.set_cookie(key="cart", value=json.dumps(cart_items))
    return {"message": "Item added to cart"}

@app.get("/cart/items")
def get_cart_items(cart: str = Cookie(default=None)):
    cart_items = get_cart_from_cookie(cart)
    flowers = [flowers_repo.get_by_id(fid) for fid in cart_items if flowers_repo.get_by_id(fid)]
    total = sum(f.price for f in flowers)
    return {
        "items": [{"id": f.id, "name": f.name, "price": f.price} for f in flowers],
        "total_price": total
    }

from repositories.purchases import PurchasesRepository

purchases_repo = PurchasesRepository()

@app.post("/purchased")
def purchase_items(
    request: Request,
    response: Response,
    token: str = Depends(oauth2_scheme),
    cart: str = Cookie(default=None)
):
    username = verify_token(token)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid token")

    cart_items = get_cart_from_cookie(cart)
    for fid in cart_items:
        purchases_repo.add_purchase(username, fid)

    response.set_cookie(key="cart", value=json.dumps([]))  # Очистить корзину
    return {"message": "Items purchased"}

@app.get("/purchased")
def get_purchased(token: str = Depends(oauth2_scheme)):
    username = verify_token(token)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid token")

    user_purchases = purchases_repo.get_user_purchases(username)
    flower_objs = [flowers_repo.get_by_id(p.flower_id) for p in user_purchases]
    return [{
        "name": f.name,
        "price": f.price
    } for f in flower_objs if f]


