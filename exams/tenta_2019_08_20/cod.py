"""Tenta 2019 08 20"""
#%%
#import math

"""Uppgift 1"""
def find_least_close_i(seq1, seq2):
    new_list = []
    furth = seq2[0]
    for num in seq1:
        for compare in seq2[1:]:
            comp_val1, comp_val2 = abs(num-compare), abs(num-furth)
            if comp_val1 > comp_val2 or (comp_val1 == comp_val2 and compare > furth):
                furth = compare
        new_list.append(furth)
    return new_list
def find_least_close_r(seq1, seq2):
    if not seq1:
        return []
    def inner(furth, comp_seq):
        if not comp_seq:
            return [furth]
        num = seq1[0]
        comp_val1, comp_val2 = abs(num-comp_seq[0]), abs(num-furth)
        if comp_val1 > comp_val2 or (comp_val1 == comp_val2 and comp_seq[0] > furth):
            return inner(comp_seq[0], comp_seq[1:])
        return inner(furth, comp_seq[1:])
    return inner(seq2[0], seq2[1:]) + find_least_close_r(seq1[1:], seq2)

"""Uppgift 2"""
def zip3_r(s1, s2, s3): #pylint: disable=invalid-name
    if not s1 or not s2 or not s3:
        return []
    return [(s1[0], s2[0], s3[0])] + zip3_r(s1[1:], s2[1:], s3[1:])
def zip3_i(s1, s2, s3): #pylint: disable=invalid-name
    new_list = []
    for i in range(min(len(s1), len(s2), len(s3))):
        new_list.append((s1[i], s2[i], s3[i]))
    return new_list

"""Uppgift 3"""
def squared_odds(seq: list):
    if not seq:
        return []
    if isinstance(seq[0], list):
        return [squared_odds(seq[0])] + squared_odds(seq[1:])
    if isinstance(seq[0], int) and not seq[0] % 2 == 0:
        return [seq[0]**2] + squared_odds(seq[1:])
    return [seq[0]] + squared_odds(seq[1:])

"""Uppgift 4"""
#4a
def each_pair(seq, fn_pair):
    if 1 >= len(seq):
        return []
    new_list = []
    prev = seq[0]
    for ele in seq[1:]:
        if isinstance(ele, type(prev)):
            new_list.append(fn_pair(prev, ele))
        else:
            new_list.append(ele)
        prev = ele
    return new_list

#4b
def combine_pairs(init, seq, fn_pair, fn_combine):
    if 1 >= len(seq):
        return init
    result = init
    prev = seq[0]
    for ele in seq[1:]:
        if isinstance(ele, type(prev)):
            result = fn_combine(result, fn_pair(prev, ele))
        else:
            result = fn_combine(result, ele)
        prev = ele
    return result

"""Uppgift 5"""
def combinations(seq):
    if len(seq) == 1:
        return set([(num,) for num in range(1, seq[0] + 1)])
    without_first = combinations(seq[1:])
    with_first = [(num,) for num in range(1, seq[0] + 1)]
    return set([first + rest for first in with_first for rest in without_first])

"""Uppgift 6"""
def make_deque():
    """Returnerar en ny tom kö."""
    return []
def length(deque):
    """Returnerar längden av kön deque."""
    return len(deque)
def front(deque):
    """Returnerar första elementet i kön deque, utan att ta bort elementet
    och utan att modifiera kön på andra sätt. Returnerar None om kön är tom."""
    if len(deque) > 0:
        return deque[0]
    return None
def back(deque):
    """Returnerar sista elementet i kön deque, utan att ta bort elementet och
    utan att modifiera kön på andra sätt. Returnerar None om kön är tom."""
    if len(deque) > 0:
        return deque[-1]
    return None

def push_front_d(deque, elt):
    """Lägg till elt först i kön deque destruktivt."""
    deque.insert(0, elt)
def pop_front_d(deque):
    """Ta bort första elementet i kön deque destruktivt."""
    if len(deque) > 0:
        deque.pop(0)
def push_back_d(deque, elt):
    """Lägg till elt sist i kön deque destruktivt."""
    deque.append(elt)
