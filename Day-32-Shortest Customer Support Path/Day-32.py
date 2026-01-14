# Day 32 - Shortest Customer Support Path
# Focus: Breadth-First Search (BFS)
# Language: Python 3

from collections import deque


class CustomerSupportNetwork:
    def __init__(self):
        self.graph = {}

    def add_agent(self, agent):
        if agent not in self.graph:
            self.graph[agent] = []

    def connect_agents(self, a, b):
        self.add_agent(a)
        self.add_agent(b)
        self.graph[a].append(b)
        self.graph[b].append(a)

    def shortest_path(self, start, end):
        if start not in self.graph or end not in self.graph:
            return []

        visited = set()
        queue = deque([(start, [start])])
        visited.add(start)

        while queue:
            current, path = queue.popleft()

            if current == end:
                return path

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return []


def main():
    network = CustomerSupportNetwork()

    network.connect_agents("Customer", "Agent-A")
    network.connect_agents("Agent-A", "Agent-B")
    network.connect_agents("Agent-B", "Agent-C")
    network.connect_agents("Agent-C", "Supervisor")
    network.connect_agents("Agent-A", "Agent-D")

    path = network.shortest_path("Customer", "Supervisor")

    if path:
        print("\nShortest Support Escalation Path:")
        print(" -> ".join(path))
    else:
        print("No path found.")


if __name__ == "__main__":
    main()
