#!/usr/bin/python3
"""BaseModel module"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """Defines all common atrributes and methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Initializes new instances of a base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)  # A new object

    def save(self):
        """
        - Updates `updated_at` with the current time
        - Must also notify FileStorage to save in the file
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values"""
        return {
            **self.__dict__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "__class__": self.__class__.__name__
        }

    def __str__(self):
        """Prints class instance  name, id and __dict__"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
