# Day 59 - Performance Optimization
# Focus: Profiling + Refactoring
# Language: Python 3

import time


# ---------------- BEFORE (Inefficient) ----------------
def has_duplicates_bruteforce(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return True
    return False


# ---------------- AFTER (Optimized using Hashing) ----------------
def has_duplicates_optimized(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False


def profile_function(func, data):
    start = time.time()
    result = func(data)
    end = time.time()
    return result, end - start


def main():
    data = list(range(10000)) + [500]  # Force duplicate

    print("\n--- Profiling Brute Force ---")
    result1, time1 = profile_function(has_duplicates_bruteforce, data)
    print("Result:", result1)
    print("Time:", time1)

    print("\n--- Profiling Optimized Version ---")
    result2, time2 = profile_function(has_duplicates_optimized, data)
    print("Result:", result2)
    print("Time:", time2)


if __name__ == "__main__":
    main()
