# Day 2 | Coupon Code Validator

## Overview
This project is part of the **60 Days of Coding | DSA x Real World Projects** series.

Day 2 focuses on applying **string processing and hashing** to build a real world coupon code validation system.  
The goal is to demonstrate how basic DSA concepts are used to validate inputs and prevent reuse efficiently.

The project includes:
- A **core DSA-based implementation** in Python
- An **optional blockchain-based extension** to explore immutability using hashing

---

## Problem Statement
Design a system that validates coupon codes based on predefined rules and ensures that a coupon cannot be reused once applied.

---

## Core DSA Concepts Used
- Strings for format validation
- Hash Set for fast lookup and reuse prevention
- Iterative character checks
- Conditional logic for rule enforcement

---

## Validation Rules
- Coupon length must be between 6 and 10 characters
- Coupon must be alphanumeric
- Coupon must contain at least one digit
- Coupon cannot be reused

---

## Project Files
- `day-2.py`  
  Core DSA-based coupon code validator using strings and hashing
- `day-2-blockchain.py`  
  Optional extension demonstrating a blockchain-style hash-linked structure
- `README.md`
- `requirements.txt`

---

## How to Run (Core DSA Version)
```bash
python day-2.py
