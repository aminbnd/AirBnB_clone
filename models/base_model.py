#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models
date = "%Y-%m-%dT%H:%M:%S.%f"
"""Defines the BaseModel class """

class BaseModel:
    """the BaseModel of the HBnB projectss """
    id = str(uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __str__(self):
        return ("[{}] {} {}".format(self.__class__.__name__, self.id, self.__dict__))
    def save(self):
        self.updated_at = datetime.now()
    def to_dict(self):
        dict_1 = self.__dict__.copy()
        dict_1["created_at"] = self.created_at.isoformat()
        dict_1["updated_at"] = self.updated_at.isoformat()
        dict_1["__class__"] = self.__class__.__name__
        return dict_1
    
