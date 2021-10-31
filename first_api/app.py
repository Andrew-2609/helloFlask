from flask import Flask

app = Flask(__name__)


@app.route('/')
def person_api():
    return ""


if __name__ == '__main__':
    app.run(debug=True)
