#%%
def is_valid(seen):
    """ Checks if the elements in seen is the numbers 1 through 9 """
    valid = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    return seen == valid


def check_row(board, row):
    """ Checks if a row is a correct sudoku row (it contains numbers 1 through 9) """
    seen = set()
    for col in range(9):
        seen.add(board[row][col])

    return is_valid(seen)


def check_board(board):
    """ Checks if board is a valid sudoku board """
    # Your implementation goes here
    # You will probably need to write more help functions
    
    for row in range(9):
        #all_true *= check_row(board, row)
        if not check_row(board, row):
            return False
    return True


if __name__ == "__main__":
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

    bad_sudoku_board = [
        [2, 9, 5, 7, 4, 3, 8, 6, 1],
        [4, 3, 1, 8, 6, 5, 9, 8, 7],
        [8, 7, 6, 1, 9, 2, 5, 4, 3],
        [3, 8, 7, 4, 5, 9, 2, 1, 6],
        [6, 1, 2, 3, 8, 7, 4, 9, 5],
        [5, 4, 9, 2, 1, 6, 7, 3, 8],
        [7, 6, 3, 5, 2, 4, 1, 8, 9],
        [9, 2, 8, 6, 7, 1, 3, 5, 4],
        [1, 5, 4, 9, 3, 8, 6, 7, 2]
    ]

    assert check_board(sudoku_board)
    assert not check_board(bad_sudoku_board)
#%%