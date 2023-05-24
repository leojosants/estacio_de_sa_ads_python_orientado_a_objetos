import datetime


class ContaPoupanca:
    def __init__(self, taxa_remuneracao):
        self.taxa_remuneracao = taxa_remuneracao
        self.data_abertura = datetime.datetime.today()
        self.saldo = 0  # adicionado

    def remuneracaoConta(self):
        self.saldo += self.saldo * self.taxa_remuneracao


class ContaCliente:

    def __init__(self, numero, IOF, IR, valor_investido, taxa_rendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valor_investido = valor_investido
        self.taxa_rendimento = taxa_rendimento

    def calculoRendimento(self):
        self.valor_investido += (self.valor_investido * self.taxa_rendimento)
        self.valor_investido = (self.valor_investido -
                                (self.taxa_rendimento * self.IOF * self.IR))

    def extrato(self):  # (1)
        print(
            f"O saldo atual da conta {self.numero} é {self.valor_investido:10.2f}")
