# Example solutions to the exam 2018-01-12
# Erik Hansson / Fredrik Heintz 2018-01-12


##### Uppgift 1

def day_of_year(date, is_leap_year):
    """
    Calculates which day of the year date corresponds to.
    :param date: the data given on the form ("mon", day)
    :type date: (str, int)
    :param is_leap_year: True if the year is a leap year else false
    :type is_leap_year: boolean
    """
    _months = (("jan", 31), ("feb", 28), ("mar", 31), ("apr", 30), ("may", 31),
               ("jun", 30), ("jul", 31), ("aug", 31), ("sep", 30), ("oct", 31),
               ("nov", 30), ("dec", 31))
    
    day = 0
    month = 0
    while (date[0] != _months[month][0]):
        day += _months[month][1] + \
               (1 if _months[month][0] == "feb" and is_leap_year else 0)
        month += 1
    return day + date[1]

assert day_of_year(('jan', 2), False) == 2
assert day_of_year(('mar', 10), False) == 69
assert day_of_year(('mar', 10), True) == 70
assert day_of_year(('feb', 27), True) == 58
assert day_of_year(('feb', 27), False) == 58
assert day_of_year(('feb', 28), True) == 59
assert day_of_year(('feb', 28), False) == 59
assert day_of_year(('feb', 29), True) == 60
assert day_of_year(('mar', 1), False) == 60
assert day_of_year(('mar', 1), True) == 61
assert day_of_year(('dec', 31), False) == 365
assert day_of_year(('dec', 31), True) == 366


##### Uppgift 2

def odd_r(seq):
    """
    Gets all the odd numbers in the input and returns them in order.
    :param seq: a list of numbers
    :type seq: [int*]
    """
    if not seq:
        return []
    else:
        return ([] if seq[0] % 2 == 0 else [seq[0]]) + odd_r(seq[1:])


def odd_i(seq):
    """
    Gets all the odd numbers in the input and returns them in order.
    :param seq: a list of numbers
    :type seq: [int*]
    """
    odds = []
    for elem in seq:
        if elem % 2 == 1:
            odds.append(elem)
    return odds

assert odd_r([1, 2, 3, 4, 5]) == [1, 3, 5]
assert odd_r([1, 3, 5]) == [1, 3, 5]
assert odd_r([2, 4, 6]) == []
assert odd_r([]) == []

assert odd_i([1, 2, 3, 4, 5]) == [1, 3, 5]
assert odd_i([1, 3, 5]) == [1, 3, 5]
assert odd_i([2, 4, 6]) == []
assert odd_i([]) == []


##### Uppgift 3

def merge_dictionaries(dict1, dict2):
    """
    Take two dictionaries mapping keys to lists and
    merge the lists with the same key.
    """
    res = dict1.copy()
    for k in dict2:
        if k in res:
            res[k] += dict2[k]
        else:
            res[k] = dict2[k]
    return res

def partition(seq):
    """
    Partitions all the strings in the input into lists of strings with
    the same length.
    :param seq: a nested list of strings
    :type seq: [ELEMS*]
    :type ELEMS: str|[seq]
    """
    if not seq:
        return dict()
    elif isinstance(seq[0], list):
        return merge_dictionaries(partition(seq[0]), partition(seq[1:]))
    else:
        res = partition(seq[1:])
        if len(seq[0]) in res:
            res[len(seq[0])].append(seq[0])
        else:
            res[len(seq[0])] = [seq[0]]
        return res

def comp_dictionaries(dict1, dict2):
    for k in dict1:
        if not k in dict2 or sorted(dict1[k]) != sorted(dict2[k]):
            return False
    return True

assert comp_dictionaries(partition(['a', 'aa', 'b', 'ccc', 'dd']), {1: ['a', 'b'], 2: ['aa', 'dd'], 3: ['ccc']})
assert comp_dictionaries(partition(['a', ['aa', ['b'], ['ccc', 'dd']]]), {1: ['b', 'a'], 2: ['dd', 'aa'], 3: ['ccc']})
assert comp_dictionaries(partition([]), {})
assert comp_dictionaries(partition([[[]]]), {})
assert comp_dictionaries(partition([[], 'a']), {1: ['a']})
assert comp_dictionaries(partition(['a', 'aa', 'b', 'ccc', 'dd']), {1: ['a', 'b'], 2: ['aa', 'dd'], 3: ['ccc']})
assert comp_dictionaries(partition([[], 'abcd']), {4: ['abcd']})
assert comp_dictionaries(partition(['a', 'aa', 'aaa', 'aaaa']), {1: ['a'], 2: ['aa'], 3: ['aaa'], 4: ['aaaa']})


