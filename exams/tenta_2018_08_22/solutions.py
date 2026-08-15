# Uppgift 1

def median(seq):
    """
    Calculates the median of the given sequence
    :param seq: the sequence to calculate the median from
    :type seq: iterable sequence
    """
    size = len(seq)
    if size % 2 == 0:
        return sum(sorted(seq)[size//2-1:size//2+1])/2
    else:
        return sorted(seq)[size//2]


### Tester
if __name__ == "__main__":
    assert median([1, 1, 2, 3, 5, 7, 7, 7, 8]) == 5
    assert median([1, 1, 2, 3, 4, 7, 7, 7, 8, 9]) == 5.5
    assert median([1, 7, 2, 3, 7, 5, 8, 3, 7, 1]) == 4
    assert median([1, 1, 2, 3, 4, 9, 7, 7, 7, 8]) == 5.5
    assert median([1, 7, 2, 3, 7, 5, 8, 7, 1]) == 5


# Uppgift 2

def interval_i(non_frees):
    """
    Calcualtes all free intervals between the given intervals.
    :param non_frees: the not free intervals
    :type non_frees: list
    """
    frees = []
    end = None
    for non_free in non_frees:
        if end is not None and end != non_free[0]:
            frees.append((end, non_free[0]))
        end = non_free[1]
    return frees


def interval_r(non_frees):
    """
    Calcualtes all free intervals between the given intervals.
    :param non_frees: the not free intervals
    :type non_frees: list
    """
    if len(non_frees) <= 1:
        return []
    elif non_frees[0][1] != non_frees[1][0]:
        return [(non_frees[0][1], non_frees[1][0])] + interval_r(non_frees[1:])
    else:
        return interval_r(non_frees[1:])

### Tester
if __name__ == "__main__":
    assert interval_r([(1, 3), (5, 8), (10, 12)]) == [(3, 5), (8, 10)]
    assert interval_i([(10, 13), (16, 19), (19, 20), (25, 33)]) == \
        [(13, 16), (20, 25)]
    assert interval_i([(1, 3), (5, 8), (10, 12)]) == [(3, 5), (8, 10)]
    assert interval_r([(10, 13), (16, 19), (19, 20), (25, 33)]) == \
        [(13, 16), (20, 25)]
    assert interval_r([(1,3)]) == []
    assert interval_i([(1,3)]) == []


# Uppgift 3
## a)
def derivate(f, h):
    """
    Generates a function that approximates the derivate
    f'(x) using a line between (x-h, f(x-h)) and (x+h, f(x+h))
    :param f: the function that is to be derived
    :type f: a function
    :param h: the step distance
    :type h: numeric
    """
    return lambda x: (f(x+h)-f(x-h))/(2*h)

### Tester
if __name__ == "__main__":
    assert isinstance(derivate(lambda x: x+1, 0.5), type(lambda x:x))
    assert derivate(lambda x: x+1, 0.5)(2) == 1
    #### Check so that the derivative is roughly 0 (floating point errors)
    assert abs(derivate(lambda x: (x-1)**2, 0.1)(1)) < 0.0000000001
    assert 1.99999999999 < abs(derivate(lambda x: (x)**2, 0.1)(1)) < \
        2.0000000001

## b)
f_x_eq_eight = derivate(lambda x: 7*x**3 + 4*x**2, 0.1)(8)

### Tester
if __name__ == "__main__":
    assert 1408.068 < f_x_eq_eight < 1408.071


# Uppgift 4 (rekursiv version)
def filter(seq, pred):
    """
    Filters a nested list by keeping only elements e that pred(e) is true for
    :param seq: the nested list
    :type seq: list
    :param pred: an unaray function that returns True for elements that
    should be kept and False for all other elements.
    :type pred: function
    """
    if not seq:
        return []
    elif isinstance(seq[0], list):
        return [filter(seq[0], pred)] + filter(seq[1:], pred)
    elif pred(seq[0]):
        return [seq[0]] + filter(seq[1:], pred)
    else:
        return filter(seq[1:], pred)

### Tester
if __name__ == "__main__":
    assert filter([1, 2, 3], lambda x: x > 1) == [2, 3]
    assert filter([[1], [2], [3]], lambda x: x > 1) == [[], [2], [3]]
    assert filter([[1, [2, [3]], 2, [7], [2, [3, 2, 1]]]],
                  lambda x: x % 2 == 0) == \
        [[[2, []], 2, [], [2, [2]]]]


# Uppgift 4 (iterativ version)
def get_sub_list(seq, depth):
    """
    Returns a reference to the list that is furtherst in the back
    of sequence and is of the given depth (depth 0 returns the list
    itself).
    :param seq: the list
    :type seq: list
    :param depth: the depth
    :type depth: int
    """
    seq = seq
    for _ in range(depth):
        seq = seq[-1]
    return seq


def filter(seq, pred):
    """
    Filters a nested list by keeping only elements e that pred(e) is true for
    :param seq: the nested list
    :type seq: list
    :param pred: an unaray function that returns True for elements that
    should be kept and False for all other elements.
    :type pred: function
    """
    call_stack = [(e, 0) for e in reversed(seq)]
    res = []
    while call_stack:
        entry, depth = call_stack[-1]
        call_stack = call_stack[:-1]
        if isinstance(entry, list):
            # Add sub list at correct spot
            get_sub_list(res, depth).append([])

            # If the list is not empty, add all sublists in the
            # call stack
            if entry:
                call_stack.extend([e, depth+1] for e in reversed(entry))

        elif pred(entry):
            # Add the element to the correct sublist
            get_sub_list(res, depth).append(entry)
    return res

### Tester
if __name__ == "__main__":
    assert filter([1, 2, 3], lambda x: x > 1) == [2, 3]
    assert filter([[1], [2], [3]], lambda x: x > 1) == [[], [2], [3]]
    assert filter([[1, [2, [3]], 2, [7], [2, [3, 2, 1]]]],
                  lambda x: x % 2 == 0) == \
        [[[2, []], 2, [], [2, [2]]]]


# Uppgift 5 (icke-effektiv, iterativ)
def sub_sequence(seq):
    """
    Calculates all possible sub-sequences of the given sequence.
    :param seq: the sequence
    :type seq: string
    """
    seq_sub = set()
    seq_sub.add("")
    for i in range(len(seq)):
        new_set = seq_sub.copy()
        for sub in seq_sub:
            new_set.add(sub + seq[i])
        seq_sub = new_set
    return seq_sub


def llcs(lseq, rseq):
    """
    Calculates the length of the longest common subsequece of
    two sequences.
    T(n, m) = O(log(m)*2^n + log(n)*m^2)
    :param lseq: the first sequence
    :param rseq: the second sequence
    :type lseq: string
    :type rseq: string
    """
    common = sub_sequence(lseq) & sub_sequence(rseq)
    if not common:
        return 0
    else:
        return max(map(len, common))


### Tester
if __name__ == "__main__":
    assert llcs('GAC', 'AGCAT') == 2
    assert llcs('GAAAC', 'AGACATA') == 4
    assert llcs('JAVA', 'PYTHON') == 0


# Uppgift 5 (effektiv variant, rekursiv, sÃ¤mre Ã¤n den effektiva iterativa)
def llcs(lseq, rseq):
    """
    Calculates the length of the longest common subsequece of
    two sequences.
    T(n, m) = O(n*m)
    :param lseq: the first sequence
    :param rseq: the second sequence
    :type lseq: string
    :type rseq: string
    """
    if not lseq or not rseq:
        return 0
    elif lseq[0] == rseq[0]:
        # It's possible to use the first letter of both
        # check best possible if using both or skipping one
        # of them (recursion will handling the case of skipping both)
        return llcs(lseq[1:], rseq[1:]) + 1
    else:
        # Can't use the same letter, hence one must be skipped
        return max(llcs(lseq[1:], rseq), llcs(lseq, rseq[1:]))


### Tester
if __name__ == "__main__":
    assert llcs('GAC', 'AGCAT') == 2
    assert llcs('GAAAC', 'AGACATA') == 4
    assert llcs('JAVA', 'PYTHON') == 0


# Uppgift 5 (effektiv variant, iterativ)
def llcs(lseq, rseq):
    """
    Calculates the length of the longest common subsequece of
    two sequences.
    T(n, m) = O(n*m)
    For a more in depth description of the algorithm see:
    https://en.wikipedia.org/wiki/Longest_common_subsequence_problem

    :param lseq: the first sequence
    :param rseq: the second sequence
    :type lseq: string
    :type rseq: string
    """
    # Column containing the length of the longest common
    # subsequence of all the substrings of lseq and rseq
    # the first row and first column are the point before
    # any token in rseq and lseq, respectively.
    sub_matrix = [[0 for _ in range(len(lseq)+1)] \
                  for _ in range(len(rseq)+1)]
    for start_on in range(1, max(len(lseq), len(rseq))+1):
        # Expand a row if there are any more rows
        if start_on < len(rseq)+1:
            for l_i in range(start_on, len(lseq)+1):
                options = []
                if rseq[start_on-1] == lseq[l_i-1]:
                    options.append(sub_matrix[start_on-1][l_i-1]+1)
                options.append(sub_matrix[start_on-1][l_i])
                options.append(sub_matrix[start_on][l_i-1])
                sub_matrix[start_on][l_i] = max(options)
        # Expand a column if there are any more columns
        if start_on < len(lseq)+1:
            for r_i in range(start_on+1, len(rseq)+1):
                options = []
                if rseq[r_i-1] == lseq[start_on-1]:
                    options.append(sub_matrix[r_i-1][start_on-1]+1)
                options.append(sub_matrix[r_i-1][start_on])
                options.append(sub_matrix[r_i][start_on-1])
                sub_matrix[r_i][start_on] = max(options)
    # The last element in the matrix (max index in both dimensions)
    # represents the longest length of the common subsequence
    # when both sequnces have been traversed
    return sub_matrix[-1][-1]


### Tester
if __name__ == "__main__":
    assert llcs('GAC', 'AGCAT') == 2
    assert llcs('GAAAC', 'AGACATA') == 4
    assert llcs('JAVA', 'PYTHON') == 0


# Uppgift 6

## Data structure
# A ring is represented as a dictionary consisting of:
# {"top": int, "data": list}
# where the value with key "top" is the index of the top element in
# the ring and "data" is a list of all the elements in the ring

## Implementation
from copy import deepcopy


def make_ring(elements):
    """
    Creates a new ring consisting of the given elements.
    :param elements: the elements that the ring is created from
    :type elements: list
    """
    return {"top": 0, "data": deepcopy(elements)}


def top(ring):
    """
    Returns the value that is the top of the ring.
    :param ring: the ring
    :type ring: "ring"
    """
    return deepcopy(ring["data"][ring["top"]])


def left_rotate(ring):
    """
    Rotates the given ring (functionally) one step left
    :param ring: the ring
    :type ring: "ring"
    """
    new_ring = deepcopy(ring)
    new_ring["top"] += 1
    if new_ring["top"] >= len(new_ring["data"]):
        new_ring["top"] -= len(new_ring["data"])
    return new_ring


def right_rotate(ring):
    """
    Rotates the given ring (functionally) one step right
    :param ring: the ring
    :type ring: "ring"
    """
    new_ring = deepcopy(ring)
    new_ring["top"] -= 1
    if new_ring["top"] < 0:
        new_ring["top"] += len(new_ring["data"])
    return new_ring


def right_rotate_in(ring):
    """
    Rotates the given ring (destructively) one step right
    :param ring: the ring
    :type ring: "ring"
    """
    ring["top"] -= 1
    if ring["top"] < 0:
        ring["top"] += len(ring["data"])


def left_rotate_in(ring):
    """
    Rotates the given ring (destructively) one step left
    :param ring: the ring
    :type ring: "ring"
    """
    ring["top"] += 1
    if ring["top"] >= len(ring["data"]):
        ring["top"] += len(ring["data"])


def test_ring():
    ring1 = make_ring([1, 2, 3])
    assert top(ring1) == 1
    assert top(left_rotate(ring1)) == 2
    assert top(ring1) == 1
    assert top(right_rotate(ring1)) == 3
    assert top(ring1) == 1
    assert top(left_rotate(left_rotate(left_rotate(ring1)))) == 1
    ring2 = make_ring(['a', 'b', 'c'])
    assert top(ring2) == 'a'
    left_rotate_in(ring2)
    assert top(ring2) == 'b'
    right_rotate_in(ring2)
    right_rotate_in(ring2)
    assert top(ring2) == 'c'

if __name__ == "__main__":
    test_ring()