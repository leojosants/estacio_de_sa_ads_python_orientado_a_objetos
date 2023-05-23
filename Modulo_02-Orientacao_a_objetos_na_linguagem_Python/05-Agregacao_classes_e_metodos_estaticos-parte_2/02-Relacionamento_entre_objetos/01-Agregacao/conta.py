class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes                    # agregação
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return f"DEPÓSITO --> Depósito no valor de R${valor} realizado!"

    def sacar(self, valor):
        if self.saldo < valor:
            return "SAQUE --> não realiado, Saldo Insuficiente!"
        else:
            self.saldo -= valor
            return "SAQUE --> realizado!"
