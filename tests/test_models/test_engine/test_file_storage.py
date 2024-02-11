"""TEST FOR FILE STORAGE"""

import os
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """tests as follow"""

    def test_FileStorage_init_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_init_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_init(self):
        self.assertEqual(type(models.storage), FileStorage)


class Test_FileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_each(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_each_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)


if __name__ == "__main__":
    unittest.main()
