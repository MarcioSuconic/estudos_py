class Loja:

    taxa = 1.15

    def __init__(self, valor: float) -> None:
        self.valor = valor

    def consultar_valor_produto(self) -> None:
        self.valor_produto = self.valor * self.taxa
        print(self.valor_produto)

    @classmethod
    def editar_taxa_rede(cls, taxa_new: float) -> None:
        cls.taxa = taxa_new

    def editar_taxa_loja(self, taxa_new: float) -> None:
        self.taxa = taxa_new

Loja1 = Loja(100)
Loja2 = Loja(100)
Loja1.consultar_valor_produto() 
Loja.editar_taxa_rede(2)
Loja2.editar_taxa_loja(3)
Loja1.consultar_valor_produto()
Loja2.consultar_valor_produto()