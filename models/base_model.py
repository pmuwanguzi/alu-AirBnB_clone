import uuid
from datetime import datetime


class BaseModel:

    """ 
    Intialising the Base model object
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization method for BaseModel.
        Paublic Instance attributes:
            id: a unique identifier 
            created at
            updated up
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at" , "updated_at"]:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()        

    """
    This returns the string representation of the object.
    """
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,self.__dict__)
    
    def save(self):
        """
        Updates the public instance attribute updated_at of the object with the current 
        datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        instance_dict =self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict