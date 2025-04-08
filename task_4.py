from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/meaning-of-life', methods=['POST'])
def meaning_of_life():
    return jsonify({"meaning": "42"})

if __name__ == '__main__':
    app.run(debug=True)


