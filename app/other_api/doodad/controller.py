from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import DoodadSchema
from .service import DoodadService
from .model import Doodad
from .interface import DoodadInterface

api = Namespace("Doodad", description="A modular namespace within Other API")  # noqa


@api.route("/")
class DoodadResource(Resource):
    """Doodads"""

    @responds(schema=DoodadSchema, many=True)
    def get(self) -> List[Doodad]:
        """Get all Doodads"""

        return DoodadService.get_all()

    @accepts(schema=DoodadSchema, api=api)
    @responds(schema=DoodadSchema)
    def post(self) -> Doodad:
        """Create a Single Doodad"""

        return DoodadService.create(request.parsed_obj)


@api.route("/<int:doodadId>")
@api.param("doodadId", "Doodad database ID")
class DoodadIdResource(Resource):
    @responds(schema=DoodadSchema)
    def get(self, doodadId: int) -> Doodad:
        """Get Single Doodad"""

        return DoodadService.get_by_id(doodadId)

    def delete(self, doodadId: int) -> Response:
        """Delete Single Doodad"""
        from flask import jsonify

        print("doodadId = ", doodadId)
        id = DoodadService.delete_by_id(doodadId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=DoodadSchema, api=api)
    @responds(schema=DoodadSchema)
    def put(self, doodadId: int) -> Doodad:
        """Update Single Doodad"""

        changes: DoodadInterface = request.parsed_obj
        Doodad = DoodadService.get_by_id(doodadId)
        return DoodadService.update(Doodad, changes)
