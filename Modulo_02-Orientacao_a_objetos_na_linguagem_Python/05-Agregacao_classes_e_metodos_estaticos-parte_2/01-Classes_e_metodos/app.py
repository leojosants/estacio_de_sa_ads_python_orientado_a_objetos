class Pessoa:

    _contador = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

        Pessoa._contador += 1

    def imprimir(self):
        print(f'{self.nome} tem {self.idade}, ano(s).')

    @property
    def contador(self):
        return type(self)._contador


def main():
    p1 = Pessoa('Leonardo', 38)
    print(p1.contador)
    print(Pessoa._contador)


if __name__ == "__main__":
    main()
