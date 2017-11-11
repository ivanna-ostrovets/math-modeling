C = 100  # equipment
M = 90  # recall sources
L = 95  # intensity
NU = 0.3  # serving_time
MU = 0.4  # recall_time


if __name__ == '__main__':
    r = [[] for _ in range(M + 1)]
    r[M].extend([1, 1])

    for i in range(2, C + 1):
        r[M].append(((L + (i - 1) * NU + M * MU) * r[M][i - 1] - L * r[M][i - 2]) / (i * NU))

    for j in range(M - 1, -1, -1):
        b, d = [0], [0]
        r[j].extend([0 for _ in range(C + 1)])

        for i in range(1, C + 1):
            b.append(i * NU * (j * MU + b[i - 1]) / (L + j * MU + b[i - 1]))
            d.append((j + 1) * MU * r[j + 1][i - 1] + (L * d[i - 1]) / (L + j * MU + b[i - 1]))

        r[j][C] = (j + 1) * MU * sum(r[j + 1][0:C]) / L

        for i in range(C - 1, -1, -1):
            r[j][i] = (d[i] + (i + 1) * NU * r[j][i + 1]) / (L + j * MU + b[i])

    pi0m = 1 / sum(map(sum, r))
    pi = [[ri * pi0m for ri in rj] for rj in r]
    pi[M][0] = pi0m

    temp = [i * sum(map(lambda pij: pij[i], pi)) for i in range(1, C + 1)]
    average_busy_equipment = sum(temp)
    print(
        'Average quantity of busy equipment:',
        round(average_busy_equipment, 2)
    )

    average_recall_sources = sum([j * sum(pi[j]) for j in range(1, M + 1)])
    print(
        'Average quantity of recall sources:',
        round(average_recall_sources, 2)
    )

    print('Average time from call to service:', round(average_recall_sources / L, 2))

    loss_call_probability = sum(map(lambda pij: pij[C], pi))
    print('Probability of loss initial call', round(loss_call_probability, 2))
