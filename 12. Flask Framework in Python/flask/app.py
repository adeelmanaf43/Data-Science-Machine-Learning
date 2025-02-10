from flask import Flask


'''
It creates an instance of the Flask class
which will be your WSGI (Web Server Gateway Interface) application.
'''


# WSGI Application
app = Flask(__name__)


# create a basic route

@app.route(rule="/")
def welcome():
    return "Welcome to this best of the best Flask Course. This should be an amazing course"


@app.route(rule="/index")
def index():
    return "Welcome to the index page"


if __name__ == "__main__":
    app.run(debug=True)
