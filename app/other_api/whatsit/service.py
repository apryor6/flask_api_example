from app import db
from typing import List
from .model import Whatsit
from .interface import WhatsitInterface


class WhatsitService:
    @staticmethod
    def get_all() -> List[Whatsit]:
        return Whatsit.query.all()

    @staticmethod
    def get_by_id(whatsit_id: int) -> Whatsit:
        return Whatsit.query.get(whatsit_id)

    @staticmethod
    def update(whatsit: Whatsit, Whatsit_change_updates: WhatsitInterface) -> Whatsit:
        whatsit.update(Whatsit_change_updates)
        db.session.commit()
        return whatsit

    @staticmethod
    def delete_by_id(whatsit_id: int) -> List[int]:
        whatsit = Whatsit.query.filter(Whatsit.whatsit_id == whatsit_id).first()
        if not whatsit:
            return []
        db.session.delete(whatsit)
        db.session.commit()
        return [whatsit_id]

    @staticmethod
    def create(new_attrs: WhatsitInterface) -> Whatsit:
        new_whatsit = Whatsit(name=new_attrs["name"], purpose=new_attrs["purpose"])

        db.session.add(new_whatsit)
        db.session.commit()

        return new_whatsit
