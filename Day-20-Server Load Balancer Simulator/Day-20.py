# Day 20 - Server Load Balancer Simulator
# Focus: Binary Search on Answer
# Language: Python 3


def can_distribute(loads, servers, max_load):
    """
    Check if tasks can be distributed across servers
    such that no server exceeds max_load.
    """
    required_servers = 1
    current_load = 0

    for load in loads:
        if load > max_load:
            return False

        if current_load + load <= max_load:
            current_load += load
        else:
            required_servers += 1
            current_load = load

            if required_servers > servers:
                return False

    return True


def find_minimum_max_load(loads, servers):
    low = max(loads)
    high = sum(loads)
    answer = high

    while low <= high:
        mid = (low + high) // 2

        if can_distribute(loads, servers, mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer


def main():
    task_loads = [10, 20, 30, 40, 50]
    servers = 3

    result = find_minimum_max_load(task_loads, servers)
    print("\nMinimum possible maximum server load:", result)


if __name__ == "__main__":
    main()
