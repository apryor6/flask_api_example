from pytest import fixture

from .model import Fizzbar
from .schema import FizzbarSchema
from .interface import FizzbarInterface


@fixture
def schema() -> FizzbarSchema:
    return FizzbarSchema()


def test_FizzbarSchema_create(schema: FizzbarSchema):
    assert schema


def test_FizzbarSchema_works(schema: FizzbarSchema):
    params: FizzbarInterface = schema.load(
        {"fizzbarId": "123", "name": "Test fizzbar", "purpose": "Test purpose"}
    )
    fizzbar = Fizzbar(**params)

    assert fizzbar.fizzbar_id == 123
    assert fizzbar.name == "Test fizzbar"
    assert fizzbar.purpose == "Test purpose"
