class ClasseSomaMultiplica:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def somar(self):
        return self.a + self.b

    def multiplicar(self):
        return self.a * self.b


class Derivada(ClasseSomaMultiplica):
    def subtrair(self):
        return self.a - self.b

    def dividir(self):
        return self.a / self.b


def main():
    valor_1 = 10
    valor_2 = 20

    _d = Derivada(valor_1, valor_2)

    print(f'\nA soma de {valor_1} com {valor_2} é: {_d.somar()}')
    print(f'{issubclass(Derivada, ClasseSomaMultiplica)} \n')


if __name__ == "__main__":
    main()
