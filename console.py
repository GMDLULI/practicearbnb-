#!/usr/bin/python3
"""
Entry point of command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    command interpreter class
    """
    prompt = '(hbnb)'

    def do_EOF(self, line):
        """exits program"""

        return True

    def do_quit(self, line):
        """Quit command to exit program"""

        print("\n")
        return True

    def emptyline(self):
        """prints nothing on Enter"""

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