##### Uppgift 4

def bind_1st(f, v):
    """
    Binds the first parameter of f to v.
    :param f: binary function
    :type f: g(x, y)
    :param v: a valid input
    :type v: v in Domain(x)
    """
    return lambda y: f(v, y)

numbers = list(map(bind_1st(lambda x, y: x+y, 3), [2, 1, 3]))

assert bind_1st(lambda x, y: x*y, 3)(2) == 6
assert numbers == [5, 4, 6]



##### Uppgift 5

def heuristics(item):
    """
    Calculate an estimate for how good it is to pack a certain item
    :param item: an item
    :type item: (number, number)
    """
    return item[1]/item[0]

def knapsack(things, max_weight):
    """
    Finds the maximum amount of value one can get within the max_weight.
    :param things: the different selectable items
    :type things: [(weight, value)*]
    :type weight, value, max_weight: number
    """
    items_w_h = sorted(
        list(map(lambda item: [item[0], item[1], heuristics(item)], things)),
        key=lambda item: item[2], reverse=True
    )

    # Options left to test
    options = [["with", "without"]]

    ## Best value gotten so far
    best_value = 0
    # Dummy item in added to give start values when nothing is in the bag
    added = [[0, 0]]

    while options != []:
        current_weight = sum(item[0] for item in added)
        current_value = sum(item[1] for item in added)
        i = len(options)-1
        remaining_potential_value = sum(item[1] for item in items_w_h[i:])

        # Can't add something more => check if best solution and
        # backtrack. Reasons i order (separeted by or) are:
        # * at maximum weight, nothing more can be gained => pruning
        #   of search tree, but can still be valid selection (implicit
        #   without for the rest of the items to consider)
        # * At leaf node
        # * At leaf node
        # * At leaf node
        # * Can't reach a better value than before => pruning
        if current_weight == max_weight or len(options) > len(items_w_h) or \
           len(options[-1]) == 0 or \
           (options[-1] == ["with"] and
            current_weight + items_w_h[i][0] > max_weight) or \
           current_value + remaining_potential_value < best_value:
            best_value = max(best_value, current_value)

            # Backtracking
            options.pop(-1)
            added.pop(-1)

        else:
            # Try to add item
            if "with" in options[-1] and \
               current_weight + items_w_h[i][0] <= max_weight:
                added.append(items_w_h[i][0:2])
                options[-1].remove("with")
            elif "without" in options[-1]:
                options[-1].remove("without")
                added.append([0, 0])

            # Check next item
            options.append(["with", "without"])
    return best_value


def simple_knapsack(things, max_weight):
    """
    Finds the maximum amount of value one can get within the max_weight.
    :param things: the different selectable items
    :type things: [(weight, value)*]
    :type weight, value, max_weight: number
    """
    # Create all permutations (i.e [True, True, False] means that
    # item 1 and 2 are packed)
    configurations = [[]]
    for _ in range(len(things)):
        extended = []
        for e in configurations:
            extended += [e + [True]]
            extended += [e + [False]]
        configurations = extended

    # Select the best configuration
    best_value = 0
    for config in configurations:
        weight = 0
        value = 0
        for i in range(len(config)):
            if config[i]:
                weight += things[i][0]
                value += things[i][1]
        if weight <= max_weight and value > best_value:
            best_value = value

    return best_value

    
def full_knapsack(things, max_weight):
    """
    Finds the maximum amount of value one can get within the max_weight.
    :param things: the different selectable items
    :type things: [(weight, value)*]
    :type weight, value, max_weight: number
    """
    if not things:
        return 0
    else:
        val_with = 0
        if things[0][0] <= max_weight:
            val_with = things[0][1] + full_knapsack(things[1:], max_weight-things[0][0])
        return max(val_with, full_knapsack(things[1:], max_weight))

