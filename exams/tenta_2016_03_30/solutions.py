### ExempellÃ¶sningar fÃ¶r datortenta i TDDD73 2016-03-30
### Fredrik Heintz 2016-03-30


### Uppgift 1
def rainfall(seq):
    """ Given a sequence of sequences of measurements where each sequence is separated by a negative number return a list of average measurements, one for each sequence."""
    res = []
    count = 0
    total = 0
    for s in seq:
        if s >= 0:
            total += s
            count += 1
        elif count > 0:
            res += [total/count]
            total = 0
            count = 0
    if count > 0:
        res += [total/count]
    return res

assert( rainfall([1, 2, 3]) == [2.0] )
assert( rainfall([2, 2, 2, -1, 3, 3, 3]) == [2.0, 3.0] )
assert( rainfall([1.5, 4, 2, -1, 1, -1]) == [2.5, 1.0] )
assert( rainfall([1.25, 4, 3, -1, 1, -1, 0]) == [2.75, 1.0, 0.0] )
assert( rainfall([-5]) == [] )
assert( rainfall([]) == [] )
assert( rainfall([1, -1, -1, 1]) == [1.0, 1.0] )


### Uppgift 2
def zip_i(seq1, seq2):
    """ Given two sequences return a sequence of tuples containing one element from each sequence."""
    res = []
    for i in range(0, min(len(seq1), len(seq2))):
        res += [(seq1[i], seq2[i])]
    return res

def zip_r(seq1, seq2):
    """ Given two sequences return a sequence of tuples containing one element from each sequence."""
    if seq1 and seq2:
        return [(seq1[0], seq2[0])] + zip_r(seq1[1:], seq2[1:])
    else:
        return []

assert( zip_r([1, 2, 3], ['a', 'b', 'c']) == [(1, 'a'), (2, 'b'), (3, 'c')] )
assert( zip_r([], [1,2,3]) == [] )
assert( zip_r([1,2,3], []) == [] )

assert( zip_i(['c', 3], [8, 'q', 9, 't']) == [('c', 8), (3, 'q')] )
assert( zip_i([], [1,2,3]) == [] )
assert( zip_i([1,2,3], []) == [] )


### Uppgift 3
sum_if = lambda f, p: lambda i, j: sum(map(f, filter(p, [x for x in range(i, j+1)])))

assert( sum_if(lambda x: x*x, lambda x: x%2==1)(0, 5) == 35 )
assert( sum_if(lambda x: x*x, lambda x: x%2==1)(1, 5) == 35 )


### Uppgift 4
def setify(x):
    """ Take a list and construct a set from it, where each element being a list is recursively turned into a set. This effectively removes duplicates as a set may only contain a single instance of each element. """
    return frozenset(map(setify, x)) if isinstance(x, list) else x

def listify(x):
    """ Take a set and construct a list from it, if the set contains sets these are recursively turned into lists. """ 
    return list(map(listify, x)) if isinstance(x, frozenset) else x

unique = lambda seq: listify(setify(seq))

assert( unique([1, 1, 1]) == [1] )
assert( unique([1, 2, 3]) == [1, 2, 3] )
assert( unique([[1], [1], [1]]) == [[1]] )
assert( unique([[2, 1, 2], [1], [1, 1, 1, 1, 2]]) == [[1, 2], [1]] )
assert( unique([[2, 1, [2]], [1], [1, 1, [2, 2, 2, 2], 1, 1, 2]]) == [[1], [1, 2, [2]]] )


### Uppgift 5
def make_graph():
    """ Construct an empty graph. A graph consists of a dictionary mapping nodes to a list of neighbors with weights. All edges are directed. """
    return dict()

def make_directed_graph(nodes=[], edges=[]):
    """ Construct a graph consisting of a set of nodes and directed edges. """
    graph = make_graph()
    add_nodes(graph, nodes)
    add_directed_edges(graph, edges)
    return graph

def make_undirected_graph(nodes=[], edges=[]):
    """ Construct a graph consisting of a set of nodes and undirected edges. """
    graph = make_graph()
    add_nodes(graph, nodes)
    add_undirected_edges(graph, edges)
    return graph

def add_nodes(graph, nodes):
    """ Add nodes to the graph. """
    for n in nodes:
        graph[n] = []  

def add_directed_edge(graph, edge):
    """ Add a directed edge to the graph. """
    (f,t,w) = edge
    if f in graph:
        graph[f].append((t,w))
    else:
        graph[f] = [(t,w)]
    if t not in graph:
        graph[t] = []

