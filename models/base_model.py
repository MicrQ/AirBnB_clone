#!/usr/bin/python3
""" Base Class for all classes """

import uuid
from datetime import datetime
import models


class BaseModel:
    """represents all classes"""

    def __init__(self, *args, **kwargs):
        """Initializer"""
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k == "created_at" or k == "updated_at":
                        v = datetime.fromisoformat(v)
                    setattr(self, k, v)
            return

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        """string representation of an object"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the instance variable updated_at with current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary that contains all key/value"""
        toDict = {**self.__dict__}
        toDict["__class__"] = type(self).__name__
        toDict['created_at'] = toDict['created_at'].isoformat()
        toDict['updated_at'] = toDict['updated_at'].isoformat()
        return toDict
