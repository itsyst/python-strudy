# Example solutions to the exam 2018-04-04
# Simon Lindblad, Fredrik Heintz, Malcom Vigren 2018-04-04


##### Uppgift 1
def score(pins):
    """ Compute the bowling score based on a list of pins knocked down. """
    score, pin = 0, 0
    for frame in range(10):
        if pins[pin] == 10:
            score += 10 + pins[pin+1] + pins[pin+2]
            pin += 1
        else:
            frame_score = pins[pin] + pins[pin+1]
            score += frame_score + (pins[pin+2] if frame_score == 10 else 0)
            pin += 2
    return score

assert score([6, 2, 8, 2, 10, 9, 0, 6, 4, 8, 1, 9, 1, 10, 10, 8, 2, 7]) == 168
assert score([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 300
assert score([1, 3, 3, 6, 2, 5, 9, 0, 0, 5, 0, 0, 4, 5, 5, 3, 1, 8, 7, 2]) == 69


#### Uppgift 2
def pairwise_add_i(seq1, seq2):
    """ Iteratively add each pair of numbers from seq1 and seq2. """
    res = []
    for i in range(len(seq1)):
        if i < len(seq2):
            res.append(seq1[i] + seq2[i])
        else:
            res.append(seq1[i])
    return res + seq2[len(seq1):]

def pairwise_add_r(seq1, seq2):
    """ Recursively add each pair of numbers from seq1 and seq2. """
    if not seq1 or not seq2:
        return seq1 + seq2
    return [seq1[0] + seq2[0]] + pairwise_add_r(seq1[1:], seq2[1:])

assert pairwise_add_i([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == [6, 6, 6, 6, 6]
assert pairwise_add_i([2, 4, 6], [1, 3]) == [3, 7, 6]
assert pairwise_add_i([2, 4, 6], [1, 3, 0, 4]) == [3, 7, 6, 4]
assert pairwise_add_r([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == [6, 6, 6, 6, 6]
assert pairwise_add_r([2, 4, 6], [1, 3]) == [3, 7, 6]
assert pairwise_add_r([2, 4, 6], [1, 3, 0, 4]) == [3, 7, 6, 4]


#### Uppgift 4
def find_three_smallest_numbers(seq):
    """ Given a list of arbitrary elements, including lists,
        return a sorted list of the three smallest numbers. """
    if not seq:
        return []
    elif isinstance(seq[0], list):
        three_smallest1 = find_three_smallest_numbers(seq[0])
        three_smallest2 = find_three_smallest_numbers(seq[1:])
        return sorted(three_smallest1 + three_smallest2)[0:3]
    elif isinstance(seq[0], int):
        return sorted(find_three_smallest_numbers(seq[1:])+[seq[0]])[0:3]
    else:
        return find_three_smallest_numbers(seq[1:])
    
assert find_three_smallest_numbers([1, 2, 3]) == [1, 2, 3]
assert find_three_smallest_numbers([[1], [[2], 3]]) == [1, 2, 3]
assert find_three_smallest_numbers([[1, [[1]]], 1, [[1], 2], 3]) == [1, 1, 1]
assert find_three_smallest_numbers([[1], 3]) == [1, 3]
assert find_three_smallest_numbers([[1, 'du', [['e']]], [1, "bra"], [[1], 2]]) == [1, 1, 1]
assert find_three_smallest_numbers([3, 2, 1]) == [1, 2, 3]
assert find_three_smallest_numbers([]) == []
assert find_three_smallest_numbers([7]) == [7]
assert find_three_smallest_numbers(['hej']) == []
assert find_three_smallest_numbers([[1], [[2], 3]]) == [1, 2, 3]
assert find_three_smallest_numbers([[1, 'du', [[1, 'e']]], 1, "bra", [[1], 2], 3]) == [1, 1, 1]
assert find_three_smallest_numbers([3, "hej", 2, 'a', 1]) == [1, 2, 3]


#### Uppgift 4a
def pairwise_apply(f):
    return lambda x: [f(x[i-1], x[i]) for i in range(1, len(x), 2)]

def multiply(x, y):
    return x*y

f = pairwise_apply(multiply)
assert f([1, 2, 3, 4, 5, 6]) == [2, 12, 30]
assert f([1, 2, 3, 4, 5, 6, 7]) == [2, 12, 30]

#### Uppgift 4b
pairwise_add = lambda s1, s2: pairwise_apply(lambda x, y: x+y)(sum(zip(s1, s2), ())) + s1[len(s2):] + s2[len(s1):]
assert pairwise_add([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == [6, 6, 6, 6, 6]
assert pairwise_add([2, 4, 6], [1, 3]) == [3, 7, 6]


#### Uppgift 5
def subset_sum(seq, num, acc = 0):
    """ Check if any subset of seq has a sum equal to num
        by recursively trying each combination, including the empty set. """
    if acc == num:
        return True
    elif not seq:
        return False
    else:
        return subset_sum(seq[1:], num, acc+seq[0]) or subset_sum(seq[1:], num, acc)


def powerset(seq):
    """ Computer the power set of seq. """
    if not seq:
        return [[]]
    else:
        power = powerset(seq[:-1])
    return power + [n + [seq[-1]] for n in power]

def subset_sum_ps(seq, num):
    """ Check if any subset of seq has a sum equal to num
        by checking each set in the powerset, including the empty set. """
    return next(filter(lambda s: sum(s) == num, powerset(seq)), False) != False

assert subset_sum([-7, -3, -2, 5, 8], 0)
assert subset_sum([-7, -3, -2, 5, 8], 5)
assert not subset_sum([-7, -3, -2, 5, 8], 7)
assert subset_sum([3, 34, 4, 12, 5, 2], 9)

assert subset_sum_ps([-7, -3, -2, 5, 8], 0)
assert subset_sum_ps([-7, -3, -2, 5, 8], 5)
assert not subset_sum_ps([-7, -3, -2, 5, 8], 7)
assert subset_sum_ps([3, 34, 4, 12, 5, 2], 9)


#### Uppgift 6
def create_board():
    """ Create a board with no fixed values. """
    return [[[i+1 for i in range(9)] for _ in range(9)] for _ in range(9)]

def row(b, r):
    """ Return row r. """
    return b[r-1]

def column(b, c):
    """ Return column c. """
    return [row[c-1] for row in b]

def square(b, s):
    """ Return square s. """
    row_square = ((s-1) // 3)*3
    col_square = ((s-1) % 3)*3
    res = []
    for row in b[row_square:row_square+3]:
        for cell in row[col_square:col_square+3]:
            res.append(cell)
    return res

def remove_value(b, r, c, v):
    """ Remove v from the set of possible values in cell r,c. """
    b[r-1][c-1].remove(v)


def set_value(b, r, c, v):
    """ Set the value of cell r,c to v. """
    if v not in b[r-1][c-1]:
        raise Exception('Move {} invalid for cell ({}, {})'.format(v, r, c))

    # update rows
    row_list = row(b, r)
    for cell in row_list:
        if v in cell:
            cell.remove(v)

    # update columns
    col_list = column(b, c)
    for cell in col_list:
        if v in cell:
            cell.remove(v)

    # update squares
    square_list = square(b, 1 + (c-1)//3 + 3*((r-1)//3))
    for cell in square_list:
        if v in cell:
            cell.remove(v)

    b[r-1][c-1] = [v]


def set_row(b, r, values):
    """ Set row r to value. """
    for c, v in enumerate(values):
        if v != 0:
            set_value(b, r, c+1, v)

b = create_board()
set_row(b, 1, [0, 0, 6, 0, 5, 4, 9, 0, 0])
set_row(b, 2, [1, 0, 0, 0, 6, 0, 0, 4, 2])
set_row(b, 3, [7, 0, 0, 0, 8, 9, 0, 0, 0])
set_row(b, 4, [0, 7, 0, 0, 0, 5, 0, 8, 1])
set_row(b, 5, [0, 5, 0, 3, 4, 0, 6, 0, 0])
set_row(b, 6, [4, 0, 2, 0, 0, 0, 0, 0, 0])
set_row(b, 7, [0, 3, 4, 0, 0, 0, 1, 0, 0])
set_row(b, 8, [9, 0, 0, 8, 0, 0, 0, 5, 0])
set_row(b, 9, [0, 0, 0, 4, 0, 0, 3, 0, 7])

assert row(b, 2) == [[1], [8, 9], [3, 5, 8, 9], [7], [6], [3, 7], [5, 7, 8], [4], [2]]
set_value(b, 2, 4, 7)
assert row(b, 2) == [[1], [8, 9], [3, 5, 8, 9], [7], [6], [3], [5, 8], [4], [2]]
assert column(b, 3) == [[6], [3, 5, 8, 9], [3, 5], [3, 9], [1, 8, 9], [2], [4], [1, 7], [1, 5, 8]]
assert square(b, 1) == [[2, 3, 8], [2, 8], [6], [1], [8, 9], [3, 5, 8, 9], [7], [2, 4], [3, 5]]
