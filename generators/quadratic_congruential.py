from .utils import *


def quadratic_congruential(min, max):
    print('\n--- Quadratic congruential generator ---')
    quantity = int(input('Enter the quantity of pseudo-randomized numbers: '))

    m = generate_prime_number(min, max)
    generated_numbers = generate_numbers(min, max, quantity, m)

    print('Generated pseudo-randomized numbers (X):', generated_numbers)

    print('Real pseudo-randomized numbers (U):', list(map(lambda number: number / m, generated_numbers)))


def generate_numbers(min, max, quantity, m=None):
    x, a, d, c, m = generate_coefficients(min, max, m)

    return list(generator(x, a, d, c, m, quantity))


def generate_coefficients(min, max, m=None):
    if not m:
        m = generate_prime_number(min, max)

    x = generate_number(0, m - 1)
    c = generate_prime_number(0, m - 1)

    divisors = find_prime_divisors(m)

    if 2 in divisors:
        divisors.remove(2)

    temp = generate_number(0, m - 1)

    while not all((temp - 1) % divisor == 0 for divisor in divisors):
        temp = generate_number(0, m - 1)

    a = temp

    if m % 4 == 0:
        d = (a - 1) % 4
    elif m % 2 == 0:
        d = (a - 1) % 2
    elif m % 3 == 0:
        excluded = 3 * c % 9
        divisors = list(filter(lambda divisor: divisor != excluded, divisors))

    temp = generate_number(0, m - 1)

    while not all(temp % divisor == 0 for divisor in divisors):
        temp = generate_number(0, m - 1)

    d = temp

    return x, a, d, c, m


def generator(x, a, d, c, m, quantity):
    while quantity > 0:
        yield x

        x = (d * x * x + a * x + c) % m
        quantity -= 1


if __name__ == "__main__":
    quadratic_congruential(100, 110)
