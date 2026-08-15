"""
Denna fil innehÃ¥ller ett antal lÃ¶sningsfÃ¶rslag fÃ¶r tentan i TDDE24 januari 2024.

Det finns alltid mÃ¥nga olika sÃ¤tt att lÃ¶sa en uppgift, och bara fÃ¶r att
lÃ¶sningsfÃ¶rslaget ser ut pÃ¥ ett visst sÃ¤tt betyder det inte att detta Ã¤r
det enda, eller ens det allra bÃ¤sta sÃ¤ttet att lÃ¶sa en uppgift.
"""

import math


def facit_sums(seq: list[int]):
    sum_so_far = 0
    results = []
    for element in seq:
        sum_so_far += element
        results.append(sum_so_far)

    return results


def facit_merge(s1: list, s2: list):
    result = []
    while True:
        if s1 and s2:
            if s1[0] < s2[0]:
                result.append(s1[0])
                s1 = s1[1:]
            else:
                result.append(s2[0])
                s2 = s2[1:]
        elif s1:
            result.append(s1[0])
            s1 = s1[1:]
        elif s2:
            result.append(s2[0])
            s2 = s2[1:]
        else:
            return result


def facit_without(nest: list, to_remove: list):
    result = []
    for element in nest:
        if isinstance(element, list):
            result.append(facit_without(element, to_remove))
        elif element not in to_remove:
            result.append(element)

    return result


def facit_split_at(seq, pred):
    result = []

    # Elementen som ska hamna i nÃ¤sta dellista
    sublist = []

    for element in seq:
        if pred(element):
            # Splitta hÃ¤r -- lÃ¤gg till den nuvarande dellistan
            # och nollstÃ¤ll den
            result.append(sublist)
            sublist = []
        else:
            # FortsÃ¤tta bygga upp dellistan
            sublist.append(element)

    # Nu har vi en allra sista dellista som ska lÃ¤ggas till
    # i slutet
    result.append(sublist)

    return result


def facit_split_at_2(seq, pred):
    result = [[]]
    for element in seq:
        if pred(element):
            result.append([])
        else:
            result[-1].append(element)
    return result


def facit_add_for_each(seq: list, func):
    sum_so_far = 0
    for element in seq:
        sum_so_far += func(element)
    return sum_so_far


def facit_is_prime(n: int):
    if n < 2:
        return False
    for divisor in range(2, int(math.sqrt(n)) + 1):
        if n % divisor == 0:
            return False
    return True


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
            if n % divisor == 0 and facit_is_prime(divisor):
                factors.append(divisor)
                n //= divisor
    return factors


def facit_is_attractive(n: int):
    return facit_is_prime(len(facit_prime_factors(n)))


def facit_create_trie() -> tuple[bool, dict]:
    return False, {}


def facit_add_word(trie: tuple[bool, dict], word):
    if not word:
        # Basfall: Vi Ã¤r klara.  (Uppgiften Ã¤r att lÃ¤gga till ett ord som
        # Ã¤r en icke-tom strÃ¤ng, sÃ¥ vi mÃ¥ste ha rekurserat hit.)
        return

    # Hitta fÃ¶rsta bokstaven och resten av ordet.
    head, tail = word[0], word[1:]

    # VÃ¤lj korrekt gren frÃ¥n barnen till denna nod.
    # Noden Ã¤r en tupel bestÃ¥ende av en flagga (kan ett ord sluta hÃ¤r?) och
    # en dictionary fÃ¶r barnen ({bokstav1: deltrÃ¤d, bokstav2: deltrÃ¤d, ...).
    ends, children = trie
    if head not in children:
        # MÃ¥ste skapa ett nytt barn fÃ¶r den givna bokstaven
        children[head] = facit_create_trie()

    if not tail:
        # SÃ¤tt flaggan som talar om att ordet slutar efter head.
        # Eftersom vi anvÃ¤nde en tupel, som inte kan Ã¤ndras, mÃ¥ste vi skapa
        # en ny tupel med True som flagga men med den gamla grenen.
        children[head] = (True, children[head][1])

    # Add the remaining characters of the word
    facit_add_word(children[head], tail)


def facit_word_in_trie(trie, word):
    # Empty words are not words.
    if not word:
        return False

    head, tail = word[0], word[1:]
    ends, lookup = trie

    if head not in lookup:
        return False

    branch = lookup[head]

    # If this is the last letter of the word, return true if this node
    # is the end of a word, false otherwise.
    if len(word) == 1:
        return branch[0]

    # Keep following the graph until the end of the word
    return facit_word_in_trie(branch, word[1:])


def facit_find_all_matches(trie, prefix):
    result = set()
    # Match this node if a word ends here and there is no prefix.
    if trie[0] is True and prefix == '':
        result.add('')
    # Match the branch of next character.
    if prefix and prefix[0] in trie[1]:
        for match in facit_find_all_matches(trie[1][prefix[0]], prefix[1:]):
            result.add(prefix[0] + match)

    # Match all branches if there is no prefix.
    if not prefix:
        for char, branch in trie[1].items():
            for match in facit_find_all_matches(branch, ''):
                result.add(char + match)

    return result
