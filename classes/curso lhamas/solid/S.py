class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:

        if isinstance(nome, str) and isinstance(idade, int):
            print('Acessando o banco de dados...')
            print(f'Cadastrar usuário {nome=}, {idade=}')
        else:
            print('dados inválidos.')






# validar é uma responsabilidade
# mexer com o banco de dados é uma responsabilidade
# tratar dados é uma responsabilidade

class SistemaCadastral_2: # com as responsabilidades separadas

    def cadastrar(self, nome: str, idade: int) -> None:

        if self.__validade_input(nome,idade): # 1
            self.__register_user(nome,idade) # 2
        else:
            self.__error_handle() # 3 

    def __validade_input(self, nome: str, idade: int) -> bool: # 1
        return isinstance(nome, str) and isinstance(idade, int)
    
    def __register_user(self, nome: str, idade: int) -> None: # 2
        print('Acessando o banco de dados...') 
        print(f'Cadastrar usuário {nome=}, {idade=}')        

    def __error_handle(self) -> None: #3
        print("dados inválidos")

sistema = SistemaCadastral_2()
sistema.cadastrar("Marcio",51)