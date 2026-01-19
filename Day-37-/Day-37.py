# Day 37 - City Infrastructure Planner
# Focus: Minimum Spanning Tree (Kruskal's Algorithm)
# Language: Python 3


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        elif self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1

        return True


def kruskal_mst(nodes, edges):
    """
    nodes: number of cities
    edges: (cost, city1, city2)
    """
    edges.sort()
    uf = UnionFind(nodes)
    mst_cost = 0
    mst_edges = []

    for cost, u, v in edges:
        if uf.union(u, v):
            mst_cost += cost
            mst_edges.append((u, v, cost))

    return mst_cost, mst_edges


def main():
    # Cities represented as numbers 0 to 4
    edges = [
        (10, 0, 1),
        (15, 0, 2),
        (30, 1, 3),
        (40, 2, 3),
        (50, 3, 4),
        (20, 2, 4)
    ]

    cost, mst = kruskal_mst(5, edges)

    print("\nMinimum Cost to Connect All Cities:", cost)
    print("Selected Roads:")
    for u, v, c in mst:
        print(f"City {u} -- City {v} | Cost: {c}")


if __name__ == "__main__":
    main()
