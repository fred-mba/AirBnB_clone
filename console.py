import cmd
import json
import os
from datetime import datetime
from models.base_model import Basemodel

class HBNBCommand(cmd.Cmd):
    intro = "Welcome to the AirBnB website"
    prompt = "(hbnb) "

    def do_create(self, args):
        """Creates a new instance of Basemodel , saves it, and prints the id"""
        if not args:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(args)
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
        else:
            args_list = args.split()
            if args_list[0] not in globals:
                print("** class doesn't exist **")
            elif len(args_list) < 2:
                print("** instance id missing **")
            else:
                obj_dict = json.loads(Basemodel.read_file())
                key = args_list[0] + "." + args_list[1]
                if key not in obj_dict:
                    print("** no instance found **")
                else:
                    print(obj_dict[key])

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True
    def do_EOF(self, args):
        """Exit file on ctrl + D"""
        print()
        return True
if __name__ == "__main__":
    HBNBCommand().cmdloop()