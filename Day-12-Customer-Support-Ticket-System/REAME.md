# Day 12 | Customer Support Ticket System

## Overview
This project is part of the **60 Days of Coding | DSA x Real World Projects** series.

Day 12 focuses on the **Queue data structure** by implementing a Customer Support Ticket System similar to real-world helpdesk platforms.

---

## Problem Statement
Design a system that:
- Accepts customer support tickets
- Processes tickets in the order they are received
- Resolves tickets one by one

---

## DSA Concepts Used
- Queue
- FIFO (First In First Out)
- Enqueue and Dequeue operations

---

## How the Solution Works
- Tickets are added to the queue when created
- Tickets are resolved in FIFO order
- Deque is used for efficient queue operations

---

## Time and Space Complexity

### Operations
- Create ticket: O(1)
- Resolve ticket: O(1)

### Space Complexity
- O(n), where n is the number of tickets

---

## How to Run
```bash
python day-12.py
