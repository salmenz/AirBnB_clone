#!/usr/bin/python3

import uuid
import datetime

class BaseModel:


    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if kwargs:
            self.my_number = kwargs['my_number']
            self.name = kwargs['name']
            self.updated_at = datetime.datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            
    
    def __str__(self):
        return str("["+str(type(self).__name__)+"] "+"("+self.id+") "+str(self.__dict__))
    
    def save(self):
        self.updated_at = datetime.datetime.now()
    
    def to_dict(self):
        dict = {}
        dict['my_number'] = self.my_number
        dict['name'] = self.name
        dict['__class__'] = type(self).__name__
        dict['updated_at'] = self.updated_at.isoformat()
        dict['id'] = self.id
        dict['created_at'] = self.created_at.isoformat()
        return dict