from Clientes import Cliente
from ContasClientesExtrato import Conta
from ContaPoupanca import ContaPoupanca
from ContaRemuneradaPoupanca import ContaRemuneradaPoupanca


def main():
    cliente_1 = Cliente("123", "João", "Rua X")
    cliente_2 = Cliente("456", "Maria", "Rua W")
    conta_1 = Conta([cliente_1, cliente_2], 1, 2000)
    conta_poupanca_1 = ContaPoupanca(0.1)

    # conta_remunerada_1 = ContaRemuneradaPoupanca(0.1, cliente_1, 5, 1000, 5) PARAMENTRO DUPLICADO
    conta_remunerada_1 = ContaRemuneradaPoupanca(0.1, cliente_1, 5, 1000)

    print()
    conta_remunerada_1.remuneraConta()
    conta_remunerada_1.gerar_saldo()


if __name__ == "__main__":
    main()
