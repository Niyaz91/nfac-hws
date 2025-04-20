from fastapi import FastAPI, Form, Request, Response, Depends, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from auth import create_jwt, get_user_id_from_jwt
from repositories.users import UsersRepository
from repositories.flowers import FlowersRepository
from repositories.purchases import PurchasesRepository

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

users_repo = UsersRepository()
flowers_repo = FlowersRepository()
purchases_repo = PurchasesRepository()

### --- AUTH ---
@app.get("/signup", response_class=HTMLResponse)
async def get_signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@app.post("/signup")
async def post_signup(request: Request, email: str = Form(), name: str = Form(), password: str = Form()):
    filename = None
    users_repo.add_user(email, name, password)
    return RedirectResponse("/login", status_code=302)

@app.get("/login", response_class=HTMLResponse)
async def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def post_login(response: Response, email: str = Form(), password: str = Form()):
    user = users_repo.find_by_email(email)
    if user and user.password == password:
        token = create_jwt(user.id)
        response = RedirectResponse("/profile", status_code=302)
        response.set_cookie("token", token)
        return response
    return RedirectResponse("/login", status_code=302)

@app.get("/profile", response_class=HTMLResponse)
async def get_profile(request: Request):
    user_id = get_user_id_from_jwt(request)
    user = users_repo.find_by_id(user_id)
    return templates.TemplateResponse("profile.html", {"request": request, "user": user})

### --- FLOWERS ---
@app.get("/flowers", response_class=HTMLResponse)
async def get_flowers(request: Request):
    flowers = flowers_repo.list_flowers()
    return templates.TemplateResponse("flowers.html", {"request": request, "flowers": flowers})

@app.post("/flowers")
async def post_flower(name: str = Form(), quantity: int = Form(), price: float = Form()):
    flowers_repo.add_flower(name, quantity, price)
    return RedirectResponse("/flowers", status_code=302)

### --- CART ---
@app.post("/cart/items")
async def add_to_cart(response: Response, request: Request, flower_id: int = Form()):
    cart = request.cookies.get("cart", "")
    cart_items = cart.split(",") if cart else []
    cart_items.append(str(flower_id))
    response = RedirectResponse("/flowers", status_code=302)
    response.set_cookie("cart", ",".join(cart_items))
    return response

@app.get("/cart/items", response_class=HTMLResponse)
async def get_cart_items(request: Request):
    cart = request.cookies.get("cart", "")
    ids = list(map(int, cart.split(","))) if cart else []
    items = [flowers_repo.find_by_id(i) for i in ids]
    total = sum(f.price for f in items if f)
    return templates.TemplateResponse("cart.html", {"request": request, "items": items, "total": total})

### --- PURCHASED ---
@app.post("/purchased")
async def post_purchased(request: Request, response: Response):
    user_id = get_user_id_from_jwt(request)
    cart = request.cookies.get("cart", "")
    ids = list(map(int, cart.split(","))) if cart else []
    for i in ids:
        purchases_repo.add_purchase(user_id, i)
    response = RedirectResponse("/purchased", status_code=302)
    response.set_cookie("cart", "")  # clear cart
    return response

@app.get("/purchased", response_class=HTMLResponse)
async def get_purchased(request: Request):
    user_id = get_user_id_from_jwt(request)
    purchases = purchases_repo.get_user_purchases(user_id)
    flowers = [flowers_repo.find_by_id(p.flower_id) for p in purchases]
    return templates.TemplateResponse("purchased.html", {"request": request, "flowers": flowers})
