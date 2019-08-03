from flask_sqlalchemy import SQLAlchemy
from typing import List
from app.test.fixtures import app, db  # noqa
from .model import Whatsit
from .service import WhatsitService  # noqa
from .interface import WhatsitInterface


def test_get_all(db: SQLAlchemy):  # noqa
    yin: Whatsit = Whatsit(whatsit_id=1, name="Yin", purpose="thing 1")
    yang: Whatsit = Whatsit(whatsit_id=2, name="Yang", purpose="thing 2")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[Whatsit] = WhatsitService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_update(db: SQLAlchemy):  # noqa
    yin: Whatsit = Whatsit(whatsit_id=1, name="Yin", purpose="thing 1")

    db.session.add(yin)
    db.session.commit()
    updates: WhatsitInterface = dict(name="New Whatsit name")

    WhatsitService.update(yin, updates)

    result: Whatsit = Whatsit.query.get(yin.whatsit_id)
    assert result.name == "New Whatsit name"


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: Whatsit = Whatsit(whatsit_id=1, name="Yin", purpose="thing 1")
    yang: Whatsit = Whatsit(whatsit_id=2, name="Yang", purpose="thing 2")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    WhatsitService.delete_by_id(1)
    db.session.commit()

    results: List[Whatsit] = Whatsit.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: WhatsitInterface = dict(name="Fancy new whatsit", purpose="Fancy new purpose")
    WhatsitService.create(yin)
    results: List[Whatsit] = Whatsit.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]
