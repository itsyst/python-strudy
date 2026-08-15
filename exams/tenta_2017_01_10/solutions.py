### Example solutions for TDDD73 exam 2017-01-10em


### Uppgift 1
def find_closest(seq1, seq2):
    """
    Create a list containing for each number n in seq1 the largest
    number in seq2 with the smallest absolute difference compared to n.
    """
    res = []
    for e in seq1:
        best_match = seq2[0]
        for m in seq2[1:]:
            if abs(e-m) < abs(e-best_match) or (abs(e-m) == abs(e-best_match) and m > best_match):
                best_match = m
        res.append(best_match)
    return res

assert find_closest([1, 2, 4], [1, 3]) == [1, 3, 3]
assert find_closest([1, 2, 4], [-5, 15, -2]) == [-2, -2, -2]

assert find_closest([-1, -2, -4], [-5, 15, -2]) == [-2, -2, -5]
assert find_closest([-1, -2, -4, 6, 18], [1]) == [1, 1, 1, 1, 1]
assert find_closest([], []) == []


### Uppgift 2
def split_i(seq, threshold):
    """ 
    Given a list and a threshold, return three lists,
    one with all smaller elements, one with all elements equal
    to the threshold and one with all larger elements.
    Iterative approach.
    """
    below = []
    on = []
    above = []
    for e in seq:
        if e < threshold:
            below.append(e)
        elif e == threshold:
            on.append(e)
        else:
            above.append(e)
    return below, on, above

assert split_i([5, 2, 1, 7, 2, 5], 0) == ([], [], [5, 2, 1, 7, 2, 5])
assert split_i([5, 2, 1, 7, 2, 5], 1) == ([], [1], [5, 2, 7, 2, 5])
assert split_i([5, 2, 1, 7, 2, 5], 2) == ([1], [2, 2], [5, 7, 5])
assert split_i([5, 2, 1, 7, 2, 5], 3) == ([2, 1, 2], [], [5, 7, 5])
assert split_i([5, 2, 1, 7, 2, 5], 5) == ([2, 1, 2], [5, 5], [7])
assert split_i([5, 2, 1, 7, 2, 5], 7) == ([5, 2, 1, 2, 5], [7], [])
assert split_i([5, 2, 1, 7, 2, 5], 8) == ([5, 2, 1, 7, 2, 5], [], [])
assert split_i([], 2) == ([], [], [])

def split_r(seq, threshold):
    """ 
    Given a list and a threshold, return three lists,
    one with all smaller elements, one with all elements equal
    to the threshold and one with all larger elements.
    Recursive approach.
    """
    if not seq:
        return [], [], []
    else:
        below_rest, on_rest, above_rest = split_r(seq[1:], threshold)
        if seq[0] < threshold:
            return [seq[0]] + below_rest, on_rest, above_rest
        elif seq[0] == threshold:
            return below_rest, [seq[0]] + on_rest, above_rest
        else:
            return below_rest, on_rest, [seq[0]] + above_rest

assert split_r([5, 2, 1, 7, 2, 5], 0) == ([], [], [5, 2, 1, 7, 2, 5])
assert split_r([5, 2, 1, 7, 2, 5], 1) == ([], [1], [5, 2, 7, 2, 5])
assert split_r([5, 2, 1, 7, 2, 5], 2) == ([1], [2, 2], [5, 7, 5])
assert split_r([5, 2, 1, 7, 2, 5], 3) == ([2, 1, 2], [], [5, 7, 5])
assert split_r([5, 2, 1, 7, 2, 5], 5) == ([2, 1, 2], [5, 5], [7])
assert split_r([5, 2, 1, 7, 2, 5], 7) == ([5, 2, 1, 2, 5], [7], [])
assert split_r([5, 2, 1, 7, 2, 5], 8) == ([5, 2, 1, 7, 2, 5], [], [])
assert split_r([], 2) == ([], [], [])


