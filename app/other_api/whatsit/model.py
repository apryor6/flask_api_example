from sqlalchemy import Integer, Column, String
from app import db  # noqa
from .interface import WhatsitInterface
from typing import Any


class Whatsit(db.Model):  # type: ignore
    """A snazzy Whatsit"""

    __tablename__ = "whatsit"

    whatsit_id = Column(Integer(), primary_key=True)
    name = Column(String(255))
    purpose = Column(String(255))

    def update(self, changes: WhatsitInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
