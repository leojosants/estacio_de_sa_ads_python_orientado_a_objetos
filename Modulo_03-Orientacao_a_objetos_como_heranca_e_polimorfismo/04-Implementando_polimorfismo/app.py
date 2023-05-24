from Banco import Banco
from ContaCliente import ContaCliente
from ContaComum import ContaComum
from ContaRemunerada import ContaRemunerada


def main():

    banco_1 = Banco(999, "teste")

    conta_cliente_1 = ContaCliente(1, 0.01, 0.1, 1000, 0.05)
    conta_comum_1 = ContaComum(2, 0.01, 0.1, 2000, 0.05)
    conta_remunerada_1 = ContaRemunerada(3, 0.01, 0.1, 2000, 0.05)

    banco_1.adicionaConta(conta_cliente_1)      # (4)
    banco_1.adicionaConta(conta_comum_1)        # (5)
    banco_1.adicionaConta(conta_remunerada_1)   # (6)
    banco_1.calculaRendimentoMensal()           # (7)
    banco_1.imprimeSaldoContas()                # (8)


if __name__ == "__main__":
    main()
