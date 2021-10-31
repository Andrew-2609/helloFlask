from flask import Flask, jsonify, request
import json

app = Flask(__name__)

developers = [
    {
        "name": "Andrew Monteiro",
        "skills": ["Java", "Python"]
    },
    {
        "name": "Leandro Lima",
        "skills": ["Java", "JavaScript"]
    }
]


@app.route('/dev/<int:developer_id>', methods=["GET", "PUT"])
def developer(developer_id):
    if request.method == "GET":
        found_developer = developers[developer_id]
        return jsonify(found_developer)
    elif request.method == "PUT":
        new_data = json.loads(request.data)
        developers[developer_id] = new_data
        return developers[developer_id]


if __name__ == '__main__':
    app.run(debug=True)
