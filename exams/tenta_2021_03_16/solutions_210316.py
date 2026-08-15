"""
Denna fil innehÃ¥ller ett antal lÃ¶sningsfÃ¶rslag fÃ¶r tentan i TDDE24 mars 2021.

Det finns alltid mÃ¥nga olika sÃ¤tt att lÃ¶sa en uppgift, och bara fÃ¶r att
lÃ¶sningsfÃ¶rslaget ser ut pÃ¥ ett visst sÃ¤tt betyder det inte att detta Ã¤r
det enda, eller ens det allra bÃ¤sta sÃ¤ttet att lÃ¶sa en uppgift.
"""


def facit_fib(k):
    if k == 0:
        return 0
    elif k == 1 or k == 2:
        return 1
    else:
        return facit_fib(k - 1) + facit_fib(k - 2)


def facit_split_fib(s: str):
    words = s.split(" ")
    ret = []
    k = 0
    while words:
        num_words = facit_fib(k + 1)
        ret.append(words[:num_words])
        # Man kan antingen hÃ¥lla reda pÃ¥ index fÃ¶r nÃ¤sta "startplats"
        # eller som hÃ¤r "ta bort" de ord som man redan har plockat ut.
        words = words[num_words:]
        k += 1
    return ret


def facit_nth_sums(seq):
    result = []
    # FÃ¶r alla startpositioner i sekvensen
    for k in range(len(seq)):
        # Hitta tal med *bÃ¶rjan* pÃ¥ position k, och med k+1 steg mellan talen
        # (man kan ocksÃ¥ skriva detta som en loop som bÃ¶rjar pÃ¥ position k
        #  och stegar upp med k+1 i varje steg).
        values_to_add = seq[k::k + 1]
        result.append(sum(values_to_add))

    return result


def facit_nth_sums_lc(seq):
    # Shouldn't actually return the first part; this is for debugging
    # return [seq[k::k + 1] for k in range(len(seq))], [sum(seq[k::k + 1]) for k in range(len(seq))]
    return [sum(seq[k::k + 1]) for k in range(len(seq))]


def facit_find_nested(nl, pred, n):
    # To keep things simpler, recursively find ALL positions of matching
    # elements, then determine how many there are.
    # Temporarily use a list to construct the position (could also start
    # with a tuple immediately)

    result = facit_find_nested_rec(nl, pred, [])
    if len(result) >= n:
        return result[:n]
    else:
        return None, None


def facit_find_nested_rec(nl, pred, pos):
    result = []
    # Traverse left to right on this level of the list
    for index, element in enumerate(nl):
        pos_of_this_element = pos + [index]
        if isinstance(element, list):
            # Traverse "downwards" into the list element using recursion
            # In the recursive call, pos_of_this_element is the position of
            # the *list*
            subresult = facit_find_nested_rec(element, pred, pos_of_this_element)
            result += subresult
        elif pred(element):
            # Predicate satisfied, convert the list to a tuple
            result.append(tuple(pos_of_this_element))
        else:
            # Not a list and didn't satisfy the predicate; skip it
            pass
    return result


def facit_new_listdict():
    return ListDict([])


def facit_listdict_put(ld: ListDict, key, value):
    for element in ld.pairs:
        if element.key == key:
            element.value = value
            return

    # Didn't exist
    ld.pairs.append(KeyValue(key, value))


def facit_listdict_get(ld: ListDict, key, default):
    for element in ld.pairs:
        if element.key == key:
            return element.value

    return default


def facit_listdict_delete(ld: ListDict, key):
    for index, element in enumerate(ld.pairs):
        if element.key == key:
            del ld.pairs[index]
            return True

    return False


def facit_listdict_contains(ld: ListDict, key):
    for element in ld.pairs:
        if element.key == key:
            return True

    return False


def facit_listdict_values(ld: ListDict):
    return set(element.value for element in ld.pairs)


def facit_listdict_from(map):
    ld = facit_new_listdict()
    for key, value in map.items():
        facit_listdict_put(ld, key, value)
    return ld


def facit_listdict_update(ld_to: ListDict, ld_from: ListDict):
    for element in ld_from.pairs:
        facit_listdict_put(ld_to, element.key, element.value)


