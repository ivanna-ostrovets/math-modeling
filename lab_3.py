from math import log
from generators.linear_congruential import generate_numbers


MIN = 5
MAX = 20


def generate_time_between_requests(parameter):
    try:
        return abs((-1 / parameter) * log(generate_numbers(MIN, MAX, 1)[0]))
    except ValueError:
        return 0.01


def generate_request_time(parameter):
    try:
        return abs((-1 / parameter) * log(generate_numbers(MIN, MAX, 1)[0]))
    except ValueError:
        return 0.01


def requests_system(tau, param_t, full_time):
    requests = 0
    times_between = 0
    serve_times = 0
    denials = 0
    served_requests = 0

    while times_between < full_time:
        time_between_requests = generate_time_between_requests(tau)
        request_time = generate_request_time(param_t)

        times_between += time_between_requests
        requests += 1
        served = False

        if serve_times > times_between:
            denials += 1
        else:
            served_requests += 1
            serve_times += request_time
            served = True

        print('| {:^3} | {:^6.2f} | {:^6.2f} | {} |'.format(
            requests,
            request_time,
            time_between_requests,
            served,
        ))

    print('Requests:', requests)
    print('Served requests:', served_requests, '\n')

    return requests, denials, served_requests, serve_times


if __name__ == '__main__':
    tau = 0.8
    param_t = 0.9
    full_time = 30 + 9 % 4
    k = 6
    all_requests = 0
    all_denials = 0
    all_served = 0
    all_serve_times = 0

    for _ in range(k):
        requests, denials, served, serve_times = requests_system(tau, param_t, full_time)

        all_requests += requests
        all_denials += denials
        all_served += served
        all_serve_times += serve_times

    print('Average number of requests:', round(all_requests / k))
    print('Average number of served requests:', round(all_served / k))
    print('Average time of request service:', round(all_serve_times / all_served, 2))
    print('Probability of service:', round(all_served / all_requests, 2))
    print('Probability of denial:', round(all_denials / all_requests, 2))


