from random import uniform


def system_with_recall_sources(m, c, mu, nu, la):
    r = [[] for _ in range(m + 1)]
    r[m].extend([1, 1])

    for i in range(2, c + 1):
        r[m].append(((la + (i - 1) * nu + m * mu) * r[m][i - 1] - la * r[m][i - 2]) / (i * nu))

    for j in range(m - 1, -1, -1):
        b, d = [0], [0]
        r[j].extend([0 for _ in range(c + 1)])

        for i in range(1, c + 1):
            b.append(i * nu * (j * mu + b[i - 1]) / (la + j * mu + b[i - 1]))
            d.append((j + 1) * mu * r[j + 1][i - 1] + (la * d[i - 1]) / (la + j * mu + b[i - 1]))

        r[j][c] = (j + 1) * mu * sum(r[j + 1][0:c]) / la

        for i in range(c - 1, -1, -1):
            r[j][i] = (d[i] + (i + 1) * nu * r[j][i + 1]) / (la + j * mu + b[i])

    pi0m = 1 / sum(map(sum, r))
    pi = [[ri * pi0m for ri in rj] for rj in r]
    pi[m][0] = pi0m

    temp = [i * sum(map(lambda pij: pij[i], pi)) for i in range(1, c + 1)]
    average_busy_equipment = sum(temp)
    average_recall_sources = sum([j * sum(pi[j]) for j in range(1, m + 1)])
    average_time_from_call_to_service = average_recall_sources / la
    loss_call_probability = sum(map(lambda pij: pij[c], pi))

    return (
        average_busy_equipment,
        average_recall_sources,
        average_time_from_call_to_service,
        loss_call_probability
    )


if __name__ == '__main__':
    tests = 10
    c = 100  # equipment
    m = 110  # recall sources
    la = 105  # intensity

    for test in range(tests):
        nu = uniform(0, 0.5)  # serving_time
        mu = uniform(0, 0.5)  # recall_time

        print('--- Test', test + 1, '---')
        print('Serving time:', round(nu * 60, 2))
        print('Recall time:', round(mu * 60, 2))

        (
            average_busy_equipment,
            average_recall_sources,
            average_time_from_call_to_service,
            loss_call_probability
        ) = system_with_recall_sources(m, c, mu, nu, la)

        print('Average quantity of busy equipment:', round(average_busy_equipment, 2))
        print('Average quantity of recall sources:', round(average_recall_sources, 2))
        print('Average time from call to service:', round(average_time_from_call_to_service * 60, 3))
        print('Probability of loss initial call:', round(loss_call_probability, 2), '\n')
