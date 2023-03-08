#!/usr/bin/python3
"""
Module consisting of BaseModel class
"""


import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """
    class that defines all common attributes
    for other classes
    """
    def __init__(self, id, *args, **Kwargs):
        """
            Initializes instance attributes
            Args:
                *args: list of arguments
                **kwargs: dict of key-values arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key = "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key = "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:

            self.id = str(uuid.uuid4())
            self.create_at = datetime.now()
            self.update_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """prints class name with atrribute"""

        return "[{}] ({}) <{}>".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        updates public attribute update_at with current datetime
        """
    return update_at = datetime.now()
    storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        """

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()

        return my_dict
