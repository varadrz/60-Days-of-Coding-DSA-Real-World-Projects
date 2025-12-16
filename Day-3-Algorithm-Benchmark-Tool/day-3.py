# Day 3 - Algorithm Benchmark Tool
# Focus: Time and Space Complexity
# Language: Python 3

import time
import tracemalloc
import random


def pair_sum_bruteforce(arr, target):
    result = []
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                result.append((arr[i], arr[j]))

    return result


def pair_sum_optimized(arr, target):
    seen = set()
    result = []

    for num in arr:
        complement = target - num
        if complement in seen:
            result.append((complement, num))
        seen.add(num)

    return result


def benchmark(function, arr, target):
    tracemalloc.start()
    start_time = time.perf_counter()

    function(arr, target)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return end_time - start_time, peak


def main():
    n = 2000
    target = 50
    arr = [random.randint(1, 50) for _ in range(n)]

    print("\n--- Algorithm Benchmark Tool ---")
    print(f"Input size: {n}")

    bf_time, bf_space = benchmark(pair_sum_bruteforce, arr, target)
    opt_time, opt_space = benchmark(pair_sum_optimized, arr, target)

    print("\nBrute Force Approach")
    print(f"Time Taken: {bf_time:.6f} seconds")
    print(f"Peak Memory: {bf_space / 1024:.2f} KB")

    print("\nOptimized Approach (Hashing)")
    print(f"Time Taken: {opt_time:.6f} seconds")
    print(f"Peak Memory: {opt_space / 1024:.2f} KB")


if __name__ == "__main__":
    main()
