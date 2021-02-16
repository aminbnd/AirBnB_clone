#!/usr/bin/python3
"""File Storage of objects """
import json
from models.base_model import BaseModel


class FileStorage:
    """this class used for serialiez and deserilalize json files """

    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel}
    def all(self):
        """returns the dictionary __objects """
        return self.__objects
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id """
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj
    def save(self):
        """serializes __objects to the JSON file """
        my_dict = {}
        for key, obj in self.__objects.items():
            my_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(my_dict, f)
    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
            for key, val in new_obj.items():
                obj = self.class_dict[val['__class__']](**val)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
