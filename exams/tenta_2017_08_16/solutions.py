# Example solutions to the exam 2017-08-16
# Erik Hansson / Fredrik Heintz 2017-08-16



# Uppgift 1

def collatz(n):
    """
    Calculate the collatz serie.
    :param n: the starting number of the collatz serie
    """
    res = [n]
    while n != 1:
        if n%2 == 1:
            n = n*3 + 1
        else:
            n = n//2
        res.append(n)
    return res

assert collatz(6) == [6, 3, 10, 5, 16, 8, 4, 2, 1]
assert collatz(7) == [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert collatz(13) == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]



# Uppgift 2

def reverse_r(items):
    """
    Creates a new list with the reveresed order of the imput list
    :param items: the input that is to be reversed.
    :type items: list
    """
    if not items:
        return []
    else:
        return reverse_r(items[1:]) + [items[0]]

assert reverse_r([]) == []
assert reverse_r([1]) == [1]
assert reverse_r(['a', 'b']) == ['b', 'a']
assert reverse_r([1, 3, 5]) == [5, 3, 1]
assert reverse_r([2, 8, 4, 6]) == [6, 4, 8, 2]


def reverse_i(items):
    """
    Creates a new list with the reveresed order of the imput list
    :param items: the input that is to be reversed.
    :type items: list
    """
    _reversed = []
    for i in range(len(items)-1, -1, -1):
        _reversed.append(items[i])
    return _reversed

assert reverse_i([]) == []
assert reverse_i([1]) == [1]
assert reverse_i(['a', 'b']) == ['b', 'a']
assert reverse_i([1, 3, 5]) == [5, 3, 1]
assert reverse_i([2, 8, 4, 6]) == [6, 4, 8, 2]



# Uppgift 3

# maps the input function to all the elements in the list
# and then takes sums all the results
add_for_each = lambda collection, fn: sum([fn(item) for item in collection])

# Calculates the avergage of all the maximum values
average_max = lambda collection: add_for_each(collection, max)/len(collection)

assert add_for_each([1, 2, 3, 4], lambda x: x**2) == 30
assert add_for_each([[1, 2, 3], [1], [1, 2, 3, 4]], lambda x: len(x)) == 8
temp = [[12,13,15,11], [8,9,10], [5,7,6], [8,9,11,10], [3,5,5,2]]
average_max(temp) == 9.6



# Uppgift 4

def palindrom(items):
    """
    Checks if the given items are a palindrom
    :param items: input that is to be checked if it's a palindrom
    :type items: list
    """
    if len(items) == 0:
        return True
    elif len(items) == 1:
        return not isinstance(items[0], list) or palindrom(items[0])
    else:
        left = items[0]
        right = items[-1]
        if isinstance(left, list) and isinstance(right, list):
            return len(left) == len(right) and palindrom(left + right) and \
                palindrom(items[1:-1])
        elif type(left) != type(right):
            return False
        else:
            return left == right and palindrom(items[1:-1])

assert palindrom([])
assert palindrom([1])
assert palindrom([1, 1])
assert palindrom([1, 1, 1])
assert palindrom([1, 1, 1, 1])
assert palindrom([[1], [2], [1]])
assert palindrom([[2, 2]])
assert palindrom([[[3], [3]]])
assert palindrom([[[[4]], [[4]]]])
assert not palindrom([[[[4]], [4]]])
assert not palindrom([1, 2])
assert not palindrom([[1], 1])
assert not palindrom([1, [1]])
assert palindrom([[1, 2, 3], 2, [7], 2, [3, 2, 1]])
assert not palindrom([[1, 2, 3]])



# Uppgift 5

def ancestors(person, tree):
    """
    Finds the ancestors of person.
    :param person: The person
    :type person: str
    :param tree: the familiy tree
    :type tree: list
    """
    if isinstance(tree, str):
        if person == tree:
            return [person]
        else:
            return []
    else:
        parent = tree[0]
        children = tree[1:]
        if parent == person:
            return [parent]
        else:
            for child in children:
                line = ancestors(person, child)
                if line != []:
                    return [parent] + line
            return []

svensson = ['Erik', ['Olle', ['Eva', 'Karin', 'Anna'],
                     ['Lars', 'Maria'],
                     ['Per', 'Sofia']],
            'Lisa',
            ['Stina', ['Gunnar', 'Lasse'],
             'Lennart']]

assert ancestors('Maria', svensson) == ['Erik', 'Olle', 'Lars', 'Maria']
assert ancestors('Erik', svensson) == ['Erik']
assert ancestors('Gunnar', svensson) == ['Erik', 'Stina', 'Gunnar']
assert ancestors('Barbro', svensson) == []



# Uppgift 6
from functools import reduce

def create_bag():
    """
    Creates a new bag
    :return: the new bag
    :type return: bag-type
    """
    return []


def add_element(b, x):
    """
    Adds an element to the bag functionally
    :param b: the bag
    :type b: bag-type
    :param x: The element that is to be added
    :return: the updated bag
    :type return: bag-type
    """
    return b + [x]


def remove_element(b, x):
    """
    Removes an occurance of an element to the bag functionally
    :param b: the bag
    :type b: bag-type
    :param x: The element that is to be removed
    :return: The updated bag
    :type return: bag-type
    """
    return [e for e in b[:b.index(x)+1] if e != x] + b[b.index(x)+1:]


def contains(b, x):
    """
    Checks of a bag contains at least one of the item
    :param b: the bag
    :type b: bag-type
    :param x: The item to be checked if it exists in the bag
    :type return: boolean
    """
    return x in b


def count(b, x):
    """
    Counts how many occurances of x that is in the bag
    :param b: the bag
    :type b: bag-type
    :param x: The item
    :type return: int
    """
    return b.count(x)


def is_sub_bag(b1, b2):
    """
    Checks if all items in b1 exists in b2 note that the count of the
    items are taken into consideration
    :param b1: the potential sub-bag
    :param b2: the potential super-bag
    :type b1, b2: bag-type
    :type return: boolean
    """
    return reduce(lambda x, y: x and y,
                  [count(b1, e) <= count(b2, e) for e in b1], True)


def bag_union(b1, b2):
    """
    Creates a union of two bags
    :param b1: the first bag
    :param b2: the second bag
    :type b1, b2: bag-type
    :return: the union of b1 and b2
    :type return: bag-type
    """
    return b1 + b2


def get_elements(b):
    """
    Gets all the elements in the bag as a sorted list
    :param b: the bag
    :type b: bag-type
    :type return: list
    """
    return sorted(b)


b1 = create_bag()
b1 = add_element(b1, 1)
b1 = add_element(b1, 1)
assert get_elements(b1) == [1, 1]
assert contains(b1, 1)
assert not contains(b1, "hej")
b2 = create_bag()
b2 = add_element(b2, 1)
assert is_sub_bag(b2, b1)
b2 = add_element(b2, 2)
assert not is_sub_bag(b2, b1)
b3 = bag_union(b1, b2)
assert get_elements(b3) == [1, 1, 1, 2]
b1 = remove_element(b1, 1)
assert get_elements(b1) == [1]
assert is_sub_bag(b1, b2)
b4 = add_element(b1, 2)
assert get_elements(b1) != get_elements(b4)
