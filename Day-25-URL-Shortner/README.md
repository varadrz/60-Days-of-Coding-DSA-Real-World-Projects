# Day 25 | URL Shortner Engine

## Overview
This project is part of the **60 Days of Coding | DSA x Real World Projects** series.

Day 25 focuses on building a **URL Shortner Engine** using core **Data Structures and Algorithms**, while also providing a simple interactive frontend for practical usage.

The primary objective is to demonstrate how **hashing enables constant-time operations** in real-world backend systems.

---

## Problem Statement
Design and implement a system that:
- Converts long URLs into short, unique URLs
- Supports fast redirection from short URL to original URL
- Avoids duplicate short code generation
- Works efficiently at scale

---

## DSA Concepts Used
- Hash Maps (Dictionaries)
- Hashing
- Collision Handling
- Constant-Time Lookup (Average Case)


---

## How the System Works
- Long URLs are mapped to short codes using hash maps
- Two dictionaries maintain bidirectional mapping
- Random short codes are generated and checked for collisions
- A production-style URL format is displayed (not localhost)
- Redirection is handled internally by the backend

---

## Time and Space Complexity
- Shorten URL: **O(1)** average
- Expand URL: **O(1)** average
- Space Complexity: **O(n)**, where *n* is the number of URLs stored

---

## How to Run

```bash
pip install flask
python app.py
