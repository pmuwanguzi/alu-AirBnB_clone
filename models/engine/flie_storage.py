import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects
    def new(self,new_obj):
        key = new_obj.__class__

