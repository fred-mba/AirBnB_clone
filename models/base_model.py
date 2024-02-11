#!/usr/bin/python3
"""Define common attributes/methods for other classes"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """Base class for all classes"""
    def __init__(self, *args, **kwargs):
        attr_list = [
            "id", "name", "description",
            "created_at", "updated_at"]
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key in attr_list:
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # add new instance to storage
            models.storage.new(self)

    def save(self):
        """ updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        obj_dict = self.__dict__.copy()

        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict

    def __str__(self):
        """prints: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
