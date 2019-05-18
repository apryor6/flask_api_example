from fte import create_app
from fte.decorators import accepts

from fte.test.fixtures import app, client  # noqa


def test_reqparse(app):
    @app.route('/hello_world')
    def respond():
        from flask import jsonify
        return jsonify('Hello, World')
    with app.test_client() as cl:
        response = cl.get('/hello_world')

        assert response.status_code == 200
        assert response.json == 'Hello, World'
