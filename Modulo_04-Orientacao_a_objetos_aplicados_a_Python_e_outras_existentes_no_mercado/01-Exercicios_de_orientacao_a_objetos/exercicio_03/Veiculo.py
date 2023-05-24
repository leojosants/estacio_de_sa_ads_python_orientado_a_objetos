class Veiculo():

    def __init__(self, modelo, velocidade_maxima, quilometros_percorridos_por_litro):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.quilometros_percorridos_por_litro = quilometros_percorridos_por_litro

    def capacidadeAssentos(self, capacidade):
        print(
            f"A capacidade máxima de assentos do veículo modelo {self.modelo} é {capacidade}")

    def imprimirVeiculo(self):
        print(f"Veículo modelo: {self.modelo}")
        print(f"Velocidade máxima: {self.velocidade_maxima}km/h")
        print(
            f"Quilômetros percorridos por litro: {self.quilometros_percorridos_por_litro}km/l")
