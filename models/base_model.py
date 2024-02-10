#!/usr/bin/python3
""" Base Class for all classes """

import uuid
from datetime import datetime
""" used to generate unique id """


class BaseModel:
    """represents all classes"""

    def __init__(self):
        """Initializer"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """string representation of an object"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the instance variable updated_at with current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary that contains all key/value"""
        toDict = {**self.__dict__}
        toDict["__class__"] = type(self).__name__
        toDict['created_at'] = toDict['created_at'].isoformat()
        toDict['updated_at'] = toDict['updated_at'].isoformat()
        return toDict
