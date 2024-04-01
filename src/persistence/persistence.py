from collections import namedtuple
from abc import ABC, abstractmethod
import json

class Persistence:
    def __init__(self, 
                 target_class):
        self.cls = target_class

    def get_class(self) -> object:
        data = self.load()
        return self.cls(*json.loads(data).values())
        
    @abstractmethod
    @staticmethod
    def load() -> str: pass

    @abstractmethod
    @staticmethod
    def save(): pass

class Restaurant: pass

class RestaurantPersistence(Persistence):
    def __init__(self):
        super().__init__(Restaurant)