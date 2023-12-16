#!/usr/bin/python3
"""
Task 6 is odd or even
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
    return f"C {text.replace('_',' ')}"


@app.route("/python/<text>", strict_slashes=False)
def show_python_value(text="is_cool"):
    """Display “Python ” followed by the value of the text"""
    return f"Python {text.replace('_', ' ')}"


@app.route("/python", strict_slashes=False)
def show_default_value():
    """displays python is cool"""
    return f"Python is cool"


@app.route("/number/<int:n>", strict_slashes=False)
def shows_num(n):
    """displays "n is a number only if it is"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def shows_html(n):
    """displays a HTML page if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def shows_odd_even(n):
    """displays a HTML page if n is an integer"""
    return render_template("6-number_odd_or_even", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
