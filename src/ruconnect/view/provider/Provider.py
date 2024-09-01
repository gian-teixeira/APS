from abc import ABC, abstractmethod

class Provider(ABC):
    @staticmethod
    @abstractmethod
    def label(obj: any) -> str: ...

    @staticmethod
    @abstractmethod
    def info(obj: any) -> tuple[tuple[str,str]]: ...