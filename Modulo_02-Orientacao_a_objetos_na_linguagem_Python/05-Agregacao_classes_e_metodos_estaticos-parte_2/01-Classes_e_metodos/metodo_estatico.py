class NomeCompleto:

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    @classmethod
    def fromString(cls, texto):
        nome, sobrenome = map(str, texto.split(" "))
        objeto = cls(nome, sobrenome)
        return objeto

    @staticmethod
    def isValid(texto):
        nomes = texto.split(" ")
        return len(nomes) > 1

def main():
    print(NomeCompleto.isValid("Leonardo"))

if __name__ == "__main__":
    main()
