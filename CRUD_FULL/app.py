from flask import Flask, render_template, request, redirect,url_for, abort
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
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

with app.app_context():
    db.create_all()

@app.route('/books')
def list_books():
    books = Book.query.all()
    return render_template('books_list.html', books=books)

@app.route('/books/new', methods=['GET'])
def new_book():
    return render_template('new_book.html')

@app.route('/books', methods=['POST'])
def create_book():
    title = request.form['title']
    author = request.form['author']
    year = int(request.form['year'])
    total_pages = int(request.form['total_pages'])
    genre = request.form['genre']

    new_book = Book(
        title=title,
        author=author,
        year=year,
        total_pages=total_pages,
        genre=genre
    )


    db.session.add(new_book)
    db.session.commit()

    return redirect(url_for('books_list'))

@app.route('/books/<int:book_id>')
def book_detail(book_id):
    book = get_book_by_id(book_id)
    if not book:
        abort(404, description="Not Found")
    return render_template('book_detail.html', book=book)

@app.route('/books/<int:book_id>/edit', methods=['GET'])
def edit_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        abort(404, description="Book not found")
    return render_template('edit_book.html', book=book)

@app.route('/books/<int:book_id>/edit', methods=['POST'])
def update_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        abort(404, description="Book not found")

    book.title = request.form['title']
    book.author = request.form['author']
    book.year = int(request.form['year'])
    book.total_pages = int(request.form['total_pages'])
    book.genre = request.form['genre']

    db.session.commit()

    return redirect(url_for('book_detail', book_id=book.id))

@app.route('/books/<int:book_id>/delete', methods=['GET'])
def delete_book_form(book_id):
    book = Book.query.get(book_id)
    if not book:
        abort(404, description="Book not found")
    return render_template('delete_book.html', book=book)

@app.route('/books/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        abort(404, description="Book not found")

    db.session.delete(book)
    db.session.commit()

    return redirect(url_for('list_books'))

'''def get_books(page=1, per_page=10):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    offset = (page - 1) * per_page
    cursor.execute('SELECT * FROM books LIMIT ? OFFSET ?', (per_page, offset))
    books = cursor.fetchall()
    conn.close()
    return books'''

def get_book_by_id(book_id):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
    book = cursor.fetchone()
    conn.close()
    return book

@app.route('/books')
def books_list():
    page = request.args.get('page', 1, type=int)
    books = get_books(page)
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM books')
    total_books = cursor.fetchone()[0]
    conn.close()

    total_pages = (total_books // 10) + (1 if total_books % 10 else 0)

    return render_template('books_list.html', books=books, page=page, total_pages=total_pages)


if __name__ == '__main__':
    app.run(debug=True)
