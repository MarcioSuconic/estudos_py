from elemento import Elemento

class Principal:
    def __init__(self) -> None:
        self.__elem = Elemento()

    def run(self) -> None:
        self.__elem.executar()
        print("Estou finalizando na classe principal")

cl1 = Principal()
cl1.run()