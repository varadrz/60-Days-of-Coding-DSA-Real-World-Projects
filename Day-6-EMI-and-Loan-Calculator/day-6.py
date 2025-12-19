# Day 6 - EMI & Loan Calculator
# Focus: Math & Number Theory
# Language: Python 3

def calculate_emi(principal, annual_rate, tenure_months):
    monthly_rate = annual_rate / (12 * 100)

    if monthly_rate == 0:
        return principal / tenure_months

    emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure_months) / \
          ((1 + monthly_rate) ** tenure_months - 1)

    return round(emi, 2)


def loan_summary(principal, annual_rate, tenure_months):
    emi = calculate_emi(principal, annual_rate, tenure_months)
    total_payment = round(emi * tenure_months, 2)
    interest = round(total_payment - principal, 2)

    return emi, total_payment, interest


def main():
    print("\n--- EMI & Loan Calculator ---")

    principal = float(input("Enter loan amount: "))
    annual_rate = float(input("Enter annual interest rate (%): "))
    tenure_months = int(input("Enter tenure (months): "))

    emi, total_payment, interest = loan_summary(
        principal, annual_rate, tenure_months
    )

    print("\nLoan Summary")
    print("Monthly EMI:", emi)
    print("Total Payment:", total_payment)
    print("Total Interest:", interest)


if __name__ == "__main__":
    main()
