from contas import Conta
from clientes import Cliente

cliente1 = Cliente(1234, 'Leonardo', 'Rua 10')
cliente2 = Cliente(9124, 'Vital', 'Rua 1023')

conta1 = Conta([cliente1, cliente2], 100, 0)

print()
conta1.gerar_saldo()

print()
print(conta1.depositar(1500))
conta1.gerar_saldo()

print()
print(conta1.sacar(500))
conta1.gerar_saldo()
