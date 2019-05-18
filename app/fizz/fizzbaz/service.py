from app import db
from typing import List
from .model import Fizzbaz
from .interface import FizzbazInterface


class FizzbazService():
    @staticmethod
    def get_all() -> List[Fizzbaz]:
        return Fizzbaz.query.all()

    @staticmethod
    def get_by_id(fizzbaz_id: int) -> Fizzbaz:
        return Fizzbaz.query.get(fizzbaz_id)

    @staticmethod
    def update(fizzbaz: Fizzbaz, Fizzbaz_change_updates: FizzbazInterface) -> Fizzbaz:
        fizzbaz.update(Fizzbaz_change_updates)
        db.session.commit()
        return fizzbaz

    @staticmethod
    def delete_by_id(fizzbaz_id: int) -> List[int]:
        fizzbaz = Fizzbaz.query.filter(Fizzbaz.fizzbaz_id == fizzbaz_id).first()
        if not fizzbaz:
            return []
        db.session.delete(fizzbaz)
        db.session.commit()
        return [fizzbaz_id]

    @staticmethod
    def create(new_attrs: FizzbazInterface) -> Fizzbaz:
        new_fizzbaz = Fizzbaz(
            name=new_attrs['name'],
            purpose=new_attrs['purpose']
        )

        db.session.add(new_fizzbaz)
        db.session.commit()

        return new_fizzbaz
