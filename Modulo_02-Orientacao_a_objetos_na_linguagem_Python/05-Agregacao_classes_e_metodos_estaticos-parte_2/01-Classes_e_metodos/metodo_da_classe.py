class NomeCompleto:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    @classmethod
    def fromString(cls, texto):
        nome, sobrenome = map(str, texto.split(" "))
        objeto = cls(nome, sobrenome)
        return objeto


def main():
    registro1 = NomeCompleto.fromString("Leonardo Santos")
    print(registro1.nome, registro1.sobrenome)


if __name__ == "__main__":
    main()
