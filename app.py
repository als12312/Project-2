# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World! This is the Flask web application.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
