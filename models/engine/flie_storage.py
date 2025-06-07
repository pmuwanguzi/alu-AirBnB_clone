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
        """
        Adds a new object to the FileStorage's dictionary of objects.
        The new object is stored in the dictionary with a key in the format.
        <class name>.<object id>. The object is then saved to disk

        Parameters
        -----------
        new_obj : BaseModel
            The new object to be added to the dictionary of objects.
        """
        key = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
        self.__objects[key] = new_obj


