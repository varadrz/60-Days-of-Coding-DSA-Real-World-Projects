# Day 47 - Seating Arrangement Planner
# Focus: N-Queens Problem (Backtracking)
# Language: Python 3


class SeatingArrangementPlanner:
    def __init__(self, n):
        self.n = n
        self.solutions = []

    def solve(self):
        board = [-1] * self.n  # board[row] = column of queen
        self._backtrack(0, board)
        return self.solutions

    def _backtrack(self, row, board):
        if row == self.n:
            self.solutions.append(board.copy())
            return

        for col in range(self.n):
            if self._is_safe(row, col, board):
                board[row] = col
                self._backtrack(row + 1, board)
                board[row] = -1  # backtrack

    def _is_safe(self, row, col, board):
        for prev_row in range(row):
            prev_col = board[prev_row]
            if prev_col == col:
                return False
            if abs(prev_col - col) == abs(prev_row - row):
                return False
        return True

    def print_solutions(self):
        for idx, solution in enumerate(self.solutions, 1):
            print(f"\nSolution {idx}:")
            for row in range(self.n):
                line = ["Q" if solution[row] == col else "." for col in range(self.n)]
                print(" ".join(line))


def main():
    n = int(input("Enter number of seats (N): "))
    planner = SeatingArrangementPlanner(n)
    planner.solve()

    print(f"\nTotal valid seating arrangements: {len(planner.solutions)}")
    planner.print_solutions()


if __name__ == "__main__":
    main()
