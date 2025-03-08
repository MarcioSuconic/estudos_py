# não existe em Python uma entidade, um elemento que se utilize que seja declaradamente uma interface
# utilizamos classes abstratas com métodos abstratos para fazer uma Interface

from abc import ABC, abstractmethod

class Trabalhador(ABC): # interface

    @abstractmethod
    def trabalhar(self) -> None: pass

    @abstractmethod
    def ir_para_casa(self) -> None: pass

    @abstractmethod
    def horario_de_almoco(self) ->  None: pass

# Interface é uma
# pré-construção de uma classe atuante
class Professor(Trabalhador):
    def trabalhar(self) -> None:
        print('O Professor está trabalhando')

    def ir_para_casa(self) -> None:
        print('O Professor está indo para casa')

    def horario_de_almoco(self) -> None:
        print('O Professor está almoçando')

class Engenheiro(Trabalhador):
    def trabalhar(self) -> None:
        print('O Engenheiro está trabalhando')

    def ir_para_casa(self) -> None:
        print('O Engenheiro está indo para casa')

    def horario_de_almoco(self) -> None:
        print('O Engenheiro está almoçando')

# Por quê é interessante trabalhar com Interfaces....
# Conseguimos tipar em trabalhador: Trabalhador
def comunicar_o_trabalhador(trabalhador: Trabalhador):
    trabalhador.trabalhar()
    print('Comunicar o trabalhador para ir para casa')
    trabalhador.ir_para_casa()

p1 = Professor()
p2 = Engenheiro()

comunicar_o_trabalhador(p1)
print()
comunicar_o_trabalhador(p2)

#UML
# linha é tracejada - - - - - - - - -
# seta sem ser preenchida