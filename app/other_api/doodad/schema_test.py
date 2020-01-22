from pytest import fixture

from .model import Doodad
from .schema import DoodadSchema
from .interface import DoodadInterface


@fixture
def schema() -> DoodadSchema:
    return DoodadSchema()


def test_DoodadSchema_create(schema: DoodadSchema):
    assert schema


def test_DoodadSchema_works(schema: DoodadSchema):
    params: DoodadInterface = schema.load(
        {"doodadId": "123", "name": "Test doodad", "purpose": "Test purpose"}
    )
    doodad = Doodad(**params)

    assert doodad.doodad_id == 123
    assert doodad.name == "Test doodad"
    assert doodad.purpose == "Test purpose"
