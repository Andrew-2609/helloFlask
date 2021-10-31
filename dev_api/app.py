from flask import Flask, jsonify, request
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

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


# noinspection PyBroadException
@app.route('/dev/<int:developer_id>', methods=["GET", "PUT", "DELETE"])
def developer(developer_id):
    if request.method == "GET":
        try:
            response = developers[developer_id]
        except IndexError:
            response = {"status": "error", "message": "developer not found"}
        except Exception:
            error_message = "unknown error, please get in touch with the API administrator (33224456789)"
            response = {"status": "error", "message": error_message}
        return jsonify(response)
    elif request.method == "PUT":
        new_data = json.loads(request.data)
        developers[developer_id] = new_data
        return developers[developer_id]
    elif request.method == "DELETE":
        developers.pop(developer_id)
        return jsonify({"status": "success", "message": "entry successfully deleted"})


if __name__ == '__main__':
    app.run(debug=True)
