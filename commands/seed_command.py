from datetime import datetime
import pandas as pd
import numpy as np
from flask_script import Command

from app import db
from app.widget import Widget
from app.fizz.fizzbaz import Fizzbaz
from app.fizz.fizzbar import Fizzbar
from app.other_api.doodad import Doodad
from app.other_api.whatsit import Whatsit


def seed_things():
    classes = [Widget, Fizzbaz, Fizzbar, Doodad, Whatsit]
    for klass in classes:
        seed_thing(klass)


def seed_thing(cls):
    things = [
        {"name": "Pizza Slicer", "purpose": "Cut delicious pizza"},
        {"name": "Rolling Pin", "purpose": "Roll delicious pizza"},
        {"name": "Pizza Oven", "purpose": "Bake delicious pizza"},
    ]
    db.session.bulk_insert_mappings(cls, things)


class SeedCommand(Command):
    """ Seed the DB."""

    def run(self):
        if (
            input(
                "Are you sure you want to drop all tables and recreate? (y/N)\n"
            ).lower()
            == "y"
        ):
            print("Dropping tables...")
            db.drop_all()
            db.create_all()
            seed_things()
            db.session.commit()
            print("DB successfully seeded.")
