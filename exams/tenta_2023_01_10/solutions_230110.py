"""
Denna fil innehÃ¥ller ett antal lÃ¶sningsfÃ¶rslag fÃ¶r tentan i TDDE24 januari 2023.

Det finns alltid mÃ¥nga olika sÃ¤tt att lÃ¶sa en uppgift, och bara fÃ¶r att
lÃ¶sningsfÃ¶rslaget ser ut pÃ¥ ett visst sÃ¤tt betyder det inte att detta Ã¤r
det enda, eller ens det allra bÃ¤sta sÃ¤ttet att lÃ¶sa en uppgift.
"""
from collections import defaultdict
from typing import Union


def facit_split_by_first(seq: list[str]):
    # En relativt rÃ¤ttfram lÃ¶sning pÃ¥ uppgift 1.
    result = dict()
    for word in seq:
        key = word[0]
        if key in result:
            result[key].append(word)
        else:
            result[key] = [word]
    return result


def facit_split_by_first(seq: list[str]):
    # Om man kÃ¤nner till defaultdict (ingÃ¥r inte i kursen) kan man anvÃ¤nda
    # detta fÃ¶r att slippa testa i fÃ¶rvÃ¤g om en nyckel redan finns i en
    # dictionary.
    result = defaultdict(list)
    for word in seq:
        result[word[0]].append(word)
    return result


def facit_split_by_first(seq: list[str]):
    # Denna lÃ¶sning Ã¤r kortare, men kan vara lÃ¥ngsammare eftersom
    # man mÃ¥ste gÃ¥ genom hela sekvensen om och om igen fÃ¶r varje
    # tecken som ett ord kan bÃ¶rja pÃ¥.
    return {x: [word for word in seq if word and word[0] == x] for x in {word[0] for word in seq}}


def facit_split_lists(seq: Union[list, tuple], sizes: str):
    result = []

    # For every number of elements...
    for count in sizes:
        count = int(count)
        if len(seq) < count:
            # Not enough elements left
            return None, None

        # OK, pick the desired number of elements (0 or more)
        # and step forward in the sequence (creates a copy of the sequence).
        result.append(seq[:count])
        seq = seq[count:]

    # Took care of the entire 'sizes'
    if seq:
        # Too many elements in seq
        return None, None
    else:
        # Got exactly as many elements as we needed
        return result


def facit_split_lists_rec(seq: Union[list, tuple], sizes: str):
    if not sizes:
        # Base case: No more sublists to create.
        if not seq:
            # Reached the end of seq; all is good
            return []
        else:
            # There are elements left but we don't want any...
            return None, None

    # OK, we do need to create at least one more sublist.  How many elements?
    count = int(sizes[0])
    if len(seq) < count:
        # Not enough elements left
        return None, None

    # As in the iterative solution, we step forward <count> elements.
    # There is no requirement to use double recursion to add one element
    # at a time; the solution is still recursive, handling each
    # specified size in <sizes> through a new recursive call.
    tail = facit_split_lists_rec(seq[count:], sizes[1:])
    if tail == (None, None):
        # Failed to solve the subproblem
        return None, None

    return [seq[:count]] + tail


def facit_doubled_odds(seq: list):
    result = []
    for element in seq:
        if isinstance(element, list):
            # Rekursera ner i listor fÃ¶r att behandla deras element
            result.append(facit_doubled_odds(element))
        elif isinstance(element, int) and element % 2 == 1:
            # Specialbehandla udda heltal
            result.append(element * 2)
        else:
            # Allt annat Ã¤r bara godtyckliga element som "kopieras Ã¶ver"
            result.append(element)
    return result


def facit_sum_satisfying(fun, pred):
    # Define a function that returns the sum of fun(val)
    # for those values <val> in <seq> that satisfy <pred>.
    def process(seq):
        result = 0
        for val in seq:
            if pred(val):
                result += fun(val)

        return result

    return process


facit_sum_square_negative_odd = facit_sum_satisfying(
    lambda val: val * val,
    lambda val: (val < 0) and val % 2 != 0
)


def facit_rows(matrix):
    """Returns the number of rows in the matrix"""
    return len(matrix)


def facit_columns(matrix):
    """Returns the number of columns in the matrix"""
    return len(matrix[0])


