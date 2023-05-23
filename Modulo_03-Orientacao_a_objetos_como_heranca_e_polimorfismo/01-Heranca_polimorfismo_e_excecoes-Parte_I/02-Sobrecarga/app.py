def somar(_x, _y, _z = 0):
    return _x + _y + _z


def main():

    valor_1 = 20
    valor_2 = 30
    valor_3 = 50

    print(f'\nA soma entre {valor_1} e {valor_2} é: {somar(valor_1, valor_2)}')
    print(
        f'A soma entre {valor_1}, {valor_2} e {valor_3} é: {somar(valor_1, valor_2, valor_3)} \n')


if __name__ == "__main__":
    main()
