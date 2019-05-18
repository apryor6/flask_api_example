from datetime import datetime
import pandas as pd
import numpy as np
from flask_script import Command


from app import db


def seed_widgets():
    from app.widget import Widget
    widgets = [
        {
            'name': 'Pizza Slicer',
            'purpose': 'Cut delicious pizza',
        },
        {
            'name': 'Rolling Pin',
            'purpose': 'Roll delicious pizza',
        },
        {
            'name': 'Pizza Oven',
            'purpose': 'Bake delicious pizza',
        },
    ]
    db.session.bulk_insert_mappings(Widget, widgets)


class SeedCommand(Command):
    """ Seed the DB."""

    def run(self):
        if input('ARE YOU SURE YOU WANT TO DROP ALL TABLES AND RECREATE? (Y/N)\n'
                 ).lower() == 'y':
            print('Dropping tables...')
            db.drop_all()
            db.create_all()
            seed_widgets()
            db.session.commit()
            print('Widgets successfully seeded.')
