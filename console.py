#!/usr/bin/python3
"""Define Command interpreter"""

import cmd
from models.base_model import   BaseModel

class HBNBCommand(cmd.Cmd):
    """Class for command interpreter
    Attributes:
        prompt (str): Command prompt.
    """
    prompt = "(hbnb) "
    classes = {"BaseModel"}
    def do_EOF(self, line):
        """To exit with Ctrl-D"""
        print("")
        return True
    def do_quit(self, line):
        """quit command to exit the program"""
        return True
    def do_create(self, line):
        """Create instance of class"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
