class Banco():

    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.contas = []

    def adicionaConta(self, conta_cliente):
        self.contas.append(conta_cliente)

    def calculaRendimentoMensal(self):  # (7)
        for _c in self.contas:
            _c.calculoRendimento()

    def imprimeSaldoContas(self):
        for _c in self.contas:
            print(_c.extrato())  # adicionado
