#!/usr/bin/python3
"""coment"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def list_states():
    """coment"""
    states = storage.all("State").values()
    return render_template('states.html', states=states)


@app.route('/states/<state_id>', strict_slashes=False)
def state_cities(state_id):
    """coment"""
    state = storage.get("State", state_id)
    if state:
        cities = state.cities
        return render_template('state_cities.html', state=state, cities=cities)
    else:
        return render_template('not_found.html')


@app.teardown_appcontext
def teardown_db(exception):
    """coment"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
