#!/usr/bin/python3

""" unittest for BaseModel class """

import unittest
from models.base_model import BaseModel
from datetime import datetime
""" BaseModel imported """


class test_BaseModel(unittest.TestCase):
    """for BaseModel class initialization"""

    def test_typeOfInstances(self):
        """testing instances type after initialization"""
        self.assertIsInstance(BaseModel().id, str)
        self.assertIsInstance(BaseModel().created_at, datetime)
        self.assertIsInstance(BaseModel().updated_at, datetime)

    def test_str(self):
        """Test method for str representation"""
        b1 = BaseModel()
        string = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
        self.assertEqual(b1.__str__(), string)

    def test_checkMethods(self):
        """checking their method"""
        test = BaseModel()
        a = test.updated_at
        test.save()
        self.assertNotEqual(test.updated_at, a)

        self.assertIsInstance(BaseModel().to_dict(), dict)


if __name__ == "__main__":
    unittest.main()
