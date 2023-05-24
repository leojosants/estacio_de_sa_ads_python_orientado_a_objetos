from EnderecoSimples import EnderecoSimples


class EnderecoCompleto(EnderecoSimples):
    def __init__(self, rua, num, bairro, complemento):
        super().__init__(rua, num, bairro)
        self.complemento = complemento

    def Endereco(self):
        return super(EnderecoCompleto, self).Endereco() + ", " + self.complemento
