from persistence.collection import Collection

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

tmp = Collection("tmp")

tmp.save()