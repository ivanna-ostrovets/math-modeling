from .linear_congruential import generate_numbers as linear_congruential
from .quadratic_congruential import generate_numbers as quadratic_congruential
from .fibonacci import generate_numbers as fibonacci
from .inverse_congruential import generate_numbers as inverse_congruential
from .utils import *


GENERATORS = {
    0: linear_congruential,
    1: quadratic_congruential,
    2: fibonacci,
    3: inverse_congruential,
}


def union(min, max):
    print('\n--- Union generator ---')
    quantity = int(input('Enter the quantity of pseudo-randomized numbers: '))
    method_1 = int(input('Enter first generator method number: '))
    method_2 = int(input('Enter second generator method number: '))

    m = generate_prime_number(min, max)
    generated_numbers = generate_numbers(min, max, quantity, method_1, method_2, m)

    print('Generated pseudo-randomized numbers (X):', generated_numbers)

    print('Real pseudo-randomized numbers (U):', list(map(lambda number: number / m, generated_numbers)))


def generate_numbers(min, max, quantity, method_1, method_2, m=None):
    if not m:
        m = generate_prime_number(min, max)

    list_1 = GENERATORS[method_1](min, max, quantity, m)
    list_2 = GENERATORS[method_2](min, max, quantity, m)

    return [(number - list_2[index]) % m for index, number in enumerate(list_1)]


if __name__ == "__main__":
    union(100, 110)
