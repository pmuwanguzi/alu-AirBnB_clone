import json
from models.base_model import BaseModel

class FileStorage:
    """
    File storage class, in charge of file storage.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary of all objects currently
        stored in FileStorage.
        The Keys are in the format <class name>.<object id>
        and the values are the corresponding object instances.
        """
        return self.__objects
    def new(self,new_obj):
        key = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
        self.__objects[key] = new_obj


