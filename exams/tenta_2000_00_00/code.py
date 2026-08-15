#%%

#---Uppgift 1---#
from random import randint

def liuid(first: str, sur: str) -> str:
    """Givet ett förnamn och efternamn så returnerar funktionen
    ett korrekt liuid med de 3 första bokstäverna från förnamnet,
    de andra 2 från efternamnet och sedan ett slumpmässigt tal mellan
    100 - 999"""
    return (first[:3] + sur[:2] + str(randint(100, 999))).lower()

#---Uppgift 2---#

def replace_r(occur, repl, seq: list) -> list:
    """Rekursiv funktion som ersätter alla förekomster av ett element
    med ett annat."""
    if not seq:
        return []
    if seq[0] == occur:
        return [repl] + replace_r(occur, repl, seq[1:])
    return [seq[0]] + replace_r(occur, repl, seq[1:])

#---Uppgift 3---#

###Deluppgift 3A

def collector(func: "function", seq: list) -> list:
    if not seq:
        return []
    if func(seq[0]):
        return [seq[0]] + collector(func, seq[1:])
    if isinstance(seq[0], list):
        return collector(func, seq[0]) + collector(func, seq[1:])
    return collector(func, seq[1:])

###Deluppgift 3B

def numbers_in_interval(i_min: int, i_max: int, seq: list) -> list:
    def func(val):
        if isinstance(val, int):
            if i_max >= val >= i_min:
                return val
    return collector(func, seq)

#---Uppgift 4---#

#from tictactoe_s import *
###Deluppgift A

#def make_move(board, position, piece):
#    "board x position x piece -> board"
#    row = change_piece(piece, position_column(position), board_row(position_row(position), board))
#    board = change_row(row, position_row(position), board)
#    return board

###Deluppgift B

#def is_winner(board, piece):
#    "board x piece -> truth value"
#    for posseq in WINNING_COMBINATIONS:
#        if check_combination(board, piece, posseq):
#            return True
#    return False
#
#def check_combination(board, piece, posseq):
#    if is_empty_posseq(posseq):
#        return True
#    pos = first_position(posseq)
#    compare = row_piece(position_column(pos), board_row(position_row(pos), board))
#    if is_same_piece(compare, piece):
#        return check_combination(board, piece, rest_posseq(posseq))
#    return False

#---Uppgift 5---#

def has_loop(start: str, path: dict) -> bool:
    def inner(curr, visited: set) -> bool:
        if not curr:
            return False
        if curr in visited:
            return True
        if isinstance(curr, tuple):
            return inner(curr[0], visited) or inner(curr[1:], visited)
        return inner(path[curr], visited | {curr}) #samma som visited.add(curr)
    return inner(start, set())

#---Uppgift 6---#

def give_change(num: int) -> list: #bad
    res = []
    for bill in [500, 100, 50, 20, 10, 5, 1]:
        while num >= bill:
            res.append(bill)
            num -= bill
    return res

if __name__ == '__main__':
    #print(liuid("Ture", "Teknolog"))
    #print(liuid("Bo", "Ek"))

    #print(replace_r('old', 'new', ['old', 'a', 'old', 'b']))
    #print(replace_r(1, 'x', [0, 1, 2, 1, 7]))

    #print(collector((lambda x: isinstance(x, str)), ['a', 1, ['b', ['c'], 2], 'd', 3]))
    #print(numbers_in_interval(10, 20, [['x', 5, [15, 'y'], 20], 2, 'z', 17]))

    #test_graph = {'a': ('b', 'd'), 'b': ('c'), 'c': ('d'), 'd': ('b', 'e'), 'e': ('f'), 'f': ()}
    #print(has_loop('a', test_graph)) #True
    #print(has_loop('c', test_graph)) #True
    #print(not has_loop('e', test_graph)) ??

    #assert give_change(177) == [100, 50, 20, 5, 1, 1]
    #assert give_change(206) == [100, 100, 5, 1]
    pass
#%%
