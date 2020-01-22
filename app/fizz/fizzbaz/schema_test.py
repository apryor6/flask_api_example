from pytest import fixture

from .model import Fizzbaz
from .schema import FizzbazSchema
from .interface import FizzbazInterface


@fixture
def schema() -> FizzbazSchema:
    return FizzbazSchema()


def test_FizzbazSchema_create(schema: FizzbazSchema):
    assert schema


def test_FizzbazSchema_works(schema: FizzbazSchema):
    params: FizzbazInterface = schema.load(
        {"fizzbazId": "123", "name": "Test fizzbaz", "purpose": "Test purpose"}
    )
    fizzbaz = Fizzbaz(**params)

    assert fizzbaz.fizzbaz_id == 123
    assert fizzbaz.name == "Test fizzbaz"
    assert fizzbaz.purpose == "Test purpose"
