# Day 15 - Fraud Transaction Detector
# Focus: Fast & Slow Pointers
# Language: Python 3


def detect_fraud(transactions):
    slow = fast = 0

    while fast < len(transactions) and fast + 1 < len(transactions):
        slow += 1
        fast += 2

        if transactions[slow] == transactions[fast]:
            return True

    return False


def main():
    transactions = [100, 250, 400, 250, 100]
    print("Fraud Detected:", detect_fraud(transactions))


if __name__ == "__main__":
    main()
