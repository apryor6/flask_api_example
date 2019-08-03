from pytest import fixture
from .model import Whatsit
from .interface import WhatsitInterface


@fixture
def interface() -> WhatsitInterface:
    return WhatsitInterface(whatsit_id=1, name="Test whatsit", purpose="Test purpose")


def test_WhatsitInterface_create(interface: WhatsitInterface):
    assert interface


def test_WhatsitInterface_works(interface: WhatsitInterface):
    whatsit = Whatsit(**interface)
    assert whatsit
