# Day 41 - Budget Optimization Tool
# Focus: Dynamic Programming (1D)
# Language: Python 3


class BudgetOptimizer:
    def __init__(self, budget, costs, values):
        self.budget = budget
        self.costs = costs
        self.values = values

    def maximize_value(self):
        """
        1D DP where dp[i] = max value achievable with budget i
        """
        dp = [0] * (self.budget + 1)

        for i in range(len(self.costs)):
            cost = self.costs[i]
            value = self.values[i]

            # iterate backwards to avoid reuse
            for b in range(self.budget, cost - 1, -1):
                dp[b] = max(dp[b], dp[b - cost] + value)

        return dp[self.budget]


def main():
    # Example scenario:
    # Budget = 50
    # Costs = expense/investment cost
    # Values = benefit/return score

    budget = 50
    costs = [10, 20, 30]
    values = [60, 100, 120]

    optimizer = BudgetOptimizer(budget, costs, values)
    result = optimizer.maximize_value()

    print("\nMaximum value achievable within budget:", result)


if __name__ == "__main__":
    main()