def facit_transpose(matrix):
    """Returns the matrix transposed, meaning the columns and the row have been switched"""
    return [[row[i] for row in matrix] for i in range(facit_columns(matrix))]


def facit_map(matrix, fun):
    """Applis the function (fun) to each number in the matrix, then returns the new matrix"""
    return [[fun(row[i]) for i in range(facit_columns(matrix))] for row in matrix]


def facit_plus(matrix1, matrix2):
    """Adds matrix1 and matrix2, then returns the result.
    Adding means each number in matrix1 gets added with the number of the corresponding position in matrix2"""
    return [[matrix1[j][i] + matrix2[j][i] for i in range(facit_columns(matrix1))] for j in range(facit_rows(matrix1))]


def facit_times(matrix1, matrix2):
    """ Multiplies two matrices. Assumes the appropriate dimensions. """
    res = []
    for i in range(facit_rows(matrix1)):
        row = []
        for j in range(facit_columns(matrix2)):
            val = 0
            for k in range(facit_columns(matrix1)):
                val += matrix1[i][k] * matrix2[k][j]
            row.append(val)
        res.append(row)
    return res


def facit_times(matrix1, matrix2):
    """
    Alternative version using list comprehensions and zip
    (Using numpy library would of course be even faster)
    """
    return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*matrix2)]
            for A_row in matrix1]


def facit_eval_pyassm(prog: list[list]) -> list[tuple]:
    # Initialize all registers to 0
    vals = {r: 0 for r in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

    return_addresses = []
    log = []

    ip = 0
    while ip < len(prog):
        inst = prog[ip]  # type: list
        op = inst[0]
        ip += 1
        if op == "LOG":
            log.append((inst[1], vals[inst[1]]))
            print(f"[{inst[1]}={vals[inst[1]]}]")
        elif op == "CPY":
            vals[inst[1]] = vals[inst[2]]
        elif op == "SET":
            vals[inst[1]] = inst[2]
        elif op == "ADD":
            vals[inst[1]] = vals[inst[1]] + inst[2]
        elif op == "MUL":
            vals[inst[1]] = vals[inst[1]] * inst[2]
        elif op == "JEQ":
            if vals[inst[1]] == vals[inst[2]]:
                ip += inst[3] - 1
        elif op == "JNE":
            if vals[inst[1]] != vals[inst[2]]:
                ip += inst[3] - 1
        elif op == "JSR":
            return_addresses.append(ip)
            ip = inst[1]
        elif op == "RET":
            ip = return_addresses.pop()
        elif op == "NOP":
            pass
        else:
            # An extra error check, but the solution would also have been
            # OK without this
            raise ValueError(f"invalid opcode {op}")

    return log


def facit_eval_pyassm(prog: list[list]) -> list[tuple]:
    # A version that does not set values to 0 initially
    vals = {}  # Register values

    def read_reg(r):
        """
        Always use this to read registers, since they are not initialized
        at the start
        """
        assert r in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if r in vals:
            return vals[r]
        return 0

    return_addresses = []
    log = []

    ip = 0
    while ip < len(prog):
        inst = prog[ip]  # type: list
        op = inst[0]
        ip += 1
        if op == "LOG":
            log.append((inst[1], read_reg(inst[1])))
            print(f"[{inst[1]}={read_reg(inst[1])}]")
        elif op == "CPY":
            vals[inst[1]] = read_reg(inst[2])
        elif op == "SET":
            vals[inst[1]] = inst[2]
        elif op == "ADD":
            vals[inst[1]] = read_reg(inst[1]) + inst[2]
        elif op == "MUL":
            vals[inst[1]] = read_reg(inst[1]) * inst[2]
        elif op == "JEQ":
            if read_reg(inst[1]) == read_reg(inst[2]):
                ip += inst[3] - 1
        elif op == "JNE":
            if read_reg(inst[1]) != read_reg(inst[2]):
                ip += inst[3] - 1
        elif op == "JSR":
            return_addresses.append(ip)
            ip = inst[1]
        elif op == "RET":
            ip = return_addresses.pop()
        elif op == "NOP":
            pass
        else:
            # An extra error check, but the solution would also have been
            # OK without this
            raise ValueError(f"invalid opcode {op}")

    return log


