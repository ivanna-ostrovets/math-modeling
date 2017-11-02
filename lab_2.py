from generators.linear_congruential import generate_numbers
from generators.utils import generate_prime_number


MIN = 100
MAX = 120


def choose_variables():
    # points = []

    # print('Enter four figure points')

    # for i in range(4):
    #     print('Point', i + 1)
    #     points.append((int(input('x: ')), int(input('y: '))))

    # n = int(input('Enter n (points number): '))
    # k = int(input('Enter k (experiments number): '))

    points = [(10, 5), (12, 7), (15, 6.5), (14, 5.5)]
    n = 100
    k = 120

    x_coordinates = [point[0] for point in points]
    y_coordinates = [point[1] for point in points]

    a = min(x_coordinates)
    b = max(x_coordinates)
    c = min(y_coordinates)
    d = max(y_coordinates)

    return points, a, b, c, d, n, k


def generate_point(a, b, c, d):
    m = generate_prime_number(MIN, MAX)

    r = generate_numbers(MIN, MAX, 1, m)[0] / m
    g = generate_numbers(MIN, MAX, 1, m)[0] / m

    x = (b - a) * r + a
    y = (d - c) * g + c

    return x, y


def belong_to_figure(points, point):
    result = False

    start_x, start_y = points[0]

    for index in range(1, len(points)):
        p1x, p1y = points[index]

        try:
            if ((point[0] - start_x) / (start_x - p1x)) == ((point[1] - start_y) / (start_y - p1y)):
                return True
        except ZeroDivisionError:
            return True

        if ((start_y > point[1]) != (p1y > point[1])) \
            and (point[0] < (p1x - start_x) * (point[1] - start_y) / (p1y - start_y) + start_x):
            result = not result

        start_x, start_y = p1x, p1y

    return result


if __name__ == '__main__':
    figure_points, a, b, c, d, points_number, tries = choose_variables()
    rectangle_points = [(a, c), (b, c), (a, d), (b, d)]
    rectangle_square = int(((b - a) ** 2) ** 0.5 * ((d - c) ** 2) ** 0.5)
    m, n = 0, 0
    squares = []

    for _ in range(tries):
        points = []

        for _ in range(points_number):
            point = generate_point(a, b, c, d)

            if belong_to_figure(figure_points, point):
                m += 1
            if belong_to_figure(rectangle_points, point):
                n += 1

        try:
            squares.append((m / n) * rectangle_square)
            print((m / n) * rectangle_square)
        except ZeroDivisionError:
            pass

    average_square = sum(squares) / tries

    print('\nFigure square:', average_square)
