#!/usr/bin/python3
"""represents a user"""

from models.base_model import BaseModel


class User(BaseModel):
    """Inherits BaseModels attribute and functionality"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
