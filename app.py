import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Путь к базе данных
DATABASE = 'cars.db'


# Функция для получения подключения к базе данных
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Чтобы результаты запросов можно было получать как словари
    return conn


# Функция для выполнения запроса и возвращения результата
def query_db(query, args=(), one=False):
    conn = get_db()
    cur = conn.execute(query, args)
    rv = cur.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv


# Функция для выполнения запроса без возврата результатов
def execute_db(query, args=()):
    conn = get_db()
    conn.execute(query, args)
    conn.commit()
    conn.close()


# Инициализация базы данных
def init_db():
    with app.app_context():
        conn = get_db()
        # Создание таблицы cars, если она не существует
        conn.execute('''
            CREATE TABLE IF NOT EXISTS cars (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                year INTEGER NOT NULL
            )
        ''')
        conn.commit()


# Запуск инициализации базы данных
init_db()


# Реализация поиска машин (GET /cars/search)
@app.route('/cars/search', methods=['GET'])
def search_cars():
    car_name = request.args.get('car_name', '')  # Получаем параметр car_name из запроса
    query = 'SELECT * FROM cars WHERE name LIKE ?'
    cars = query_db(query, [f'%{car_name}%'])
    return render_template('cars/search.html', cars=cars, car_name=car_name)


# Реализация добавления машины (POST /cars/new)
@app.route('/cars/new', methods=['GET', 'POST'])
def new_car():
    if request.method == 'POST':
        name = request.form['name']
        year = request.form['year']

        # Добавляем новую машину в базу данных
        query = 'INSERT INTO cars (name, year) VALUES (?, ?)'
        execute_db(query, [name, year])

        # Редирект на страницу с машинами
        return redirect(url_for('get_cars'))

    return render_template('cars/new.html')


# Получение всех машин (GET /cars)
@app.route('/cars', methods=['GET'])
def get_cars():
    cars = query_db('SELECT * FROM cars')
    return render_template('cars/index.html', cars=cars)


# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)
