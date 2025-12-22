# Day 9 | User Session Manager

## Overview
This project is part of the **60 Days of Coding | DSA x Real World Projects** series.

Day 9 focuses on **Hashing** by implementing a User Session Manager similar to what is used in backend systems for tracking logged-in users.

---

## Problem Statement
Design a system that:
- Creates user sessions
- Tracks active sessions
- Expires inactive sessions
- Supports login and logout operations efficiently

---

## DSA Concepts Used
- Hash Maps (Dictionary)
- Constant-time lookup
- Iteration over hash table

---

## How the Solution Works
- User sessions are stored in a hash map
- Each session stores the last active timestamp
- Active status is checked using time difference
- Expired sessions are removed using iteration

---

## Time and Space Complexity

### Session Operations
- Login: O(1)
- Logout: O(1)
- Session Check: O(1)

### Cleanup
- Time Complexity: O(n)
- Space Complexity: O(n)

---

## How to Run
```bash
python day-9.py
