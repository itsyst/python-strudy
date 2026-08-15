#%%
import math

def pi_func(val: int) -> float:
    """Pi function"""
    var = 0
    loop = 0
    until = val+1

    while loop < until:
        var += (math.factorial(4*val)*(1103 + 26390*val))/(math.factorial(val)**4 * 396**(4*val))
        val -= 1
        loop += 1

    var = 1/(var * ((2*math.sqrt(2))/9801))

    return var

def reverseeach_r(seq: list) -> list:
    if not seq:
        return ""
    curr = seq[0]
    rest_el = seq[1:]
    if not curr:
        return []
        #return reverseeach_r(rest_el)
    if isinstance(seq, str):
        first = seq[-1]
        rest = seq[:-1]
        return first + reverseeach_r(rest)
    #print(f"show: {reverseeach_r(rest_el)}")
    first = [reverseeach_r(curr)]
    rest = reverseeach_r(rest_el)
    print(f"first: {first}")
    print(f"rest: {rest}")
    return first + [rest]

def reverseeach_i(seq: list) -> list:
    lst = []
    for ele in enumerate(seq):
        a_str = ""
        for i in range(len(ele[1])):
            a_str += ele[1][-(i+1)]
        lst.append(a_str)
    return lst

### Uppgift 3a
def is_leaf(tree):
    """ Return true iff tree is a leaf. """
    return not isinstance(tree, list)

def left_tree(tree):
    """ Return the left sub-tree of tree. """
    if not is_leaf(tree):
        return tree[0]

def right_tree(tree):
    """ Return the right sub-tree of tree. """
    if not is_leaf(tree):
        return tree[1]

def tree_apply(fn, tree):
    """ Apply fn to each sub-tree of tree. """
    if is_leaf(tree):
        return tree
    return fn(tree_apply(fn, left_tree(tree)), tree_apply(fn, right_tree(tree)))

###Uppgift 4

def lcs(s1: str, s2: str) -> int:
    pass


if __name__ == "__main__":
    #print(reverseeach_r(["paris", "i", "sirap"]))
    #print(reverseeach_r(["hanna", "leo"]))
    #print(reverseeach_i(["hanna", "leo"]))
    print(tree_apply(lambda x, y: x+y, [[1, 2], 3]))

#%%
