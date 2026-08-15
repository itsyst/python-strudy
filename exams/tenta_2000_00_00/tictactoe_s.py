
# encoding: iso-8859-1

# ---------------------------------------------------------------------
#  Tic-tac-toe (student version)
#  Assignment for the course TDDD64 Programming in Python
#  Original Common Lisp version by Anders Haraldsson
# ---------------------------------------------------------------------

from random import randint

# ---------------------------------------------------------------------
#  1. Primitives
# ---------------------------------------------------------------------

# Primitives for the board datatype

def make_board():
    "-> board"
    return [make_row(), make_row(), make_row()]
    
def change_row(row, row_index, board):
    "row x integer x board -> board"
    board[row_index - 1] = row
    return board
    
def board_row(row_index, board):
    "integer x board -> row"
    return board[row_index - 1]

def for_each_row(board, row_fn):
    "board x (row ->) ->"
    for row in board:
        row_fn(row)
    
# Primitives for the row datatype

def make_row():
    "-> row"
    return [make_piece('empty'), make_piece('empty'), make_piece('empty')]
    
def change_piece(piece, column_index, row):
    "piece x integer x row -> row"
    row[column_index - 1] = piece
    return row
    
def row_piece(column_index, row):
    "integer x row -> piece"
    return row[column_index - 1]
    
def for_each_piece(row, piece_fn):
    "row x (piece ->) ->"
    for piece in row:
        piece_fn(piece)
    
# Primitives for the piece datatype

def make_piece(value):
    "string -> piece"
    return value
    
def is_same_piece(p1, p2):
    "piece x piece -> truth value"
    return p1 == p2
    
def piece_to_string(p):
    "piece -> string"
    table = {'empty': ' ', 'ring': 'O', 'cross': 'X'}
    return table[p]

# Primitives for the position datatype

def make_position(row_index, column_index):
    "integer x integer -> position"
    return (row_index, column_index)
    
def position_row(pos):
    "position -> integer"
    return pos[0]
    
def position_column(pos):
    "position -> integer"
    return pos[1]
    
# Primitives for the position sequence datatype

def make_posseq():
    "-> position sequence"
    return []
    
def is_empty_posseq(posseq):
    "position sequence -> truth value"
    return not posseq
    
def insert_position(pos, posseq):
    "position x position sequence -> position sequence"
    return [pos] + posseq
    
def first_position(posseq):
    "position sequence -> position"
    return posseq[0]
    
def rest_posseq(posseq):
    "position sequence -> position sequence"
    return posseq[1:]
    
# ---------------------------------------------------------------------
#  2. The game
# ---------------------------------------------------------------------

# Display a board

def print_board(board):
    print('-' * 9)
    for_each_row(board, lambda row: \
        print('! ',end='') or for_each_piece(row, lambda piece: \
            print(piece_to_string(piece) + ' ',end='')) or print('!'))
    print('-' * 9)

# Check if a position is unoccupied

def is_free(p, b):
    "position x board -> truth value"
    return is_same_piece(make_piece('empty'), \
        row_piece(position_column(p), board_row(position_row(p), b)))

# Let the human player make a move
        
def human_move(board, piece):
    "board x piece -> board"
    while True:
        print("Where do you want to place your piece? Please enter row and column!")
        try:
            s = input().split(' ')
            r, c = int(s[0]), int(s[1])
            if 1 <= r <= 3 and 1 <= c <= 3:
                p = make_position(r, c)
                if is_free(p, board):
                    break
                else:
                    print("That position is occupied!")
            else:
                print("Coordinates must be in the interval 1-3!")
        except:
            print("Just enter row and column coordinates (1-3) separated by space!")
    return make_move(board, p, piece)

# Create a random position
    
def make_random_position():
    "-> position"
    return make_position(randint(1, 3), randint(1, 3))

# Make a random move for the given piece
    
def make_random_move(board, piece):
    "board x piece -> board"
    p = make_random_position()
    while not is_free(p, board):
        p = make_random_position()
    return make_move(board, p, piece)

# The main function for making the computer move. If a smarter
# computer player is needed, create a new function and call it from here.
    
def computer_move(board, piece):
    "board x piece -> board"
    return make_random_move(board, piece)
            
# Update the board with the given move, without checks.
# (Implement this in assignment A.)

def make_move(board, position, piece):
    "board x position x piece -> board"
    row = change_piece(piece, position_column(position), board_row(position_row(position), board))
    board = change_row(row, position_row(position), board)
    return board

# Check if player with the given piece has won.
# (Implement this in assignment B.)
   
def is_winner(board, piece):
    "board x piece -> truth value"
    for posseq in WINNING_COMBINATIONS:
        if check_combination(board, piece, posseq):
            return True
    return False

def check_combination(board, piece, posseq):
    if is_empty_posseq(posseq):
        return True
    pos = first_position(posseq)
    compare = row_piece(position_column(pos), board_row(position_row(pos), board))
    if is_same_piece(compare, piece):
        return check_combination(board, piece, rest_posseq(posseq))
    return False

# The set of all winning combinations.
    
WINNING_COMBINATIONS = ( \
    insert_position(make_position(1, 1), \
      insert_position(make_position(2, 2), \
        insert_position(make_position(3, 3), make_posseq()))),
    insert_position(make_position(3, 1), \
      insert_position(make_position(2, 2), \
        insert_position(make_position(1, 3), make_posseq()))),
    insert_position(make_position(1, 1), \
      insert_position(make_position(1, 2), \
        insert_position(make_position(1, 3), make_posseq()))),
    insert_position(make_position(2, 1), \
      insert_position(make_position(2, 2), \
        insert_position(make_position(2, 3), make_posseq()))),
    insert_position(make_position(3, 1), \
      insert_position(make_position(3, 2), \
        insert_position(make_position(3, 3), make_posseq()))),
    insert_position(make_position(1, 1), \
      insert_position(make_position(2, 1), \
        insert_position(make_position(3, 1), make_posseq()))),
    insert_position(make_position(1, 2), \
      insert_position(make_position(2, 2), \
        insert_position(make_position(3, 2), make_posseq()))),
    insert_position(make_position(1, 3), \
      insert_position(make_position(2, 3), \
        insert_position(make_position(3, 3), make_posseq()))) )

def main():
    board = make_board()
    computer_piece = make_piece('cross')
    human_piece = make_piece('ring')
    print("Welcome to Tic-Tac-Toe. The computer plays (X), you play (O).")
    moves = 0
    while True:
        print("The computer makes a move.")
        board = computer_move(board, computer_piece)
        print_board(board)
        if is_winner(board, computer_piece):
            print("The computer wins!")
            break
        moves += 1
        if moves >= 9:
            print("It's a draw!")
            break
        board = human_move(board, human_piece)
        if is_winner(board, human_piece):
            print("You win against the computer! Well done!")
            break
        moves += 1

main()