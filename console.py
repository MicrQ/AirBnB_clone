#!/usr/bin/python3
""" The command line Interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """ Represents The Interprater """

    prompt = "(hbnb) "
    def do_exit(self, arg):
        """to exit the interpreter"""
        return True
    
    def do_EOF(self, arg):
        """to exit interpreter when EOF detected"""
        print("")
        return True
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()