#!/usr/bin/python3
""" The command line Interpreter"""

import cmd


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
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()