from pytest import fixture
from flask_sqlalchemy import SQLAlchemy
from app.test.fixtures import app, db  # noqa
from .model import Fizzbaz


@fixture
def fizzbaz() -> Fizzbaz:
    return Fizzbaz(fizzbaz_id=1, name="Test fizzbaz", purpose="Test purpose")


def test_Fizzbaz_create(fizzbaz: Fizzbaz):
    assert fizzbaz


def test_Fizzbaz_retrieve(fizzbaz: Fizzbaz, db: SQLAlchemy):  # noqa
    db.session.add(fizzbaz)
    db.session.commit()
    s = Fizzbaz.query.first()
    assert s.__dict__ == fizzbaz.__dict__
