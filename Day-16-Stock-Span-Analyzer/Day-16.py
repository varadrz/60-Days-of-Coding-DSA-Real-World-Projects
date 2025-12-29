# Day 16 - Stock Span Analyzer
# Focus: Monotonic Stack
# Language: Python 3


def stock_span(prices):
    stack = []
    span = [0] * len(prices)

    for i in range(len(prices)):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()

        span[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)

    return span


def main():
    prices = [100, 80, 60, 70, 60, 75, 85]
    print("Stock Span:", stock_span(prices))


if __name__ == "__main__":
    main()
