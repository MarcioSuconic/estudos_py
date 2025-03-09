from abc import ABC, abstractmethod

class ElementoInterface(ABC):
    
    @abstractmethod
    def executar(self) -> None:
        print("Estou executando o elemento.....")