def add_directed_edges(graph, edges):
    """ Add directed edges to the graph. """
    for e in edges:
        add_directed_edge(graph, e)

def add_undirected_edges(graph, edges):
    """ Add undirected edges to the graph. An undirected edge is transformed into two directed edges. """
    for (f,t,w) in edges:
        add_directed_edge(graph, (f,t,w))
        add_directed_edge(graph, (t,f,w))

def get_edges(graph):
    """ Get all the edges in the graph. """
    edges = []
    for f in graph:
        for (t,w) in graph[f]:
            edges.append((f,t,w))
    return sorted(edges)

def get_nodes(graph):
    """ Get all the nodes in the graph. """
    nodes = []
    for n in graph:
        nodes.append(n)
    return sorted(nodes)

def get_neighbors(graph, node):
    """ Get all neighbors of a node. """
    return graph[node]

def has_cycle(graph, node, visited=[]):
    """ Return true iff there is a cycle in the graph starting at node. """
    if node in visited:
        return True
    else:
        for (n,w) in get_neighbors(graph, node):
            if has_cycle(graph, n, visited+[node]):
                return True
    return False

g = make_directed_graph(['A', 'B', 'C', 'D', 'E', 'F', 'G'], [('A', 'B', 7), ('A', 'D', 5), ('B', 'C', 8), ('B', 'D', 9), ('B', 'E', 7), ('C', 'E', 5), ('D', 'E', 15), ('D', 'F', 6), ('E', 'F', 8), ('E', 'G', 9), ('F', 'G', 11)])
assert( get_nodes(g) == ['A', 'B', 'C', 'D', 'E', 'F', 'G'] )
assert( get_edges(g) == [('A', 'B', 7), ('A', 'D', 5), ('B', 'C', 8), ('B', 'D', 9), ('B', 'E', 7), ('C', 'E', 5), ('D', 'E', 15), ('D', 'F', 6), ('E', 'F', 8), ('E', 'G', 9), ('F', 'G', 11)] )
assert( get_neighbors(g, 'B') == [('C', 8), ('D', 9), ('E', 7)] )
h = make_graph()
add_undirected_edges(h, get_edges(g))
assert( get_nodes(h) == get_nodes(g) )

assert( not has_cycle(g, 'A') )
assert( has_cycle(h, 'A') )


### Uppgift 6
def mst(edges):
    """ Given a set of weighted edges return the cost of the minimum spanning tree and its edges. """

    def extend_reachable(reachable, f, t):
        """ Given a dictionary mapping nodes to the set of nodes that can be reached from it, extend it with an edge from f to t. """ 
        if t not in reachable[f]:
            for n in reachable[f]:
                if t not in reachable[n]:
                    reachable[n] = sorted(reachable[n] + [t])
            reachable[f] = sorted(reachable[f] + [t])
        
    reachable = dict()
    tree = []
    cost = 0
    used_edges = []
    for (f,t,w) in sorted(edges, key=lambda e: e[2]):
        use_edge = False
        if t not in tree:
            tree.append(t)
            if f in tree:
                reachable[t] = list(reachable[f])
                extend_reachable(reachable, f, t)
                extend_reachable(reachable, t, f)
            else:
                reachable[t] = []
            use_edge = True
        if f not in tree:
            tree.append(f)
            reachable[f] = list(reachable[t])
            extend_reachable(reachable, f, t)
            extend_reachable(reachable, t, f)
            use_edge = True
        if f in tree and t in tree and (t not in reachable[f] and f not in reachable[t]):
            reach_f = list(reachable[f])
            reachable[f] += reachable[t]
            reachable[t] += reach_f
            use_edge = True
            
        if use_edge:
            used_edges.append((f,t,w))
            cost += w
    return cost, used_edges

mst_edges1 = [('A', 'B', 7), ('A', 'D', 5), ('B', 'C', 8), ('B', 'D', 9), ('B', 'E', 7), ('C', 'E', 5), ('D', 'E', 15), ('D', 'F', 6), ('E', 'F', 8), ('E', 'G', 9), ('F', 'G', 11)]
assert( mst(mst_edges1) == (39, [('A', 'D', 5), ('C', 'E', 5), ('D', 'F', 6), ('A', 'B', 7), ('B', 'E', 7), ('E', 'G', 9)]) )