def pop_back_d(deque):
    """Ta bort sista elementet i kön deque destruktivt."""
    if len(deque) > 0:
        deque.pop(-1)

def push_front_f(deque, elt):
    """Returnera en kö som motsvarar att elt har lagts till först i kön deque."""
    return [elt] + deque
def pop_front_f(deque):
    """Returnera en kö som motsvarar att första elementet i kön deque har tagits bort."""
    return deque[1:]
def push_back_f(deque, elt):
    """Returnera en kö som motsvarar att elt har lagts till sist i kön deque"""
    return deque + [elt]
def pop_back_f(deque):
    """Returnera en kö som motsvarar att sista elementet i kön deque har tagits bort."""
    return deque[:-1]

if __name__ == "__main__":
    if True:
        assert find_least_close_i([], [1]) == [] # pylint: disable=use-implicit-booleaness-not-comparison
        assert find_least_close_i([10], [5, 8, 12, 15]) == [15]
        assert find_least_close_i([12, 10], [-1000, 5, 8, 12, 15]) == [-1000, -1000]
        assert find_least_close_r([], [1]) == [] # pylint: disable=use-implicit-booleaness-not-comparison
        assert find_least_close_r([10], [5, 8, 12, 15]) == [15]
        assert find_least_close_r([12, 10], [-1000, 5, 8, 12, 15]) == [-1000, -1000]

        assert zip3_r([], [], [1]) == []  # pylint: disable=use-implicit-booleaness-not-comparison
        assert zip3_r([1, 2, 3], [4, 5, 6], ['a', 'b']) == [(1, 4, 'a'), (2, 5, 'b')]
        assert zip3_i([], [], [1]) == []  # pylint: disable=use-implicit-booleaness-not-comparison
        assert zip3_i([1, 2, 3], [4, 5, 6], ['a', 'b']) == [(1, 4, 'a'), (2, 5, 'b')]

        assert squared_odds([]) == []
        assert squared_odds([1, 2, 3]) == [1, 2, 9]
        assert squared_odds([-1, [2, 3], ['Hi', 4, [7]]]) == [1, [2, 9], ['Hi', 4, [49]]]

        assert each_pair([3, 7, 9, 15, 23, 27, 33], (lambda x, y: y-x)) == [4, 2, 6, 8, 4, 6]
        assert each_pair(['Hel', 'lo', 'op'], (lambda x, y: x+y)) == ['Hello', 'loop']

        assert combine_pairs([], [3, 7, 9, 15, 23, 27, 33], (lambda x, y: y-x),
        (lambda c,n: c + [n])) == [4, 2, 6, 8, 4, 6]
        assert combine_pairs(True, [1, 2, 5, 4], (lambda x,y: x<y), (lambda a,b: a and b)) == False #pylint: disable=singleton-comparison
        assert combine_pairs(True, [1, 2, 3, 4], (lambda x,y: x<y), (lambda a,b: a and b)) == True #pylint: disable=singleton-comparison
        assert combine_pairs(False, [1, 2, 5, 4], (lambda x,y: x<y), (lambda a,b: a or b)) == True #pylint: disable=singleton-comparison
        
        assert combinations([1]) == {(1,)}
        assert combinations([2, 2]) == {(1, 2), (1, 1), (2, 1), (2, 2)}
        assert combinations([4, 2, 2]) == {(1, 2, 1), (2, 2, 2), (4, 2, 2), (3, 1, 1), (3, 2, 1), (1, 2, 2), (2, 2, 1), (2, 1, 1), (4, 2, 1), (1, 1, 2), (3, 2, 2), (4, 1, 1), (2, 1, 2), (1, 1, 1), (4, 1, 2), (3, 1, 2)}
    #6
    #q = make_deque()
    #push_front_d(q, 15)
    #assert length(q) == 1
    #push_back_d(q, 22)
    #assert length(q) == 2
    #assert front(q) == 15
    #assert back(q) == 22
    #pop_front_d(q)
    #assert front(q) == 22
    #pop_back_d(q)
    #assert length(q) == 0
#%%
