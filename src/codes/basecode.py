from abc import ABC, abstractmethod

class Command(ABC):
    
    line = None

    def __init__(self, line, index=None):

        self.line = line
        self.index = index
        


    @abstractmethod
    def run(self) -> bool:

        return True
    
    @abstractmethod
    def get_data(self):
        
        return None