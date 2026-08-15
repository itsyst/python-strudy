"""
Denna fil innehÃ¥ller ett antal lÃ¶sningsfÃ¶rslag fÃ¶r tentan i TDDE24 mars 2020.

Det finns alltid mÃ¥nga olika sÃ¤tt att lÃ¶sa en uppgift, och bara fÃ¶r att
lÃ¶sningsfÃ¶rslaget ser ut pÃ¥ ett visst sÃ¤tt betyder det inte att detta Ã¤r
det enda, eller ens det allra bÃ¤sta sÃ¤ttet att lÃ¶sa en uppgift.
"""


def correct_roundrobin(seq):
    result = []

    # To keep track of when we should end...
    maxlen = max((len(subseq) for subseq in seq), default=0)

    # For all indexes that exist in SOME subsequence
    for index in range(0, maxlen):
        for subseq in seq:
            # Check if there is an element with this tindex
            # in the current subsequence; otherwise, skip it
            if index < len(subseq):
                result.append(subseq[index])
    return result


def by_sensor_lc(seq):
    return {key: [measurement[1] for measurement in seq if measurement[0] == key]
            for key in [measurement[0] for measurement in seq]}


def expand(mem, msg):
    result = []

    if not msg:
        return result

    for element in msg:
        if isinstance(element, list):
            result.append(expand(mem, element))
        elif isinstance(element, str):
            result.append(element)
        else:
            result.append(mem[element])

    return result


def expand_concat(mem, msg):
    result = []

    if not msg:
        return result

    # Need to keep track of the difference between not having seen any
    # strings, and having seen the empty string. Therefore we can't
    # represent "nothing accumulated yet" as the empty string.
    # Let's use None instead.
    accumulated = None

    for element in msg:
        if isinstance(element, list):
            # We may have accumulated something already.  If so, let's
            # add that string to the result and reset the accumulation.
            if accumulated is not None:
                result.append(accumulated)
            accumulated = None
            # Expand recursively and add the expanded version.
            result.append(expand_concat(mem, element))
        elif isinstance(element, str):
            if accumulated is None:
                # Nothing found before => set
                accumulated = element
            else:
                # Something found before => append
                accumulated += element
        else:
            if accumulated is None:
                accumulated = mem[element]
            else:
                accumulated += mem[element]

    # End of elements, but we may have accumulated a string that we haven't added yet.
    if accumulated is not None:
        result.append(accumulated)

    return result


def pred_comp(p, t, f):
    return lambda x: t(x) if p(x) else f(x)


safe_div = pred_comp(lambda div: div[1] != 0,
                     lambda div: div[0] / div[1],
                     lambda div: 0)


def min_change_inf_greedy(coins: List[int], n: int):
    # WRONG SOLUTION

    # print(coins, n)
    if n == 0:
        # Base case: No coins of any kind are required
        return [0] * len(coins)

    if not coins:
        # No more possibility of making the right amount of change
        return [float('inf')]

    if n < coins[0]:
        # Initial coin cannot be used
        sol = min_change_inf_greedy(coins[1:], n)
        # print("c1", coins, n, sol)
        return [0] + sol  # Works even with infinity
    else:
        # WRONG: Always use the larger coin, since it "fits"
        sol = min_change_inf_greedy(coins, n - coins[0])
        sol[0] += 1
        return sol


# From the web: An efficient dynamic programming solution.
# Not what we're expecting here.
def change_making(coins, n: int):
    """This function assumes that all coins are available infinitely.
    n is the number to obtain with the fewest coins.
    coins is a list or tuple with the available denominations.
    """
    m = _get_change_making_matrix(coins, n)
    for c in range(1, len(coins) + 1):
        for r in range(1, n + 1):
            # Just use the coin coins[c - 1].
            if coins[c - 1] == r:
                m[c][r] = 1
            # coins[c - 1] cannot be included.
            # Use the previous solution for making r,
            # excluding coins[c - 1].
            elif coins[c - 1] > r:
                m[c][r] = m[c - 1][r]
            # coins[c - 1] can be used.
            # Decide which one of the following solutions is the best:
            # 1. Using the previous solution for making r (without using coins[c - 1]).
            # 2. Using the previous solution for making r - coins[c - 1] (without
            #      using coins[c - 1]) plus this 1 extra coin.
            else:
                m[c][r] = min(m[c - 1][r], 1 + m[c][r - coins[c - 1]])
    return m[-1][-1]


def min_change(coins: List[int], n: int):
    # print(coins, n)
    if n == 0:
        # Base case: No coins of any kind are required
        return [0] * len(coins)

    if not coins:
        # No more possibility of making the right amount of change
        return None

    if n < coins[0]:
        # Initial coin cannot be used
        sol = min_change(coins[1:], n)
        # print("c1", coins, n, sol)
        if sol:
            return [0] + sol
        else:
            return None
    else:
        # Can choose to use initial coin, in which case it can still be used
        # in the recursive call...
        sol2 = min_change(coins, n - coins[0])
        # ...or not to use it
        sol1 = min_change(coins[1:], n)
        # print("c2", coins, n, sol1, sol2)

        if sol1:
            sol1 = [0] + sol1
        if sol2:
            sol2[0] += 1

        if sol1 is None:
            return sol2
        elif sol2 is None:
            return sol1
        elif sum(sol1) < sum(sol2):
            return sol1
        else:
            return sol2


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


def plus(matrix1, matrix2):
    """ Adds two matrices. Assumes equal dimensions of matrices. """
    res = []
    for i in range(rows(matrix1)):
        row = []
        for j in range(columns(matrix1)):
            row.append(matrix1[i][j] + matrix2[i][j])
        res.append(row)
    return res


def times(matrix1, matrix2):
    """ Multiplies two matrices. Assumes the appropriate dimensions. """
    res = []
    for i in range(rows(matrix1)):
        row = []
        for j in range(columns(matrix2)):
            val = 0
            for k in range(columns(matrix1)):
                val += matrix1[i][k] * matrix2[k][j]
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
