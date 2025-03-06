class MinhaClasse:

    # quando se põe a variável fora do construtor é static
    var_estatico = "Marcio"

    def __init__(self, estado: bool) -> None:
        self.__estado = estado
        print(self.__estado)

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)
print(obj1.var_estatico)
print(obj2.var_estatico)
print(MinhaClasse.var_estatico)
obj2.var_estatico = "diferente"
print(obj1.var_estatico)
print(obj2.var_estatico)
print(MinhaClasse.var_estatico)

MinhaClasse.var_estatico = "programador"
print(obj1.var_estatico)
print(obj2.var_estatico)
print(MinhaClasse.var_estatico)
# todo munda muda
MinhaClasse.var_estatico = "Cláudio"
print(obj1.var_estatico)
print(obj2.var_estatico)
print(MinhaClasse.var_estatico)

# contexto da classe e tem o contexto do objeto