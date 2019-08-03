from pytest import fixture
from .model import Fizzbaz
from .interface import FizzbazInterface


@fixture
def interface() -> FizzbazInterface:
    return FizzbazInterface(fizzbaz_id=1, name="Test fizzbaz", purpose="Test purpose")


def test_FizzbazInterface_create(interface: FizzbazInterface):
    assert interface


def test_FizzbazInterface_works(interface: FizzbazInterface):
    fizzbaz = Fizzbaz(**interface)
    assert fizzbaz
