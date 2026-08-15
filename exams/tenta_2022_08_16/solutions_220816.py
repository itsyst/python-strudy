"""
Denna fil innehÃ¥ller ett antal lÃ¶sningsfÃ¶rslag fÃ¶r tentan i TDDE24 augusti 2022.

Det finns alltid mÃ¥nga olika sÃ¤tt att lÃ¶sa en uppgift, och bara fÃ¶r att
lÃ¶sningsfÃ¶rslaget ser ut pÃ¥ ett visst sÃ¤tt betyder det inte att detta Ã¤r
det enda, eller ens det allra bÃ¤sta sÃ¤ttet att lÃ¶sa en uppgift.
"""


def facit_doors():
    is_open = []
    for i in range(100):
        for doornum in range(i + 1, 101, i + 1):
            if doornum in is_open:
                is_open.remove(doornum)
            else:
                is_open.append(doornum)
    return sorted(is_open)


def facit_fusc_r(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 == 0:
        return facit_fusc_r(n // 2)
    else:
        return facit_fusc_r((n - 1) // 2) + facit_fusc_r((n + 1) // 2)


def facit_fusc_i(n: int):
    if n == 0:
        return 0

    fuscs = [0, 1]
    for n in range(2, n + 1):
        if n % 2 == 0:
            fuscs.append(fuscs[n // 2])
        else:
            fuscs.append(fuscs[(n - 1) // 2] + fuscs[(n + 1) // 2])
    return fuscs[-1]


def facit_greater_nested(seq1: list, seq2: list) -> set:
    result = set()
    for index, element1 in enumerate(seq1):
        element2 = seq2[index]
        if isinstance(element1, list):
            # Rekursera ner i listor fÃ¶r att behandla deras element
            result.update(facit_greater_nested(element1, element2))
        elif element1 > element2:
            result.add(element1)
    return result


def facit_curry(fn, v1):
    def newfun(v2):
        return fn(v1, v2)

    return newfun


facit_pow2 = facit_curry(math.pow, 2)


def facit_create_trie() -> tuple[bool, dict]:
    return False, {}


def facit_add_word(trie: tuple[bool, dict], word):
    if not word:
        return

    # Separate the first character from the rest
    head, tail = word[0], word[1:]

    # Select the correct existing branch or create it if missing
    _, lookup = trie
    if head in lookup:
        branch = lookup[head]
    else:
        branch = facit_create_trie()
        lookup[head] = branch

    # If the word ends, mark that last node as being the end of a word
    if len(word) == 1:
        lookup[head] = (True, branch[1])

    # Add the remaining characters of the word
    facit_add_word(branch, tail)


def facit_word_in_trie(trie, word):
    # Empty words are not words.
    if not word:
        return False

    head, tail = word[0], word[1:]
    ends, lookup = trie

    if head not in lookup:
        return False

    branch = lookup[head]

    # If this is the last letter of the word, return whether this node
    # is the end of a word.
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


def facit_rle(seq):
    result = []
    for element in seq:
        if not result:
            result.append((1, element))
        else:
            last = result[-1]
            if last[1] == element:
                result[-1] = (last[0] + 1, last[1])
            else:
                result.append((1, element))
    return result
