"""Regression coverage for the first round's default category selection.

Run: python -m unittest discover -s tests
Uses SQLite in memory; never connects to the configured PostgreSQL database.
"""
import importlib
import unittest
from html.parser import HTMLParser
from unittest.mock import patch

from flask_sqlalchemy import SQLAlchemy


def isolated_database(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    return SQLAlchemy(app)


with patch('flask_sqlalchemy.SQLAlchemy', side_effect=isolated_database):
    plants = importlib.import_module('app')


class Inputs(HTMLParser):
    def __init__(self):
        super().__init__()
        self.checked = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'input' and attrs.get('type') == 'checkbox' and 'checked' in attrs:
            self.checked.add(attrs['id'])


class InitialRoundTests(unittest.TestCase):
    def setUp(self):
        plants.app.config['TESTING'] = True
        context = plants.app.app_context()
        context.push()
        self.addCleanup(context.pop)
        plants.db.create_all()
        self.addCleanup(plants.db.drop_all)
        self.addCleanup(plants.db.session.remove)
        self.client = plants.app.test_client()

    def add_plant(self, model, name, image_type):
        row = model(name, image_type, f'https://example.org/{name}/{image_type}.webp',
                    name, 'Tree' if model == plants.Trees else 'Other', 'Photo credit', '')
        plants.db.session.add(row)
        return row

    def get_initial_round(self):
        # Pick duplicate species first to force the refill path deterministically.
        with patch.object(plants.random, 'sample', side_effect=lambda ids, count: ids[:count]), \
                patch.object(plants.random, 'shuffle'), \
                patch.object(plants, 'render_template', wraps=plants.render_template) as render:
            response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        return response, render.call_args.kwargs

    def test_first_image_and_choices_only_use_trees_and_leaves(self):
        eligible_urls = set()
        for name in ('Oak', 'Elm', 'Pine', 'Maple'):
            for role in ('close_fullsize', 'leaf'):
                eligible_urls.add(self.add_plant(plants.Trees, name, role).image_url)
            self.add_plant(plants.Trees, name, 'bark')
        self.add_plant(plants.Trees, 'Bark only', 'bark')
        for model in plants.tables[1:]:
            self.add_plant(model, model.__name__, 'close_fullsize')
        plants.db.session.commit()

        response, context = self.get_initial_round()
        self.assertEqual(len(context['plant_names']), 4)
        self.assertEqual(len(set(context['plant_names'])), 4)
        self.assertTrue(set(context['plant_image_url']).issubset(eligible_urls))
        self.assertEqual(set(context['plant_types']), {'Tree'})
        self.assertIn(f'src="{context["plant_image_url"][0]}"', response.get_data(as_text=True))
        inputs = Inputs()
        inputs.feed(response.get_data(as_text=True))
        self.assertEqual(inputs.checked, {'switchRoundedDefault_trees', 'switchRoundedDefault_leaves'})

    def test_small_tree_pool_does_not_fall_back_to_other_categories(self):
        self.add_plant(plants.Trees, 'Oak', 'leaf')
        self.add_plant(plants.Trees, 'Oak', 'close_fullsize')
        self.add_plant(plants.Trees, 'Bark only', 'bark')
        self.add_plant(plants.Flowers, 'Sunflower', 'close_fullsize')
        plants.db.session.commit()

        _, context = self.get_initial_round()
        self.assertEqual(context['plant_names'], ['Oak'])
        self.assertEqual(context['plant_types'], ['Tree'])


if __name__ == '__main__':
    unittest.main()
