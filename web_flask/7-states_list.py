#!/usr/bin/python3
"""coments"""


from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with the states listed in alphabetical order"""
    states = sorted(storage.all("State").values(), key=lambda x: x.name)
    return render_template('states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
