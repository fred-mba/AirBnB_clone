#!/usr/bin/python3
"""Serialization and deserialization of python objects"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Storage class"""
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
        for key, obj in self.all().items():
            serialized_obj[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding="UTF-8") as file:
            json.dump(serialized_obj, file)

    def reload(self):
        """Deserializes JSON file to __objects, that is,
        converting data back into its origial data structure or object
        allowing it to be used in the program as it was before."""

        class_list = {
            'Amenity': Amenity,
            'BaseModel': BaseModel,
            'City': City,
            'Place': Place,
            'Review': Review,
            'State': State,
            'User': User,
        }

        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as file:
                data = json.load(file)

            for key, value in data.items():
                """Tuple unpacking"""
                class_name = value['__class__']
                class_obj = class_list[class_name]
                obj = class_obj(**value)
                all_objects = self.all()
                all_objects[key] = obj

        except FileNotFoundError:
            pass
