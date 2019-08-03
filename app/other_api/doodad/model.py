from sqlalchemy import Integer, Column, String
from app import db  # noqa
from .interface import DoodadInterface
from typing import Any


class Doodad(db.Model):  # type: ignore
    """A snazzy Doodad"""

    __tablename__ = "doodad"

    doodad_id = Column(Integer(), primary_key=True)
    name = Column(String(255))
    purpose = Column(String(255))

    def update(self, changes: DoodadInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
