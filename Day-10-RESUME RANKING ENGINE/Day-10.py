# Day 10 - Resume Ranking Engine
# Focus: Sorting Algorithms
# Language: Python 3


class Candidate:
    def __init__(self, name, score, experience):
        self.name = name
        self.score = score
        self.experience = experience

    def __repr__(self):
        return f"{self.name} | Score: {self.score} | Exp: {self.experience} yrs"


def rank_candidates(candidates):
    """
    Sort candidates by:
    1. Higher score
    2. Higher experience (if scores tie)
    """
    return sorted(
        candidates,
        key=lambda c: (c.score, c.experience),
        reverse=True
    )


def main():
    candidates = [
        Candidate("Alice", 85, 2),
        Candidate("Bob", 90, 1),
        Candidate("Charlie", 85, 3),
        Candidate("David", 92, 2),
        Candidate("Eva", 90, 4)
    ]

    print("\n--- Resume Ranking Engine ---")
    print("\nBefore Ranking:")
    for c in candidates:
        print(c)

    ranked = rank_candidates(candidates)

    print("\nAfter Ranking:")
    for idx, c in enumerate(ranked, start=1):
        print(f"{idx}. {c}")


if __name__ == "__main__":
    main()
