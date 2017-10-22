from generators.linear_congruential import linear_congruential
from generators.quadratic_congruential import quadratic_congruential
from generators.fibonacci import fibonacci
from generators.inverse_congruential import inverse_congruential
from generators.union import union


GENERATORS = {
    0: linear_congruential,
    1: quadratic_congruential,
    2: fibonacci,
    3: inverse_congruential,
    4: union,
}


if __name__ == "__main__":
    min, max = 100, 110

    print('Generator numbers:')
    print('0 - Linear congruential generator')
    print('1 - Quadratic congruential generator')
    print('2 - Fibonacci numbers generator')
    print('3 - Inverse congruential generator')
    print('4 - Union generator')

    generator = int(input('\nChoose generator: '))

    GENERATORS[generator](min, max)


