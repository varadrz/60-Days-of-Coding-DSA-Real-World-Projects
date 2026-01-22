# Day 40 - Graph Revision and API-style Abstraction
# Focus: Revising Graph Concepts + Service-Oriented Thinking
# Language: Python 3


class GraphService:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, u, v):
        self.add_node(u)
        self.add_node(v)
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        from collections import deque
        visited = set()
        queue = deque([start])
        order = []

        visited.add(start)

        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    def dfs(self, start):
        visited = set()
        order = []

        def dfs_util(node):
            visited.add(node)
            order.append(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs_util(neighbor)

        dfs_util(start)
        return order


def main():
    service = GraphService()

    service.add_edge("A", "B")
    service.add_edge("A", "C")
    service.add_edge("B", "D")
    service.add_edge("C", "E")

    print("\nBFS Traversal:", service.bfs("A"))
    print("DFS Traversal:", service.dfs("A"))


if __name__ == "__main__":
    main()
