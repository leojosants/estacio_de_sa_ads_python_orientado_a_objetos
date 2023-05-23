class Argentina():

    def capital(self):
        print("Buenos Aires é a capital da Argentina.")

    def lingua_oficial(self):
        print("O espanhol é a língua oficial da Argentina.")


class Brasil():

    def capital(self):
        print("Brasília é a capital do Brasil.")

    def lingua_oficial(self):
        print("O português é a língua oficial do Brasil.")


def main():
    obj_arg = Argentina()
    obj_bra = Brasil()

    print()

    for pais in (obj_arg, obj_bra):
        pais.capital()
        pais.lingua_oficial()


if __name__ == "__main__":
    main()
