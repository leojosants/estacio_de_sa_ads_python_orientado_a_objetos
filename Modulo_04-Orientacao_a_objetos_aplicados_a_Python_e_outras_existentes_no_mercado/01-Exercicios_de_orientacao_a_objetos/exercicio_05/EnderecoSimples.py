class EnderecoSimples(object):
    def __init__(self, rua, num, bairro):
        self.rua = rua
        self.num = num
        self.bairro = bairro

    def Endereco(self):
        return self.rua + ", " + self.num + ", " + self.bairro
