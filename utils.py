from random import randint


def generate_prime_number(min, max):
    number = generate_number(min, max)

    return number if is_prime(number) else generate_prime_number(min, max)


def generate_number(min, max):
    return randint(min, max)


def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False

    return True


def find_divisors(number):
    return filter(lambda element: number % element == 0, range(1, number + 1))


def find_prime_divisors(number):
    return filter(lambda element: is_prime(element), find_divisors(number))
