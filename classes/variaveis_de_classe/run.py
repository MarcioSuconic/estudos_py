
class MinhaClasse:

    estatico = "Marcio"

    def __init__(self, estado: bool) -> None:
        self.__estado = estado

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)

MinhaClasse.estatico = "Cláudio"
obj1.estatico = "joão"
MinhaClasse.estatico = "Cláudio 2"

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)