import random
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def generate_random_number():
    return jsonify({'random_number': random.randint(1, 100)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
