from abc import ABC, abstractmethod

class Trabalhador(ABC): # interface

    @abstractmethod
    def trabalhar(self) -> None: pass

    @abstractmethod
    def ir_para_casa(self) -> None: pass

    @abstractmethod
    def consultar_beneficios(self) ->  None: pass

# estabelecer que uma classe não pode ser forçada a depender de uma Interface
# que ela não utiliza

class Professor(Trabalhador):
    def trabalhar(self) -> None:
        print('O Professor está trabalhando')

    def ir_para_casa(self) -> None:
        print('O Professor está indo para casa')

    def consultar_beneficios(self) -> None:
        print('O Professor está consultando benefícios da CLT')

# implementa a Interface
class ProfessorSubstituto(Trabalhador): # não tem benefícios, ele é um substituto
    def trabalhar(self) -> None:
        print('O Professor está trabalhando')

    def ir_para_casa(self) -> None:
        print('O Professor está indo para casa')

    # quebra da segregação de Interfaces
    def consultar_beneficios(self) -> None:
        raise Exception("O Professor Substituto não tem benefícios")

p2 = ProfessorSubstituto()
p2.consultar_beneficios()