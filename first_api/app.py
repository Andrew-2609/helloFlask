from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def person_api():
    return jsonify({"name": "Andrew"})


if __name__ == '__main__':
    app.run(debug=True)
