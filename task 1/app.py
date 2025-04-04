from flask import Flask, render_template, request, abort
import sqlite3

app = Flask(__name__)

def get_books(page=1, per_page=10):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    offset = (page - 1) * per_page
    cursor.execute('SELECT * FROM books LIMIT ? OFFSET ?', (per_page, offset))
    books = cursor.fetchall()
    conn.close()
    return books

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

# Детальная информация о книге
@app.route('/books/<int:book_id>')
def book_detail(book_id):
    book = get_book_by_id(book_id)
    if not book:
        abort(404, description="Not Found")
    return render_template('book_detail.html', book=book)

if __name__ == '__main__':
    app.run(debug=True)
