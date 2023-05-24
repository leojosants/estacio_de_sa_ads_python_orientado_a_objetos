# Classe Salário
class Salario:
    def __init__(self, base, bonus):
        self.base = base
        self.bonus = bonus

    def salario_anual(self):
        return (self.base * 12) + self.bonus


class Empregado:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario_agregado = salario  # agregação

    #
    def salario_total(self):
        return self.salario_agregado.salario_anual()


salario = Salario(10000, 700)
empregado = Empregado('Leonardo', 38, salario)
print(empregado.salario_total())
