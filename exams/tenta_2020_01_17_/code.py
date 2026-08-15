"""1"""
import math
#%%
def distribute_i(num, seq):
    """delar upp listor"""
    new_list = [[] for _ in range(num)]
    step = 0
    for element in seq:
        new_list[step].append(element)
        step = 0 if step == num-1 else step + 1
    return new_list

def distribute_r(num, seq):
    """Recursive function to divide elements in a list"""
    if not seq:
        return []
    def inner(first, inner_seq):
        if not inner_seq:
            return []
        if inner_seq[num:]:
            return [[inner_seq[0]] + inner(False, inner_seq[num:])]
        elif not first:
            return [inner_seq[0]]
        return []
    return inner(True, seq) + distribute_r(num, seq[1:])

#Uppgift 2

def rle_i(seq):
    """i"""
    new_list = []
    prev = seq[0]
    count = 1
    for i in range(1, len(seq)):
        if seq[i] == prev:
            count += 1
            if not seq[i+1:]:
                new_list += [prev] + [count]
        else:
            new_list += [prev] + [count]
            count = 1
        prev = seq[i]
    return new_list

def rle_r(seq):
    """1"""
    prev = seq[0]
    def inner(prev, count, seq):
        if not seq:
            return []
        if seq[0] == prev:
            if not seq[1:]:
                return [prev] + [count+1]
            return inner(seq[0], count+1, seq[1:])
        return [prev] + [count] + inner(seq[0], 1, seq[1:])
    return inner(prev, 1, seq[1:])

#Uppgift 3

def reverse_all(seq: list) -> list:
    """1"""
    if not seq:
        return []
    last = seq[-1]
    if isinstance(last, list):
        return [reverse_all(last)] + reverse_all(seq[:-1])
    return [last] + reverse_all(seq[:-1])

#Uppgift 4

def integrate(f): #pylint: disable=invalid-name
    """takes a function"""
    def inner(a, b): #pylint: disable=invalid-name
        """1"""
        ret_val = (b-a) * f((a+b)/2)
        if ret_val % 1 == 0:
            ret_val = int(ret_val)
        return ret_val
    return inner

#4b

def intsquare(a,b): #pylint: disable=invalid-name
    """1"""
    return integrate(lambda x: 3*(x**2))(a,b)
    ##**VET EJ HUR MAN GÖR *** flr att init 1 gång bara

#Uppgift 54
#5a
def subsequences(tpl: tuple) -> set: #fel
    """Divides integers in a tuple into a set of every subsequence
    consisting of elements in the tuple"""
    #lst = list(tpl)
    result = set()
    for i in range(len(tpl)):
        add = (tpl[:-i])
        result.add(add)
    return result

#Uppgift 6

def prime(num):
    """tar ett heltal och returnerar sant om och endast om detta är ett primtal"""
    if num > 1:
        if num == 2:
            return True
        for i in range(2, num//2+1):
            if num % i == 0:
                return False
        return True
    return False

def siffer_summ(seq):
    """Räknar ut siffersumman på en lista av tal"""
    summ = 0
    for num in seq:
        if 10 > num:
            summ += num
        else:
            curr = num
            while curr >= 10:
                summ += curr % 10
                curr //= 10
            summ += curr
    return summ


def prime_factors(num):
    """tar ett heltal och returnerar dess primtalsfaktorer"""
    factors = []
    loopcount = num
    while True:
        if prime(loopcount):
            factors.append(loopcount)
            break
        for i in range(2, loopcount//2+1):
            if loopcount % i == 0: #and prime(i):
                factors.append(i)
                break
        loopcount //= i
    return factors

def smith(num):
    """Determines wheter the given number is a smith number"""
    return siffer_summ([int(x) for x in str(num)]) == siffer_summ(prime_factors(num))


if __name__ == '__main__':
    #print(distribute_i(3, [1,2,3,4,5,6]))
    #print(distribute_r(3, [1,2,3,4,5,6]))

    #print(rle_i(["a","a","b","a","c","c"]))
    #print(rle_r(["a","a","b","a","c","c"]))

    assert reverse_all([1, 2, 3, [4, 5, ['x', 7]], 8]) == [8, [[7, 'x'], 5, 4], 3, 2, 1]
    assert reverse_all([]) == []
    assert reverse_all([1, 2, 3]) == [3, 2, 1]
    assert reverse_all([-1, [2, 3], ['Hi', 4, [7]]]) == [[[7], 4, 'Hi'], [3, 2], -1]

    assert intsquare(2, 4) == 54
    assert intsquare(-1, 10) == 668.25

    print(subsequences((1, 2)))

#%%
