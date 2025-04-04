from app2 import app
from models import db

with app.app_context():
    db.create_all()  # Создаст таблицы, если они не существуют
