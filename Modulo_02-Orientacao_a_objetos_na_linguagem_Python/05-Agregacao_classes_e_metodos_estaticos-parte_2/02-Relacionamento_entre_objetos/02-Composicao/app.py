from conta import Conta, Extrato
from cliente import Cliente

cliente1 = Cliente("111111111-11", "Leonardo", "Belo Horizonte")
cliente2 = Cliente("111155551-11", "Leonel", "Ritápolis")

conta_conjunta = Conta([cliente1, cliente2], 1000, 20)

conta_conjunta.depositar(1000)
conta_conjunta.sacar(500)
conta_conjunta.extrato.imprimir()