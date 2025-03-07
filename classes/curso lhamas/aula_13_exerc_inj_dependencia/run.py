class ConectorBancoDados:
    def __init__(self) -> None:
        self.connection = None

    def conectar_ao_banco(self) -> None:
        self.connection = True


class RepositorioBancoDados:
    def __init__(self, conexao: ConectorBancoDados) -> None:
        self.__conexao = conexao

    def busca_dados(self) -> list:
        if self.__conexao.connection:
            return [1,2,3,4,5]
        return None
        

class RegraNegocio:
    def __init__(self, repo: RepositorioBancoDados) -> None:
        self.__repo = repo

    def calcular_resultados(self) -> None:
        dados = self.__repo.busca_dados()
        if not dados:
            print('Dados não encontrados, verifique sua Conexão com o Banco de Dados.')
        else:
            resposta = 0
            for dado in dados:
                resposta += dado
            print(f'resultado é {resposta=}')

        
conn = ConectorBancoDados()
conn.conectar_ao_banco()

repo = RepositorioBancoDados(conn)
regra = RegraNegocio(repo)

regra.calcular_resultados()

