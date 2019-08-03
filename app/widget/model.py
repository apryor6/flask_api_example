from sqlalchemy import Integer, Column, String
from app import db  # noqa
from .interface import WidgetInterface


class Widget(db.Model):  # type: ignore
    """A snazzy Widget"""

    __tablename__ = "widget"

    widget_id = Column(Integer(), primary_key=True)
    name = Column(String(255))
    purpose = Column(String(255))

    def update(self, changes: WidgetInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
