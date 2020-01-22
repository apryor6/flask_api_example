from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import FizzbarSchema
from .service import FizzbarService
from .model import Fizzbar
from .interface import FizzbarInterface

api = Namespace("Fizzbar", description="A modular namespace within fizz")  # noqa


@api.route("/")
class FizzbarResource(Resource):
    """Fizzbars"""

    @responds(schema=FizzbarSchema, many=True)
    def get(self) -> List[Fizzbar]:
        """Get all Fizzbars"""

        return FizzbarService.get_all()

    @accepts(schema=FizzbarSchema, api=api)
    @responds(schema=FizzbarSchema)
    def post(self) -> Fizzbar:
        """Create a Single Fizzbar"""

        return FizzbarService.create(request.parsed_obj)


@api.route("/<int:fizzbarId>")
@api.param("fizzbarId", "Fizzbar database ID")
class FizzbarIdResource(Resource):
    @responds(schema=FizzbarSchema)
    def get(self, fizzbarId: int) -> Fizzbar:
        """Get Single Fizzbar"""

        return FizzbarService.get_by_id(fizzbarId)

    def delete(self, fizzbarId: int) -> Response:
        """Delete Single Fizzbar"""
        from flask import jsonify

        print("fizzbarId = ", fizzbarId)
        id = FizzbarService.delete_by_id(fizzbarId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=FizzbarSchema, api=api)
    @responds(schema=FizzbarSchema)
    def put(self, fizzbarId: int) -> Fizzbar:
        """Update Single Fizzbar"""

        changes: FizzbarInterface = request.parsed_obj
        Fizzbar = FizzbarService.get_by_id(fizzbarId)
        return FizzbarService.update(Fizzbar, changes)
