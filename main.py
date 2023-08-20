# Import what we need from flask
from flask import Flask

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
def main():
    @app.route('/')
    def index():
        return 'Hello, world!'

    @app.route('/cow')
    def cow():
        return 'MOoooOo!'

@app.route('/test')
def test():
    return 'Test successfull'

    def sum(a,b):
        return a + b

    