from abc import ABC, abstractmethod

class ABCInputInterpreter(ABC):
    
    @abstractmethod
    def interpret(input): 
        pass