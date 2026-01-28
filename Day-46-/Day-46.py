# Day 46 - Sudoku Solver Engine
# Focus: Backtracking
# Language: Python 3


class SudokuSolver:
    def __init__(self, board):
        self.board = board

    def solve(self):
        empty = self.find_empty()
        if not empty:
            return True  # solved

        row, col = empty

        for num in range(1, 10):
            if self.is_valid(num, row, col):
                self.board[row][col] = num

                if self.solve():
                    return True

                self.board[row][col] = 0  # backtrack

        return False

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def is_valid(self, num, row, col):
        # Row check
        if num in self.board[row]:
            return False

        # Column check
        for i in range(9):
            if self.board[i][col] == num:
                return False

        # 3x3 box check
        box_x = (col // 3) * 3
        box_y = (row // 3) * 3

        for i in range(box_y, box_y + 3):
            for j in range(box_x, box_x + 3):
                if self.board[i][j] == num:
                    return False

        return True

    def print_board(self):
        for row in self.board:
            print(row)


def main():
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    solver = SudokuSolver(board)

    print("\nOriginal Sudoku Board:")
    solver.print_board()

    solver.solve()

    print("\nSolved Sudoku Board:")
    solver.print_board()


if __name__ == "__main__":
    main()
