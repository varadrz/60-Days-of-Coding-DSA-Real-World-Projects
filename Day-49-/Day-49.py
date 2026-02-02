# Day 49 - Smart Energy Consumption Optimizer
# Focus: State Compression Dynamic Programming
# Language: Python 3


class EnergyOptimizer:
    def __init__(self, energy_costs):
        """
        energy_costs[i] = energy cost of turning ON device i
        """
        self.costs = energy_costs
        self.n = len(energy_costs)
        self.dp = {}

    def minimize_energy(self):
        """
        dp[mask] = minimum energy cost for devices represented by mask
        """
        return self._solve(0)

    def _solve(self, mask):
        if mask == (1 << self.n) - 1:
            return 0

        if mask in self.dp:
            return self.dp[mask]

        min_cost = float("inf")

        for i in range(self.n):
            if not (mask & (1 << i)):
                new_mask = mask | (1 << i)
                cost = self.costs[i] + self._solve(new_mask)
                min_cost = min(min_cost, cost)

        self.dp[mask] = min_cost
        return min_cost


def main():
    # Example: Energy cost of devices
    energy_costs = [5, 8, 3, 6]

    optimizer = EnergyOptimizer(energy_costs)
    result = optimizer.minimize_energy()

    print("\nMinimum Total Energy Consumption:", result)


if __name__ == "__main__":
    main()
