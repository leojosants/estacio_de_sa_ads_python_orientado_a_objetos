from contas1 import Conta
from clientes1 import Cliente

cliente1 = Cliente(1234, 'Leonardo', 'Rua 10')
cliente2 = Cliente(9124, 'Vital', 'Rua 1023')

conta1 = Conta([cliente1, cliente2], 100, 2000)

print()
conta1.gerar_saldo()

print()
print(conta1.depositar(1000))
conta1.gerar_saldo()

print()
print(conta1.sacar(1500))
conta1.gerar_saldo()
print()

conta1.extrato.extrato(conta1.numero)
print()
