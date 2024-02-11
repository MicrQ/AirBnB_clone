#!/usr/bin/python3
""" The command line Interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage

clas_s = {'BaseModle': BaseModel}


class HBNBCommand(cmd.Cmd):
    """ Represents The Interprater """

    prompt = "(hbnb) "

    def do_exit(self, arg):
        """to exit the interpreter, type: exit"""
        return True

    def do_EOF(self, arg):
        """to exit interpreter when EOF detected"""
        print("")
        return True

    def do_help(self, arg):
        """To get help, type: help <topic>"""
        return super().do_help(arg)

    def emptyline(self):
        """ to execute nothing when emptyline entered"""
        pass

    def do_create(self, arg):
        """Creates a new Instance"""
        args = arg.split()
        if not valid(args):
            return
        obj = clas_s[args[0]]()
        print(obj.id)

    def do_show(self, arg):
        """Displays string representation of instance"""
        args = arg.split()
        if not valid(args):
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objects = storage.all()
        key = "{}.{}".format(args[0],args[1])
        str_repr = objects.get(key)

        if str_repr is None:
            print('** no instance found **')
            return
        print(str_repr)


def valid(self, args):
    """validates given argument for command"""
    if len(args) < 1:
        print("** class name missing **")
        return False
    if args[0] not in clas_s:
        print("** class doesn't exist **")
        return False
    return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
