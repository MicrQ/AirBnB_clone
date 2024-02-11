#!/usr/bin/python3
"""File storage to have persistence storage"""

import os
import json
from models.user import BaseModel, User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """Represents the persistence storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the __objects instance dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[type(obj).__name__ + '.' + obj.id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as fp:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()}, fp)

    def reload(self):
        """ deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists
        """
        clas_s = {'BaseModel': BaseModel, 'User': User, 'Amenity': Amenity,
                  'City': City, 'Place': Place, 'Review': Review, 'State': State}

        if not os.path.exists("file.json"):
            return

        from_file = None
        with open(FileStorage.__file_path, 'r') as fp:
            try:
                from_file = json.load(fp)
            except json.JSONDecodeError:
                pass
            if from_file is not None:
                FileStorage.__objects = {
                    k: clas_s[k.split('.')[0]](**v)
                    for k, v in from_file.items()}
