from .utils import *


def inverse_congruential(min, max):
    print('\n--- Inverse congruential generator ---')
    quantity = int(input('Enter the quantity of pseudo-randomized numbers: '))

    m = generate_prime_number(min, max)
    generated_numbers = generate_numbers(min, max, quantity, m)

    print('Generated pseudo-randomized numbers (X):', generated_numbers)

    print('Real pseudo-randomized numbers (U):', list(map(lambda number: number / m, generated_numbers)))


def generate_numbers(min, max, quantity, m=None):
    x, a, c, m, p = generate_coefficients(min, max, m)

    return list(generator(x, a, c, m, quantity))


def generate_coefficients(min, max, m=None):
    if not m:
        m = generate_prime_number(min, max)

    p = generate_prime_number(min, max)
    x = generate_number(0, p - 1)
    c = generate_number(0, p - 1)
    a = generate_number(0, c - 1)

    return x, a, c, m, p


def generator(x, a, c, p, quantity):
    while quantity > 0:
        yield x

        inversed = get_inversed(x, p)
        x = (a * inversed + c) % p
        quantity -= 1


if __name__ == "__main__":
    inverse_congruential(100, 110)
