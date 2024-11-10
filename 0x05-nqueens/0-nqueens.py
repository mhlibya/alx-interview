#!/usr/bin/python3
"""
solving the N queens problem
"""
import sys

def is_safe(board, row, col, N):
    """
    is safe
    """
    # Check the column and both diagonals for another queen
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, N, solutions):
    """
    solve nqueens
    """
    # Base case: all queens are placed successfully
    if row == N:
        solutions.append([[r, board[r]] for r in range(N)])
        return
    # Try placing the queen in each column of the current row
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(board, row + 1, N, solutions)
            board[row] = -1  # Backtrack

def main():
    """
    the main function
    """
    # Check the number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Validate if N is an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Validate if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board and list of solutions
    board = [-1] * N
    solutions = []

    # Solve the N-Queens problem
    solve_nqueens(board, 0, N, solutions)

    # Print each solution
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
