class Circo:

    def apresentar(self, command: int) -> None:
        if command == 1:
            self.__show_palhaco()
        if command == 2:
            self.__show_malabarista()
        if command == 3:
            self.__show_magico()

    def __show_palhaco(self) -> None:
        print('O palhaço está apresentando seu show')

    def __show_malabarista(self) -> None:
        print('O malabarista está apresentando seu show')
    
    def __show_magico(self) -> None:
        print('O mágico está apresentando seu show')

circo = Circo()
command = 3
circo.apresentar(command)

# Não está de acordo com o Princípio do Aberto/Fechado - O de SOLID
# Ficaria correto assim....

class Artista:
    def __init__(self, tipo: str) -> None:
        self.tipo = tipo

    def apresentar_show(self) -> None:
        print(f"O {self.tipo} está apresentando o seu show!")

class Circo_2:

    def apresentar(self, artista:Artista) -> None:
        print("O circo está funcionando.")
        artista.apresentar_show()
        print('O público aplaude, respeitou o O de SOLID')

print()
circo_2 = Circo_2()
palhaco = Artista("palhaço")
magico = Artista("mágico")
print()
circo_2.apresentar(palhaco)
print()
circo_2.apresentar(magico)
