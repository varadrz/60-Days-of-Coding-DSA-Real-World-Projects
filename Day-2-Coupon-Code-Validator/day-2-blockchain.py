# Day 2 - Coupon Code Validator (Blockchain Extension)
# Focus: Hashing and Immutability Concept
# Language: Python 3

import hashlib
import time


class Block:
    def __init__(self, coupon_code, previous_hash):
        self.coupon_code = coupon_code
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = f"{self.coupon_code}{self.timestamp}{self.previous_hash}"
        return hashlib.sha256(data.encode()).hexdigest()


class CouponBlockchain:
    def __init__(self):
        self.chain = []
        self.used_coupons = set()

        genesis_block = Block("GENESIS", "0")
        self.chain.append(genesis_block)

    def is_valid_format(self, code):
        if not (6 <= len(code) <= 10):
            return False
        if not code.isalnum():
            return False
        return any(ch.isdigit() for ch in code)

    def add_coupon(self, code):
        if code in self.used_coupons:
            return "Invalid: Coupon already used (Blockchain verified)"

        if not self.is_valid_format(code):
            return "Invalid: Coupon format not valid"

        new_block = Block(code, self.chain[-1].hash)
        self.chain.append(new_block)
        self.used_coupons.add(code)

        return "Valid: Coupon added to blockchain"

    def display_chain(self):
        print("\n--- Coupon Blockchain ---")
        for i, block in enumerate(self.chain):
            print(f"Block {i}")
            print(f" Coupon Code: {block.coupon_code}")
            print(f" Hash: {block.hash}")
            print(f" Previous Hash: {block.previous_hash}")
            print("-" * 30)


def main():
    blockchain = CouponBlockchain()

    while True:
        print("\n===== Blockchain Coupon Validator =====")
        print("1. Apply Coupon")
        print("2. View Blockchain")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            code = input("Enter coupon code: ").strip()
            print(blockchain.add_coupon(code))

        elif choice == "2":
            blockchain.display_chain()

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