### Uppgift 3
def sum_nth(seq, n):
    """ Sum every nth element in seq, where seq may contain arbitrarily nested lists. """
    def sum_nth_helper(seq, n, count):
        if not seq:
            return 0, count
        elif isinstance(seq[0], list):
            sum_first, count_first = sum_nth_helper(seq[0], n, count)
            sum_rest, count_rest = sum_nth_helper(seq[1:], n, count_first)
            return sum_first+sum_rest, count_rest
        elif count == n:
            sum_rest, count_rest = sum_nth_helper(seq[1:], n, 1)
            return seq[0]+sum_rest, count_rest
        else:
            return sum_nth_helper(seq[1:], n, count + 1)

    return sum_nth_helper(seq, n, 1)[0]

assert sum_nth([1, 2, 3, 4, 5], 1) == 15
assert sum_nth([1, 2, 3, 4, 5], 2) == 6
assert sum_nth([1, 2, 3, 4, 5], 3) == 3
assert sum_nth([1, 2, 3, 4, 5], 6) == 0
assert sum_nth([1, [2, 3], 4, [5]], 2) == 6
assert sum_nth([1, [[2, [3]], 4], [5]], 2) == 6


### Uppgift 4a
def derivate(f, h):
    """
    Given a function f and an offset h, return the a function that
    numerically derivates f based on the offset h.
    """
    return lambda x: (f(x+h)-f(x-h))/(2.0*h)

assert abs(derivate(lambda x: 2*x, 0.0001)(2) - 2) < 0.0001
assert abs(derivate(lambda x: 2*x*x*x, 0.0001)(2) - 24) < 0.0001

### Uppgift 4b
derivate(lambda x: 2*x*x*x, 0.0001)(2)


### Uppgift 5
def lis(seq, cur_val=float('-inf')):
    """ Compute the length of the longest increasing subsequence of seq. """
    if not seq:
        return 0
    else:
        if seq[0] >= cur_val:
            return max(1+lis(seq[1:], seq[0]), lis(seq[1:], cur_val))
        else:
            return lis(seq[1:], cur_val)

assert lis([0, 2, 4, 8]) == 4
assert lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6
assert lis([-2, -1, 3, 7278]) == 4
assert lis([]) == 0
assert lis([-1]) == 1
assert lis([-1, -2]) == 1


### Uppgift 6
import math

def create_network(nodes, transfer_func):
    """
    Creates a neural network represented as a pair of weights and a
    transfer function. The weights are represented as a list of
    layers, where each layer contains one list of weights for each
    node in that layer, the length of the list is the number of nodes
    in the previous layer.
    """    
    weights = []
    prev_layer = nodes[0]
    default_weight = 0
    for layer in nodes[1:]:
        w = []
        for j in range(layer):
            wj = []
            for i in range(prev_layer):
                wj.append(default_weight)
            w.append(wj)
        weights.append(w)
        prev_layer = layer
    return weights, transfer_func

def weights(nn):
    """ Given a neural network, returns the weights. """
    return nn[0]

def transfer_func(nn):
    """ Given a neural network, returns the transfer function. """
    return nn[1]

def init_weights(nn):
    """ Initializes the weights of the neural network to either 0.1 or -0.1. """
    weight = 0.1
    for layer in weights(nn):
        for node in layer:
            for j in range(len(node)):
                node[j] = weight
                weight *= -1
        
def feed_forward(nn, inputs):
    """ Computes the output for each layer of nn given inputs. """
    outputs = [inputs]
    for layer in weights(nn):
        output = []
        for node in layer:
            v = 0
            for i in range(0, len(outputs[-1])):
                v += outputs[-1][i] * node[i]
            output.append(transfer_func(nn)(v))
        outputs.append(output)
    return outputs[1:]

nn = create_network([3, 4, 2], lambda x: 1/(1+math.exp(-x)))
assert feed_forward(nn, [1, 0, 1]) == [[0.5, 0.5, 0.5, 0.5], [0.5, 0.5]]
init_weights(nn)
output = feed_forward(nn, [1, 0, 1])
assert len(output) == 2
assert len(output[0]) == 4
assert len(output[1]) == 2
