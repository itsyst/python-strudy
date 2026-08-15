# Example solutions to the exam 2017-04-19
# Erik Hansson / Fredrik Heintz 2017-04-18

def analyze_data(data_points:list) -> dict:
    """
    Extracting the amount of data points for one type of data and extracts
    the minimum and the maximum for each type of data
    :param data_points: All the data points
    :return: The analysis
    """
    stats = {}
    for dp in data_points:
        if dp[0] not in stats:
            stats[dp[0]] = [1, dp[1], dp[1]]
        else:
            stats[dp[0]][0] += 1
            stats[dp[0]][1] = min(stats[dp[0]][1], dp[1])
            stats[dp[0]][2] = max(stats[dp[0]][2], dp[1])
    return stats


def test_assignment_1() -> None:
    """
    Tests so that the first assignment works according to the examples
    :return: None
    """
    assert analyze_data([('a', -1), ('a', 1)]) == { 'a': [2, -1, 1] }
    assert analyze_data([('a', 2), ('b', 0), ('a', 6), ('c', 0), ('b', 1)]) == \
        { 'a': [2, 2, 6], 'b': [2, 0, 1], 'c': [1, 0, 0] }


# Assignment 2
def merge_r(ll:list, rl:list) -> list:
    """
    Merges two lists recursively
    :param ll, rl: The two sequences that is to be merged
    :return: The merged list
    """
    if not ll:
        return rl
    elif not rl:
        return ll
    elif rl[0] < ll[0]:
        return [rl[0]] + merge_r(ll, rl[1:])
    else:
        return [ll[0]] + merge_r(ll[1:], rl)


def merge_i(ll:list, rl:list) -> list:
    """
    Merges two lists iteratively
    :param ll, rl: The two sequences that is to be merged
    :return: The merged list
    """
    res = []
    li = 0
    ri = 0
    while li < len(ll) and ri < len(rl):
        if rl[ri] < ll[li]:
            res.append(rl[ri])
            ri += 1
        else:
            res.append(ll[li])
            li += 1
    res.extend(rl[ri:])
    res.extend(ll[li:])
    return res


