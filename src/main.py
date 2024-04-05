from persistence.collection import Collection

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

tmp = Collection("tmp")

tmp.insert({
    "name": "Gian",
    "age": 21
})

tmp.delete({
    "name": "Gian",
    "age": 20
})

print(tmp.find({
    "name": "Gian"
}))