from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    data = {
        'key_one': 1,
        'key_two': 2,
        'key_three': 3
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run('0.0.0.0')
