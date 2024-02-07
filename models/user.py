#!/usr/bin/python3
"""
    This class contains users details to authenticate the user to
    retrive their personal information and process bookings
"""
from models.base_model import BaseModel

class User(BaseModel):
    """Class representing the user"""
    email: str = ''
    password: str = ''
    first_name: str = ''
    last_name: str = ''