### Example solutions for TDDD73 exam 2017-01-10fm

### Uppgift 1
def diophantine(a, b, c, d, min_val, max_val):
    """
    Count the number of solutions to the diophantine equation ax+by+cz=d
    where the variables are in the interval [min_val, max_val].
    """
    count = 0
    for x in range(min_val, max_val+1):
        for y in range(min_val, max_val+1):
            for z in range(min_val, max_val+1):
                if a*x + b*y + c*z == d:
                    count += 1
    return count

assert diophantine(2, 3, 4, 10, 0, 2) == 3
assert diophantine(2, 3, 4, 10, 0, 10) == 5
assert diophantine(2, 3, 4, 9, 1, 1) == 1
assert diophantine(2, 3, 4, 10, 1, 10) == 0
assert diophantine(2, 3, 4, 15, 1, 15) == 3
assert diophantine(2, 3, 4, 10, -5, 10) == 54


### Uppgift 2
def sum_nth_i(seq, n):
    """ Sum every nth element in seq using an iterative approach. """
    sum = 0
    for i in range(n-1, len(seq), n):
        sum += seq[i]
    return sum

assert sum_nth_i([1, 2, 3, 4, 5], 1) == 15
assert sum_nth_i([1, 2, 3, 4, 5], 2) == 6
assert sum_nth_i([1, 2, 3, 4, 5], 3) == 3
assert sum_nth_i([1, 2, 3, 4, 5], 6) == 0
assert sum_nth_i([9, 3, 1, -4, 445], 2) == -1
assert sum_nth_i([], 6) == 0


def sum_nth_r(seq, n, count=1):
    """ Sum every nth element in seq using a recursive approach. """
    if not seq:
        return 0
    elif count == n:
        return seq[0]+sum_nth_r(seq[1:], n, 1)
    else:
        return sum_nth_r(seq[1:], n, count + 1)

assert sum_nth_r([1, 2, 3, 4, 5], 1) == 15
assert sum_nth_r([1, 2, 3, 4, 5], 2) == 6
assert sum_nth_r([1, 2, 3, 4, 5], 3) == 3
assert sum_nth_r([1, 2, 3, 4, 5], 6) == 0
assert sum_nth_r([9, 3, 1, -4, 445], 2) == -1
assert sum_nth_r([], 6) == 0


### Uppgift 3
def split(seq, threshold):
    """
    Given a list and a threshold, return three lists,
    one with all smaller elements, one with all elements equal
    to the threshold and one with all larger elements.
    """
    if not seq:
        return [], [], []
    else:
        below_rest, on_rest, above_rest = split(seq[1:], threshold)
        if isinstance(seq[0], list):
            below_first, on_first, above_first = split(seq[0], threshold)
            return below_first + below_rest, on_first+on_rest, above_first+above_rest
        else:
            if seq[0] < threshold:
                return [seq[0]] + below_rest, on_rest, above_rest
            elif seq[0] == threshold:
                return below_rest, [seq[0]] + on_rest, above_rest
            else:
                return below_rest, on_rest, [seq[0]] + above_rest

assert split([5, [2, 1, 7], 2, [5]], 5) == ([2, 1, 2], [5, 5], [7])
assert split([5, [2, [1, 7]], 2, [[5]]], 5) == ([2, 1, 2], [5, 5], [7])
assert split([5, [2, [1, [7]]], 2, [5]], 5) == ([2, 1, 2], [5, 5], [7])

assert split([5, 2, 1, 7, 2, 5], -1) == ([], [], [5, 2, 1, 7, 2, 5])
assert split([5, 2, 1, 7, 2, 5], 0) == ([], [], [5, 2, 1, 7, 2, 5])
assert split([5, 2, 1, 7, 2, 5], 1) == ([], [1], [5, 2, 7, 2, 5])
assert split([5, 2, 1, 7, 2, 5], 2) == ([1], [2, 2], [5, 7, 5])
assert split([5, 2, 1, 7, 2, 5], 3) == ([2, 1, 2], [], [5, 7, 5])
assert split([5, 2, 1, 7, 2, 5], 5) == ([2, 1, 2], [5, 5], [7])
assert split([5, 2, 1, 7, 2, 5], 7) == ([5, 2, 1, 2, 5], [7], [])
assert split([5, 2, 1, 7, 2, 5], 8) == ([5, 2, 1, 7, 2, 5], [], [])
assert split([5, -2, 1, -7, 2, 5], -1) == ([-2, -7], [], [5, 1, 2, 5])
assert split([5, -2, 1, -7, 2, 5], -2) == ([-7], [-2], [5, 1, 2, 5])
assert split([5, -2, 1, -7, 2, 5], -7) == ([], [-7], [5, -2, 1, 2, 5])
assert split([], 2) == ([], [], [])


