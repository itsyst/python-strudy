
# Tree primitives and example for assignent 4

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
