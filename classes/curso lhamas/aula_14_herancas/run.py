class Mamifero:
    def __init__(self, localizacao="Brasil") -> None:
        self.localizacao = localizacao

    def andar(self) -> None:
        print(f'mamífero andando... pelo {self.localizacao}')


class Cachorro(Mamifero):
    # quando põe o método init já vem o super().__init__
    # ele chama o init da classe superior
    def __init__(self, localizacao="Brasil") -> None:
        super().__init__(localizacao) # refere-se ao construtor da classe superior, quando eu passo a localizacao 
        # para Cachorro, Cachorro já passa para Mamifero tambem

    def latir(self) -> None:
        print("O cachorro está latindo...")
        self.andar()    


class Gato(Mamifero):    
    def __init__(self, localizacao="Brasil") -> None:
        super().__init__(localizacao)
    
    def miar(self):
        print('O gato está miando')


dog = Cachorro('Ioguslávia')
dog.andar()
valor = dog.localizacao
print(valor)

dog.latir()

cat = Gato('Noruega')
cat.miar()