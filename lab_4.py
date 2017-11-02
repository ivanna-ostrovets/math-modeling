from math import log


def get_preferable_service_places(clients_by_hour, serving_time, service_places, pref_waiting_time):
    waiting_time = pref_waiting_time + 1

    while waiting_time > pref_waiting_time:
        service_places += 1
        served_by_hour = 60 / serving_time * service_places
        system_capacity = clients_by_hour / served_by_hour
        waiting_time = system_capacity / (served_by_hour - clients_by_hour)

    return service_places

def mass_service_system_without_limit(clients_by_hour, serving_time, waiting_queue, service_places=1):
    served_by_hour = 60 / serving_time * service_places
    system_capacity = clients_by_hour / served_by_hour

    full_employment_probability = system_capacity ** service_places * (1 - system_capacity)
    empty_probability = 1 - system_capacity
    average_clients_in_system = system_capacity / (1 - system_capacity)
    average_clients_in_queue = system_capacity ** 2 / (1 - system_capacity)
    average_free_service_places = max(service_places - average_clients_in_system, 0)
    average_time_in_system = 1 / (served_by_hour - clients_by_hour)
    average_time_in_queue = system_capacity / (served_by_hour - clients_by_hour)
    place_in_queue_probability = 1 - system_capacity ** waiting_queue * (1 - system_capacity)
    preferable_queue_size = round(log(0.1) / log(system_capacity) - 1)

    return (
        round(full_employment_probability, 2),
        round(empty_probability, 2),
        round(average_clients_in_system, 2),
        round(average_clients_in_queue, 2),
        round(average_free_service_places, 2),
        round(average_time_in_system, 2),
        round(average_time_in_queue, 2),
        round(place_in_queue_probability, 2),
        round(preferable_queue_size, 2),
    )


def n_clients_pobability(system_capacity, n, limit):
    if system_capacity == 1:
        n_clients_pobability = 1 / (limit + 1)
    else:
        n_clients_pobability = (1 - system_capacity) * system_capacity ** n / (1 - system_capacity ** (limit + 1))

    return n_clients_pobability


def mass_service_system_with_limit(clients_by_hour, serving_time, waiting_queue, service_places=1):
    served_by_hour = 60 / serving_time * service_places
    system_capacity = clients_by_hour / served_by_hour
    limit = waiting_queue + 1
    pow_capacity = system_capacity ** (limit + 1)

    full_employment_probability = n_clients_pobability(system_capacity, service_places, limit)
    empty_probability = 1 - system_capacity
    loss_probability = n_clients_pobability(system_capacity, limit, limit)
    loss_intensity = clients_by_hour * loss_probability
    effective_intensity = clients_by_hour * (1 - loss_probability)
    average_clients_in_system = (system_capacity * (1 - (limit + 1) * system_capacity ** limit + limit * pow_capacity)) \
                                / ((1 - system_capacity) * (1 - pow_capacity))

    average_time_in_system = average_clients_in_system / effective_intensity
    average_time_in_queue = average_time_in_system - 1 / served_by_hour

    return (
        round(full_employment_probability, 2),
        round(empty_probability, 2),
        round(loss_probability, 2),
        round(loss_intensity, 2),
        round(effective_intensity, 2),
        round(average_clients_in_system, 2),
        round(average_time_in_system, 2),
        round(average_time_in_queue, 2),
    )


if __name__ == '__main__':
    print('--- Task 1 ---')
    (
        full_employment_probability,
        empty_probability,
        average_clients_in_system,
        average_clients_in_queue,
        average_free_service_places,
        average_time_in_system,
        average_time_in_queue,
        place_in_queue_probability,
        preferable_queue_size,
    ) = mass_service_system_without_limit(10, 5, 3)
    print('Probability that the client who arrived will not wait:', empty_probability)
    print('Average amount of the clients that are waiting for service:', average_clients_in_system)
    print('Average time that client is spending in system:', average_time_in_system * 60)
    print('Average time that client is spending by waiting before service:', average_time_in_queue * 60)
    print('Probability that the client who arrived can wait near service point:', place_in_queue_probability)
    print('Preferable parking size:', preferable_queue_size)

    print('\n--- Task 2 ---')
    (
        full_employment_probability,
        empty_probability,
        loss_probability,
        loss_intensity,
        effective_intensity,
        average_clients_in_system,
        average_time_in_system,
        average_time_in_queue,
    ) = mass_service_system_with_limit(8, 6, 7)
    print('Effective customer flow intensity:', effective_intensity)
    print('Probability that the client who arrived will not wait:', empty_probability)
    print('Average amount of the clients that are waiting for service:', average_clients_in_system)
    print('Average time that client is spending by waiting before service:', average_time_in_queue * 60)
    print('Average time that client is spending in system:', average_time_in_system * 60)
    print('Probability of loss of the client:', loss_probability)

    print('\n--- Task 3 ---')
    (
        full_employment_probability,
        empty_probability,
        average_clients_in_system,
        average_clients_in_queue,
        average_free_service_places,
        average_time_in_system,
        average_time_in_queue,
        place_in_queue_probability,
        preferable_queue_size,
    ) = mass_service_system_without_limit(8, 12, 0, 2)
    print('Probability that all cars in each of the two services are on the call:', full_employment_probability * 2)
    print('Average amount of the clients that are waiting for car:', average_clients_in_queue * 2)
    print('Average time that client is spending by waiting for car:', average_time_in_queue * 60)
    print('Average amount of free cars:', average_free_service_places * 2)

    print('-- After services union --')
    (
        full_employment_probability_2,
        empty_probability_2,
        average_clients_in_system_2,
        average_clients_in_queue_2,
        average_free_service_places_2,
        average_time_in_system_2,
        average_time_in_queue_2,
        place_in_queue_probability_2,
        preferable_queue_size_2,
    ) = mass_service_system_without_limit(16, 12, 0, 4)
    preferable_service_places = get_preferable_service_places(16, 12, 4, 5)
    print('Average time that client is spending by waiting for car:', average_time_in_queue_2 * 60)
    print('Union was', 'successful' if average_time_in_queue > average_time_in_queue_2 else 'unsuccessful')
    print('Preferable amount of cars (waiting time < 5 minutes):', preferable_service_places)

    print('\n--- Task 4 ---')
    (
        full_employment_probability,
        empty_probability,
        loss_probability,
        loss_intensity,
        effective_intensity,
        average_clients_in_system,
        average_time_in_system,
        average_time_in_queue,
    ) = mass_service_system_with_limit(16, 12, 6, 4)
    print('Effective customer flow intensity:', effective_intensity)
    print('Probability that the client who arrived will not wait:', empty_probability)
    print('Average amount of the clients that are waiting for service:', average_clients_in_system)
    print('Average time that client is spending by waiting before service:', average_time_in_queue * 60)
    print('Average time that client is spending in system:', average_time_in_system * 60)
    print('Probability of loss of the client:', loss_probability)

    print('Probability that all cars are on the call:', full_employment_probability)
    print('Average amount of the clients that are waiting for car:', average_clients_in_queue)
    print('Average time that client is spending by waiting for car:', average_time_in_queue * 60)
    print('Lost customers per day:', loss_intensity * 24)

