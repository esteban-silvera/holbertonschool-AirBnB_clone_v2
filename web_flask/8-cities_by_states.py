#!/usr/bin/python3
"""coments"""


from flask import Flask, render_template
from ..models import storage, State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """comets"""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """comet"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
