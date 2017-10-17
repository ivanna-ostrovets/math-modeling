from generators.linear_congruential import linear_congruential


GENERATORS = {
    0: linear_congruential,
}


if __name__ == "__main__":
    min, max = 100, 110

    print('Generator numbers:')
    print('0 - Linear congruential generator')

    generator = int(input('Choose generator: '))

    GENERATORS[generator](min, max)


