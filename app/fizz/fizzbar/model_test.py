from pytest import fixture
from flask_sqlalchemy import SQLAlchemy
from app.test.fixtures import app, db  # noqa
from .model import Fizzbar


@fixture
def fizzbar() -> Fizzbar:
    return Fizzbar(fizzbar_id=1, name="Test fizzbar", purpose="Test purpose")


def test_Fizzbar_create(fizzbar: Fizzbar):
    assert fizzbar


def test_Fizzbar_retrieve(fizzbar: Fizzbar, db: SQLAlchemy):  # noqa
    db.session.add(fizzbar)
    db.session.commit()
    s = Fizzbar.query.first()
    assert s.__dict__ == fizzbar.__dict__