assert knapsack([(12,4), (2,2), (1,2), (1,1), (4,10)], 15) == 15
assert knapsack([(12,12), (2,2), (1,2), (1,1), (4,10)], 15) == 16
assert knapsack([(12,9), (2,2), (1,3), (1,2), (1,2), (1,1), (4,10)], 15) == 20
assert knapsack([(24,9), (5,5), (5,5)], 25) == 10
assert knapsack([(19,2), (5,5), (19,2), (5,5)], 25) == 10
assert knapsack([(1, 1), (1, 1), (2, 3)], 2) == 3
assert simple_knapsack([(12,4), (2,2), (1,2), (1,1), (4,10)], 15) == 15
assert simple_knapsack([(12,12), (2,2), (1,2), (1,1), (4,10)], 15) == 16
assert simple_knapsack([(12,9), (2,2), (1,3), (1,2), (1,2), (1,1), (4,10)], 15) == 20
assert simple_knapsack([(24,9), (5,5), (5,5)], 25) == 10
assert full_knapsack([(12,4), (2,2), (1,2), (1,1), (4,10)], 15) == 15
assert full_knapsack([(12,12), (2,2), (1,2), (1,1), (4,10)], 15) == 16
assert full_knapsack([(12,9), (2,2), (1,3), (1,2), (1,2), (1,1), (4,10)], 15) == 20
assert full_knapsack([(24,9), (5,5), (5,5)], 25) == 10
assert full_knapsack([(19,2), (5,5), (19,2), (5,5)], 25) == 10
assert full_knapsack([(1, 1), (1, 1), (2, 3)], 2) == 3


### Uppgift 6
def create_table(columns, rows = []):
    """ 
    Creates a table with columns and rows.
    Represent a table as a tuple (columns, rows).
    """
    table = (columns, [])
    add_rows(table, rows)
    return table

def get_columns(table):
    """
    Get the column names of table.
    """
    return table[0]

def get_rows(table):
    """
    Get the rows of table.
    """
    return table[1]
    
def rows(table):
    """
    Get the number of rows in table.
    """
    return len(get_rows(table))

def columns(table):
    """
    Get the number of columns in table.
    """
    return len(get_columns(table))

def add_rows(table, rows):
    """
    Add rows to table. Assume they have the right number of columns.
    """
    for row in rows:
        assert len(row) == columns(table)
    get_rows(table).extend(rows)

def add_row(table, row):
    """
    Add row to table. Assume it has the right number of columns.
    """
    assert len(row) == columns(table)
    get_rows(table).append(row)

def get_column_name(table, index):
    """
    Returns the column name for column index in table.
    """
    return get_columns(table)[index]

def get_index_of_column_name(table, column_name):
    """
    Returns the index of the first column in table with name column_name.
    """
    return get_columns(table).index(column_name)


def select(table, pred):
    """
    Return a new table containing all rows in table satisfying pred.
    """
    return create_table(get_columns(table),
                        [row for row in get_rows(table) if pred(row)])


def project(table, columns):
    """
    Return a new table containing all rows in table but only columns.
    """
    rows = get_rows(table)
    new_rows = []
    for row in rows:
        new_row = []
        for (i, v) in enumerate(row):
            if get_column_name(table, i) in columns:
                new_row.append(v)
        new_rows.append(new_row)
    return create_table(columns, new_rows)


def join(table1, column1, table2, column2):
    """
    Join table1 with table2 based on column1 and column2.
    In the cartesian product of rows select all rows where
    the value of column1 is equal to the value of column2.
    """
    new_rows = []
    col_ind1 = get_index_of_column_name(table1, column1)
    col_ind2 = get_index_of_column_name(table2, column2)
    for row1 in get_rows(table1):
        for row2 in get_rows(table2):
            if row1[col_ind1] == row2[col_ind2]:
                new_rows.append(row1+row2)
    return create_table(get_columns(table1) + get_columns(table2), new_rows)


# static test data

def test_table():
    """
    Simple test suit of the table datatype.
    """
    student_table_columns = ["Namn", "Klass", "Kurs"]
    student_table_rows = [["Ada", "U1", "TDDE24"],
                          ["Bo", "D1", "TDDE24"],
                          ["My", "D1", "TDDE25"]]

    student = create_table(student_table_columns)
    assert get_columns(student) == student_table_columns
    assert rows(student) == 0
    assert get_rows(student) == []
    for (i, cn) in enumerate(student_table_columns):
        assert get_column_name(student, i) == cn
        assert get_index_of_column_name(student, cn) == i

    add_rows(student, student_table_rows)
    assert get_columns(student) == student_table_columns
    assert rows(student) == len(student_table_rows)
    assert get_rows(student) == student_table_rows


