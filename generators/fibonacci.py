from .utils import *


def fibonacci(min, max):
    print('\n--- Fibonacci numbers generator ---')
    quantity = int(input('Enter the quantity of pseudo-randomized numbers: '))

    m = generate_prime_number(min, max)
    generated_numbers = generate_numbers(min, max, quantity, m)

    print('Generated pseudo-randomized numbers (X):', generated_numbers)

    print('Real pseudo-randomized numbers (U):', list(map(lambda number: number / m, generated_numbers)))


def generate_numbers(min, max, quantity, m=None):
    if not m:
        m = generate_prime_number(min, max)

    return list(generator(m, quantity))


def generator(m, quantity):
    x1, x2 = 0, 1

    yield x1
    yield x2
    quantity -= 2

    while quantity > 0:
        x3 = (x1 + x2) % m
        yield x3

        x1, x2 = x2, x3
        quantity -= 1


if __name__ == "__main__":
    fibonacci(100, 110)
