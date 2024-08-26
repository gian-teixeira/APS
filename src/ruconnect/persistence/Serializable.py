from abc import ABC, abstractmethod

class Serializable:
    @abstractmethod
    def get_id(self): ...