from flask_sqlalchemy import SQLAlchemy
from typing import List
from app.test.fixtures import app, db  # noqa
from .model import Doodad
from .service import DoodadService  # noqa
from .interface import DoodadInterface


def test_get_all(db: SQLAlchemy):  # noqa
    yin: Doodad = Doodad(doodad_id=1, name="Yin", purpose="thing 1")
    yang: Doodad = Doodad(doodad_id=2, name="Yang", purpose="thing 2")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[Doodad] = DoodadService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_update(db: SQLAlchemy):  # noqa
    yin: Doodad = Doodad(doodad_id=1, name="Yin", purpose="thing 1")

    db.session.add(yin)
    db.session.commit()
    updates: DoodadInterface = dict(name="New Doodad name")

    DoodadService.update(yin, updates)

    result: Doodad = Doodad.query.get(yin.doodad_id)
    assert result.name == "New Doodad name"


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: Doodad = Doodad(doodad_id=1, name="Yin", purpose="thing 1")
    yang: Doodad = Doodad(doodad_id=2, name="Yang", purpose="thing 2")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    DoodadService.delete_by_id(1)
    db.session.commit()

    results: List[Doodad] = Doodad.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: DoodadInterface = dict(name="Fancy new doodad", purpose="Fancy new purpose")
    DoodadService.create(yin)
    results: List[Doodad] = Doodad.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]
