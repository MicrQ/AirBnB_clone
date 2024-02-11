#!/usr/bin/python3
"""unittest for Review class"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models.review import Review
from models import storage
from datetime import datetime


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
        """Test class attributes"""

        rvw1 = Review()
        rvw3 = Review("hello", "wait", "in")
        k = f"{type(rvw1).__name__}.{rvw1.id}"
        self.assertIsInstance(rvw1.text, str)
        self.assertIsInstance(rvw1.user_id, str)
        self.assertIsInstance(rvw1.place_id, str)
        self.assertEqual(rvw3.text, "")

    def test_init(self):
        """Test public instances"""
        usr1 = Review()
        usr2 = Review(**usr1.to_dict())
        self.assertIsInstance(usr1.id, str)
        self.assertIsInstance(usr1.created_at, datetime)
        self.assertIsInstance(usr1.updated_at, datetime)
        self.assertEqual(usr1.updated_at, usr2.updated_at)

    def test_str(self):
        """Test str representation"""
        usr1 = Review()
        string = f"[{type(usr1).__name__}] ({usr1.id}) {usr1.__dict__}"
        self.assertEqual(usr1.__str__(), string)

    def test_save(self):
        """Test save"""
        usr1 = Review()
        old_update = usr1.updated_at
        usr1.save()
        self.assertNotEqual(usr1.updated_at, old_update)

    def test_todict(self):
        """Test dict"""
        usr1 = Review()
        usr2 = Review(**usr1.to_dict())
        a_dict = usr2.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(usr2).__name__)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(usr1, usr2)


if __name__ == "__main__":
    unittest.main()