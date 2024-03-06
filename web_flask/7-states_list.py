#!/usr/bin/python3
"""coments"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """coment"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """coment"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda x: x.name)
    return render_template('states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
