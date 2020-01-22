from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import FizzbazSchema
from .service import FizzbazService
from .model import Fizzbaz
from .interface import FizzbazInterface

api = Namespace("Fizzbaz", description="A modular namespace within fizz")  # noqa


@api.route("/")
class FizzbazResource(Resource):
    """Fizzbaz"""

    @responds(schema=FizzbazSchema, many=True)
    def get(self) -> List[Fizzbaz]:
        """Get all Fizzbaz"""

        return FizzbazService.get_all()

    @accepts(schema=FizzbazSchema, api=api)
    @responds(schema=FizzbazSchema)
    def post(self) -> Fizzbaz:
        """Create a Single Fizzbaz"""

        return FizzbazService.create(request.parsed_obj)


@api.route("/<int:fizzbazId>")
@api.param("fizzbazId", "Fizzbaz database ID")
class FizzbazIdResource(Resource):
    @responds(schema=FizzbazSchema)
    def get(self, fizzbazId: int) -> Fizzbaz:
        """Get Single Fizzbaz"""

        return FizzbazService.get_by_id(fizzbazId)

    def delete(self, fizzbazId: int) -> Response:
        """Delete Single Fizzbaz"""
        from flask import jsonify

        id = FizzbazService.delete_by_id(fizzbazId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=FizzbazSchema, api=api)
    @responds(schema=FizzbazSchema)
    def put(self, fizzbazId: int) -> Fizzbaz:
        """Update Single Fizzbaz"""

        changes: FizzbazInterface = request.parsed_obj
        Fizzbaz = FizzbazService.get_by_id(fizzbazId)
        return FizzbazService.update(Fizzbaz, changes)
