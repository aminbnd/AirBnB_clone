#!/usr/bin/python3
"""Command interpreter """

import cmd
class HBNBCommand(cmd.Cmd):
    """Class for command interpreter """
    prompt = "(hbnb) "
    def do_EOF(self, line):
        """To exit with Ctrl-D """
        print()
        return True
    def do_quit(self, line):
            """quit command to exit the program """
            return True
if __name__ == "__main__":
    HBNBCommand().cmdloop()
