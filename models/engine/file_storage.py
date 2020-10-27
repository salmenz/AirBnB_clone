#!/usr/bin/python3

class FileStorage:

    def __init__(self):
        self.__file_path = ""
        self.__objects = {}
    
    def all(self):
        return self.__objects
    
    def new(self, obj):
        self.__objects['{}'.format(obj)] = type(obj).__name__+"."+obj.id = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            f.write("{\"")
            for key in self.__objects:
                k = "\""+str(key)+"\": "
                f.write(k)
                f.write(str(self.__objects[key]).replace("'", "\"")+", ")
            f.write("}")
        