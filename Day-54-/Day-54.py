# Day 54 - Speed Coding Challenge
# Focus: Timed Problem Solving
# Language: Python 3


# ---------------- PROBLEM 1 ----------------
# Reverse a string

def reverse_string(s):
    return s[::-1]


# ---------------- PROBLEM 2 ----------------
# Check if number is palindrome

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


# ---------------- PROBLEM 3 ----------------
# Find missing number (0 to n)

def missing_number(nums):
    n = len(nums)
    expected = n * (n + 1) // 2
    return expected - sum(nums)


# ---------------- PROBLEM 4 ----------------
# First non-repeating character

def first_unique_char(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1


# ---------------- PROBLEM 5 ----------------
# Max difference (buy-sell stock once)

def max_profit(prices):
    min_price = float("inf")
    profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


def main():
    print("Reverse String:", reverse_string("speed"))
    print("Is Palindrome:", is_palindrome(121))
    print("Missing Number:", missing_number([3, 0, 1]))
    print("First Unique Char Index:", first_unique_char("leetcode"))
    print("Max Profit:", max_profit([7, 1, 5, 3, 6, 4]))


if __name__ == "__main__":
    main()
