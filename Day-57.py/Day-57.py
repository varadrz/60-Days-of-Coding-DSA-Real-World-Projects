# Day 57 - Ride Sharing Backend Engine
# Focus: Greedy + Heaps + Graphs
# Language: Python 3

import heapq


class RideSharingEngine:
    def __init__(self):
        self.graph = {}          # Graph: location -> [(neighbor, distance)]
        self.available_drivers = []  # Min-heap based on distance

    # -------- GRAPH OPERATIONS --------
    def add_route(self, src, dest, distance):
        if src not in self.graph:
            self.graph[src] = []
        if dest not in self.graph:
            self.graph[dest] = []

        self.graph[src].append((dest, distance))
        self.graph[dest].append((src, distance))

    # -------- HEAP OPERATIONS --------
    def add_driver(self, driver_id, distance_from_user):
        heapq.heappush(self.available_drivers, (distance_from_user, driver_id))

    def assign_driver(self):
        if not self.available_drivers:
            return "No drivers available"

        distance, driver_id = heapq.heappop(self.available_drivers)
        return f"Driver {driver_id} assigned (Distance: {distance})"


def main():
    engine = RideSharingEngine()

    # Add routes (Graph)
    engine.add_route("A", "B", 5)
    engine.add_route("B", "C", 4)
    engine.add_route("A", "C", 8)

    # Add drivers (Heap)
    engine.add_driver("D1", 3)
    engine.add_driver("D2", 1)
    engine.add_driver("D3", 5)

    print(engine.assign_driver())
    print(engine.assign_driver())
    print(engine.assign_driver())
    print(engine.assign_driver())


if __name__ == "__main__":
    main()
