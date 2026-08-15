
def decode(bits, tree):
  return decode_one(bits, tree, tree)
  
def decode_one(bits, tree, current_branch):
  if is_empty_bit_sequence(bits):
    # Your code here
    return "NOT IMPLEMENTED"
  else:
    next_branch = choose_branch(first_bit(bits), current_branch)
    if is_leaf(next_branch):
      return add_symbol(next_branch, decode_one(rest_bit_sequence(bits), tree, tree))
    else:
      return decode_one(rest_bit_sequence(bits), tree, next_branch)
      
def choose_branch(bit, branch):
  if bit_equal(bit, 0):
    return left_branch(branch)
  elif bit_equal(bit, 1):
    return right_branch(branch)
  else:
    raise ValueError("Bad bit")
    
# ----- Primitives for the datatype SYMBOL SEQUENCE -----

def add_symbol(symbol, symbol_sequence):
  "SYMBOL x SYMBOL SEQUENCE -> SYMBOL SEQUENCE"
  return symbol + symbol_sequence
  
def first_symbol(symbol_sequence):
  "SYMBOL SEQUENCE -> SYMBOL"
  return symbol_sequence[0]
  
def rest_symbol_sequence(symbol_sequence):
  "SYMBOL SEQUENCE -> SYMBOL SEQUENCE"
  return symbol_sequence[1:]
  
def the_empty_symbol_sequence():
  "-> SYMBOL SEQUENCE"
  return ''
   
# ----- Primitives for the datatype BIT -----

def bit_equal(bit1, bit2):
  "BIT x BIT -> Truth value"
  return bit1 == bit2
  
# ----- Primitives for the datatype BIT SEQUENCE -----

def is_empty_bit_sequence(bits):
  "BIT SEQUENCE -> Truth value"
  return not bits
  
def first_bit(bits):
  "BIT SEQUENCE -> Binary digit"
  return bits[0]
  
def rest_bit_sequence(bits):
  "BIT SEQUENCE -> Binary digit"
  return bits[1:]
  
# ----- Primitives for the datatype HUFFMAN TREE -----

def left_symbols(tree):
  "HUFFMAN TREE -> SYMBOL SEQUENCE"
  return tree[0]
  
def right_symbols(tree):
  "HUFFMAN TREE -> SYMBOL SEQUENCE"
  return tree[1]
  
def left_branch(tree):
  "HUFFMAN TREE -> HUFFMAN TREE"
  return tree[2]
  
def right_branch(tree):
  "HUFFMAN TREE -> HUFFMAN TREE"
  return tree[3]
  
def is_same_tree(tree1, tree2):
  "HUFFMAN TREE x HUFFMAN TREE -> Truth value"
  return tree1 == tree2
  
def is_leaf(tree):
  "HUFFMAN TREE -> Truth value"
  return isinstance(tree, str)

# ----- Examples -----

ht1 = [['A'], ['B', 'C', 'D', 'E', 'F', 'G', 'H'],  
         'A',
         [['E', 'F', 'G', 'H'], ['B', 'C', 'D'],  
            [['G', 'H'], ['E', 'F'], 
               [['H'], ['G'], 'H', 'G'], 
               [['F'], ['E'], 'F', 'E']],
            [['D', 'C'], ['B'], 
               [['D'], ['C'], 'D', 'C'], 
               'B']]]
               
bs1 = [1,1,1, 0, 1,1,0,1, 0, 1,1,0,0, 0, 1,0,1,1, 0, 1,0,1,0, 1,0,0,0]
