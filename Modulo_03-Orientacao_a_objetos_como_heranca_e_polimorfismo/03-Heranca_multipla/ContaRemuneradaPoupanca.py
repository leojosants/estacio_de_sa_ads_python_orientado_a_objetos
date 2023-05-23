from ContasClientesExtrato import Conta
from ContaPoupanca import ContaPoupanca


class ContaRemuneradaPoupanca(Conta, ContaPoupanca):

    # def __init__(self, taxa_remuneracao, clientes, numero, saldo, taxa_remuneracao): PARAMETRO DUPLICADO
    def __init__(self, taxa_remuneracao, clientes, numero, saldo):
        Conta.__init__(self, clientes, numero, saldo)
        ContaPoupanca.__init__(self, taxa_remuneracao)
        self.taxa_remuneracao = taxa_remuneracao

    def remuneraConta(self):
        self.saldo += self.saldo * (self.taxa_remuneracao / 30)
        self.saldo -= self.taxa_remuneracao
