def main():
    x = 10

    if x > 5:
        raise Exception(
            f"'X' não pode ser maior do que '5'. O valor de 'X' foi de: {x}"
        )


if __name__ == "__main__":
    main()
