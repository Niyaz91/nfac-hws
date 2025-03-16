from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

cars = [
    {"id": 1, "name": "Ford Taurus", "year": "2019"},
    {"id": 2, "name": "Toyota Camry", "year": "2020"},
    {"id": 3, "name": "Honda Accord", "year": "2018"},
    {"id": 4, "name": "BMW X5", "year": "2021"},
    {"id": 5, "name": "Audi A6", "year": "2017"},
    {"id": 6, "name": "Chevrolet Malibu", "year": "2019"},
    {"id": 7, "name": "Nissan Altima", "year": "2020"},
    {"id": 8, "name": "Hyundai Sonata", "year": "2022"},
    {"id": 9, "name": "Kia Optima", "year": "2020"},
    {"id": 10, "name": "Mazda 6", "year": "2019"},
    {"id": 11, "name": "Ford Fusion", "year": "2020"},
    {"id": 12, "name": "Toyota Corolla", "year": "2021"},
    {"id": 13, "name": "Honda Civic", "year": "2022"},
    {"id": 14, "name": "BMW 3 Series", "year": "2020"},
    {"id": 15, "name": "Mercedes-Benz C-Class", "year": "2021"}
    ]

users = [
    {"id": 1, "email": "test@test.com", "first_name": "Aibek", "last_name": "Bekturov", "username": "deadly_knight95"},
    {"id": 2, "email": "john@example.com", "first_name": "John", "last_name": "Doe", "username": "john_doe"},
    {"id": 3, "email": "alice@example.com", "first_name": "Alice", "last_name": "Johnson", "username": "alice_johnson"},
    {"id": 4, "email": "bob@example.com", "first_name": "Bob", "last_name": "Smith", "username": "bob_smith"},
    {"id": 5, "email": "mary@example.com", "first_name": "Mary", "last_name": "Johnson", "username": "mary_johnson"},
    {"id": 6, "email": "paul@example.com", "first_name": "Paul", "last_name": "Walker", "username": "paul_walker"},
    {"id": 7, "email": "jane@example.com", "first_name": "Jane", "last_name": "Doe", "username": "jane_doe"},
    {"id": 8, "email": "mike@example.com", "first_name": "Mike", "last_name": "Jones", "username": "mike_jones"},
    {"id": 9, "email": "lucy@example.com", "first_name": "Lucy", "last_name": "Brown", "username": "lucy_brown"},
    {"id": 10, "email": "mark@example.com", "first_name": "Mark", "last_name": "Davis", "username": "mark_davis"}
]

@app.route('/cars', methods = ['GET'])
def get_cars():
    page = int(request.args.get('page',1))
    limit = int(request.args.get('limit',10))
    start = (page - 1) * limit
    end = start + limit
    paginated_cars = cars[start:end]

    return jsonify(paginated_cars)

@app.route('/cars/<int:id>', methods=['GET'])
def get_car_by_id(id):
    car = next((car for car in cars if car['id'] == id), None)
    if car:
        return jsonify(car)
    else:
        return "Not found", 404

@app.route('/users', methods=['GET'])
def get_users():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))

    start = (page - 1) * limit
    end = start + limit
    paginated_users = users[start:end]

    user_table = """
    <table>
        <tr><th>Username</th><th>Name</th></tr>
        {% for user in users %}
        <tr>
            <td>{{ user.username }}</td>
            <td><a href="/users/{{ user.id }}">{{ user.first_name }} {{ user.last_name }}</a></td>
        </tr>
        {% endfor %}
    </table>
    """
    return render_template_string(user_table, users=paginated_users)

@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = next((user for user in users if user['id'] == id), None)
    if user:
        user_info = f"""
        <h1>{user['first_name']} {user['last_name']}</h1>
        <p>Email: {user['email']}</p>
        <p>Username: {user['username']}</p>
        """
        return render_template_string(user_info)
    else:
        return "User not found", 404

if __name__ == '__main__':
    app.run(debug=True)

