from contas import Conta
from clientes import Cliente


cliente1 = Cliente(1234, 'Leonardo Santos', 'Rua 10')
cliente2 = Cliente(9124, 'Vitor Lemos', 'Rua 1023')
cliente3 = Cliente(3214, 'Vilma Andrade', 'Rua 1023423')
cliente4 = Cliente(5324, 'Dênis Corrêia', 'Rua 1023')

conta1 = Conta([cliente1, cliente2], 100, 0)
conta2 = Conta([cliente3, cliente4], 200, 0)

print('\nRelação de CONTAS:')

for c in conta1.clientes:
    print(f'\tTitular: {c.nome} \t Endereço: {c.endereco}')

for c in conta2.clientes:
    print(f'\tTitular: {c.nome} \t Endereço: {c.endereco}')
