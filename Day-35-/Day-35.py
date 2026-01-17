# Day 35 - Google Maps Like Path Finder
# Focus: Dijkstra's Algorithm
# Language: Python 3

import heapq


class MapGraph:
    def __init__(self):
        self.graph = {}

    def add_location(self, location):
        if location not in self.graph:
            self.graph[location] = []

    def add_road(self, from_loc, to_loc, distance):
        self.add_location(from_loc)
        self.add_location(to_loc)
        self.graph[from_loc].append((to_loc, distance))
        self.graph[to_loc].append((from_loc, distance))  # undirected

    def shortest_path(self, start, end):
        pq = [(0, start)]
        distances = {node: float("inf") for node in self.graph}
        previous = {}

        distances[start] = 0

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_node == end:
                break

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        # reconstruct path
        path = []
        node = end
        while node in previous:
            path.append(node)
            node = previous[node]
        path.append(start)
        path.reverse()

        return path, distances[end]


def main():
    city_map = MapGraph()

    city_map.add_road("A", "B", 4)
    city_map.add_road("A", "C", 2)
    city_map.add_road("B", "C", 1)
    city_map.add_road("B", "D", 5)
    city_map.add_road("C", "D", 8)
    city_map.add_road("C", "E", 10)
    city_map.add_road("D", "E", 2)

    path, distance = city_map.shortest_path("A", "E")

    print("\nShortest Path:")
    print(" -> ".join(path))
    print("Total Distance:", distance)


if __name__ == "__main__":
    main()
