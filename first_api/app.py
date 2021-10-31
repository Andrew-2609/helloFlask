from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/<int:person_id>')
def person_api(person_id):
    return jsonify({"id": person_id, "name": "Andrew"})


@app.route('/sum/get/<int:first_value>/<int:second_value>')
def sum_get(first_value, second_value):
    total = first_value + second_value
    return jsonify({"sum": total})


if __name__ == '__main__':
    app.run(debug=True)
