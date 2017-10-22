from .utils import *


def linear_congruential(min, max):
    print('\n--- Linear congruential generator ---')
    quantity = int(input('Enter the quantity of pseudo-randomized numbers: '))

    m = generate_prime_number(min, max)
    generated_numbers = generate_numbers(min, max, quantity, m)

    print('Generated pseudo-randomized numbers (X):', generated_numbers)

    print('Real pseudo-randomized numbers (U):', list(map(lambda number: number / m, generated_numbers)))


def generate_numbers(min, max, quantity, m=None):
    x, a, c, m = generate_coefficients(min, max, m)

    return list(generator(x, a, c, m, quantity))


def generate_coefficients(min, max, m=None):
    if not m:
        m = generate_prime_number(min, max)

    x = generate_number(0, m - 1)
    c = generate_prime_number(0, m - 1)

    divisors = find_prime_divisors(m)

    if m % 4 == 0:
        divisors = list(filter(lambda divisor: divisor % 4 == 0, divisors))

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


if __name__ == '__main__':
    linear_congruential(100, 110)
