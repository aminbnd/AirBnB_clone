# AirBnB_clone
## Project description:

******

* *This is the first phase of the Airbnb Clone: the console. This repository holds a command interpreter and classes (i.e. BaseModel class and several other classes that inherit from it: Amenity, City, State, Place, Review), and a command interpreter. The command interpreter, like a shell, can be activated, take in user input, and perform certain tasks to manipulate the object instances.*


## How to start it:
******
##### Interactive mode, $ ./console.py, and you will prompted with (hbnb)
##### Non-interactive mode, $ echo "help" | ./console.py
******

### How to Use Command Interpreter:
******

|   Commands  |           Usage                |      Fonctionality               |
| ----------- |:------------------------------:|:--------------------------------|
| help        | help                           | displays all commands available  |
| create      | create <class>                 | creates new object               |
| update      |User.update({'name':'Holberton'})|updates attribute of an object	  |
| destroy     |User.destroy('object')          | destroys specified object        |
| show        | User.show('object')            | retrieve an object from a file   |
| all         | User.all()                     | display all objects in class     |
| quit        | quit                           | exits                            |

******


##### (hbnb) all MyModel
** class doesn't exist **
##### (hbnb) show BaseModel
** instance id missing **
##### (hbnb) show BaseModel Holberton
** no instance found **
##### hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
##### (hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
##### (hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
##### (hbnb) destroy
** class name missing **
##### (hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
##### (hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
##### (hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
##### (hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
##### (hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
##### (hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
##### (hbnb) 

******
<br>
<br>

* *This project is written by **Mehdi Zitouni** and **Amin Bondi** as a part of end of trimester project of Holbeton School*
<br>
<img src="https://www.holbertonschool.com/holberton-logo.png">


