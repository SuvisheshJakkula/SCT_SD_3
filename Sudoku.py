def print_grid(grid):
    """Function to print the Sudoku grid in a readable format."""
    for row in grid:
        print(row)


def find_empty_location(grid):
    """Finds an empty spot in the grid (denoted by 0)."""
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None


def is_safe(grid, row, col, num):
    """Checks if placing 'num' in grid[row][col] is valid."""
    # Check row
    if num in grid[row]:
        return False

    # Check column
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Check 3x3 box
    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(grid):
    """Solves Sudoku using backtracking."""
    empty_pos = find_empty_location(grid)
    if not empty_pos:
        return True  # Solved

    row, col = empty_pos

    for num in range(1, 10):  # Try numbers 1–9
        if is_safe(grid, row, col, num):
            grid[row][col] = num  # Place number

            if solve_sudoku(grid):  # Continue solving
                return True

            grid[row][col] = 0  # Undo move (backtrack)

    return False


# Example unsolved Sudoku (0 = empty cell)
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_grid):
    print("Sudoku solved successfully:")
    print_grid(sudoku_grid)
else:
    print("No solution exists.")