from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Infobell ... This is a test run"

app.run(host='0.0.0.0',port=int("3000"),debug=True)