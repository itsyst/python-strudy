# ExempellÃ¶sningar till datortenta i TDDD73 2016-01-12 fÃ¶rmiddag


### Uppgift 1
import math

def pi(max_k):
    """ Approximate pi using the first max_k+1 terms of Ramanujans series. Works for max_k up to 1228. """
    ans = 0
    for k in range(max_k+1):
        ans += math.factorial(4*k)*(1103+26390*k)/(math.factorial(k)**4 * 396**(4*k))
    return 9801/(2*math.sqrt(2)*ans)


### Uppgift 2
def reverseeach_r(seq):
    """ Reverse each string in the sequence seq recursively. """
    if not seq:
        return []
    else:
        return [seq[0][::-1]] + reverseeach_r(seq[1:])

def reverseeach_i(seq):
    """ Reverse each string in the sequence seq iteratively. """
    res = []
    for i in seq:
        res.append(i[::-1])
    return res

    
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
    else:
        return fn(tree_apply(fn, left_tree(tree)), tree_apply(fn, right_tree(tree)))

### Uppgift 3b
def second_smallest(seq):
    """ Returns the second smallest element in a list. """
    
    smallest = tree_apply(min, seq)

    def smallest_larger_than_smallest(x, y):
        """ Given two values, return the smallest of them larger than the value of the variable smallest. If both elements are equal to smallest return it. """
        res = x
        if x > smallest:
            if y > smallest:
                return min(x,y)
            else:
                return x
        else:
            return y
            
    return tree_apply(smallest_larger_than_smallest, seq)

    
### Uppgift 4    
def lcs(s1, s2):
    """ Compute the longest common subsequence of two strings s1 and s2. """
    if len(s1) == 0 or len(s2) == 0:
        return 0
    else:
        if s1[0] == s2[0]:
            return 1+lcs(s1[1:], s2[1:])
        else:
            return max(lcs(s1[1:], s2), lcs(s1, s2[1:]))


### Uppgift 5            
"""
Solution from Jonatan StÃ¶dman

A trie is represented as a graph where each node is a pair of a
boolean that specifies if a word ends at this node and a dictionary
that contains references to the node's children.

The root node has no letter (no edge leads to root) so that words
starting with any letter may be a child of the root.

A node does not contain its own letter value, these are obtained
through the edges to the nodes.
"""

def create_trie():
    """
    Create an empty trie.

    Returns:
        A trie object.
    """
    return [False, {}]


def add_word(trie, word):
    """
    Add a word to a trie.
    Adding an empty word ('') has no effect.
    
    Args:
        trie: a trie object
        word: a string to be added to the trie

    Returns:
        The original trie object which has been updated with the new word.
    """
    if not word:
        return trie
    # Separate the first character from the rest
    head, tail = word[0], word[1:]
    # Select the correct existing branch or create it if missing
    branch = trie[1].setdefault(head, create_trie())
    # If the word ends, mark that last node as being the end of a word
    if len(word) == 1:
        branch[0] = True
    # Add the remaining characters of the word
    add_word(branch, tail)
    return trie


def word_in_trie(trie, word):
    """
    Determine whether a word is in a trie.

    Args:
        trie: a trie object
        word: the word to search for as a string

    Returns:
        True | False
    """
    # Empty words are not words.
    if not word:
        return False
    # Get the branch for the next character in the word.
    branch = trie[1].get(word[0], None)
    # If no such branch was found, then the word is not in the trie
    if branch is None:
        return False
    # If this is the last letter of the word, return whether this node
    # is the end of a word.
    if len(word) == 1:
        return branch[0]
    # Keep following the graph until the end of the word
    return word_in_trie(branch, word[1:])


def find_all_matches(trie, prefix):
    """
    Search a trie for all words that begin with `prefix`.
    An empty prefix ( '' ) matches all words.

    Args:
        trie: a trie object
        prefix: the leading characters of the words that are to be matched
            as a string.

    Returns:
        A list of words as strings.
    """
    result = []
    # Match this node if a word ends here and there is no prefix.
    if trie[0] is True and prefix == '':
        result.append('')
    # Match the branch of next character.
    if prefix and prefix[0] in trie[1]:
        result += [prefix[0] + match
                   for match
                   in find_all_matches(trie[1][prefix[0]], prefix[1:])]
    # Match all branches if there is no prefix.
    if not prefix:
        for char, branch in trie[1].items():
            result += [char + matches
                       for matches
                       in find_all_matches(branch, '')]
    return result


### Uppgift 6a
def permutations_6a(seq):
    """ Return the list of all permutations of the elements in the list seq. """
    if len(seq) <= 1:
        return [seq]
    else:
        ans = []
        for perm in permutations_6a(seq[1:]):
            for i in range(len(seq)):
                ans.append(perm[:i] + [seq[0]] + perm[i:])
        return ans

### Uppgift 6b
def permutations(seq):
    """ Return the list of all permutations, including all permutations of sublists, of the elements in a list. """
    
    def extend_permutations_with_element(seq, element):
        """ Given a list and an element, compute all permutations of the list and add the element in every position in each of the permutations. """
        res = []
        for p in permutations(seq[1:]):
            for i in range(len(seq)):
                res.append(p[:i] + [element] + p[i:])
        return res
        
    if len(seq) <= 1:
        return [seq]
    elif isinstance(seq[0], list):
        res = []
        for perm in permutations(seq[0]):
            res += extend_permutations_with_element(seq, perm)
        return res
    else:
        return extend_permutations_with_element(seq, seq[0])
