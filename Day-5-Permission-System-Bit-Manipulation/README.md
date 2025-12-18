# Day 5 | Permission System using Bit Manipulation

## Overview
This project is part of the **60 Days of Coding | DSA x Real World Projects** series.

Day 5 focuses on **Bit Manipulation and Bit Masking** by implementing a permission system similar to how operating systems (like Linux) manage file permissions.

The project demonstrates how permissions can be represented and managed efficiently using binary operations.

---

## Problem Statement
Design a permission system that:
- Represents permissions using bits
- Supports Read, Write, and Execute operations
- Allows adding, removing, and checking permissions
- Performs all operations in constant time

---

## Permission Representation

| Permission | Binary | Decimal |
|-----------|--------|---------|
| Read | 100 | 4 |
| Write | 010 | 2 |
| Execute | 001 | 1 |

A permission value like **6 (110)** means:
- Read: Allowed
- Write: Allowed
- Execute: Not Allowed

---

## DSA Concepts Used
- Bit Manipulation
- Bit Masking
- Bitwise AND (`&`)
- Bitwise OR (`|`)
- Bitwise NOT (`~`)

---

## How the Solution Works
- Each user’s permissions are stored as an integer
- Individual permissions are toggled using bitwise operations
- Permission checks are performed using bitwise AND
- All operations execute in constant time

---

## Time and Space Complexity

### Permission Operations
- Set permission: O(1)
- Add permission: O(1)
- Remove permission: O(1)
- Check permission: O(1)

### Space Complexity
- O(n), where n is the number of users

---

## How to Run
```bash
python day-5.py
