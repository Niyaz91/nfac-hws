from fastapi import FastAPI
from routers import auth, flowers, purchased

app = FastAPI()

app.include_router(auth.router)
app.include_router(flowers.router)
app.include_router(purchased.router)
