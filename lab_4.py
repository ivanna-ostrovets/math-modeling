from math import log


def mass_service_system_without_limit(clients_by_hour, serving_time, waiting_stack):
    served_by_hour = 60 / serving_time
    system_capacity = clients_by_hour / served_by_hour

    empty_probability = 1 - system_capacity
    average_clients_in_system = system_capacity / (1 - system_capacity)
    average_clients_in_queue = system_capacity ** 2 / (1 - system_capacity)
    average_time_in_system = 1 / (served_by_hour - clients_by_hour)
    average_time_in_queue = system_capacity / (served_by_hour - clients_by_hour)
    place_in_stack_probability = 1 - system_capacity ** waiting_stack * (1 - system_capacity)
    preferable_stack_size = round(log(0.1) / log(system_capacity) - 1)

    return (
        empty_probability,
        average_clients_in_system,
        average_clients_in_queue,
        average_time_in_system,
        average_time_in_queue,
        place_in_stack_probability,
        preferable_stack_size,
    )


def n_clients_pobability(system_capacity, n, limit):
    if system_capacity == 1:
        n_clients_pobability = 1 / (limit + 1)
    else:
        n_clients_pobability = (1 - system_capacity) * system_capacity ** n / (1 - system_capacity ** (limit + 1))

    return n_clients_pobability

def mass_service_system_with_limit(clients_by_hour, serving_time, waiting_stack):
    served_by_hour = 60 / serving_time
    system_capacity = clients_by_hour / served_by_hour
    limit = waiting_stack + 1
    pow_capacity = system_capacity ** (limit + 1)

    loss_probability = n_clients_pobability(system_capacity, limit, limit)
    effective_intensity = clients_by_hour * (1 - loss_probability)
    average_clients_in_system = (system_capacity * (1 - (limit + 1) * system_capacity ** limit + limit * pow_capacity)) \
                                / ((1 - system_capacity) * (1 - pow_capacity))

    average_time_in_system = average_clients_in_system / effective_intensity
    average_time_in_queue = average_time_in_system - 1 / served_by_hour

    return (
        loss_probability,
        effective_intensity,
        average_clients_in_system,
        average_time_in_system,
        average_time_in_system,
        average_time_in_queue,
    )


if __name__ == '__main__':
    print('--- Task 1 ---')
    (
        empty_probability,
        average_clients_in_system,
        average_clients_in_queue,
        average_time_in_system,
        average_time_in_queue,
        place_in_stack_probability,
        preferable_stack_size
    ) = mass_service_system_without_limit(10, 5, 3)

    print('--- Task 2 ---')
    (
        loss_probability,
        effective_intensity,
        average_clients_in_system,
        average_time_in_system,
        average_time_in_system,
        average_time_in_queue,
    ) = mass_service_system_with_limit(8, 6, 7)
