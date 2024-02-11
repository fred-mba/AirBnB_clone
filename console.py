#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
import json
import uuid
import models
import re
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """The command class"""
    prompt = "(hbnb) "

    class_list = [
        "BaseModel", "Amenity", "City",
        "Place", "Review", "State", "User"]
    
    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        if not args:
            print("** class name missing **")

        args_list = args.split()
        class_name = args_list[0]
        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return

        obj = eval(class_name)()
        print(obj.id)
        obj.save()

    def do_show(self, args):
        """Prints the string representation of an instance based on
        the class name and id. Ex: $ show BaseModel 1234-1234-1234"""
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        class_name = args_list[0]
        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        obj_id = args_list[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objects = models.storage.all()

        if key in all_objects:
            print(all_objects[key])
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances based or not
        on the class name. Ex: $ all BaseModel or $ all"""
        line_args = args.split()
        objects = models.storage.all()

        if not line_args or line_args[0] not in self.class_list:
            print("** class doesn't exist **")
            return

        result = []
        for obj in objects.values():
            if obj.__class__.__name__ == line_args[0]:
                result.append(str(obj))

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
            obj_id = line_args[1].strip('"')
            key = "{}.{}".format(class_name, obj_id)
            all_objects = models.storage.all()

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
                    models.storage.save()

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
            all_objects = models.storage.all()

            if key not in all_objects:
                print("** no instance found **")
            else:
                del all_objects[key]
                models.storage.save()

    def do_count(self, args):
        """Retrieve the number of instances of a class: <class name>.count()"""
        line_args = args.split()

        if not line_args:
            print("** class name missing **")

        else:
            class_name = line_args[0]

            if class_name in self.class_list:
                all_objects = models.storage.all()

                count = 0
                for key in all_objects.keys():
                    if key.startswith(class_name):
                        count += 1
                print(count)

            else:
                print("** class doesn't exist **")

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Exit program on ctrl + D"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
