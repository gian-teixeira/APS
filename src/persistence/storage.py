
class Storage:
    pass

class StorageLinker:
    def __init__(self, 
                 target : Storable):
        self._target = target
    def update(self): pass

class Storable: 
    @property
    def manager(self) -> StorageLinker: ...
    
    def updater(self, func):
        def wrapper(*args, **kwargs):
            self.manager.update()
            func(*args, **kwargs)
        return wrapper