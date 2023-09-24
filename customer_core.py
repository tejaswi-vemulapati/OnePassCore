import uuid

class OnePassCustomer:
    businesses = []
    def __init__(self, name, location, bio):
        self.name = name
        self.location = location
        self.bio = bio