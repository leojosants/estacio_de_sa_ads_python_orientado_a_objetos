from cliente import Cliente
from conta import Conta

cliente1 = Cliente("111111111-11", "Leonardo", "Belo Horizonte")
cliente2 = Cliente("111155551-11", "Leonel", "Ritápolis")

conta_conjunta = Conta([cliente1, cliente2], 1000, 20)

print(f"\nSaldo: R$ {conta_conjunta.saldo}")
print(conta_conjunta.sacar(40))
print(conta_conjunta.depositar(40))
print(f"Saldo: R$ {conta_conjunta.saldo} \n")
