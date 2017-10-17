from ..utils import *


def linear_congruential(min, max):
    print('\n--- Linear congruential generator ---')
    sequence_length = int(input('Enter the quantity of pseudo-randomized numbers: '))

    x, a, c, m = generate_coefficients(min, max)

    print(list(generator(x, a, c, m, sequence_length)))


def generate_coefficients(min, max):
    m = generate_prime_number(min, max)
    x = generate_number(0, m - 1)
    c = generate_prime_number(0, m - 1)

    divisors = find_prime_divisors(m)
    temp = generate_number(0, m - 1)

    while not all((temp - 1) % divisor == 0 for divisor in divisors):
        temp = generate_number(0, m - 1)

    a = temp

    return x, a, c, m


def generator(x, a, c, m, quantity):
    while quantity > 0:
        yield x

        x = (a * x + c) % m
        quantity -= 1


if __name__ == "__main__":
    linear_congruential(100, 110)
