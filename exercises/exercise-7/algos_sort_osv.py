# Implementations from the page

# -------------------------
# Selection Sort
# -------------------------
def selection_sort_copy(seq):
    res = []
    seq = list(seq)
    while seq:
        e = min(seq)
        res.append(e)
        seq.remove(e)
    return res

def selection_sort_inplace(seq):
    n = len(seq)
    for bottom in range(n-1):
        minpos = bottom
        for i in range(bottom+1, n):
            if seq[i] < seq[minpos]:
                minpos = i
        seq[bottom], seq[minpos] = seq[minpos], seq[bottom]

# -------------------------
# Insertion Sort
# -------------------------
def insertion_sort_copy(seq):
    res = []
    for e in seq:
        i = 0
        while i < len(res) and res[i] < e:
            i += 1
        res.insert(i, e)
    return res

def insertion_sort_inplace(seq):
    for i in range(1, len(seq)):
        item = seq[i]
        hole = i
        while hole > 0 and seq[hole-1] > item:
            seq[hole] = seq[hole-1]
            hole -= 1
        seq[hole] = item

# -------------------------
# Anagrams
# -------------------------
def anagrams(s):
    if s == "":
        return [s]
    ans = []
    first = s[0]
    rest = s[1:]
    for w in anagrams(rest):
        for pos in range(len(w)+1):
            ans.append(w[:pos] + first + w[pos:])
    return ans

# -------------------------
# Tower of Hanoi
# -------------------------
def move_tower(n, source, dest, temp, moves=None):
    if moves is None:
        moves = []
    if n == 1:
        moves.append((source, dest))
    else:
        move_tower(n-1, source, temp, dest, moves)
        move_tower(1, source, dest, temp, moves)
        move_tower(n-1, temp, dest, source, moves)
    return moves

# -------------------------
# Binary Search Tree representation
# -------------------------
def is_empty_tree(tree):
    return isinstance(tree, list) and not tree

def is_leaf(tree):
    return isinstance(tree, int)

def create_tree(left_subtree, key, right_subtree):
    return [left_subtree, key, right_subtree]

def left_subtree(tree):
    return tree[0]

def key(tree):
    if is_leaf(tree):
        return tree
    return tree[1]

def right_subtree(tree):
    return tree[2]

# -------------------------
# BST Search
# -------------------------
def search(tree, x):
    if is_empty_tree(tree):
        return False
    elif is_leaf(tree):
        return key(tree) == x
    elif key(tree) < x:
        return search(left_subtree(tree), x)
    elif key(tree) > x:
        return search(right_subtree(tree), x)
    else:
        return True

# -------------------------
# TAKE n and print
# -------------------------
def take_and_print():
    n = input("Enter a number: ")
    
    product =0
    for k in range(1,12):
        product += k* int(n)
    return product

# -------------------------
# Tests
# -------------------------
if __name__ == '__main__':
    print("Selection sort copy: [5,3,8,1] -> ", selection_sort_copy([5,3,8,1]))
    s = [5,3,8,1]
    selection_sort_inplace(s)
    print("Selection sort inplace:", s)

    print("Insertion sort copy: [5,3,8,1] -> ", insertion_sort_copy([5,3,8,1]))
    s = [5,3,8,1]
    insertion_sort_inplace(s)
    print("Insertion sort inplace:", s)

    print("Anagrams of 'abc': ->", anagrams('abc'))

    print("Hanoi (3 disks):", move_tower(3, 'A', 'C', 'B'))

    tree = create_tree(
        create_tree(1, 3, create_tree(4, 6, 7)),
        8,
        create_tree([], 10, create_tree(13, 14, []))
    )
    print("Search 6:", search(tree, 6))
    print("Search 11:", search(tree, 11))
    
    print(take_and_print())
