from EnderecoCompleto import EnderecoCompleto
from EnderecoSimples import EnderecoSimples


def main():
    _a = EnderecoSimples("Av Brasil", "243", "Floresta")
    _b = EnderecoCompleto("Av Miracema", "12", "Centro", "apto 3")

    print(_a.Endereco())
    print(_b.Endereco())


if __name__ == "__main__":
    main()
