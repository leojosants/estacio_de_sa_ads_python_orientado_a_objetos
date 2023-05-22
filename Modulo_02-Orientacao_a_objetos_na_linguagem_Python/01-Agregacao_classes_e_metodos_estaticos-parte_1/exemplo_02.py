""" Método de Classe x Método estático  """
from datetime import date


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    """ Um método de classe para criar um objeto Pessoa através do ano de nascimento """
    @classmethod
    def apartirAnoNascimento(cls, nome, ano):
        return cls(nome, date.today().year - ano)

    """ Métodos Estático: Verificar se é maior de idade.    """
    @staticmethod
    def ehMaioridade(idade):
        return idade >= 18


pessoa1 = Pessoa('Leonardo', 38)
pessoa2 = Pessoa.apartirAnoNascimento('Leonardo Santos', 1984)

print(pessoa1.idade)
print(pessoa2.idade)

# Imprimir o resultado
print(Pessoa.ehMaioridade(17))
