from sqlalchemy import Integer, Column, String
from app import db  # noqa
from .interface import FizzbarInterface
from typing import Any


class Fizzbar(db.Model):  # type: ignore
    """A snazzy Fizzbar"""

    __tablename__ = "fizzbar"

    fizzbar_id = Column(Integer(), primary_key=True)
    name = Column(String(255))
    purpose = Column(String(255))

    def update(self, changes: FizzbarInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
