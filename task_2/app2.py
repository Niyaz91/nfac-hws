from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Инициализация приложения и базы данных
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'  # Путь к базе данных SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Модель для книги
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    total_pages = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Book {self.title} by {self.author}>"

# Создание таблиц в базе данных
with app.app_context():
    db.create_all()

# Обработчик маршрута GET для отображения формы
@app.route('/books/new', methods=['GET'])
def new_book():
    return render_template('new_book.html')

@app.route('/books')
def list_books():
    books = Book.query.all()  # Получаем все книги из базы данных
    return render_template('list_books.html', books=books)

# Обработчик маршрута POST для создания новой книги
@app.route('/books', methods=['POST'])
def create_book():
    title = request.form['title']
    author = request.form['author']
    year = int(request.form['year'])
    total_pages = int(request.form['total_pages'])
    genre = request.form['genre']

    # Создание нового объекта книги
    new_book = Book(
        title=title,
        author=author,
        year=year,
        total_pages=total_pages,
        genre=genre
    )

    # Добавление книги в базу данных
    db.session.add(new_book)
    db.session.commit()

    return redirect(url_for('new_book'))  # Перенаправление обратно на страницу создания книги

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)
