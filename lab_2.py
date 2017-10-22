from generators.linear_congruential import generate_numbers


MIN = 100
MAX = 100


def generate_point():
    r = generate_numbers(MIN, MAX, 1)
    g = generate_numbers(MIN, MAX, 1)


if __name__ == '__main__':
    print('Enter rectangle coordinates ((a, c), (b, c), (a, d), (b, d))')
    a = int(input('a: '))
    b = int(input('b: '))

    while a > b:
        b = int(input('b should not exceed a: '))

    c = int(input('c: '))
    d = int(input('d: '))

    while c > d:
        d = int(input('d should not exceed c: '))

    n = int(input('Enter n (points number): '))

    square = int(((b - a) ** 2) ** 0.5 * ((d - c) ** 2) ** 0.5)

