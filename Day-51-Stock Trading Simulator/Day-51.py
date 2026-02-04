# Day 51 - Stock Trading Simulator
# Focus: Advanced Dynamic Programming Patterns
# Language: Python 3


class StockTradingSimulator:
    def __init__(self, prices):
        self.prices = prices

    def max_profit(self):
        """
        DP State:
        hold = max profit when holding a stock
        not_hold = max profit when not holding a stock
        """
        hold = -self.prices[0]
        not_hold = 0

        for price in self.prices[1:]:
            new_hold = max(hold, not_hold - price)
            new_not_hold = max(not_hold, hold + price)

            hold = new_hold
            not_hold = new_not_hold

        return not_hold


def main():
    prices = [7, 1, 5, 3, 6, 4]
    simulator = StockTradingSimulator(prices)

    profit = simulator.max_profit()
    print("\nMaximum Profit:", profit)


if __name__ == "__main__":
    main()