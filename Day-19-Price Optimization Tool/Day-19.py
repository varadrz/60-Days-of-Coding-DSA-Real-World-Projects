# Day 19 - Price Optimization Tool
# Focus: Binary Search
# Language: Python 3


def is_affordable(prices, budget, max_price):
    total = 0
    for price in prices:
        total += min(price, max_price)
    return total <= budget


def find_optimal_price(prices, budget):
    low, high = 0, max(prices)
    optimal_price = 0

    while low <= high:
        mid = (low + high) // 2

        if is_affordable(prices, budget, mid):
            optimal_price = mid
            low = mid + 1
        else:
            high = mid - 1

    return optimal_price


def main():
    prices = [120, 80, 150, 200, 90]
    budget = 400

    optimal_price = find_optimal_price(prices, budget)

    print("\nOptimal Maximum Price Cap:", optimal_price)


if __name__ == "__main__":
    main()
