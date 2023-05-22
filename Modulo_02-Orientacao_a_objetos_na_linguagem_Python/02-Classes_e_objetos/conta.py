class Conta:
    # Construtor
    def __init__(self, numero, cpf, nome_titular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nome_titular = nome_titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def gerar_extrato(self):
        print(
            f'Extrato --> Número: {self.numero}\t Titular: {self.nome_titular}\t cpf: {self.cpf}\t saldo: {self.saldo}')

    def transfere_valor(self, conta_destino, valor):
        if self.saldo < valor:
            return ("Não existe saldo suficiente")
        else:
            conta_destino.depositar(valor)
            self.saldo -= valor
        return f"Transferencia no valor de R$ {valor} realizada!"
