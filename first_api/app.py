from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route('/<int:person_id>')
def person_api(person_id):
    return jsonify({"id": person_id, "name": "Andrew"})


@app.route('/sum/get/<int:first_value>/<int:second_value>')
def sum_get(first_value, second_value):
    total = first_value + second_value
    return jsonify({"sum": total})


@app.route('/sum/post', methods=["POST"])
def sum_post():
    data = json.loads(request.data)
    total = sum(data['values'])
    return jsonify({"sum": total})


if __name__ == '__main__':
    app.run(debug=True)
