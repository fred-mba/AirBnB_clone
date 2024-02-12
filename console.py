#!/usr/bin/python3
"""
Entry point of the command interpreter
Commands implemented:
- Create()
- Show()
- Update()
- Destroy()
- all()
- count()
"""

import cmd
import json
import re
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """The command class
    Defines the commands to be used in the user interactive mode
    """
    prompt = "(hbnb) "

    class_list = {
        "Amenity": Amenity,
        "BaseModel": BaseModel,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User,
        }

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        if not args:
            print("** class name missing **")

        args_input = args.split()
        class_name = args_input[0]
        if class_name not in self.class_list:
            print("** class doesn't exist **")

        else:
            class_name = args_input[0]
            if class_name in self.class_list:
                class_obj = self.class_list[class_name]()
                storage.new(class_obj)
                storage.save()
                print(class_obj.id)

            else:
                print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance based on
        the class name and id. Ex: $ show BaseModel 1234-1234-1234"""
        if not args:
            print("** class name missing **")

        args_input = args.split()
        class_name = args_input[0]
        if class_name not in self.class_list:
            print("** class doesn't exist **")

        elif len(args_input) < 2:
            print("** instance id missing **")

        else:
            obj_id = args_input[1]
            key = "{}.{}".format(class_name, obj_id)
            all_objects = storage.all()

            if key in all_objects:
                print(all_objects[key])
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances based or not
        on the class name. Ex: $ all BaseModel or $ all"""
        args_input = args.split()
        all_objects = storage.all()

        if not args_input:
            print([str(obj) for obj in all_objects.values()])

        else:
            class_name = args_input[0]

            if class_name not in self.class_list:
                print("** class doesn't exist **")

            else:
                result = []
                for key, val in all_objects.items():
                    if key.startswith(class_name):
                        result.append(str(val))

                print(result)

    def do_update(self, args):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""
        if not args:
            print("** class name missing **")

        line_args = args.split()
        class_name = line_args[0]
        if class_name not in self.class_list:
            print("** class doesn't exist **")
        elif len(line_args) == 1:
            print("** instance id missing **")
        else:
            obj_id = line_args[1]
            key = "{}.{}".format(class_name, obj_id)
            all_objects = storage.all()

            if key not in all_objects:
                print("** no instance found **")

            elif len(line_args) == 2:
                print("** attribute name missing **")

            else:
                attr_name = line_args[2]
                if len(line_args) == 3:
                    print("** value missing **")
                else:
                    attr_val = line_args[3].strip('"')

                    instance = all_objects[key]
                    setattr(instance, attr_name, attr_val)
                    storage.save()

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return

        line_args = args.split()
        class_name = line_args[0]
        if class_name not in self.class_list:
            print("** class doesn't exist **")
        elif len(line_args) == 1:
            print("** instance id missing **")
        else:
            obj_id = line_args[1].strip('"')
            key = "{}.{}".format(class_name, obj_id)
            all_objects = storage.all()

            if key not in all_objects:
                print("** no instance found **")
            else:
                del all_objects[key]
                storage.save()

    def do_count(self, args):
        """Retrieve the number of instances of a class: <class name>.count()"""
        line_args = args.split()

        if not line_args:
            print("** class name missing **")

        else:
            class_name = line_args[0]

            if class_name in self.class_list:
                all_objects = storage.all()

                count = 0
                for key in all_objects.keys():
                    if key.startswith(class_name):
                        count += 1
                print(count)

            else:
                print("** class doesn't exist **")

    def default(self, args):
        """Handles operations of <class name>.<command>"""
        if args.endswith('.count()'):
            class_name = args.split(".")[0]
            self.do_count(class_name)

    def emptyline(self):
        """Returns True for an empty line"""
        pass

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Exit program on ctrl + D"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
