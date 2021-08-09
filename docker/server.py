from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World! Username: " + os.environ.get('USERNAME') + " Password: " + os.environ.get('PASSWORD')
