#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
<<<<<<< HEAD
print(BaseModel().id)
my_model_json = my_model.to_dict()
print(my_model_json)
#BaseModel.__dict__)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
=======
# my_model_json = my_model.to_dict()
# print(my_model_json)
# print("JSON of my_model:")
# for key in my_model_json.keys():
# print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), \
# my_model_json[key]))
>>>>>>> f67ddd71b2ea9ac3a029bcc40efec8c1d881c015

# Just for testing git
