
# encoding: iso-8859-1

# -----------------------------------------------------------------------------
#  Datortentamen i kursen TDDD64 Programmering i Python
#  2013-03-27
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#  Uppgift 1
# -----------------------------------------------------------------------------

from random import randint
    
def manhattan(width, low, high):
    houses = []
    for i in range(width):
        houses.append(randint(low, high))
    for row_index in range(high, low-1, -1):
        for column_index in range(width):
            if houses[column_index] >= row_index:
                print('#',end='')
            else:
                print(' ',end='')
        print()
    for i in range(low-1):
        print('#' * width)

# -----------------------------------------------------------------------------
#  Uppgift 2
# -----------------------------------------------------------------------------

def insert_r(pos, new, seq):
	if pos == 0:
		return [new] + seq
	else:
		return [seq[0]] + insert_r(pos-1, new, seq[1:])
		
def insert_i(pos, new, seq):
	res = []
	while pos > 0:
		res.append(seq[0])
		seq = seq[1:]
		pos -= 1
	return res + [new] + seq
	
assert insert_r(2, 'c', ['a', 'b', 'd', 'e']) == ['a', 'b', 'c', 'd', 'e']
assert insert_i(2, 'c', ['a', 'b', 'd', 'e']) == ['a', 'b', 'c', 'd', 'e']

# -----------------------------------------------------------------------------
#  Uppgift 3
# -----------------------------------------------------------------------------
        
def remover(pred, seq):
    if not seq:
        return []
    elif pred(seq[0]):
        return remover(pred, seq[1:])
    elif isinstance(seq[0], list):
        return [remover(pred, seq[0])] + remover(pred, seq[1:])
    else:
        return [seq[0]] + remover(pred, seq[1:])

def rem_values(low, high, seq):
    return remover(lambda x: isinstance(x, int) and low <= x <= high, seq)

assert remover(lambda x: isinstance(x, int), [1, ['b', [2], 'c'], 'd', 3]) == [['b', [], 'c'], 'd']

assert rem_values(10, 20, [['x', 5, [15, 'y'], 20], 2, 'z', 17]) == [['x', 5, ['y']], 2, 'z']

# -----------------------------------------------------------------------------
#  Uppgift 4
# -----------------------------------------------------------------------------

def count_level(lvl, seq):
    if not seq or lvl == 0:
        return 0
    elif isinstance(seq[0], list):
        return count_level(lvl - 1, seq[0]) + count_level(lvl, seq[1:])
    elif lvl == 1:
        return 1 + count_level(lvl, seq[1:])
    else:
        return count_level(lvl, seq[1:])
        
assert count_level(1, ['a', 'b', ['c', 'd', 'e']]) == 2
assert count_level(3, ['a', ['b', ['c', ['d'], 'e']]]) == 2

# -----------------------------------------------------------------------------
#  Uppgift 5
# -----------------------------------------------------------------------------

svensson = ['Erik', ['Olle', ['Eva', 'Karin', 'Anna'],
                             ['Lars', 'Maria'],
                             ['Pär', 'Sofia']],
                    'Lisa',
                    ['Stina', ['Gunnar', 'Lasse'],
                              'Lennart']]

def ancestors(person, tree):
    if isinstance(tree, str):
        if person == tree:
            return [person]
        else:
            return []
    elif person == tree[0]:
        return [person]
    else:
        for child_tree in tree[1:]:
            result = ancestors(person, child_tree)
            if result:
                return [tree[0]] + result
        return []

# -----------------------------------------------------------------------------
#  Uppgift 6
# -----------------------------------------------------------------------------

# Inget lösningsförslag
