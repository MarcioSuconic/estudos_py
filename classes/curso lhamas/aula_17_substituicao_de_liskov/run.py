class Animal:
    def alimentar(self):
        print('O Animal está se alimentando...')

class Cachorro(Animal):
    def latir(self):
        print('O Cachorro está latindo')

# aqui, tudo OK
class Peixe(Animal):
    def nadar(self):
        print('O Peixe está nadando')

# aqui há uma quebra do Princípio de Liskov
# uma classe filha pode substituir uma classe mãe - Liskov
class Peixe(Cachorro):
    def nadar(self):
        print('O Peixe está nadando')
    
    # polimorfismo
    def latir(self):
        raise Exception("Peixe não late.")
    

def verificar_animal(animal: any):
    animal.alimentar()

obj1 = Animal()
obj2 = Cachorro()
obj3 = Peixe()
verificar_animal(obj3)

