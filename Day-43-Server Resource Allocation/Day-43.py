# Day 43 - Server Resource Allocation
# Focus: Knapsack Variants (0/1 Knapsack)
# Language: Python 3


class ServerResourceAllocator:
    def __init__(self, capacity, resource_costs, resource_values):
        self.capacity = capacity
        self.costs = resource_costs
        self.values = resource_values

    def allocate(self):
        """
        dp[i][w] = max value using first i resources with capacity w
        """
        n = len(self.costs)
        W = self.capacity

        dp = [[0] * (W + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(W + 1):
                if self.costs[i - 1] <= w:
                    dp[i][w] = max(
                        dp[i - 1][w],
                        dp[i - 1][w - self.costs[i - 1]] + self.values[i - 1]
                    )
                else:
                    dp[i][w] = dp[i - 1][w]

        return dp[n][W]


def main():
    # Example:
    # capacity = server capacity
    # costs = resource consumption
    # values = performance gain

    capacity = 50
    resource_costs = [10, 20, 30]
    resource_values = [60, 100, 120]

    allocator = ServerResourceAllocator(capacity, resource_costs, resource_values)
    result = allocator.allocate()

    print("\nMaximum performance achievable:", result)


if __name__ == "__main__":
    main()
