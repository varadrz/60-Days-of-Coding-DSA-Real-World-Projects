
---

# 📄 Day 7 README.md  
👉 `Day-7-Network-Traffic-Analyzer/README.md`

```md
# Day 7 | Network Traffic Analyzer

## Overview
This project is part of the **60 Days of Coding | DSA x Real World Projects** series.

Day 7 focuses on the **Sliding Window technique** to analyze network traffic data and identify peak usage intervals efficiently.

---

## Problem Statement
Given network traffic data recorded at regular intervals, identify the contiguous window of fixed size with the maximum traffic.

---

## DSA Concepts Used
- Sliding Window
- Arrays
- Single-pass traversal
- Window optimization

---

## How the Solution Works
- Computes the sum of the first window
- Slides the window by adding the next element and removing the previous one
- Tracks the maximum traffic observed

---

## Time and Space Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## How to Run
```bash
python day-7.py
