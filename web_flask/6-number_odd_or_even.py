#!/usr/bin/python3
"""cometn"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """cometns"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """cometns"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c_text(text):
    """cometns"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python_text(text="is cool"):
    """cometns"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    """cometns"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_number_template(n):
    """cometns"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def display_number_odd_or_even(n):
    """cometns"""
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html",
                               n=n, odd_or_even="even")
    else:
        return render_template("6-number_odd_or_even.html",
                               n=n, odd_or_even="odd")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
