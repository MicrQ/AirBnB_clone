#!/usr/bin/python3
""" The command line Interpreter"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
import re
import json

clas_s = {'BaseModel': BaseModel, 'User': User, 'Amenity': Amenity,
          'City': City, 'Place': Place, 'Review': Review, 'State': State}


class HBNBCommand(cmd.Cmd):
    """ Represents The Interprater """

    prompt = "(hbnb) "

    def do_exit(self, arg):
        """to exit the interpreter,
        Usage: (hbnb) exit"""
        return True

    def do_EOF(self, arg):
        """to exit interpreter when EOF detected"""
        print("")
        return True

    def do_help(self, arg):
        """To get help document
            Usage: (hbnb) help <optional command>"""
        return super().do_help(arg)

    def emptyline(self):
        """ executes nothing when emptyline entered"""
        pass

    def do_create(self, arg):
        """Creates a new Instance of a given class
            Usage: create <Class Name>"""
        args = arg.split()
        if not valid(args):
            return
        obj = clas_s[args[0]]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Displays string representation of instance
            Usage: show <class name> <instance id>"""
        args = arg.split()
        if not valid(args, id=True):
            return

        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])
        str_repr = objects.get(key)

        if str_repr is None:
            print('** no instance found **')
            return
        print(str_repr)

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id
            Usage: destroy <class name> <instance id>"""
        args = arg.split()
        if not valid(args, id=True):
            return

        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])
        str_repr = objects.get(key)

        if str_repr is None:
            print('** no instance found **')
            return
        del objects[key]
        storage.save()

    def precmd(self, line):
        """to modify command before execution"""
        args = line.split('.')
        if len(args) > 1 and args[1] == 'all()':
            return "all " + args[0]
        if len(args) > 1 and args[1] == 'count()':
            return "count " + args[0]
        return line

    def do_all(self, arg):
        """Prints a string representation of instances
            Usage: all <optional class name>"""

        args = arg.split()
        objects = storage.all()

        if len(args) < 1:
            print(["{}".format(str(v)) for _, v in objects.items()])
            return
        if args[0] not in clas_s.keys():
            print("** class doesn't exist **")
            return
        else:
            print(["{}".format(str(v))
                  for _, v in objects.items() if type(v).__name__ == args[0]])
            return

    def do_update(self, arg):
        """Updates an instance based on the class name and id
          Usage: update <class name> <instance id> <attr name> <attr value>"""
        args = arg.split()
        if not valid(args, id=True):
            return
        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])
        str_repr = objects.get(key)

        if str_repr is None:
            print('** no instance found **')
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr = re.findall(r"^[\"\'](.*?)[\"\']", args[3])
        if attr:
            setattr(str_repr, args[2], attr[0])
        else:
            values = args[3].split()
            setattr(str_repr, args[2], parseStr(values[0]))
        storage.save()

    def do_count(self, arg):
        """Counts the number of instances
            Usage: <class name>.count()
                    or
                   count <class name>"""
        if arg not in clas_s:
            print("** class doesn't exist **")
            return
        i = 0
        for k in storage.all().keys():
            if re.match(arg, k):
                i += 1
        print(i)


def valid(args, id=False):
    """validates given argument for command"""
    if len(args) < 1:
        print("** class name missing **")
        return False
    if args[0] not in clas_s:
        print("** class doesn't exist **")
        return False
    if len(args) < 2 and id:
        print("** instance id missing **")
        return False
    return True


def is_float(x):
    """Checks if x is float."""
    try:
        a = float(x)
    except (TypeError, ValueError):
        return False
    else:
        return True


def is_int(x):
    """Checks if x is int.
    """
    try:
        a = float(x)
        b = int(a)
    except (TypeError, ValueError):
        return False
    else:
        return a == b


def parseStr(arg):
    """Parse to int || float || str
    """
    parsed = re.sub("\"", "", arg)

    if is_int(parsed):
        return int(parsed)
    elif is_float(parsed):
        return float(parsed)
    else:
        return arg


if __name__ == '__main__':
    HBNBCommand().cmdloop()
