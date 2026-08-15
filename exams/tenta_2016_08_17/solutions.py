### ExempellÃ¶sningar fÃ¶r datortenta i TDDD73 2016-08-17

### Uppgift 1
def expand(mem, msg):
    """
    Given two lists generate a new string from msg by replacing all integers
    with the correspondingly indexed strings in mem.
    """
    res = ""
    for s in msg:
        if isinstance(s, int):
            res += mem[s]
        else:
            res += s
    return res

mem1 = [" ", "att", "lycka", "tenta", "till", "pÃ¥", "Ã¤r"]
assert expand(mem1, [2, 0, 6, 0, 1, 0, 3]) == "lycka Ã¤r att tenta"
assert expand(mem1, [2, 0, 4, 0, 5, 0, 3, "n"]) == "lycka till pÃ¥ tentan"
assert mem1 == [" ", "att", "lycka", "tenta", "till", "pÃ¥", "Ã¤r"]
assert expand([], ['abc']) == 'abc'
assert expand(mem1, []) == ''
msg = [2, '!']
assert expand(mem1, msg) == 'lycka!'
assert msg == [2, '!']


### Uppgift 2
def interleave_i(seq1, seq2):
    """
    Combines two indexable containers by interleaving them.
    """
    res = []
    last_index = min(len(seq1), len(seq2))
    for i in range(last_index):
        res += [seq1[i], seq2[i]]
    return res + seq1[last_index:] + seq2[last_index:]

assert interleave_i([], []) == []
assert interleave_i([], [1, 2, 3]) == [1, 2, 3]
assert interleave_i(['a'], [1, 2, 3]) == ['a', 1, 2, 3]
assert interleave_i(['a', 'b'], [1, 2, 3]) == ['a', 1, 'b', 2, 3]
assert interleave_i(['a', 'b', 'c'], [1, 2, 3]) == ['a', 1, 'b', 2, 'c', 3]
assert interleave_i(['a', 'b', 'c'], [1, 2]) == ['a', 1, 'b', 2, 'c']
assert interleave_i(['a', 'b', 'c'], [1]) == ['a', 1, 'b', 'c']
assert interleave_i(['a', 'b', 'c'], []) == ['a', 'b', 'c']
seq1 = [1, 3, 5]
assert interleave_i(seq1, seq1) == [1, 1, 3, 3, 5, 5]
assert seq1 == [1, 3, 5]

def interleave_r(seq1, seq2):
    """
    Combines two indexable containers by interleaving them.
    """
    if seq1 and seq2:
        return [seq1[0], seq2[0]] + interleave_r(seq1[1:], seq2[1:])
    else:
        return seq1 + seq2

assert interleave_r([], []) == []
assert interleave_r([], [1, 2, 3]) == [1, 2, 3]
assert interleave_r(['a'], [1, 2, 3]) == ['a', 1, 2, 3]
assert interleave_r(['a', 'b'], [1, 2, 3]) == ['a', 1, 'b', 2, 3]
assert interleave_r(['a', 'b', 'c'], [1, 2, 3]) == ['a', 1, 'b', 2, 'c', 3]
assert interleave_r(['a', 'b', 'c'], [1, 2]) == ['a', 1, 'b', 2, 'c']
assert interleave_r(['a', 'b', 'c'], [1]) == ['a', 1, 'b', 'c']
assert interleave_r(['a', 'b', 'c'], []) == ['a', 'b', 'c']
seq1 = [1, 3, 5]
assert interleave_r(seq1, seq1) == [1, 1, 3, 3, 5, 5]
assert seq1 == [1, 3, 5]



### Uppgift 3a
def reduce(fn, seq):
    """
    Reduces an indexable container of elements.
    :param seq: A none empty container where elements can be accessed through
    index
    """
    if not seq:
        # Undefined behaviour returning None and throwing errors is
        # acceptable behaviour as well as ignoring this case
        return None
    elif len(seq) == 1:
        return seq[0]
    else:
        return fn(seq[0], reduce(fn, seq[1:]))

