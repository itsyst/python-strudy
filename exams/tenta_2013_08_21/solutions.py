# encoding: iso-8859-1

# -----------------------------------------------------------------------------
#  Datortentamen i kursen TDDD64 Programmering i Python
#  2013-08-21
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#  Uppgift 1
# -----------------------------------------------------------------------------

def print_calendar(days, start):
    i = 1 - start
    c = 0
    while i <= days:
        if i <= 0:
            print('   ', end='')
        else:
            print(' {:2}'.format(i), end='')
        i += 1
        c += 1
        if c % 7 == 0:
            print()
    if c % 7 != 0:
        print()

# -----------------------------------------------------------------------------
#  Uppgift 2
# -----------------------------------------------------------------------------

def interval_r(seq):
    if not seq[1:]:
        return []
    else:
        return [(seq[0][1], seq[1][0])] + interval_r(seq[1:])

def interval_i(seq):
    res = []
    for i in range(len(seq)-1):
        res.append((seq[i][1], seq[i+1][0]))
    return res

# -----------------------------------------------------------------------------
#  Uppgift 3
# -----------------------------------------------------------------------------

def is_anagram_r(seq1, seq2):
	if not seq1:
		return not seq2
	elif seq1[0] in seq2:
		seq2.remove(seq1[0])
		return is_anagram_r(seq1[1:], seq2)
	else:
		return False
		
def is_anagram_i(seq1, seq2):
	for e in seq1:
		if e in seq2:
			seq2.remove(e)
		else:
			return False
	return not seq2

# -----------------------------------------------------------------------------
#  Uppgift 4
# -----------------------------------------------------------------------------

def analyze(seq, fn):
    if len(seq) <= 1:
        return True
    elif fn(seq[0]) == seq[1]:
        return analyze(seq[1:], fn)
    else:
        return False

def double_odd(seq):
    return analyze(seq, lambda x: x + 1 if x % 2 == 0 else x * 2)

# -----------------------------------------------------------------------------
#  Uppgift 5
# -----------------------------------------------------------------------------

def is_leaf(node):
    return not isinstance(node, list)
    
def node_name(node):
    return node[0]
   
def left_tree(node):
    return node[2]
    
def right_tree(node):
    return node[4]
    
def left_distance(node):
    return node[1]
    
def right_distance(node):
    return node[3]

tree1 = ['a', 7, ['b', 3, 'd', 2, ['e', 1, 'h', 4, 'i']], 4, ['c', 8, 'f', 3, 'g']]

def connected(length, tree):
    if length < 0:
        return False
    elif is_leaf(tree):
        if length == 0:
            return [tree]
        else:
            return False
    else:
        left_road = connected(length - left_distance(tree), left_tree(tree))
        if not left_road:
            right_road = connected(length - right_distance(tree), right_tree(tree))
            if not right_road:
                return False
            else:
                return [node_name(tree)] + right_road
        else:
            return [node_name(tree)] + left_road

# -----------------------------------------------------------------------------
#  Uppgift 6
# -----------------------------------------------------------------------------

from huffman_s import *

def contains_symbol(symbol, symbol_sequence):
  "SYMBOL x SYMBOL SEQUENCE -> Truth value"
  return symbol in symbol_sequence
  
def is_empty_symbol_sequence(seq):
  "SYMBOL SEQUENCE -> Truth value"
  return not seq

def add_bit(bit, bits):
  "Binary digit x BIT SEQUENCE -> BIT SEQUENCE"
  return [bit] + bits

def the_empty_bit_sequence():
  "-> BIT SEQUENCE"
  return []
  
def append_bit_sequence(seq1, seq2):
  "BIT SEQUENCE x BIT SEQUENCE -> BIT SEQUENCE"
  return seq1 + seq2

def decode_one(bits, tree, current_branch):
  if is_empty_bit_sequence(bits):
    if is_same_tree(tree, current_branch):
      return the_empty_symbol_sequence()
    else:
      raise ValueError("Incomplete bit sequence")
  else:
    next_branch = choose_branch(first_bit(bits), current_branch)
    if is_leaf(next_branch):
      return add_symbol(next_branch, decode_one(rest_bit_sequence(bits), tree, tree))
    else:
      return decode_one(rest_bit_sequence(bits), tree, next_branch)

def encode(seq, tree):
  if is_empty_symbol_sequence(seq):
    return the_empty_bit_sequence()
  else:
    return append_bit_sequence(encode_one(first_symbol(seq), tree),
                               encode(rest_symbol_sequence(seq), tree))
                               
def encode_one(symbol, tree):
  if is_leaf(tree):
    return the_empty_bit_sequence()
  elif contains_symbol(symbol, left_symbols(tree)):
    return add_bit(0, encode_one(symbol, left_branch(tree)))
  elif contains_symbol(symbol, right_symbols(tree)):
    return add_bit(1, encode_one(symbol, right_branch(tree)))
  else:
    raise ValueError("Bad symbol")
