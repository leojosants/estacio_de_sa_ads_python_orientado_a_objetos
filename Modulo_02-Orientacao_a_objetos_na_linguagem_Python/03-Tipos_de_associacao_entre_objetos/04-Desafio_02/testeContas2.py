from contas2 import Conta
from clientes2 import Cliente

cliente1 = Cliente(1234, 'Leonardo', 'Rua 10')
cliente2 = Cliente(9124, 'Vital', 'Rua 1023')
cliente3 = Cliente(9124, 'Megane', 'Rua 123')
cliente4 = Cliente(9124, 'Rhuan', 'Rua 343')

conta1 = Conta([cliente1, cliente2], 100, 2000)
conta2 = Conta([cliente3, cliente4], 200, 0)

print()
conta1.gerar_saldo()
conta1.transfere_valor(conta2, 2000)

print()
conta2.extrato.extrato(cliente1)
conta2.gerar_saldo()
print()

# print()
# conta1.gerar_saldo()

# print()
# conta1.gerar_saldo()
# print(conta1.depositar(1000))
# print()
# print(conta1.sacar(1500))
# conta1.gerar_saldo()
# print()

# conta1.extrato.extrato(conta1.numero)
# print()
