import json

class DAO:
    def persistant(func):
        def wrapper(*args):
            self = args[0]
            with open(self.path, 'r+') as stream:
                string = stream.read()
                self.data = json.loads(string)
            result = func(*args)
            with open(self.path, 'w+') as stream:
                string = json.dumps(self.data)
                stream.write(string)
            return result
        return wrapper
    
    def __init__(self, path):
        self.path = path
        self.data = list()

    @persistant
    def append(self):
        self.data.append(2)
        print(self.data)