from flask_sqlalchemy import SQLAlchemy
from typing import List
from app.test.fixtures import app, db  # noqa
from .model import Fizzbaz
from .service import FizzbazService  # noqa
from .interface import FizzbazInterface


def test_get_all(db: SQLAlchemy):  # noqa
    yin: Fizzbaz = Fizzbaz(fizzbaz_id=1, name='Yin', purpose='thing 1')
    yang: Fizzbaz = Fizzbaz(fizzbaz_id=2, name='Yang', purpose='thing 2')
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[Fizzbaz] = FizzbazService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_update(db: SQLAlchemy):  # noqa
    yin: Fizzbaz = Fizzbaz(fizzbaz_id=1, name='Yin', purpose='thing 1')

    db.session.add(yin)
    db.session.commit()
    updates: FizzbazInterface = dict(name='New Fizzbaz name')

    FizzbazService.update(yin, updates)

    result: Fizzbaz = Fizzbaz.query.get(yin.fizzbaz_id)
    assert result.name == 'New Fizzbaz name'


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: Fizzbaz = Fizzbaz(fizzbaz_id=1, name='Yin', purpose='thing 1')
    yang: Fizzbaz = Fizzbaz(fizzbaz_id=2, name='Yang', purpose='thing 2')
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    FizzbazService.delete_by_id(1)
    db.session.commit()

    results: List[Fizzbaz] = Fizzbaz.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: FizzbazInterface = dict(name='Fancy new fizzbaz', purpose='Fancy new purpose')
    FizzbazService.create(yin)
    results: List[Fizzbaz] = Fizzbaz.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]
