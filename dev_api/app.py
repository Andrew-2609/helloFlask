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


@app.route('/dev/<int:developer_id>', methods=["GET", "PUT", "DELETE"])
def developer(developer_id):
    if request.method == "GET":
        found_developer = developers[developer_id]
        return jsonify(found_developer)
    elif request.method == "PUT":
        new_data = json.loads(request.data)
        developers[developer_id] = new_data
        return developers[developer_id]
    elif request.method == "DELETE":
        developers.pop(developer_id)
        return jsonify({"status": "success", "message": "entry successfully deleted"})


if __name__ == '__main__':
    app.run(debug=True)
