from pytest import fixture
from .model import Doodad
from .interface import DoodadInterface


@fixture
def interface() -> DoodadInterface:
    return DoodadInterface(doodad_id=1, name="Test doodad", purpose="Test purpose")


def test_DoodadInterface_create(interface: DoodadInterface):
    assert interface


def test_DoodadInterface_works(interface: DoodadInterface):
    doodad = Doodad(**interface)
    assert doodad
