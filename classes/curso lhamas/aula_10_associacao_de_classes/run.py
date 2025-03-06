class Interruptor:

    def __init__(self, comodo: str) -> None:
        self.comodo = comodo

    def acender(self) -> None:
        print(f"Estou acendendo o {self.comodo}")

    def apagar(self) -> None:
        print(f'Estou apagando o {self.comodo}')


class Pessoa:

    def acionar_on_interruptor(self, interruptor:Interruptor) -> None:
        interruptor.acender()

    def acionar_off_interruptor(self, interruptor:Interruptor) -> None:
        interruptor.apagar()

    def dormir(self) -> None:
        print('Foi dormir.....!')

Agnaldo = Pessoa()
interruptor_sala = Interruptor("sala")
interruptor_quarto = Interruptor("quarto")
Agnaldo.acionar_on_interruptor(interruptor_quarto)
Agnaldo.acionar_off_interruptor(interruptor_sala)
Agnaldo.acionar_off_interruptor(interruptor_quarto)
Agnaldo.dormir()