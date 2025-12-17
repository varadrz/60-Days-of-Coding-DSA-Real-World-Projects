# Day 4 | File Explorer using Recursion

## Overview
This project is part of the **60 Days of Coding | DSA x Real World Projects** series.

Day 4 focuses on **Recursion and Tree Traversal** by implementing a recursive file explorer similar to how operating systems traverse directory structures.

The project demonstrates how recursion naturally fits problems involving hierarchical data.

---

## Problem Statement
Design a program that:
- Traverses directories and subdirectories recursively
- Prints the directory structure with proper indentation
- Searches for a specific file within the directory tree

---

## DSA Concepts Used
- Recursion
- Tree Traversal
- Depth First Search (DFS)
- Call Stack

---

## How the Solution Works
- Each directory is treated as a node in a tree
- Files and subdirectories are explored recursively
- Depth of recursion represents directory depth
- File search uses recursive DFS traversal

---

## Time and Space Complexity

### Directory Traversal
- Time Complexity: O(n)  
  (n = total number of files and directories)
- Space Complexity: O(h)  
  (h = maximum directory depth due to recursion stack)

### File Search
- Time Complexity: O(n)
- Space Complexity: O(h)

---

## How to Run
```bash
python day-4.py
