"""
Denna fil innehÃ¥ller ett antal lÃ¶sningsfÃ¶rslag fÃ¶r tentan i TDDE24 mars 2021.

Det finns alltid mÃ¥nga olika sÃ¤tt att lÃ¶sa en uppgift, och bara fÃ¶r att
lÃ¶sningsfÃ¶rslaget ser ut pÃ¥ ett visst sÃ¤tt betyder det inte att detta Ã¤r
det enda, eller ens det allra bÃ¤sta sÃ¤ttet att lÃ¶sa en uppgift.
"""


def facit_cut_sequence_at(seq, pred):
    """ Docs here, docs here, docs here, docs here, docs here, docs here """
    result = []
    subresult = []
    for element in seq:
        if subresult and pred(element):
            result.append(subresult)
            subresult = []
        subresult.append(element)
    result.append(subresult)
    return result


def facit_cut_sequence_recursively(seq, pred):
    """ Docs here, docs here, docs here, docs here, docs here, docs here """

    if not seq:
        # Base case
        return [[]]
    if len(seq) == 1:
        # Base case 2:  There's only one element
        return [[seq[0]]]

    first = seq[0]

    # Because of our base cases, we only recurse
    # if we have at least 2 elements to start with,
    # so we have at least 1 element in the result
    subresult = facit_cut_sequence_recursively(seq[1:], pred)

    # Suppose we cut at odd elements
    # If the result was [[2],[3,4]], then first_list is [2]
    first_list = subresult[0]

    if pred(first_list[0]):
        # If the first element in the *result* satisfied the predicate,
        # then that element should be in a new sublist,
        # so our "first" element should *not* be in the same list
        return [[first]] + subresult
    else:
        # The first element in the result should not start a new list,
        # so our "first" element should be in the same list
        return [[first] + first_list] + subresult[1:]


def facit_cut_sequence_and_wrap(seq, pred):
    result = []
    while seq:
        element = seq[0]
        if result and pred(element):
            result.append(facit_cut_sequence_and_wrap(seq, pred))
            return result
        result.append(element)
        seq = seq[1:]
    return result


def facit_flatten(nest):
    result = []
    for element in nest:
        if isinstance(element, list):
            result.extend(facit_flatten(element))
        else:
            result.append(element)
    return result


def facit_median_of_flat_int_list(flat):
    ordered = sorted(flat)
    n = len(ordered)
    if n % 2 == 0:
        # JÃ¤mnt
        return (ordered[n // 2 - 1] + ordered[n // 2]) / 2
    else:
        return ordered[n // 2]


def facit_nested_median(nest):
    """ Docs here, docs here, docs here, docs here, docs here, docs here """

    flat = facit_flatten(nest)
    only_ints = filter(lambda x: isinstance(x, int), flat)
    return facit_median_of_flat_int_list(only_ints)


def min_jumps(seq):
    pos = 0

    if len(seq) == 0:
        # There is no solution:  We can never reach pos == len(seq)-1 == 0-1 == -1
        return None

    if len(seq) == 1:
        # This is already a solution:  We have pos == len(seq)-1 == 1-1 == 0, so no steps are required
        return ()

    alternatives = []

    if pos + 1 < len(seq):
        alternatives.append(('+1',) + min_jumps(seq[1:]))
    if pos + 2 < len(seq):
        alternatives.append(('+2',) + min_jumps(seq[2:]))
    if pos + seq[pos] < len(seq):
        alternatives.append(('+k',) + min_jumps(seq[seq[pos]:]))

    shortest = min(alternatives, key=lambda x: len(x))

    return shortest


def facit_prime(n):
    """
    Docstring docstring docstring docstring docstring docstring
    """
    # Nothing smaller than 2 is a prime
    if n < 2:
        return False
    # If it's divisible by a number smaller than its square root: Not a prime
    # Must add 1 when we use range, since range excludes the 'stop' number;
    # this is easily seen when you test prime(4)
    for k in range(2, int(sqrt(n)) + 1):
        if n % k == 0:
            return False

    # OK, a prime
    return True


def facit_compute_factors(num):
    """
    Prime factorization for numbers num >= 2
    """
    assert num >= 2

    factors = []

    # Let's start testing the smallest prime
    factor = 2

    # While we still have factors left to return
    while num > 1:
        if num % factor == 0:
            # It's divisible by factor
            factors.append(factor)
            num /= factor
        else:
            # Not divisible with factor; step up to the next prime
            factor += 1
            while not facit_prime(factor):
                factor += 1

    return factors


def facit_make_int_list():
    return []


def facit_add_int(int_list, num):
    factors = facit_compute_factors(num)

    int_list.append({factor: len([f for f in factors if f == factor]) for factor in set(factors)})


def facit_get_int(int_list, pos):
    result = 1
    for factor, exponent in int_list[pos].items():
        result *= factor ** exponent
    return result


def facit_square_all(int_list):
    for entry in int_list:
        for key, value in entry.items():
            entry[key] = value * 2
