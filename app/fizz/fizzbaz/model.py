from sqlalchemy import Integer, Column, String
from app import db  # noqa
from .interface import FizzbazInterface
from typing import Any


class Fizzbaz(db.Model):  # type: ignore
    """A snazzy Fizzbaz"""

    __tablename__ = "fizzbaz"

    fizzbaz_id = Column(Integer(), primary_key=True)
    name = Column(String(255))
    purpose = Column(String(255))

    def update(self, changes: FizzbazInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
