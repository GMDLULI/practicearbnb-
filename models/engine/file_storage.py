#!/usr/bin/python3
"""
Module with FileStorage class
"""
import pandas as ps


class FileStorage():
    """
    serializes instances to JASON file and deserializes
    JASON file to instances
    """

    __file_path = ps.read_json('file.json')
    __objects = {}

    def all(self):
        """
        public instance method that returns dictionary __objects
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes class instance to JSAON file
        """

        with open(FileStorage.__file_path, "w", encoding="utf-8") as fp:
            json.dump(__objects, fp)

    def reload(self):
        """
        deserializes the JSON file to class instance
        """

        if FileStorage.__file_path is not None:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as fp:
                json_str = json.jump(fp)

            return json_str

        else:
            return
