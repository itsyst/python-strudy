def anagrams(s):
    if len(s) == 1:
        return [s]
    result = []
    for i, letter in enumerate(s):
        remaining = s[:i] + s[i+1:]
        for anagram in anagrams(remaining):
            result.append(letter + anagram)
    return result


word = 'abc'
gram = anagrams(word)
print(gram)
