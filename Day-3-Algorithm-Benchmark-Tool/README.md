# Day 3 | Algorithm Benchmark Tool

## Overview
This project is part of the **60 Days of Coding | DSA x Real World Projects** series.

Day 3 focuses on understanding **Time and Space Complexity** through practical measurement rather than theory alone.  
Two different algorithms solving the same problem are benchmarked to demonstrate real performance differences.

---

## Problem Statement
Given an array of integers and a target value, find all pairs whose sum equals the target.

---

## Approaches Compared

### Brute Force Approach
- Uses nested loops to check all possible pairs

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

---

### Optimized Approach (Hashing)
- Uses a hash set to track complements

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

---

## Key Concepts Used
- Arrays
- Hash Sets
- Time Complexity Analysis
- Space Complexity Analysis
- Performance Benchmarking

---

## How Benchmarking Works
- Execution time measured using `time.perf_counter()`
- Memory usage measured using `tracemalloc`
- Same input used for both algorithms to ensure fairness

---

## How to Run
```bash
python day-3.py