assert reduce(lambda x,y: x+y, [47]) == 47
assert reduce(lambda x,y: x*y, [47, 11]) == 517
assert reduce(lambda x,y: x+y, [47, 11, 42, 13]) == 113
reduce_seq = [47, 11, 42, 13]
assert reduce(lambda x,y: x+y, reduce_seq) == 113
assert reduce_seq == [47, 11, 42, 13]


### Uppgift 3b
reduce_if = lambda f, p: lambda seq: reduce(f, list(filter(p, seq)))

assert reduce_if(lambda x, y: x+y, lambda x: x%2 == 1)(range(5)) == 4
assert reduce_if(lambda x, y: x+y, lambda x: x%2 == 0)([0]) == 0



### Uppgift 4
def sum_all(seq):
    """
    Take a list that may contain lists and return the sum of all numbers.
    """
    if not seq:
        return 0
    elif isinstance(seq[0], list):
        return sum_all(seq[0]) + sum_all(seq[1:])
    else:
        return seq[0] + sum_all(seq[1:])

assert sum_all([]) == 0
assert sum_all([1, 1, 1]) == 3
assert sum_all([[1], [1], [1]]) == 3
assert sum_all([[1], [[1], [[1]]]]) == 3
random_ints = [[2, 1, 2], [1], [1, 1, 1, 1, 2]]
assert sum_all(random_ints) == 12
assert random_ints == [[2, 1, 2], [1], [1, 1, 1, 1, 2]]
assert sum_all([[2, 1, [2]], [1], [1, 1, [2, 2, 2, 2], 1, 1, 2]]) == 20



### Uppgift 5
def make_deque():
    """
    Create an empty double ended queue (deque).
    A double ended queue is represented as a list of elements.
    """
    return list()

def length(deque):
    """ Return the length of the deque. """
    return len(deque)

def front(deque):
    """ Return the first element in the deque. """
    if ( length(deque) > 0 ):
        return deque[0]
    else:
        return None

def back(deque):
    """ Return the last element in the deque. """
    if ( length(deque) > 0 ):
        return deque[-1]
    else:
        return None

def push_front_d(deque, elt):
    """
    Add an element to the front of the deque destructively.
    Return the updated deque.
    """
    deque.insert(0, elt)
    return deque

def pop_front_d(deque):
    """
    Remove the first element of the deque destructively.
    Return the updated deque.
    """
    if length(deque) > 0:
        deque.pop(0)
    return deque

def push_back_d(deque, elt):
    """
    Add an element to the end of the deque destructively.
    Return the updated deque.
    """
    deque.append(elt)
    return deque

def pop_back_d(deque):
    """
    Remove the last element of the deque destructively.
    Return the updated deque.
    """
    if length(deque) > 0:
        deque.pop()
    return deque

def push_front_f(deque, elt):
    """
    Add an element to the front of the deque functionally.
    Return the new deque.
    """
    return push_front_d(list(deque), elt)

def pop_front_f(deque):
    """
    Remove the first element of the deque functionally.
    Return the new deque.
    """
    return pop_front_d(list(deque))

def push_back_f(deque, elt):
    """
    Add an element to the end of the deque functionally.
    Return the new deque.
    """
    return push_back_d(list(deque), elt)

def pop_back_f(deque):
    """
    Remove the last element of the deque functionally.
    Return the new deque.
    """
    return pop_back_d(list(deque))

q = make_deque()
assert length(q) == 0
q1 = push_front_d(q, 1)
assert q == q1
assert length(q) == 1
q2 = push_back_d(q, 2)
assert q == q2
assert length(q) == 2
assert front(q) == 1
assert back(q) == 2
q3 = pop_front_d(q)
assert q == q3
assert front(q) == 2
q4 = pop_back_d(q)
assert q == q4
assert length(q) == 0

q = make_deque()
assert length(q) == 0
q1 = push_front_f(q, 1)
assert length(q) == 0
assert length(q1) == 1
q2 = push_back_f(q1, 2)
assert length(q) == 0
assert length(q1) == 1
assert length(q2) == 2
assert front(q2) == 1
assert back(q2) == 2
q3 = pop_front_f(q2)
assert length(q) == 0
assert length(q1) == 1
assert length(q2) == 2
assert front(q3) == 2
q4 = pop_back_f(q3)
assert length(q) == 0
assert length(q1) == 1
assert length(q2) == 2
assert front(q3) == 2
assert length(q4) == 0



