from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'  # база данных SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    total_pages = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Book {self.title} by {self.author}>"

# Создание таблиц
with app.app_context():
    db.create_all()
