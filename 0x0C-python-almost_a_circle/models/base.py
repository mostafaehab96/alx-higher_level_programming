#!/usr/bin/python3

"""Defining simple Base class."""
import json
import csv


class Base:
    """A simple Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize class with id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries."""
        if (list_dictionaries is None
                or len(list_dictionaries) == 0):
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        data = []
        for obj in list_objs:
            data.append(obj.to_dictionary())
        data = Base.to_json_string(data)
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as file:
            file.write(data)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string."""
        if json_string is None or json_string.strip() == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set."""
        instance = cls(2, 2)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from a file."""
        filename = f"{cls.__name__}.json"
        try:
            file = open(filename, "r")
        except FileNotFoundError:
            return []
        else:
            dict_list = Base.from_json_string(file.read())
            objs_list = []
            for dic in dict_list:
                objs_list.append(cls.create(**dic))
            file.close()
            return objs_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves a list of objects into a CSV file."""
        filename = f"{cls.__name__}.csv"
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", 'x', 'y']
        else:
            fieldnames = ["id", "size", 'x', 'y']
        dict_list = []
        for obj in list_objs:
            dict_list.append(obj.to_dictionary())
        with open(filename, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(dict_list)

    @classmethod
    def load_from_file_csv(cls):
        """Reads a CSV file and return a list of objects."""
        filename = f"{cls.__name__}.csv"

        try:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                dict_list = []
                for row in reader:
                    dic = {k: int(v) for k, v in row.items()}
                    dict_list.append(dic)

                list_objs = []
                for dic in dict_list:
                    list_objs.append(cls.create(**dic))
                return list_objs
        except FileNotFoundError:
            return []
