# classes abstratas

# elementos abstratos em Python
from abc import ABC, abstractmethod

# classe abstrata não possui objetos, em tese.
class Pessoa(ABC):
    def correr(self):
        print('A pessoa está correndo de manhã.')

    # força as classes filhas a terem o método trabalhar
    @abstractmethod
    def trabalhar(self):
        pass

class Professor(Pessoa):
    def trabalhar(self):
        print('O Professor está dando aula...')

class Cozinheiro(Pessoa):
    def trabalhar(self):
        print('O Cozinheiro está na cozinha.........')

p1 = Professor()
p1.trabalhar()
p1.correr()

p2 = Cozinheiro()
p2.trabalhar()
p2.correr()
