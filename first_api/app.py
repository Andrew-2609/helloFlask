from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/<int:person_id>')
def person_api(person_id):
    return jsonify({"id": person_id, "name": "Andrew"})


if __name__ == '__main__':
    app.run(debug=True)
