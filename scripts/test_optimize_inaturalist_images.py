"""Check delivery-image bounds, provenance, and safe repeat execution."""
import hashlib
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from PIL import Image
import optimize_inaturalist_images as optimizer


class OptimizationTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)

    def row(self, size):
        key = 'texas_trees/leaf/example.jpeg'
        path = self.root / 'images' / key
        path.parent.mkdir(parents=True)
        Image.new('RGB', size, (40, 130, 50)).save(path)
        return dict(s3_key=key, sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                    source='Photographer; CC BY; unmodified image', uploaded=False)

    def test_resize_preserves_aspect_and_source(self):
        row = self.row((1600, 1200))
        original_digest = row['sha256']
        with patch.object(optimizer, 'DATA', self.root):
            optimizer.optimize([row])
        self.assertEqual(row['image_dimensions'], [960, 720])
        self.assertEqual(row['original_sha256'], original_digest)
        self.assertIn('Photographer; CC BY', row['source'])
        self.assertIn('resized', row['source'])
        self.assertNotIn('unmodified image', row['source'])
        with Image.open(self.root / 'images' / row['s3_key']) as im:
            self.assertEqual(im.format, 'WEBP')
        self.assertTrue((self.root / 'images' / row['original_s3_key']).exists())

    def test_repeat_does_not_upscale_or_invalidate_same_upload(self):
        row = self.row((400, 300))
        with patch.object(optimizer, 'DATA', self.root):
            optimizer.optimize([row])
            row['uploaded'] = True
            key = row['s3_key']
            optimizer.optimize([row])
        self.assertEqual(row['image_dimensions'], [400, 300])
        self.assertEqual(row['s3_key'], key)
        self.assertTrue(row['uploaded'])


if __name__ == '__main__':
    unittest.main()
