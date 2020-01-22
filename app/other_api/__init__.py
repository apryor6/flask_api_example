BASE_ROUTE = "other_api"


def register_routes(api, app, root="api"):
    from flask import Blueprint
    from flask_restx import Api

    bp = Blueprint("other_api", __name__)
    api = Api(bp, title="Another API with separate Swagger docs", version="0.1.0")

    from .doodad.controller import api as doodad_api
    from .whatsit.controller import api as whatsit_api

    api.add_namespace(doodad_api, path=f"/doodad")
    api.add_namespace(whatsit_api, path=f"/whatsit")
    app.register_blueprint(bp, url_prefix=f"/{root}/{BASE_ROUTE}")
