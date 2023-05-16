from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def run_python_function():
    # Perform some operation here
    return jsonify({'result': 'Python function executed successfully!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
