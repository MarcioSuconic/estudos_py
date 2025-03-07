class ClasseQualquer:
    def fazer(self) -> None:
        print('Estou fazendo algo')


class OutraCoisa(ClasseQualquer):
    def preparar(self) -> None:
        print('Estou preparando algo....')
    
    def fazer(self) -> None:
        print('Estou fazendo a outra coisa....')


def fazer_func() -> None:
    print('Estou fazendo a outra coisa em func....')

obj1 = ClasseQualquer()
obj2 = OutraCoisa()
obj3 = OutraCoisa()
# pode-se usar o polimorfismo assim:
obj2.fazer = fazer_func

obj1.fazer()
obj2.fazer()
obj3.fazer()

# isto é polimorfismo -> dois métodos iguais tendo comportamentos diferentes.

# pode-se descrever melhor o outro método como:

class OutraCoisa(ClasseQualquer):
    def preparar(self) -> None:
        print('Estou preparando algo....')
    
    def fazer_outra_coisa(self) -> None:
        print('Estou fazendo a outra coisa....')