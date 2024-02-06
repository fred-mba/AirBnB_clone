#!/bin/bash/python3
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

def all(self):
    """Returns the dictionary __objects"""
    return self.__objects
def new(self, obj):
    """sets in __objects the obj with key <obj class name>.id"""
    key = "{}.{}".format(obj.__class__.__name__, obj.id)
    self.__objects[key] = obj

def save(self):
    """Serializes __objects to JSON file, that is,
    covert objects into a format that can easily be stored"""
    serialized_obj = {}
    for key, obj in self.__objects.items():
        serialized_obj[key] = obj.to_dict()

    with open(self.__file_path, 'w') as file:
        json.dump(serialized_obj, file)

def reload(self):
    """Deserializes JSON file to __objects, that is,
    converting data back into its origial data structure or object
    allowing it to be used in the program as it was before serialization."""
    try:
        with open(self.__file_path, 'r') as file:
            data = json.load(file)
        for key, value in data.items():
            """Tuple unpacking"""
            class_name, obj_id = key.split('.')
            obj = eval(class_name)(**value)
            self.__objects[key] = obj

    except FileNotFoundError:
        pass