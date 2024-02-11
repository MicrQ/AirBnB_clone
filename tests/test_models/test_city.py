#!/usr/bin/python3
"""unittest for City class"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models.city import City
from models import storage
from datetime import datetime

cty1 = City()
cty2 = City(**cty1.to_dict())
cty3 = City("wow", "mom", "coc")


class TestState(unittest.TestCase):
    """Test cases"""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_args(self):
        """Test method for class attributes"""
        k = f"{type(cty1).__name__}.{cty1.id}"
        self.assertIsInstance(cty1.name, str)
        self.assertEqual(cty3.name, "")
        cty1.name = "Abuja"
        self.assertEqual(cty1.name, "Abuja")

    def test_init(self):
        """Test public instances"""
        usr1 = City()
        usr2 = City(**usr1.to_dict())
        self.assertIsInstance(usr1.id, str)
        self.assertIsInstance(usr1.created_at, datetime)
        self.assertIsInstance(usr1.updated_at, datetime)
        self.assertEqual(usr1.updated_at, usr2.updated_at)

    def test_str(self):
        """Test str representation"""
        usr1 = City()
        string = f"[{type(usr1).__name__}] ({usr1.id}) {usr1.__dict__}"
        self.assertEqual(usr1.__str__(), string)

    def test_save(self):
        """Test save"""
        usr1 = City()
        old_update = usr1.updated_at
        usr1.save()
        self.assertNotEqual(usr1.updated_at, old_update)

    def test_todict(self):
        """Test dict"""
        usr1 = City()
        usr2 = City(**usr1.to_dict())
        a_dict = usr2.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(usr2).__name__)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(usr1, usr2)


if __name__ == "__main__":
    unittest.main()