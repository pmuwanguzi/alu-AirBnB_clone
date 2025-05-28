import uuid
from datetime import datetime


class BaseModel:

    """ 
    Intialising the object
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    """
    This returns the string representation of the object.
    """
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name, self.id,self.__dict__)
    
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        instance_dict =self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict