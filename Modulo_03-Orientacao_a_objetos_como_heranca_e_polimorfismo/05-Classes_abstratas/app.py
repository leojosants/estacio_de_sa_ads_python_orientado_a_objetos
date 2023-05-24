from ContaCliente import ContaCliente
from ContaComum import ContaComum
from ContaVIP import ContaVIP


def main():

    # conta_cliente_1 = ContaCliente(1, 0.1, 0.25, 0.1)

    conta_comum_1 = ContaComum(1, 0.1, 0.01, 2000, 0.03)
    conta_vip_1 = ContaVIP(1, 0.5, 0.05, 4000, 0.10)

    print(conta_comum_1.calculoRendimento())
    print(conta_vip_1.calculoRendimento())


if __name__ == "__main__":
    main()
