"""
Denna fil innehÃ¥ller ett antal lÃ¶sningsfÃ¶rslag fÃ¶r tentan i TDDE24 mars 2022.

Det finns alltid mÃ¥nga olika sÃ¤tt att lÃ¶sa en uppgift, och bara fÃ¶r att
lÃ¶sningsfÃ¶rslaget ser ut pÃ¥ ett visst sÃ¤tt betyder det inte att detta Ã¤r
det enda, eller ens det allra bÃ¤sta sÃ¤ttet att lÃ¶sa en uppgift.
"""


def facit_split_by_first(seq: list[str]):
    result = dict()
    for word in seq:
        key = word[0]
        if key in result:
            result[key].append(word)
        else:
            result[key] = [word]
    return result


def facit_merge_i(s1: list, s2: list):
    result = []
    while True:
        if s1:
            if s2:
                if s1[0] < s2[0]:
                    result.append(s1[0])
                    # Changes a pointer, doesn't change the actual list
                    s1 = s1[1:]
                else:
                    result.append(s2[0])
                    s2 = s2[1:]
            else:
                result.append(s1[0])
                s1 = s1[1:]
        else:
            # not s1
            if s2:
                result.append(s2[0])
                s2 = s2[1:]
            else:
                return result


def facit_merge_r(s1, s2):
    return facit_merge_i(s1, s2)


def facit_add_nested(seq1: list, seq2: list):
    result = []
    for index, element1 in enumerate(seq1):
        element2 = seq2[index]
        if isinstance(element1, list):
            # Rekursera ner i listor fÃ¶r att behandla deras element
            result.append(facit_add_nested(element1, element2))
        else:
            # Allt annat Ã¤r bara godtyckliga element som "kopieras Ã¶ver"
            result.append(element1 + element2)
    return result


def facit_make_val_finder(val):
    def finder(seq):
        return val in seq

    return finder


facit_contains_14 = facit_make_val_finder(14)


def facit_rows(matrix):
    """Returns the number of rows in the matrix"""
    return len(matrix)


def facit_columns(matrix):
    """Returns the number of columns in the matrix"""
    return len(matrix[0])


def facit_transpose(matrix):
    """Returns the matrix transposed, meaning the columns and the row have been switched"""
    return [[row[i] for row in matrix] for i in range(columns(matrix))]


def facit_map(matrix, fun):
    """Applies the function (fun) to each number in the matrix, then returns the new matrix"""
    return [[fun(row[i]) for i in range(columns(matrix))] for row in matrix]


def facit_plus(matrix1, matrix2):
    """Adds matrix1 and matrix2, then returns the result.
    Adding means each number in matrix1 gets added with the number of the corresponding position in matrix2"""
    return [[matrix1[j][i] + matrix2[j][i] for i in range(columns(matrix1))] for j in range(rows(matrix1))]


def facit_times(matrix1, matrix2):
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


def facit_is_anagram(word1: str, word2: str):
    return sorted(word1) == sorted(word2) and word1 != word2


def facit_is_deranged_anagram(word1: str, word2: str):
    return facit_is_anagram(word1, word2) and all(
        ch1 != ch2 for ch1, ch2 in zip(word1, word2)
    )


def facit_all_anagrams(word: str):
    # import time
    # start = time.time()

    if not word:
        return []

    def all_unfiltered_anagrams(word: str):
        if len(word) == 1:
            return [word[0]]
        else:
            words = set()
            for pos in range(len(word)):
                for subresult in all_unfiltered_anagrams(word[:pos] + word[pos + 1:]):
                    words.add(word[pos] + subresult)
            return words

    result = all_unfiltered_anagrams(word)
    result.remove(word)
    result = list(result)
    result = sorted(result)  # To provide a sorted facit
    # end = time.time()
    # print(end - start)
    return result


def all_anagrams_2(word: str):
    # import time
    # start = time.time()
    result = set()
    for perm in itertools.permutations(word, len(word)):
        result.add("".join(perm))
    result.remove(word)
    result = list(result)
    # end = time.time()
    # print(end - start)
    return result


def facit_all_deranged_anagrams(word: str):
    return [anag for anag in facit_all_anagrams(word) if facit_is_deranged_anagram(anag, word)]
