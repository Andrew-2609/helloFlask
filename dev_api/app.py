from flask import Flask, jsonify

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


@app.route('/dev/<int:developer_id>')
def developer(developer_id):
    found_developer = developers[developer_id]
    return jsonify(found_developer)


if __name__ == '__main__':
    app.run(debug=True)
