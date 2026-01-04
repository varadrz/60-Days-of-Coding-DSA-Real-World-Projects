# Day 22 - Delivery Route Optimizer
# Focus: Greedy Algorithm
# Language: Python 3


def optimize_delivery_routes(routes, max_distance):
    """
    routes: list of delivery distances
    max_distance: maximum distance per delivery trip
    """
    routes.sort()
    trips = 0
    current_load = 0

    for distance in routes:
        if distance > max_distance:
            return -1  # Not possible to deliver this route

        if current_load + distance <= max_distance:
            current_load += distance
        else:
            trips += 1
            current_load = distance

    if current_load > 0:
        trips += 1

    return trips


def main():
    delivery_routes = [10, 20, 30, 15, 25, 35]
    max_distance = 50

    trips_required = optimize_delivery_routes(delivery_routes, max_distance)

    if trips_required == -1:
        print("Delivery not possible with given constraints.")
    else:
        print("Minimum number of delivery trips required:", trips_required)


if __name__ == "__main__":
    main()
