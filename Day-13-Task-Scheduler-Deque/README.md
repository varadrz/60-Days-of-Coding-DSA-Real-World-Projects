# Day 13 | Task Scheduler using Deque

## Overview
This project is part of the **60 Days of Coding | DSA x Real World Projects** series.

Day 13 focuses on the **Deque (Double-Ended Queue)** data structure by implementing a Task Scheduler that handles both high and low priority tasks efficiently.

---

## Problem Statement
Design a system that:
- Accepts tasks with different priorities
- Executes high-priority tasks first
- Maintains task order efficiently

---

## DSA Concepts Used
- Deque
- FIFO and LIFO behavior
- Double-ended insertion and removal

---

## How the Solution Works
- High-priority tasks are added to the front of the deque
- Low-priority tasks are added to the rear
- Tasks are executed from the front
- Deque allows O(1) insertion and removal from both ends

---

## Time and Space Complexity

### Operations
- Add high priority task: O(1)
- Add low priority task: O(1)
- Execute task: O(1)

### Space Complexity
- O(n), where n is the number of tasks

---

## How to Run
```bash
python day-13.py
