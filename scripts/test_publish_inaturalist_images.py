"""Regression checks for seed activation without AWS or a database."""
import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import publish_inaturalist_images as publisher


class ActivationTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.path = self.root / 'seed_database.py'
        self.path.write_text('trees = [\n    # Trees("Oak", "bark", "", "Quercus test", "Tree", "", ""),\n]\n'
                             'flowers = [\n    Flowers("Existing", "close_fullsize", "old", "Existing", "Flower", "credit", "")\n'
                             '    # Flowers("New", "close_fullsize", "", "New", "Flower", "", "")\n]\n')
        self.row = dict(model='Trees', plant_name='Oak', image_type='bark',
                        image_url='https://example.org/new.jpg', scientific_name='Quercus test',
                        plant_type='Tree', source="Photographer O'Brien; CC BY", location_counties='',
                        reviewed=True, uploaded=True, license_code='cc-by')

    def activate(self, rows):
        with patch.object(publisher, 'ROOT', self.root), contextlib.redirect_stdout(io.StringIO()):
            publisher.activate(rows)
        return self.path.read_text()

    def test_unuploaded_or_restricted_photos_stay_commented(self):
        for changes in ({'uploaded': False}, {'reviewed': False}, {'license_code': 'cc-by-nc'}):
            content = self.activate([dict(self.row, **changes)])
            self.assertIn('# Trees(', content)

    def test_activation_preserves_credit_and_is_repeatable(self):
        content = self.activate([self.row])
        self.assertNotIn('# Trees(', content)
        self.assertIn("O'Brien", content)
        self.assertEqual(content, self.activate([self.row]))
        self.assertIn('"old"', content)

    def test_new_flower_repairs_the_preceding_comma(self):
        row = dict(self.row, model='Flowers', plant_name='New', image_type='close_fullsize',
                   scientific_name='New', plant_type='Flower')
        content = self.activate([row])
        self.assertNotIn('# Flowers(', content)
        self.assertIn('"credit", ""),', content)

    def test_prepared_rows_remain_disabled_until_uploaded(self):
        with patch.object(publisher, 'ROOT', self.root), contextlib.redirect_stdout(io.StringIO()):
            publisher.activate([dict(self.row, uploaded=False)], prepare_only=True)
        content = self.path.read_text()
        self.assertIn('# Trees(', content)
        self.assertIn(self.row['image_url'], content)


if __name__ == '__main__':
    unittest.main()
