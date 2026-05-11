# N-Queens Problem using Backtracking

def is_safe(board, row, col):
    """Checks if it's safe to place a queen at board[col] = row"""
    for prev_col in range(col):
        prev_row = board[prev_col]
        
        # 1. Check if same row
        if prev_row == row:
            return False
            
        # 2. Check diagonals (Distance in rows == Distance in columns)
        if abs(prev_row - row) == abs(prev_col - col):
            return False
            
    return True

def solve_n_queens(board, col, n):
    # BASE CASE: If all columns are filled, we found a solution
    if col == n:
        return True

    # Try placing a queen in every row of the current column
    for row in range(n):
        if is_safe(board, row, col):
            board[col] = row  # Place queen
            
            # Recursively try to place the next queen in the next column
            if solve_n_queens(board, col + 1, n):
                return True
            
            # BACKTRACK: If placing queen here doesn't lead to a solution,
            # the loop continues and tries the next row.
            board[col] = -1 
            
    return False

# Execution
n = 4  # You can change this to 8 for a standard board
board = [-1] * n # Initialize board with -1 (meaning no queens placed)

if solve_n_queens(board, 0, n):
    print(f"Solution for {n}-Queens:")
    # Visualizing the board
    for row in range(n):
        line = ""
        for col in range(n):
            if board[col] == row:
                line += " Q "
            else:
                line += " . "
        print(line)
else:
    print("No solution exists.")















[ START ]
    |
    V
[ Start at Column 0 ] <---------------------------------------+
    |                                                         |
    V                                                         |
[ Try Row i (0 to N-1) ] <----------+                         |
    |                               |                         |
    V                               |                         |
/-----------\                [ Try Next Row ]          [ Backtrack ]
|  Is Safe? |---(No)----------------^                  [ Remove Queen]
\-----------/                                                 ^
    |                                                         |
  (Yes)                                                       |
    |                                                         |
[ Place Queen ]                                               |
    |                                                         |
    V                                                         |
/------------------\                                          |
| All Columns Done?|---(No)--> [ Move to Next Column ] -------+
\------------------/
    |
  (Yes)
    |
[ Print Board & END ]