def facit_listdict_add_value(ld: ListDict, key, value):
    for element in ld.pairs:
        if element.key == key:
            if isinstance(element.value, list):
                element.value.append(value)
                return
            else:
                raise TypeError

    # Didn't find it
    facit_listdict_put(ld, key, value)


def facit_listdict_internal_sort(ld: ListDict, pred):
    ld.pairs.sort(key=lambda e: e.key)


def facit_is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True

    for div in range(2, int(math.sqrt(n)) + 1):
        if n % div == 0:
            # Delbart
            return False

    return True


def facit_split_in_primes_3_wrong(n: int):
    res = facit_split_in_primes_n(n)
    if len(res) <= 3:
        return res
    else:
        return None, None


def facit_split_in_primes_3_complex(n: int):
    numstring = str(n)
    for split1 in range(0, len(numstring) + 1):
        part1 = numstring[0:split1]
        if split1 == 0 or facit_is_prime(int(part1)):
            for split2 in range(split1, len(numstring) + 1):
                part2 = numstring[split1:split2]
                if split2 == split1 or facit_is_prime(int(part2)):
                    part3 = numstring[split2:len(numstring) + 1]
                    if split2 == len(numstring) or facit_is_prime(int(part3)):
                        numbers = []
                        if split1 != 0:
                            numbers.append(int(part1))
                        if split2 != split1:
                            numbers.append(int(part2))
                        if len(numstring) != split2:
                            numbers.append(int(part3))

                            return numbers
    return None, None


def facit_split_in_primes_3(n: int):
    # In this suggested solution we have separate checks for dividing
    # the number into 1, 2 or 3 primes.  This requires a bit more
    # time when the code is executed, and makes the code longer, but
    # results in a somewhat simpler structure.

    # Can we "split" into *one* part?  Test the entire number.
    if facit_is_prime(n):
        return [n]

    # OK, it would need to be split, so convert it to a string.
    numstring = str(n)

    # All positions where we can split numstring into *two*
    # non-empty parts.  Start at 1 because we want at least 1
    # digit in the first number.  The end index is excluded, so
    # looping until len(numstring) leaves at least 1 digit in the
    # second number.
    for pos1 in range(1, len(numstring)):
        num1 = int(numstring[:pos1])
        num2 = int(numstring[pos1:])
        if facit_is_prime(num1) and facit_is_prime(num2):
            return [num1, num2]

    # All ways of splitting numstring into *three* parts.  This
    # could also be shortened by integrating it with the previous
    # loop.

    for pos1 in range(1, len(numstring)):
        num1 = int(numstring[0:pos1])
        if facit_is_prime(int(num1)):
            # First part was a prime, so let's split remaining into
            # another two parts
            remaining = numstring[pos1:]
            for pos2 in range(1, len(remaining)):
                num2 = int(remaining[:pos2])
                num3 = int(remaining[pos2:])

                if facit_is_prime(num2) and facit_is_prime(num3):
                    return [num1, num2, num3]

    # Tried everything
    return None, None


def facit_split_in_primes_n(n: int):
    assert "0" not in str(n)

    def mysplit(digits: str):
        # Hur mÃ¥nga siffror vill vi ha med i vÃ¥rt fÃ¶rsta tal?
        # Var som helst
        for prefix_length in range(1, len(digits) + 1):

            # Dela upp i fÃ¶rsta talet och resten av strÃ¤ngen
            first_number = int(digits[:prefix_length])
            rest = digits[prefix_length:]

            if facit_is_prime(first_number):
                # OK, med denna prefixlÃ¤ngd blev fÃ¶rsta talet ett primtal.

                if not rest:
                    # Vi har konsumerat hela strÃ¤ngen.
                    return [first_number]

                # OK, sÃ¥ vi har en sifferstrÃ¤ng kvar att fÃ¶rsÃ¶ka dela upp.
                rest_result = mysplit(rest)

                if rest_result == (None, None):
                    # Det gick inte att dela upp resten i primtal.
                    # FortsÃ¤tt med nÃ¤sta "lÃ¤ngd"
                    pass
                else:
                    # OK, vi har fÃ¥tt ett primtal i first_number och
                    # ett eller flera primtal i rest_result.
                    return [first_number] + rest_result

        # Fungerade inte fÃ¶r nÃ¥gon lÃ¤ngd pÃ¥ fÃ¶rsta talet.
        return None, None

    return mysplit(str(n))
