# Day 39 - Cloud Resource Allocator
# Focus: Graph Optimization (Greedy + Graph Traversal)
# Language: Python 3


class CloudResourceAllocator:
    def __init__(self):
        self.graph = {}

    def add_server(self, server):
        if server not in self.graph:
            self.graph[server] = []

    def add_connection(self, s1, s2, cost):
        self.add_server(s1)
        self.add_server(s2)
        self.graph[s1].append((s2, cost))
        self.graph[s2].append((s1, cost))

    def allocate_resources(self, start_server):
        visited = set()
        total_cost = 0
        allocation_order = []

        visited.add(start_server)
        allocation_order.append(start_server)

        edges = self.graph[start_server][:]

        while edges:
            # pick lowest cost connection
            edges.sort(key=lambda x: x[1])
            next_server, cost = edges.pop(0)

            if next_server not in visited:
                visited.add(next_server)
                total_cost += cost
                allocation_order.append(next_server)

                for neighbor in self.graph[next_server]:
                    if neighbor[0] not in visited:
                        edges.append(neighbor)

        return allocation_order, total_cost


def main():
    allocator = CloudResourceAllocator()

    allocator.add_connection("Server-A", "Server-B", 4)
    allocator.add_connection("Server-A", "Server-C", 3)
    allocator.add_connection("Server-B", "Server-D", 2)
    allocator.add_connection("Server-C", "Server-D", 5)
    allocator.add_connection("Server-D", "Server-E", 1)

    order, cost = allocator.allocate_resources("Server-A")

    print("\nResource Allocation Order:")
    for s in order:
        print(s)

    print("Total Allocation Cost:", cost)


if __name__ == "__main__":
    main()