### Uppgift 4a
def integrate(f):
    """
    Return a function that takes two arguments a and b that
    numerically integrates the function f over an interval [a, b].
    """
    return lambda a, b: (b-a)*(f(a)+f(b))/2.0

assert abs(integrate(lambda x: 2*x)(0, 1) - 1) < 0.0001
assert abs(integrate(lambda x: 2*x)(2, 4) - 12) < 0.0001
assert abs(integrate(lambda x: 3*x*x)(2, 4) - 60) < 0.0001

### Uppgift 4b
integrate(lambda x: 3*x*x)(2, 4)


### Uppgift 5
def count_change(coins, amount):
    """ Count the number of ways to produce amount using coins. """
    if amount == 0:
        return 1
    elif not coins:
        return 0
    elif coins[0] <= amount:
        return count_change(coins, amount-coins[0]) + count_change(coins[1:], amount)
    else:
        return count_change(coins[1:], amount)

assert count_change([10, 5, 2, 1], 5) == 4
assert count_change([10, 5, 2, 1], 10) == 11
assert count_change([10, 5, 2, 1], 100) == 2156
assert count_change([50, 25, 10, 5, 1], 0) == 1
assert count_change([50, 25, 10, 5, 1], 1) == 1
assert count_change([50, 25, 10, 5, 1], 5) == 2
assert count_change([50, 25, 10, 5, 1], 9) == 2
assert count_change([50, 25, 10, 5, 1], 10) == 4
assert count_change([50, 25, 10, 5, 1], 15) == 6
assert count_change([50, 25, 10, 5, 1], 20) == 9
assert count_change([50, 25, 10, 5, 1], 25) == 13
assert count_change([50, 25, 10, 5, 1], 30) == 18
assert count_change([50, 25, 10, 5, 1], 50) == 50
assert count_change([50, 25, 10, 5, 1], 75) == 134
assert count_change([50, 25, 10, 5, 1], 100) == 292


### Uppgift 6
def rows(matrix):
    """ Returns the number of rows in a matrix. """
    return len(matrix)

def columns(matrix):
    """ Returns the number of columns in a matrix. """
    return len(matrix[0])

def transpose(matrix):
    """ Returns the transpose of a matrix. """
    res = []
    # Swapping rows for columns
    for i in range(columns(matrix)):
        row = []
        for j in range(rows(matrix)):
            row.append(matrix[j][i])
        res.append(row)
    return res

def add(matrix1, matrix2):
    """ Adds two matrices. Assumes equal dimensions of matrices. """
    res = []
    for i in range(rows(matrix1)):
        row = []
        for j in range(columns(matrix1)):
            row.append(matrix1[i][j] + matrix2[i][j])
        res.append(row)
    return res

def multiply(matrix1, matrix2):
    """ Multiplies two matrices. Assumes the appropriate dimensions. """
    res = []
    for i in range(rows(matrix1)):
        row = []
        for j in range(columns(matrix2)):
            val = 0
            for k in range(columns(matrix1)):
                val += matrix1[i][k]*matrix2[k][j]
            row.append(val)
        res.append(row)
    return res
    
def map(matrix, fun):
    """ Returns a new matrix with fun applied to every cell. """
    res = []
    for i in range(rows(matrix)):
        row = []
        for j in range(columns(matrix)):
            row.append(fun(matrix[i][j]))
        res.append(row)
    return res

m1 = [[1, 0, 2], [-1, 3, 1]]
assert rows(m1) == 2
assert columns(m1) == 3
m2 = transpose(m1)
assert m2 == [[1, -1], [0, 3], [2, 1]]
m3 = [[3, 1], [2, 1], [1, 0]]
assert add(m2, m3) == [[4, 0], [2, 4], [3, 1]]
assert multiply(m1, m3) == [[5, 1], [4, 2]]
assert map(m1, lambda x: -x) == [[-1, 0, -2], [1, -3, -1]]
