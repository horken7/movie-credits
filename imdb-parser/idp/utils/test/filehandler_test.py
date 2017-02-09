import unittest
from ..filehandler import *
from ... import settings

class FileHandlerTests(unittest.TestCase):
    def setUp(self):
        self.list = 'movies'

    def test_get_full_path(self):
        self.assertEqual(get_full_path(self.list), settings.INPUT_DIR+self.list)


if __name__ == '__main__':
    unittest.main()
