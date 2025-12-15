# Day 2 - Coupon Code Validator
# Focus: Strings and Hashing (DSA)
# Language: Python 3


def is_valid_format(code):
    """
    Validation Rules:
    - Length between 6 and 10 characters
    - Alphanumeric only
    - Must contain at least one digit
    """
    if len(code) < 6 or len(code) > 10:
        return False

    if not code.isalnum():
        return False

    digit_found = False
    for ch in code:
        if ch.isdigit():
            digit_found = True
            break

    return digit_found


def validate_coupon(code, used_coupons):
    if code in used_coupons:
        return "Invalid: Coupon already used"

    if not is_valid_format(code):
        return "Invalid: Coupon format not valid"

    used_coupons.add(code)
    return "Valid: Coupon applied successfully"


def main():
    used_coupons = set()  # Hash Set for O(1) lookup

    while True:
        print("\n===== Coupon Code Validator =====")
        print("1. Enter coupon code")
        print("2. Exit")

        choice = input("Choose an option (1-2): ").strip()

        if choice == "1":
            # Input normalization (VERY IMPORTANT)
            raw_input = input("Enter coupon code: ")
            code = raw_input.strip().upper()

            result = validate_coupon(code, used_coupons)
            print(result)

        elif choice == "2":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
