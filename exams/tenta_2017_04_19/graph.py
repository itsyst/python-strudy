### graph.py
### Fredrik Heintz 2016-08-16

def make_graph():
    """
    Construct an empty graph.
    A graph consists of a dictionary mapping nodes to a list of neighbors.
    All edges are directed.
    """
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
    (f,t) = edge
    if f in graph:
        graph[f].append(t)
    else:
        graph[f] = [t]
    if t not in graph:
        graph[t] = []

def add_directed_edges(graph, edges):
    """ Add directed edges to the graph. """
    for e in edges:
        add_directed_edge(graph, e)

def add_undirected_edges(graph, edges):
    """
    Add undirected edges to the graph.
    An undirected edge is transformed into two directed edges.
    """
    for (f,t) in edges:
        add_directed_edge(graph, (f,t))
        add_directed_edge(graph, (t,f))

def get_edges(graph):
    """ Get all the edges in the graph. """
    edges = []
    for f in graph:
        for t in graph[f]:
            edges.append((f,t))
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
