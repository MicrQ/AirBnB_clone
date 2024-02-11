#!/usr/bin/python3
"""unittest for Place class"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models.place import Place
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

    def test_params(self):
        """Test class attributes"""

        plc1 = Place()
        plc3 = Place("hello", "wait", "in")
        k = f"{type(plc1).__name__}.{plc1.id}"
        self.assertIsInstance(plc1.name, str)
        self.assertIn(k, storage.all())
        self.assertEqual(plc3.name, "")

        self.assertIsInstance(plc1.name, str)
        self.assertIsInstance(plc1.user_id, str)
        self.assertIsInstance(plc1.city_id, str)
        self.assertIsInstance(plc1.description, str)
        self.assertIsInstance(plc1.number_bathrooms, int)
        self.assertIsInstance(plc1.number_rooms, int)
        self.assertIsInstance(plc1.price_by_night, int)
        self.assertIsInstance(plc1.max_guest, int)
        self.assertIsInstance(plc1.longitude, float)
        self.assertIsInstance(plc1.latitude, float)
        self.assertIsInstance(plc1.amenity_ids, list)

    def test_init(self):
        """Test public instances"""
        usr1 = Place()
        usr2 = Place(**usr1.to_dict())
        self.assertIsInstance(usr1.id, str)
        self.assertIsInstance(usr1.created_at, datetime)
        self.assertIsInstance(usr1.updated_at, datetime)
        self.assertEqual(usr1.updated_at, usr2.updated_at)

    def test_str(self):
        """Test str representation"""
        usr1 = Place()
        string = f"[{type(usr1).__name__}] ({usr1.id}) {usr1.__dict__}"
        self.assertEqual(usr1.__str__(), string)

    def test_save(self):
        """Test save"""
        usr1 = Place()
        old_update = usr1.updated_at
        usr1.save()
        self.assertNotEqual(usr1.updated_at, old_update)

    def test_todict(self):
        """Test dict"""
        usr1 = Place()
        usr2 = Place(**usr1.to_dict())
        a_dict = usr2.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(usr2).__name__)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(usr1, usr2)


if __name__ == "__main__":
    unittest.main()