#!/usr/bin/python3
"""coments"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello_hbnb():
    """cometns"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """cometns"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def show_value(text):
    """cometns"""
    return f"C {text.replace('_',' ')}"


@app.route("/python/<text>", strict_slashes=False)
def show_python_value(text="is_cool"):
    """cometns"""
    return f"Python {text.replace('_', ' ')}"


@app.route("/python", strict_slashes=False)
def show_default_value():
    """cometns"""
    return f"Python is cool"


@app.route("/number/<int:n>", strict_slashes=False)
def shows_num(n):
    """cometns"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def shows_html(n):
    """cometns"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
