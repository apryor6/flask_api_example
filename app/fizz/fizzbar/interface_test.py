from pytest import fixture
from .model import Fizzbar
from .interface import FizzbarInterface


@fixture
def interface() -> FizzbarInterface:
    return FizzbarInterface(fizzbar_id=1, name="Test fizzbar", purpose="Test purpose")


def test_FizzbarInterface_create(interface: FizzbarInterface):
    assert interface


def test_FizzbarInterface_works(interface: FizzbarInterface):
    fizzbar = Fizzbar(**interface)
    assert fizzbar
