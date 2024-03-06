#!/usr/bin/python3
"""coments"""

from flask import Flask


def create_app():
    """coments function"""
    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def hello():
        return 'Hello HBNB!'

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
