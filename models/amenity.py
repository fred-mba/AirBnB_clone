#!/usr/bin/python3
"""Defines amenity class with an empty string name"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    name: str = ''