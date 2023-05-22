from conta import Conta


def main():
    print()

    _c1 = Conta(1, 123, 'Joao', 0)  # Objeto sendo instanciado
    _c2 = Conta(3, 456, 'Maria', 0)  # Objeto sendo instanciado

    # _c1 = _c2

    if _c1 != _c2:
        print('Endereços diferentes na memória! \n')
    else:
        print('Endereços iguais na memória! \n')

    # print(f'_c1.cpf = {_c1.cpf}')
    # print(f'_c2.cpf = {_c2.cpf} \n')

    # print(f"Nome do titular da conta: {_c1.nome_titular}")
    # print(f"Número da conta: {_c1.numero}")
    # print(f"CPF do titular da conta: {_c1.cpf}")
    # print(f"Saldo da conta: {_c1.saldo}")

    _c1.gerar_extrato()
    _c2.gerar_extrato()

    _c1.depositar(1000)
    _c1.gerar_extrato()

    print(_c1.transfere_valor(_c2, 500))

    _c1.gerar_extrato()
    _c2.gerar_extrato()

if __name__ == "__main__":
    main()
