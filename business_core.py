import uuid

class OnePassBusiness:
    clients = []
    def __init__(self, name, location, desc):
        self.uid = uuid.uuid1()
        self.name = name
        self.location = location
        self.desc = desc
        
    

