class Mae:

    def __init__(self) -> None:
        self.endereco = 'Rua do Balao'
        self.Sobrenome = 'Silva'

    def comer(self) -> None:
        print('Estou comendo !!!')

    def estudar(self) -> None:
        print('Estou estudando !!!')

class Filha (Mae):
    def __init__(self):
        super().__init__()

Ana = Filha()
print(Ana.endereco)