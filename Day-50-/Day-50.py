# Day 50 - Performance Analyzer Dashboard
# Focus: Memoization vs Tabulation
# Language: Python 3

import time


class FibonacciAnalyzer:
    def __init__(self):
        self.memo = {}

    # ---------------- MEMOIZATION (Top-Down) ----------------
    def fib_memo(self, n):
        if n <= 1:
            return n
        if n in self.memo:
            return self.memo[n]

        self.memo[n] = self.fib_memo(n - 1) + self.fib_memo(n - 2)
        return self.memo[n]

    # ---------------- TABULATION (Bottom-Up) ----------------
    def fib_tab(self, n):
        if n <= 1:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


def main():
    n = 35
    analyzer = FibonacciAnalyzer()

    # Memoization timing
    start = time.time()
    result_memo = analyzer.fib_memo(n)
    memo_time = time.time() - start

    # Tabulation timing
    start = time.time()
    result_tab = analyzer.fib_tab(n)
    tab_time = time.time() - start

    print("\nFibonacci Number:", n)
    print("Result (Memoization):", result_memo)
    print("Time (Memoization):", memo_time)

    print("\nResult (Tabulation):", result_tab)
    print("Time (Tabulation):", tab_time)


if __name__ == "__main__":
    main()
