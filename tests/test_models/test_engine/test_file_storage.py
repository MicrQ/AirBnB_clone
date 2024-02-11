"""TEST FOR FILE STORAGE"""

import os
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """tests as follow"""

    def test_FileStorage_init_no_args(self):
        """no args"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_init_with_arg(self):
        """with args"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_str(self):
        """str file path"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_dict(self):
        """dict __object"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_init(self):
        """type of storage"""
        self.assertEqual(type(models.storage), FileStorage)


class Test_FileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    def setUp(self):
        """setup"""
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_each(self):
        """test each"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_each_with_arg(self):
        """each"""
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        """test new"""
        bm = BaseModel()
        # us = User()
        # st = State()
        # pl = Place()
        # cy = City()
        # am = Amenity()
        # rv = Review()
        models.storage.new(bm)
        # models.storage.new(us)
        # models.storage.new(st)
        # models.storage.new(pl)
        # models.storage.new(cy)
        # models.storage.new(am)
        # models.storage.new(rv)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        # self.assertIn("User." + us.id, models.storage.all().keys())
        # self.assertIn(us, models.storage.all().values())
        # self.assertIn("State." + st.id, models.storage.all().keys())
        # self.assertIn(st, models.storage.all().values())
        # self.assertIn("Place." + pl.id, models.storage.all().keys())
        # self.assertIn(pl, models.storage.all().values())
        # self.assertIn("City." + cy.id, models.storage.all().keys())
        # self.assertIn(cy, models.storage.all().values())
        # self.assertIn("Amenity." + am.id, models.storage.all().keys())
        # self.assertIn(am, models.storage.all().values())
        # self.assertIn("Review." + rv.id, models.storage.all().keys())
        # self.assertIn(rv, models.storage.all().values())

    def test_new_with_args(self):
        """new with arg"""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        """exception"""
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        """testing save"""
        bm = BaseModel()
        # us = User()
        # st = State()
        # pl = Place()
        # cy = City()
        # am = Amenity()
        # rv = Review()
        models.storage.new(bm)
        # models.storage.new(us)
        # models.storage.new(st)
        # models.storage.new(pl)
        # models.storage.new(cy)
        # models.storage.new(am)
        # models.storage.new(rv)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            # self.assertIn("User." + us.id, save_text)
            # self.assertIn("State." + st.id, save_text)
            # self.assertIn("Place." + pl.id, save_text)
            # self.assertIn("City." + cy.id, save_text)
            # self.assertIn("Amenity." + am.id, save_text)
            # self.assertIn("Review." + rv.id, save_text)

    def test_save_with_arg(self):
        """save with args"""
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        """test reload"""
        bm = BaseModel()
        # us = User()
        # st = State()
        # pl = Place()
        # cy = City()
        # am = Amenity()
        # rv = Review()
        models.storage.new(bm)
        # models.storage.new(us)
        # models.storage.new(st)
        # models.storage.new(pl)
        # models.storage.new(cy)
        # models.storage.new(am)
        # models.storage.new(rv)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        # self.assertIn("User." + us.id, objs)
        # self.assertIn("State." + st.id, objs)
        # self.assertIn("Place." + pl.id, objs)
        # self.assertIn("City." + cy.id, objs)
        # self.assertIn("Amenity." + am.id, objs)
        # self.assertIn("Review." + rv.id, objs)

    def test_reload_with_arg(self):
        """reload with args"""
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
