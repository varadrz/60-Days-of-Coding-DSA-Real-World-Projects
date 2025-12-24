# Day 11 | Browser History Manager

## Overview
This project is part of the **60 Days of Coding | DSA x Real World Projects** series.

Day 11 focuses on the **Stack data structure** by implementing a Browser History Manager similar to how modern web browsers handle back and forward navigation.

---

## Problem Statement
Design a system that:
- Tracks visited web pages
- Supports back navigation
- Supports forward navigation
- Updates history correctly on new visits

---

## DSA Concepts Used
- Stack
- LIFO behavior
- Push and Pop operations

---

## How the Solution Works
- Back history is stored using one stack
- Forward history is stored using another stack
- Visiting a new page clears forward history
- Back and forward operations use stack pop and push

---

## Time and Space Complexity

### Operations
- Visit: O(1)
- Back: O(1)
- Forward: O(1)

### Space Complexity
- O(n), where n is the number of visited pages

---

## How to Run
```bash
python day-11.py
