def is_valid(seen):
    """Checks if the elements in seen is the numbers 1 through 9"""
    valid = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    return seen == valid


def check_row(board, row):
    """Checks if a row is a correct sudoku row (it contains numbers 1 through 9)"""
    seen = set()
    for col in range(9):
        seen.add(board[row][col])
    
    return is_valid(seen)


def check_column(board, col):
    """
    Checks if a column is a correct sudoku column.
    
    Args:
        board: The sudoku board (list of lists)
        col: Column index (0-8)
    
    Returns:
        True if column contains 1-9 exactly once
    """
    seen = set()
    for row in range(9):
        seen.add(board[row][col])
    
    return is_valid(seen)


def check_block(board, block_row, block_col):
    """
    Checks if a 3x3 block is valid.
    
    Args:
        board: The sudoku board
        block_row: Block row index (0, 1, or 2)
        block_col: Block column index (0, 1, or 2)
    
    Returns:
        True if block contains 1-9 exactly once
    
    Example:
        Block (0,0) is top-left, (1,1) is center, (2,2) is bottom-right
    """
    seen = set()
    
    # Calculate starting position for this block
    start_row = block_row * 3
    start_col = block_col * 3
    
    # Check all 9 cells in the 3x3 block
    for row in range(start_row, start_row + 3):
        for col in range(start_col, start_col + 3):
            seen.add(board[row][col])
    
    return is_valid(seen)


def check_all_rows(board):
    """
    Checks if all rows are valid.
    
    Returns:
        True if all rows contain 1-9 exactly once
    """
    for row in range(9):
        if not check_row(board, row):
            return False
    return True


def check_all_columns(board):
    """
    Checks if all columns are valid.
    
    Returns:
        True if all columns contain 1-9 exactly once
    """
    for col in range(9):
        if not check_column(board, col):
            return False
    return True


def check_all_blocks(board):
    """
    Checks if all 3x3 blocks are valid.
    
    Returns:
        True if all blocks contain 1-9 exactly once
    """
    for block_row in range(3):
        for block_col in range(3):
            if not check_block(board, block_row, block_col):
                return False
    return True


def check_board(board):
    """
    Checks if board is a valid sudoku board.
    
    A valid sudoku board must have:
    - All rows containing 1-9 exactly once
    - All columns containing 1-9 exactly once
    - All 3x3 blocks containing 1-9 exactly once
    
    Args:
        board: 9x9 list of lists containing numbers
    
    Returns:
        True if board is valid, False otherwise
    """
    return (check_all_rows(board) and 
            check_all_columns(board) and 
            check_all_blocks(board))


# ============================================================================
# TESTS
# ============================================================================

if __name__ == "__main__":
    # Valid sudoku board
    sudoku_board = [
        [2, 9, 5, 7, 4, 3, 8, 6, 1],
        [4, 3, 1, 8, 6, 5, 9, 2, 7],
        [8, 7, 6, 1, 9, 2, 5, 4, 3],
        [3, 8, 7, 4, 5, 9, 2, 1, 6],
        [6, 1, 2, 3, 8, 7, 4, 9, 5],
        [5, 4, 9, 2, 1, 6, 7, 3, 8],
        [7, 6, 3, 5, 2, 4, 1, 8, 9],
        [9, 2, 8, 6, 7, 1, 3, 5, 4],
        [1, 5, 4, 9, 3, 8, 6, 7, 2]
    ]

    # Invalid sudoku board (row 2 has duplicate 8)
    bad_sudoku_board = [
        [2, 9, 5, 7, 4, 3, 8, 6, 1],
        [4, 3, 1, 8, 6, 5, 9, 8, 7],  # Two 8s in this row!
        [8, 7, 6, 1, 9, 2, 5, 4, 3],
        [3, 8, 7, 4, 5, 9, 2, 1, 6],
        [6, 1, 2, 3, 8, 7, 4, 9, 5],
        [5, 4, 9, 2, 1, 6, 7, 3, 8],
        [7, 6, 3, 5, 2, 4, 1, 8, 9],
        [9, 2, 8, 6, 7, 1, 3, 5, 4],
        [1, 5, 4, 9, 3, 8, 6, 7, 2]
    ]

    # Run tests
    print("Testing valid sudoku board...")
    assert check_board(sudoku_board), "Valid board should return True"
    print("✓ Valid board test passed!")
    
    print("\nTesting invalid sudoku board...")
    assert not check_board(bad_sudoku_board), "Invalid board should return False"
    print("✓ Invalid board test passed!")
    
    print("\n" + "="*50)
    print("ALL TESTS PASSED!")
    print("="*50)
    
    # Additional detailed tests
    print("\nDetailed validation:")
    print("-"*50)
    print(f"Valid board - All rows valid: {check_all_rows(sudoku_board)}")
    print(f"Valid board - All columns valid: {check_all_columns(sudoku_board)}")
    print(f"Valid board - All blocks valid: {check_all_blocks(sudoku_board)}")
    print()
    print(f"Bad board - All rows valid: {check_all_rows(bad_sudoku_board)}")
    print(f"Bad board - All columns valid: {check_all_columns(bad_sudoku_board)}")
    print(f"Bad board - All blocks valid: {check_all_blocks(bad_sudoku_board)}")
