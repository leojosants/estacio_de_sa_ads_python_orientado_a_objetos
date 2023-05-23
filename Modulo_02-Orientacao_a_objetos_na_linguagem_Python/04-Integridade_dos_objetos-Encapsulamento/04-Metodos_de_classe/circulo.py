class Circulo:
    _total_circulos = 0

    def __init__(self, pontox, pontoy, raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        type(self)._total_circulos += 1

    # @classmethod
    # def get total_circulos(cls):
    #     return cls_.total_circulos
