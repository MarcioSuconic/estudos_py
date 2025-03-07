class Celular:
    def __init__(self, modelo):
        self.modelo = modelo
        
    def enviar_mensagem(self, mensagem: str) -> None:
        print (f'enviando mensagem {mensagem}')

    def abrir_emails(self) -> None:
        print('abrindo emails')

    def abrir_youtube(self) -> None:
        print('Abrindo YouTube...')

android = Celular("Samsung")
iphone = Celular("iphone")

class Pessoa:
    def __init__(self, celular:Celular) -> None:
        self.__celular = celular

    def pedir_pizza(self) -> None:
        print(f'buscando o celular...')
        print('definindo o sabor....')
        self.__celular.enviar_mensagem('quero uma pizza de Calabresa')
        print('aguardando a chegada da pizza')

    def estudar(self) -> None:
        print('Sentado ao computador')
        self.__celular.abrir_youtube()
        print("anotando o conteúdo")

Reginaldo = Pessoa(android)
Marlene = Pessoa(iphone)

Reginaldo.pedir_pizza()
print()
Marlene.estudar()

# livro clean code, dependencia tem que ser um atributo privado da classe