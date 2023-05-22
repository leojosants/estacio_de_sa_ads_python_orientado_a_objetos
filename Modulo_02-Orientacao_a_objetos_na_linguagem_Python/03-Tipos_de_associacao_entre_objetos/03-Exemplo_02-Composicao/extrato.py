class Extrato:
    def __init__(self):
        self.transacoes = []

    def extrato(self, numero_conta):
        print(f"Extrato da conta número: {numero_conta}")

        for _p in self.transacoes:
            print(
                f" - {_p[0]:10s} {_p[1]:10.2f} {_p[2]:10s} {_p[3].strftime('%d/%b/%y')}")