def test_select():
    """
    Simple test of SQL operation select.
    """
    student_table_columns = ["Namn", "Klass", "Kurs"]
    student_table_rows = [["Ada", "U1", "TDDE24"],
                          ["Bo", "D1", "TDDE24"],
                          ["My", "D1", "TDDE25"]]
    select_rows = [["Ada", "U1", "TDDE24"],
                   ["Bo", "D1", "TDDE24"]]

    student = create_table(student_table_columns, student_table_rows)
    select_res = select(student, lambda row: row[get_index_of_column_name(student, "Kurs")] == "TDDE24")
    assert get_columns(student) == get_columns(select_res)
    assert get_rows(student) == student_table_rows
    assert get_rows(select_res) == select_rows


def test_project():
    """
    Simple test of SQL operation project.
    """
    student_table_columns = ["Namn", "Klass", "Kurs"]
    student_table_rows = [["Ada", "U1", "TDDE24"],
                          ["Bo", "D1", "TDDE24"],
                          ["My", "D1", "TDDE25"]]
    project_columns = ["Namn", "Klass"]
    project_rows = [["Ada", "U1"],
                    ["Bo", "D1"],
                    ["My", "D1"]]

    student = create_table(student_table_columns, student_table_rows)
    project_res = project(student, project_columns)
    assert get_columns(student) == student_table_columns
    assert get_columns(project_res) == project_columns
    assert get_rows(student) == student_table_rows
    assert get_rows(project_res) == project_rows


def test_join1():
    """
    Simple test of SQL operation join.
    """
    student_table_columns = ["Namn", "Klass", "Kurs"]
    student_table_rows = [["Ada", "U1", "TDDE24"],
                          ["Bo", "D1", "TDDE24"],
                          ["My", "D1", "TDDE25"]]

    kurs_table_name = "kurs"
    kurs_table_columns = ["Kurs", "Examinator"]
    kurs_table_rows = [["TDDE24", "Peter"],
                       ["TDDE25", "Fredrik"]]

    join_columns = ["Namn", "Klass", "Kurs", "Kurs", "Examinator"]
    join_rows = [["Ada", "U1", "TDDE24", "TDDE24", "Peter"],
                 ["Bo", "D1", "TDDE24", "TDDE24", "Peter"],
                 ["My", "D1", "TDDE25", "TDDE25", "Fredrik"]]
    
    student = create_table(student_table_columns, student_table_rows)
    kurs = create_table(kurs_table_columns, kurs_table_rows)

    join_res = join(student, "Kurs", kurs, "Kurs")
    assert get_columns(student) == student_table_columns
    assert get_columns(kurs) == kurs_table_columns
    assert get_columns(join_res) == join_columns
    assert get_rows(student) == student_table_rows
    assert get_rows(kurs) == kurs_table_rows
    assert get_rows(join_res) == join_rows


def test_join2():
    """
    Simple test of SQL operation join.
    """
    student_table_columns = ["Namn", "Klass", "Kurs"]
    student_table_rows = [["Ada", "U1", "TDDE24"],
                          ["Bo", "D1", "TDDE24"],
                          ["My", "D1", "TDDE25"]]

    kurs_table_name = "kurs"
    kurs_table_columns = ["Kurs", "Examinator"]
    kurs_table_rows = [["TDDE24", "Peter"],
                       ["TDDE25", "Fredrik"]]

    join_columns = ["Kurs", "Examinator", "Namn", "Klass", "Kurs"]
    join_rows = [["TDDE24", "Peter", "Ada", "U1", "TDDE24"],
                 ["TDDE24", "Peter", "Bo", "D1", "TDDE24"],
                 ['TDDE25', 'Fredrik', 'My', 'D1', 'TDDE25']]
    
    student = create_table(student_table_columns, student_table_rows)
    kurs = create_table(kurs_table_columns, kurs_table_rows)

    join_res = join(kurs, "Kurs", student, "Kurs")
    assert get_columns(student) == student_table_columns
    assert get_columns(kurs) == kurs_table_columns
    assert get_columns(join_res) == join_columns
    assert get_rows(student) == student_table_rows
    assert get_rows(kurs) == kurs_table_rows
    assert get_rows(join_res) == join_rows
    
    
test_table()
test_select()
test_project()
test_join1()
test_join2()
