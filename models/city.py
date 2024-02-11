#!/usr/bin/python3
"""Defines city attributes -- state_id and name"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class representation of city"""
    state_id: str = ''
    name: str = ''
