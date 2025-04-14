from flask import Flask, render_template, request, redirect,url_for, abort
import sqlite3


app = Flask(__name__)

def get_books(page=1, per_page=10):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    offset = (page - 1) * per_page
    cursor.execute('SELECT * FROM books LIMIT ? OFFSET ?', (per_page, offset))
    books = cursor.fetchall()
    conn.close()
    return books

def get_total_books():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM books')
    total_books = cursor.fetchone()[0]
    conn.close()
    return total_books

def get_book_by_id(book_id):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
    book = cursor.fetchone()
    conn.close()
    return book

def update_book(book_id, title, author, year, description):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE books
    SET title = ?, author = ?, year = ?, description = ?
    WHERE id = ?
    ''', (title, author, year, description, book_id))
    conn.commit()
    conn.close()

def add_book(title, author, year, description):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO books (title, author, year, description)
        VALUES (?, ?, ?, ?)
    ''', (title, author, year, description))
    conn.commit()
    conn.close()

@app.route('/books')
def books_list():
    page = request.args.get('page', 1, type=int)  # Получаем номер страницы из параметров URL
    per_page = 10
    books = get_books(page, per_page)
    total_books = get_total_books()
    total_pages = (total_books // per_page) + (1 if total_books % per_page else 0)

    return render_template('books_list.html', books=books, page=page, total_pages=total_pages)

@app.route('/books/new', methods=['GET'])
def new_book():
    return render_template('new_book.html')

@app.route('/books', methods=['POST'])
def create_book():
    title = request.form['title']
    author = request.form['author']
    year = int(request.form['year'])
    description = request.form['description']

    add_book(title, author, year, description)
    return redirect(url_for('books_list'))

@app.route('/books/<int:book_id>')
def book_detail(book_id):
    book = get_book_by_id(book_id)
    if not book:
        abort(404, description="Book not found")
    return render_template('book_detail.html', book=book)

@app.route('/books/<int:book_id>/edit', methods=['GET'])
def edit_book(book_id):
    book = get_book_by_id(book_id)
    if not book:
        abort(404, description="Book not found")

    return render_template('edit_book.html', book=book)

@app.route('/books/<int:book_id>/edit', methods=['POST'])
def update_book_details(book_id):
    book = get_book_by_id(book_id)
    if not book:
        abort(404, description="Book not found")

    # Получаем данные из формы
    title = request.form['title']
    author = request.form['author']
    year = int(request.form['year'])
    description = request.form['description']

    # Обновляем книгу в базе данных
    update_book(book_id, title, author, year, description)

    # Перенаправляем на страницу с деталями книги
    return redirect(url_for('book_detail', book_id=book_id))

@app.route('/books/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    book = get_book_by_id(book_id)
    if not book:
        abort(404, description="Book not found")

    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    conn.close()

    return redirect(url_for('books_list'))

if __name__ == '__main__':
    app.run(debug=True)