### Uppgift 6
from graph import *
def bfs(graph, start, goal):
    """
    Given an unweighted graph, return the length of the shortest path
    to the goal node.
    """
    deque = make_deque()
    push_back_d(deque, (start, 0))
    visited = [start]
    while length(deque) > 0:
        node, dist = front(deque)
        pop_front_d(deque)
        visited.append(node)
        if node == goal:
            return dist
        for neighbor in get_neighbors(graph, node):
            if not neighbor in visited:
                push_back_d(deque, (neighbor, dist+1))
    return None

g = make_undirected_graph(['A', 'B', 'C', 'D', 'E', 'F', 'G'],
                          [('A', 'B'), ('A', 'D'), ('B', 'C'), ('B', 'D'),
                           ('B', 'E'), ('C', 'E'), ('D', 'E'), ('D', 'F'),
                           ('E', 'F'), ('E', 'G'), ('F', 'G')])
assert bfs(g, 'A', 'A') == 0
assert bfs(g, 'A', 'B') == 1
assert bfs(g, 'A', 'C') == 2
assert bfs(g, 'A', 'D') == 1
assert bfs(g, 'A', 'E') == 2
assert bfs(g, 'A', 'F') == 2
assert bfs(g, 'A', 'G') == 3
assert bfs(g, 'B', 'A') == 1
assert bfs(g, 'B', 'B') == 0
assert bfs(g, 'B', 'C') == 1
assert bfs(g, 'B', 'D') == 1
assert bfs(g, 'B', 'E') == 1
assert bfs(g, 'B', 'F') == 2
assert bfs(g, 'B', 'G') == 2
assert bfs(g, 'E', 'A') == 2
assert bfs(g, 'E', 'B') == 1
assert bfs(g, 'E', 'C') == 1
assert bfs(g, 'E', 'D') == 1
assert bfs(g, 'E', 'E') == 0
assert bfs(g, 'E', 'F') == 1
assert bfs(g, 'E', 'G') == 1


def bfs_r(graph, start, goal, visited = []):
    """
    Given an unweighted graph, return the length of the shortest path
    to the goal node.
    This is worse than the bfs solution since python does not use tail recursion
    """
    def bfs(queue, visited):
        if length(queue) > 0:
            node, dist = front(queue)
            pop_front_d(queue)
            if node == goal:
                return dist

            return bfs(queue + list(map(lambda n: (n, dist+1),
                                        filter(lambda _node: _node not in visited,
                                               get_neighbors(graph, node))
                                    )),
                       [node] + visited
                   )
        return None
    return bfs([(start, 0)], [])

g = make_undirected_graph(['A', 'B', 'C', 'D', 'E', 'F', 'G'],
                          [('A', 'B'), ('A', 'D'), ('B', 'C'), ('B', 'D'),
                           ('B', 'E'), ('C', 'E'), ('D', 'E'), ('D', 'F'),
                           ('E', 'F'), ('E', 'G'), ('F', 'G')])
assert bfs_r(g, 'A', 'A') == 0
assert bfs_r(g, 'A', 'B') == 1
assert bfs_r(g, 'A', 'C') == 2
assert bfs_r(g, 'A', 'D') == 1
assert bfs_r(g, 'A', 'E') == 2
assert bfs_r(g, 'A', 'F') == 2
assert bfs_r(g, 'A', 'G') == 3
assert bfs_r(g, 'B', 'A') == 1
assert bfs_r(g, 'B', 'B') == 0
assert bfs_r(g, 'B', 'C') == 1
assert bfs_r(g, 'B', 'D') == 1
assert bfs_r(g, 'B', 'E') == 1
assert bfs_r(g, 'B', 'F') == 2
assert bfs_r(g, 'B', 'G') == 2
assert bfs_r(g, 'E', 'A') == 2
assert bfs_r(g, 'E', 'B') == 1
assert bfs_r(g, 'E', 'C') == 1
assert bfs_r(g, 'E', 'D') == 1
assert bfs_r(g, 'E', 'E') == 0
assert bfs_r(g, 'E', 'F') == 1
assert bfs_r(g, 'E', 'G') == 1

