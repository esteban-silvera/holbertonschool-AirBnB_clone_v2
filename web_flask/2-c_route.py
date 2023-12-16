#!/usr/bin/python3
"""
Task 2 C is fun
"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello_hbnb():
    """returns hello hbnh!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def show_value(text):
    """display “C ” followed by the value of the text variable"""
    return f"C{text.replace('_',' ')}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
