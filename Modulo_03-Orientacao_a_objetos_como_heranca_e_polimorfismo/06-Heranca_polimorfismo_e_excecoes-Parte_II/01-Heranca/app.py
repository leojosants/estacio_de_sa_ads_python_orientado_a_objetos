from Clientes import Cliente
from ContasClientesExtrato import Conta
from ContaEspecial import ContaEspecial


def main():
    cliente_1 = Cliente("123", "João", "Rua X")
    cliente_2 = Cliente("456", "Maria", "Rua W")
    cliente_3 = Cliente("789", "Joana", "Rua H")

    conta_1 = Conta([cliente_1, cliente_2], 1, 2000)
    conta_2 = ContaEspecial([cliente_3], 3, 1000, 2000)

    print()
    conta_2.depositar(100)
    conta_2.sacar(3200)
    conta_2.extrato.extrato(conta_2.numero)

if __name__ == "__main__":
    main()
