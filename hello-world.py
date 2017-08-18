from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    response_body = 'Hello World! <br/><br/>' + \
                   'Welcome to a Python application, deployed by Ansible <br/>' + \
                   '<img src="./static/python-logo.png" width="260" height="77" />'

    return response_body
