# Day 36 - Network Connectivity Checker
# Focus: Union-Find (Disjoint Set Union)
# Language: Python 3


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        # Union by rank
        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        elif self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1

        return True

    def is_connected(self, a, b):
        return self.find(a) == self.find(b)


def main():
    # 6 network nodes
    uf = UnionFind(6)

    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)

    print("\nNetwork Connectivity Checks:")
    print("0 connected to 2:", uf.is_connected(0, 2))
    print("0 connected to 4:", uf.is_connected(0, 4))

    uf.union(2, 4)
    print("0 connected to 4 after union:", uf.is_connected(0, 4))


if __name__ == "__main__":
    main()
