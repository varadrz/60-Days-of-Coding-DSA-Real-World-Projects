# Day 48 - Delivery Route Planning
# Focus: Bitmask Dynamic Programming (TSP-style)
# Language: Python 3


class DeliveryRoutePlanner:
    def __init__(self, distances):
        self.dist = distances
        self.n = len(distances)
        self.dp = {}

    def find_min_cost(self):
        """
        dp[mask][pos] = minimum cost to visit cities in mask ending at pos
        """
        return self._tsp(1, 0)

    def _tsp(self, mask, pos):
        if mask == (1 << self.n) - 1:
            return self.dist[pos][0]

        if (mask, pos) in self.dp:
            return self.dp[(mask, pos)]

        ans = float("inf")

        for city in range(self.n):
            if mask & (1 << city) == 0:
                new_cost = self.dist[pos][city] + self._tsp(
                    mask | (1 << city), city
                )
                ans = min(ans, new_cost)

        self.dp[(mask, pos)] = ans
        return ans


def main():
    # Distance matrix between delivery locations
    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]

    planner = DeliveryRoutePlanner(distances)
    cost = planner.find_min_cost()

    print("\nMinimum Delivery Route Cost:", cost)


if __name__ == "__main__":
    main()
