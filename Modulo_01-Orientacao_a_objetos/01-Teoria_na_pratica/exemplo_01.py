class Pessoa:

    # Construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def imprimir(self):
        print(f'{self.nome}, tem {self.idade} ano(s).')

    def getIdade(self):
        return self.idade

    def setIdade(self, idade):
        self.idade = idade


class Profissional(Pessoa):  # Herança
    def __init__(self, nome, idade, profissao):
        super().__init__(nome, idade)
        self.profissao = profissao

    def imprimir(self):     # Polimorfismo
        super().imprimir()
        print(f'\t e trabalha como {self.profissao}')


# pessoa = Pessoa('Ana', 25)
# pessoa.imprimir()

profissional = Profissional('Ana', 25, 'Balconista')
profissional.imprimir()
