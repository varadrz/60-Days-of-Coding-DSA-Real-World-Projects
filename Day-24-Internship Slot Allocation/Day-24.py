# Day 24 - Internship Slot Allocation
# Focus: Greedy with Sorting
# Language: Python 3


def allocate_internships(applicants, slots):
    """
    applicants: list of tuples (name, score)
    slots: total available internship slots
    """
    # Sort applicants by score (descending)
    applicants.sort(key=lambda x: x[1], reverse=True)

    selected = []
    for i in range(min(slots, len(applicants))):
        selected.append(applicants[i])

    return selected


def main():
    applicants = [
        ("Alice", 85),
        ("Bob", 92),
        ("Charlie", 78),
        ("David", 88),
        ("Eva", 90)
    ]

    slots = 3
    selected_interns = allocate_internships(applicants, slots)

    print("\nSelected Interns:")
    for name, score in selected_interns:
        print(f"{name} | Score: {score}")


if __name__ == "__main__":
    main()

