#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    # Check if a queen can be placed in a given cell (row, col)

    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(n):
    if n < 4:
        print("N must be at least 4")
        return

    def solve(board, col):
        # Base case: If all queens are placed, print the solution
        if col >= n:
            solution = []
            for row in range(n):
                for col in range(n):
                    if board[row][col] == 1:
                        solution.append([row, col])
            solutions.append(solution)
            return

        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                solve(board, col + 1)
                board[i][col] = 0  # Backtrack

    solutions = []
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve(board, 0)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
