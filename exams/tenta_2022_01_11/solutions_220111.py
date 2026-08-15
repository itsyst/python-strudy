"""
Denna fil innehÃ¥ller ett antal lÃ¶sningsfÃ¶rslag fÃ¶r tentan i TDDE24 januari 2022.

Det finns alltid mÃ¥nga olika sÃ¤tt att lÃ¶sa en uppgift, och bara fÃ¶r att
lÃ¶sningsfÃ¶rslaget ser ut pÃ¥ ett visst sÃ¤tt betyder det inte att detta Ã¤r
det enda, eller ens det allra bÃ¤sta sÃ¤ttet att lÃ¶sa en uppgift.
"""


def facit_gapful(n: int):
    digits = str(n)
    divisor = int(digits[0] + digits[-1])
    return n % divisor == 0


def facit_reverse_pairs(seq: list):
    result = []

    for pos in range(0, len(seq), 2):
        if pos + 1 < len(seq):
            result.append(seq[pos + 1])
        result.append(seq[pos])

    return result


def facit_reverse_pairs_r(seq: list):
    if not seq:
        return []
    elif len(seq) == 1:
        return seq
    else:
        return [seq[1], seq[0]] + facit_reverse_pairs_r(seq[2:])


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


def facit_multiple_apply(fn, times: int):
    def retfun(x):
        for k in range(times):
            x = fn(x)
        return x

    return retfun


def facit_pow2(n: int):
    return facit_multiple_apply(lambda y: 2 * y, n)(1)


def facit_pow2mult(n: int, c: int):
    multiplier = facit_multiple_apply(lambda y: 2 * y, n)
    return multiplier(c)


def facit_is_prime(n: int):
    if n < 2:
        return False
    for divisor in range(2, int(math.sqrt(n)) + 1):
        if n % divisor == 0:
            return False
    return True


def facit_is_prime_2(n: int):
    return n >= 2 and all(n % divisor != 0 for divisor in range(2, int(math.sqrt(n)) + 1))


def facit_prime_factors(n: int):
    # This isn't efficient for larger numbers, but that wasn't required.
    # Could also use a sieve to find primes, or more advanced methods.
    factors = []
    prime = 2
    while n != 1:
        if n % prime == 0:
            factors.append(prime)
            n /= prime
            # Iterate and try the same factor again
        else:
            # Find next prime
            prime += 1
            while not facit_is_prime(prime):
                prime += 1
    return factors


def facit_prime_factors_2(n: int):
    factors = []
    while n != 1:
        for divisor in range(1, n + 1):
            if n % divisor == 0 and is_prime(divisor):
                factors.append(divisor)
                n //= divisor
    return factors


def facit_is_attractive(n: int):
    return facit_is_prime(len(facit_prime_factors(n)))


def facit_all_splits(seq):
    if not seq:
        return [([], [])]

    ret = []
    for seq1, seq2 in facit_all_splits(seq[1:]):
        ret.append((seq1 + [seq[0]], seq2))
        ret.append((seq1, seq2 + [seq[0]]))

    return ret


def facit_minimize_differences(seq: list[int]):
    splits = facit_all_splits(seq)
    best = splits[0]
    best_diff = abs(sum(best[0]) - sum(best[1]))

    for candidate in splits[1:]:
        candidate_diff = abs(sum(candidate[0]) - sum(candidate[1]))
        if candidate_diff < best_diff:
            best_diff = candidate_diff
            best = candidate

    return best


def facit_minimize_differences_2(seq: list[int]):
    return min(facit_all_splits(seq), key=lambda p: abs(sum(p[0]) - sum(p[1])))
