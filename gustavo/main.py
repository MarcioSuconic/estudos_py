class Carros:

    def __init__(self, marca, modelo, cor, velocidade_maxima, velocidade_atual=0):
        self.marca = marca
        self.model = modelo
        self.cor = cor
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = velocidade_atual
        self.descricao = f'{marca} - {modelo} - {cor}'

    def alterar_velocidade(self, velocidade):        
        self.velocidade_atual = velocidade
        if velocidade > self.velocidade_maxima:
            self.velocidade_atual = self.velocidade_maxima

        if velocidade < 0:
            self.velocidade_atual = 0


corola = Carros("Toyota","Corolla XEI", "prata", 240, 60)
fusca = Carros("VW", "Fusca bolinha", "bege", 95)
siena = Carros("FIAT", "Siena Copa", "vermelha", 120)

print(f'O corola tem a cor {corola.cor}')
print(f'O corola tem a velocidade de {corola.velocidade_atual}')
corola.alterar_velocidade(320)
print(f'O corola tem a velocidade de {corola.velocidade_atual}')

print(f'O fusca tem a cor {fusca.cor}')
print(f'O fusca tem a velocidade de {fusca.velocidade_atual}')
fusca.alterar_velocidade(60)
print(f'O fusca tem a velocidade de {fusca.velocidade_atual}')


print(f'O siena tem a cor {siena.cor}')
print(f'O siena tem a velocidade de {siena.velocidade_atual}')
siena.alterar_velocidade(20)
print(f'O siena tem a velocidade de {siena.velocidade_atual}')


