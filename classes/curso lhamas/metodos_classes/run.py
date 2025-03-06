class MinhaClasse:

    # quando se põe a variável fora do construtor é static
    var_estatico = "Marcio"

    def __init__(self, estado: bool) -> None:
        self.__estado = estado

    def print_variavel_de_classe(self):
        # self aqui é fundamental para acessar o cara lá de cima
        print(self.var_estatico)

    @classmethod
    def alterar_variavel_de_classe(cls):
        cls.var_estatico = "qualquer_coisa"

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)
obj1.print_variavel_de_classe()
obj1.alterar_variavel_de_classe()
print(obj1.var_estatico)
print(obj2.var_estatico)
print(MinhaClasse.var_estatico)

obj2.var_estatico = "eu"
print(obj1.var_estatico)
print(obj2.var_estatico)
print(MinhaClasse.var_estatico)

