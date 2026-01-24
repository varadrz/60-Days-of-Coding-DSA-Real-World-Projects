# Day 42 - Exam Timetable Optimizer
# Focus: Dynamic Programming (2D)
# Language: Python 3


class ExamTimetableOptimizer:
    def __init__(self, subjects, time_slots):
        self.subjects = subjects
        self.time_slots = time_slots

    def optimize(self):
        """
        dp[i][j] = True if first i subjects can be scheduled
                   using j time slots
        """
        n = len(self.subjects)
        m = self.time_slots

        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # Either skip current subject or assign it to a slot
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - 1]

        return dp[n][m]


def main():
    subjects = ["Maths", "DSA", "DBMS", "OS"]
    time_slots = 4

    optimizer = ExamTimetableOptimizer(subjects, time_slots)
    result = optimizer.optimize()

    if result:
        print("\nTimetable can be scheduled successfully.")
    else:
        print("\nTimetable scheduling not possible.")


if __name__ == "__main__":
    main()
