# Day 10 | Resume Ranking Engine

## Overview
This project is part of the **60 Days of Coding | DSA x Real World Projects** series.

Day 10 focuses on **Sorting Algorithms** by building a Resume Ranking Engine similar to systems used in hiring platforms to rank candidates efficiently.

---

## Problem Statement
Design a system that:
- Stores candidate profiles
- Ranks candidates based on multiple criteria
- Produces an ordered list of candidates

---

## DSA Concepts Used
- Sorting
- Custom comparator
- Multi-key sorting
- Stable sorting behavior

---

## How the Solution Works
- Each candidate has a score and experience
- Candidates are sorted primarily by score
- Experience is used as a secondary sorting key
- Sorting is performed in descending order

---

## Time and Space Complexity
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)

---

## How to Run
```bash
python day-10.py
