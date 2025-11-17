import sys

def is_valid_sudoku(board):
    # Convert the flat list to a 9x9 grid
    grid = []
    for i in range(9):
        row = board[i*9:(i+1)*9]
        grid.append(row)
    
    # Check rows for duplicates
    for row in grid:
        if len(row) != len(set(row)):
            return False
    
    # Check columns for duplicates
    for col in range(9):
        column = [grid[row][col] for row in range(9)]
        if len(column) != len(set(column)):
            return False
    
    # Check 3x3 sub-grids for duplicates
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            subgrid = []
            for i in range(3):
                for j in range(3):
                    subgrid.append(grid[box_row + i][box_col + j])
            if len(subgrid) != len(set(subgrid)):
                return False
    
    return True

for line in sys.stdin:
    # Parse the comma-delimited input
    digits = list(map(int, line.strip().split(',')))
    
    # Validate the sudoku board
    result = is_valid_sudoku(digits)
    print(result)


#Time complexity : O(1) - The size of the Sudoku board is fixed (9x9), so the operations performed are constant time.
#Space complexity: O(1) - The space used does not scale with input size, as the board size is fixed.