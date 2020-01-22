from pytest import fixture

from .model import Whatsit
from .schema import WhatsitSchema
from .interface import WhatsitInterface


@fixture
def schema() -> WhatsitSchema:
    return WhatsitSchema()


def test_WhatsitSchema_create(schema: WhatsitSchema):
    assert schema


def test_WhatsitSchema_works(schema: WhatsitSchema):
    params: WhatsitInterface = schema.load(
        {"whatsitId": "123", "name": "Test whatsit", "purpose": "Test purpose"}
    )
    whatsit = Whatsit(**params)

    assert whatsit.whatsit_id == 123
    assert whatsit.name == "Test whatsit"
    assert whatsit.purpose == "Test purpose"
