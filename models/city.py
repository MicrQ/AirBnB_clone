#!/usr/bin/python3
"""City class: inherites from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """represents a City"""

    name = ""
    state_id = ""
