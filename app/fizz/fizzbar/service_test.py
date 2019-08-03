from flask_sqlalchemy import SQLAlchemy
from typing import List
from app.test.fixtures import app, db  # noqa
from .model import Fizzbar
from .service import FizzbarService  # noqa
from .interface import FizzbarInterface


def test_get_all(db: SQLAlchemy):  # noqa
    yin: Fizzbar = Fizzbar(fizzbar_id=1, name="Yin", purpose="thing 1")
    yang: Fizzbar = Fizzbar(fizzbar_id=2, name="Yang", purpose="thing 2")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[Fizzbar] = FizzbarService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_update(db: SQLAlchemy):  # noqa
    yin: Fizzbar = Fizzbar(fizzbar_id=1, name="Yin", purpose="thing 1")

    db.session.add(yin)
    db.session.commit()
    updates: FizzbarInterface = dict(name="New Fizzbar name")

    FizzbarService.update(yin, updates)

    result: Fizzbar = Fizzbar.query.get(yin.fizzbar_id)
    assert result.name == "New Fizzbar name"


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: Fizzbar = Fizzbar(fizzbar_id=1, name="Yin", purpose="thing 1")
    yang: Fizzbar = Fizzbar(fizzbar_id=2, name="Yang", purpose="thing 2")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    FizzbarService.delete_by_id(1)
    db.session.commit()

    results: List[Fizzbar] = Fizzbar.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: FizzbarInterface = dict(name="Fancy new fizzbar", purpose="Fancy new purpose")
    FizzbarService.create(yin)
    results: List[Fizzbar] = Fizzbar.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]
