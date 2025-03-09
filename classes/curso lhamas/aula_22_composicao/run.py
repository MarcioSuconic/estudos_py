class Select:
    def by_id(self) -> any:
        print('selecionando um elemento no banco de dados')

    
class Insert:
    def inserir_value(self) -> None:
        print('inserindo um valor no BD')


class Repositorio:
    def __init__(self) -> None:
        self.__select = Select() # composicao, podia ser importando...
        self.__insert = Insert() # composicao

    def select_by_id(self, id: int) -> any:
        self.__select.by_id()

repo = Repositorio()
repo.select_by_id(45)
