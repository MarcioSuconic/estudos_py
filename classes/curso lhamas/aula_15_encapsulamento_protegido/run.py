class Mamifero:
    def __init__(self, localizacao: str) -> None:
        self.localizacao = localizacao
        self._tamanho = 1.23

    def andar(self) -> None:
        print(f'mamífero andando... pelo {self.localizacao}')

    def _dormir(self) -> None:
        print('O animal está dormindo')


class Gato(Mamifero):    
    def __init__(self, localizacao: str) -> None:
        super().__init__(localizacao)
    
    def miar(self):
        print(f'O gato que está em {self.localizacao} está miando')
        self._dormir()
        print(self._tamanho)

cat = Gato('Argentina')
cat.miar()
cat._dormir() # deveria dar erro em outras linguagens, pois é protegido, em python não tem métodos protegidos fora da classe mãe e filha
print(cat._tamanho)
