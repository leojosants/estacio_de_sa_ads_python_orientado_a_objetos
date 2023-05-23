import datetime


class ContaPoupanca:
    def __init__(self, taxa_remuneracao):
        self.taxa_remuneracao = taxa_remuneracao
        self. data_abertura = datetime.datetime.today()

        def remuneracaoConta(self):
            self.saldo += self.saldo * self.taxa_remuneracao
