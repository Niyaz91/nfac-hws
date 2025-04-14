from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/books/new', methods=['GET'])
def new_book():
    return render_template('new_book.html')

@app.route('/books')
def list_books():
    books = Book.query.all()
    return render_template('list_books.html', books=books)


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

    return redirect(url_for('new_book'))


if __name__ == '__main__':
    app.run(debug=True)