def test_assignment_2()->None:
    """
    Tests so that the second assignment works according to the examples
    :return: None
    """
    assert merge_r([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_r([2, 4, 6], [1, 3, 5]) == [1, 2, 3, 4, 5, 6]
    assert merge_r([1, 2], [1, 2]) == [1, 1, 2, 2]
    assert merge_i([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_i([2, 4, 6], [1, 3, 5]) == [1, 2, 3, 4, 5, 6]
    assert merge_i([1, 2], [1, 2]) == [1, 1, 2, 2]


# Assignment 3 a)
def pred_comp(p, t, f):
    """
    Generates a function that returns t(x) if p(x) is true else f(x)
    :param p: The predicate function
    :param t, f: The functions calculating the actual value
    :type p, t, f: functions taking one parameter as input
    :return: Unary function
    """
    return lambda x: t(x) if p(x) else f(x)


# Assignemnt 3 b)
def safe_div(numerator, denominator):
    """
    Divides two numbers and returns 0 instead of division by zero if
    the denominator is 0
    :param numerator: the numerator
    :param denominator: the denominator
    :type numerator, denominator: int or float
    :return: numerator/denominator if denominator != 0 else numerator
    """
    return pred_comp(lambda div: div[1] != 0, lambda div: div[0]/div[1],
                     lambda div: 0)((numerator, denominator))


def test_assignment_3() -> None:
    """
    Tests so that the third assignment works according to the examples
    :return: None
    """
    assert pred_comp(lambda x: x > 0, lambda x: x, lambda x: -x)(-4) == 4
    assert pred_comp(lambda x: x < 0, lambda x: x, lambda x: -x)(-4) == -4
    assert safe_div(10, 5) == 2
    assert safe_div(10, 0) == 0


# Assignment 4
def remove_duplicates(seq:list) -> list:
    """
    Removes all the duplicates that are following after each other
    :param seq: A list containing anything
    """
    # Make a shallow copy of the list
    # Note that a shallow copy is ok since only the outer list is
    # modified in each call
    seq = seq[:]

    # Handle first element specifically since it doesn't have a
    # previous element
    if isinstance(seq[0], list):
        seq[0] = remove_duplicates(seq[0])

    # Handle the rest
    i = 1
    while i < len(seq):
        # Recursively handle nestled lists
        if isinstance(seq[i], list):
            seq[i] = remove_duplicates(seq[i])
        if seq[i-1] == seq[i]:
            del seq[i]
        else:
            i += 1
    return seq


def test_assignment_4() -> None:
    """
    Tests so that the fourth assignment works according to the examples
    :return: None
    """
    assert remove_duplicates([1, 1, 1]) == [1]
    assert remove_duplicates([[1], [1], [1]]) == [[1]]
    assert remove_duplicates([[2, 1, 2], [2], [1, 1, 1, 1, 2]]) == \
        [[2, 1, 2], [2], [1, 2]]
    assert remove_duplicates([2, [2], 2, [2]]) == [2, [2], 2, [2]]
    assert remove_duplicates([[1, 1, [2, 2, 2, 2]], [1, 1, [2]]]) == [[1, [2]]]


# Assignment 5
def make_priority_queue() -> list:
    """
    Create an empty priority queue
    :return: empty priority queue
    """
    return []


def length(pq:list):
    """
    Gets the length of the priority queue
    :param pq: the priority queue
    :return: length of the priority queue
    """
    return len(pq)


def front(pq:list):
    """
    Gets the first element in the priority queue
    :param pq: the priority queue
    :return: the element in the priority queue
    """
    return pq[0]


def back(pq:list):
    """
    Gets the last element in the priority queue
    :param pq: the priority queue
    :return: the last element in the priority queue
    """
    return pq[-1]


def push_d(pq:list, elem) -> list:
    """
    Adds an element to the priority queue destructively
    :param pq: the priority queue
    :param elem: the element to add
    :return: the priority queue
    """
    pq.append(elem)
    pq.sort(reverse=True)
    return pq


def pop_d(pq:list) -> list:
    """
    Removes the first element of the priority queue destructively
    :param pq: the priority queue
    :return: the priority queue
    """
    del pq[0]
    return pq


def push_f(pq:list, elem) -> list:
    """
    Adds an element to the priority queue
    :param pq: the priority queue
    :param elem: the element to add
    :return: the priority queue
    """
    return sorted(pq + [elem], reverse=True)


def pop_f(pq:list) -> list:
    """
    Removes the first element of the priority queue
    :param pq: the priority queue
    :return: the priority queue
    """
    return pq[1:]


def test_assignment_5() -> None:
    """
    Tests so that the fifth assignment works according to the examples
    :return: None
    """
    pq = make_priority_queue()
    pq1 = push_d(pq, 1)
    assert length(pq) == 1
    assert length(pq1) == 1
    # Only works due to the selected representation
    assert push_d(pq, 2) == [2, 1]
    assert front(pq) == 2
    assert back(pq) == 1
    # Only works due to the selected representation
    assert pop_d(pq) == [1]
    assert front(pq) == 1
    # Only works due to the selected representation
    assert pop_d(pq) == []
    pq = make_priority_queue()
    pq1 = push_f(pq, 1)
    assert length(pq) == 0
    assert length(pq1) == 1
    pq2 = push_f(pq1, 2)
    assert front(pq2) == 2
    assert back(pq2) == 1
    pq3 = pop_f(pq2)
    assert front(pq3) == 1
    # Only works due to the selected representation
    assert pop_d(pq3) == []



# Assignment 6
import graph
from functools import reduce


def topsort(g) -> list:
    """
    Makes a toplogical sorting of a DAG (directed acyclic graph)
    :param g: the graph
    :type g: a graph as represented in the graph module
    :return: A topologically sorted list of nodes
    """
    # Finds all nodes that doesn't have an incomming edge
    get_non_blocked_nodes = lambda edges, nodes: \
                            [node for node in nodes if not reduce(
                                lambda rarg, larg: rarg or larg,
                                map(lambda edge: node == edge[1], edges),
                                False
                            )]

    # Start with all edges and nodes in the graph
    remaining_edges = graph.get_edges(g)
    remaining_nodes = graph.get_nodes(g)
    res = []
    free_nodes = sorted(get_non_blocked_nodes(remaining_edges, remaining_nodes))
    # Remove all the nodes that doesn't have an incomming edge
    remaining_nodes = list(filter(lambda node: node not in free_nodes,
                                  remaining_nodes))

    while free_nodes:
        res.append(free_nodes[0])
        # Remove all edges from the selected node
        remaining_edges = list(filter(lambda edge: edge[0] != res[-1],
                                      remaining_edges))
        # Find all nodes that are free now
        update_with = get_non_blocked_nodes(remaining_edges, remaining_nodes)
        # Remove them from the remaining nodes
        remaining_nodes = list(filter(lambda node: node not in update_with,
                                      remaining_nodes))
        # Update the free nodes
        free_nodes = sorted(free_nodes[1:] + update_with)

    if remaining_edges:
        raise Exception("Not a DAG")
    else:
        return res


def test_assignment_6() -> None:
    """
    Tests so that the sixth assignment works according to the examples
    :return: None
    """
    g = graph.make_directed_graph(['A', 'B', 'C', 'D', 'E', 'F', 'G'],
                                  [('A', 'B'), ('A', 'D'), ('B', 'C'),
                                   ('D', 'B'), ('E', 'B'), ('E', 'C'),
                                   ('D', 'E'), ('D', 'F'), ('E', 'F'),
                                   ('E', 'G'), ('F', 'G')])
    assert topsort(g) == ['A', 'D', 'E', 'B', 'C', 'F', 'G']


if __name__ == "__main__":
    test_assignment_1()
    test_assignment_2()
    test_assignment_3()
    test_assignment_4()
    test_assignment_5()
    test_assignment_6()
