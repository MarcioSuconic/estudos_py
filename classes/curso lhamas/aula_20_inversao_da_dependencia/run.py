from elementos.interfaces.elemento_interface import ElementoInterface
from elementos.elemento import Elemento
from elementos.elemento_2 import Elemento_2

class Principal:
    def __init__(self) -> None:
        self.__elem = Elemento()

    def run(self) -> None:
        self.__elem.executar()
        print("Estou finalizando na classe principal")

cl1 = Principal()
cl1.run()

# nada de errado aqui
# relação muito dura muito forte, relação de dependência muito forte
# se mudar Elementos complica

#dentro da pasta elementos vai ser criado o correto
# segue o correto.....
class Principal_new:
    def __init__(self, elem: ElementoInterface) -> None:
        self.__elem = elem

    def run(self) -> None:
        self.__elem.executar()
        print("Estou finalizando na classe principal")

print('-----------------------')

el = Elemento()
cl2 = Principal_new(el)
cl2.run()

# classe Principal_new pega dados de uma Interface
# facilitador

# dá para fazer um elemento_2 .....

cl3 = Elemento_2()
cl3 = Principal_new(el)
cl3.run()