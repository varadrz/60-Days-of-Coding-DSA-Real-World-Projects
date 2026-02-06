# Day 53 - Interview Mock Problems
# Focus: Interview Practice + Pattern Recall
# Language: Python 3


# ---------------- PROBLEM 1 ----------------
# Two Sum (Hashing)

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []


# ---------------- PROBLEM 2 ----------------
# Valid Parentheses (Stack)

def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in mapping:
            top = stack.pop() if stack else '#'
            if mapping[ch] != top:
                return False
        else:
            stack.append(ch)

    return not stack


# ---------------- PROBLEM 3 ----------------
# Maximum Subarray (Kadane’s Algorithm)

def max_subarray(nums):
    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


def main():
    print("\nTwo Sum:", two_sum([2, 7, 11, 15], 9))
    print("Valid Parentheses:", is_valid_parentheses("({[]})"))
    print("Maximum Subarray:", max_subarray([-2,1,-3,4,-1,2,1,-5,4]))


if __name__ == "__main__":
    main()
