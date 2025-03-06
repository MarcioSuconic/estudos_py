
class Pessoa:
    
    def __init__(self, altura, cpf) -> None:
        self.altura = altura
        self.__cpf = cpf

    def apresentar(self):
        print(f'Olá! Minha altura é: {self.altura}')
        self.__coletar_documento()

    def __coletar_documento(self): # métodos privados
        print(f'Meu documento é {self.__cpf}')

Jorge = Pessoa(1.70,"17487468801")
Jorge.apresentar()
print(Jorge.altura)

