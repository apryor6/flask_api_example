def create_bp(env=None):
    from flask import Blueprint, jsonify
    from flask_sqlalchemy import SQLAlchemy
    from flask_restx import Api, Resource, Namespace

    bp = Blueprint("Example third party API", __name__)
    api = Api(bp, title="Flaskerific API", version="0.1.0")
    ns = Namespace("Third party hello world API")

    @ns.route("/")
    class ExampleResource(Resource):
        def get(self):
            return "I'm a third party API!"

    api.add_namespace(ns, path="/hello_world")
    return bp
