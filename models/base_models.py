#!/usr/bin/python3
""" Base Class for all classes """

import uuid
import datetime
""" used to generate unique id """


class BaseModel:
    """represents all classes"""

    def __init__(self):
        """Initializer"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime
