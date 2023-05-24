class ExcecaoCustomizada(Exception):
    pass


def main():
    x = -1
    if x < 0:
        raise Exception("Valor negativo!")

    x = 'Hello'
    if not type(x) is int:
        raise TypeError("Use apenas inteiros!")


if __name__ == "__main__":
    main()
