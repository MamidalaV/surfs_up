from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'

# app = Flask(__name__)
# @app.route('/WelcomePage')
# def second_route():
#     return 'Second Route'

