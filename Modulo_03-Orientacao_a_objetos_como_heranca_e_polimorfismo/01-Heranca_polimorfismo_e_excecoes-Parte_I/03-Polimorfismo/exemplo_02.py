class Veiculo():
    def rodar(self):
        print("Reduz o consumo de combustível.")


class VeiculoEletrico(Veiculo):
    def rodar(self):
        super().rodar()
        print("Esse veículo utiliza eletricidade.")


def main():
    veiculo_eletrico = VeiculoEletrico()

    print()
    veiculo_eletrico.rodar()
    print()


if __name__ == "__main__":
    main()
