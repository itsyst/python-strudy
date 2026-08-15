"""
HÃ¤r finns ett antal testfall fÃ¶r uppgifter i en tenta i TDDE24.

Testfallen Ã¤r skapade frÃ¥n anrop till ett egenutvecklat testramverk, som
ocksÃ¥ samlar ihop testresultat och kategoriserar olika problem som kan
uppstÃ¥.  De har alltsÃ¥ inte kÃ¶rts exakt sÃ¥ som de stÃ¥r hÃ¤r.

Som en hjÃ¤lp finns lÃ¶sningsfÃ¶rslagen med i filen.  ErsÃ¤tt dem med egna
lÃ¶sningar och kÃ¶r filen i Python 3.11 (python test.py) fÃ¶r att se om du har
nÃ¥gra fel och i sÃ¥ fall var.  Du kan gÃ¤rna lÃ¥ta lÃ¶sningsfÃ¶rslagen ligga
kvar, men lÃ¤gg dÃ¥ dina egna lÃ¶sningar *efter* lÃ¶sningsfÃ¶rslagen i filen.
Det Ã¤r den sista definitionen innan sjÃ¤lva testfallen som testas!

NÃ¤r du tittar pÃ¥ felaktiga och korrekta svar, kom dÃ¥ ihÃ¥g att ett svar kan
vara korrekt trots att det inte ser identiskt ut!  Till exempel Ã¤r {1,2}
samma som {2,1}, eftersom mÃ¤ngder inte har nÃ¥gon ordning.  PÃ¥ samma sÃ¤tt Ã¤r
{1: 42, 2: 11} samma som {2: 11, 1: 42}, eftersom mÃ¤ngder inte har nÃ¥gon
ordning, och True==1, och 1==(1+0j) om vi anvÃ¤nder komplexa tal.



FÃ¶r vissa uppgifter finns vÃ¤ldigt mÃ¥nga testfall.  De allra flesta problem
som vi ser i inlÃ¤mningarna skulle ha upptÃ¤ckts med en *mycket* mindre
uppsÃ¤ttning testfall, som inte alls hade tagit mycket tid att skapa.  Att
vi anvÃ¤nder sÃ¥ mÃ¥nga testfall beror pÃ¥ att det underlÃ¤ttar nÃ¤r man har
mÃ¥nga inlÃ¤mningar som inte bara ska granskas utan Ã¤ven betygsÃ¤ttas:

1) Vi anvÃ¤nder inte bara testfall fÃ¶r att *upptÃ¤cka* problem utan ocksÃ¥
fÃ¶r att gruppera och *kategorisera* dem.  FÃ¶r er kan det gÃ¥ snabbare att
hitta exakt vad felet var genom att gÃ¥ genom er egen kod noggrannt.  FÃ¶r
oss kan det gÃ¥ snabbare att skriva extra testfall sÃ¥ vi kan se mÃ¶nster i
alla inlÃ¤mningar: 'NÃ¤r dessa 17 testfall misslyckas, men inte de andra 83
testfallen, brukar det bero pÃ¥ ...'.

2) Vi mÃ¥ste lÃ¤gga ner mycket arbete pÃ¥ att bedÃ¶ma alla pÃ¥ ett likvÃ¤rdigt
sÃ¤tt, med likvÃ¤rdiga poÃ¤ng.  Att ha mÃ¥nga testfall hjÃ¤lper oss att fÃ¥ en
*konsistent* bedÃ¶mning av alla inlÃ¤mningar.

3) Det finns *vÃ¤ldigt* mÃ¥nga sÃ¤tt att lÃ¶sa en uppgift, och tanken bakom
en lÃ¶sning Ã¤r ofta inte uppenbar fÃ¶r den som inte skrev den.  Medan
fÃ¶rfattaren Ã¤ven kan felsÃ¶ka sin egen *idÃ©* om hur lÃ¶sningen ska fungera,
har vi bara tillgÃ¥ng till programkoden och behÃ¶ver fler testfall fÃ¶r att
fÃ¶rstÃ¥ hur koden fungerar och var felen kan tÃ¤nkas uppstÃ¥.

Vissa testfall Ã¤r egentligen skapade genom loopar, men pÃ¥ grund av
Ã¶versÃ¤ttningen till enkla assertions syns inte looparna hÃ¤r.
"""
"""
Denna fil innehÃ¥ller ett antal lÃ¶sningsfÃ¶rslag fÃ¶r tentan i TDDE24 januari 2024.

Det finns alltid mÃ¥nga olika sÃ¤tt att lÃ¶sa en uppgift, och bara fÃ¶r att
lÃ¶sningsfÃ¶rslaget ser ut pÃ¥ ett visst sÃ¤tt betyder det inte att detta Ã¤r
det enda, eller ens det allra bÃ¤sta sÃ¤ttet att lÃ¶sa en uppgift.
"""

import math


def sums(seq: list[int]):
    sum_so_far = 0
    results = []
    for element in seq:
        sum_so_far += element
        results.append(sum_so_far)

    return results


def merge(s1: list, s2: list):
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


def without(nest: list, to_remove: list):
    result = []
    for element in nest:
        if isinstance(element, list):
            result.append(without(element, to_remove))
        elif element not in to_remove:
            result.append(element)

    return result


def split_at(seq, pred):
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


def split_at_2(seq, pred):
    result = [[]]
    for element in seq:
        if pred(element):
            result.append([])
        else:
            result[-1].append(element)
    return result


def add_for_each(seq: list, func):
    sum_so_far = 0
    for element in seq:
        sum_so_far += func(element)
    return sum_so_far


def is_prime(n: int):
    if n < 2:
        return False
    for divisor in range(2, int(math.sqrt(n)) + 1):
        if n % divisor == 0:
            return False
    return True


def prime_factors(n: int):
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
            while not is_prime(prime):
                prime += 1
    return factors


def prime_factors_2(n: int):
    factors = []
    while n != 1:
        for divisor in range(1, n + 1):
            if n % divisor == 0 and is_prime(divisor):
                factors.append(divisor)
                n //= divisor
    return factors


def is_attractive(n: int):
    return is_prime(len(prime_factors(n)))


def create_trie() -> tuple[bool, dict]:
    return False, {}


def add_word(trie: tuple[bool, dict], word):
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
        children[head] = create_trie()

    if not tail:
        # SÃ¤tt flaggan som talar om att ordet slutar efter head.
        # Eftersom vi anvÃ¤nde en tupel, som inte kan Ã¤ndras, mÃ¥ste vi skapa
        # en ny tupel med True som flagga men med den gamla grenen.
        children[head] = (True, children[head][1])

    # Add the remaining characters of the word
    add_word(children[head], tail)


def word_in_trie(trie, word):
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
    return word_in_trie(branch, word[1:])


def find_all_matches(trie, prefix):
    result = set()
    # Match this node if a word ends here and there is no prefix.
    if trie[0] is True and prefix == '':
        result.add('')
    # Match the branch of next character.
    if prefix and prefix[0] in trie[1]:
        for match in find_all_matches(trie[1][prefix[0]], prefix[1:]):
            result.add(prefix[0] + match)

    # Match all branches if there is no prefix.
    if not prefix:
        for char, branch in trie[1].items():
            for match in find_all_matches(branch, ''):
                result.add(char + match)

    return result

# HÃ¤r lÃ¤gger du egna lÃ¶sningar!


# HÃ¤r finns extra funktioner som inte ingÃ¥r i lÃ¶sningarna, men som anvÃ¤nds
# av testfallen.
def print_exception():
    import traceback
    import sys
    print(f"    {sys.exc_info()[0]}")

    for line in traceback.format_exc().split("\n"):
        print(f"    " + line)


def is_zero(x):
    return x == 0


def is_two(x):
    return x == 2


def is_even(x):
    return x % 2 == 0


def always_false(x):
    return False


def always_true(x):
    return True


def squared(x):
    return x ** 2


def half(x):
    return x / 2


def is_even_int(x):
    return isinstance(x, int) and x % 2 == 0


def is_four(x):
    return x == 4


def is_b(x):
    return x == "b"




# noinspection PyBroadException
def test_1():
    print('PÃ¥bÃ¶rjar tester fÃ¶r uppgift 1')

    print('Startar test 1/1')
    try:
        res = sums([])
        exp = []
        if res != exp:
            print("Fel i test 1/1: sums([])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 1: Exception')
        print_exception()

    print('Startar test 1/2')
    try:
        res = sums([1, 2, 3, 4, 5])
        exp = [1, 3, 6, 10, 15]
        if res != exp:
            print("Fel i test 1/2: sums([1, 2, 3, 4, 5])")
            print("Korrekt svar: [1, 3, 6, 10, 15]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2: Exception')
        print_exception()

    print('Startar test 1/3')
    try:
        res = sums([42])
        exp = [42]
        if res != exp:
            print("Fel i test 1/3: sums([42])")
            print("Korrekt svar: [42]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3: Exception')
        print_exception()

    print('Startar test 1/4')
    try:
        res = sums([42, 43])
        exp = [42, 85]
        if res != exp:
            print("Fel i test 1/4: sums([42, 43])")
            print("Korrekt svar: [42, 85]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4: Exception')
        print_exception()

    print('Startar test 1/5')
    try:
        res = sums([42, 43, 44])
        exp = [42, 85, 129]
        if res != exp:
            print("Fel i test 1/5: sums([42, 43, 44])")
            print("Korrekt svar: [42, 85, 129]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5: Exception')
        print_exception()

    print('Startar test 1/6')
    try:
        res = sums([42, 43, 44, 45])
        exp = [42, 85, 129, 174]
        if res != exp:
            print("Fel i test 1/6: sums([42, 43, 44, 45])")
            print("Korrekt svar: [42, 85, 129, 174]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 6: Exception')
        print_exception()

    print('Startar test 1/7')
    try:
        res = sums([42, 43, 44, 45, 46])
        exp = [42, 85, 129, 174, 220]
        if res != exp:
            print("Fel i test 1/7: sums([42, 43, 44, 45, 46])")
            print("Korrekt svar: [42, 85, 129, 174, 220]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 7: Exception')
        print_exception()

    print('Startar test 1/8')
    try:
        res = sums([42, 43, 44, 45, 46, 47])
        exp = [42, 85, 129, 174, 220, 267]
        if res != exp:
            print("Fel i test 1/8: sums([42, 43, 44, 45, 46, 47])")
            print("Korrekt svar: [42, 85, 129, 174, 220, 267]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 8: Exception')
        print_exception()

    print('Startar test 1/9')
    try:
        res = sums([42, 43, 44, 45, 46, 47, 48])
        exp = [42, 85, 129, 174, 220, 267, 315]
        if res != exp:
            print("Fel i test 1/9: sums([42, 43, 44, 45, 46, 47, 48])")
            print("Korrekt svar: [42, 85, 129, 174, 220, 267, 315]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 9: Exception')
        print_exception()

    print('Startar test 1/10')
    try:
        res = sums([42, 43, 44, 45, 46, 47, 48, 49])
        exp = [42, 85, 129, 174, 220, 267, 315, 364]
        if res != exp:
            print("Fel i test 1/10: sums([42, 43, 44, 45, 46, 47, 48, 49])")
            print("Korrekt svar: [42, 85, 129, 174, 220, 267, 315, 364]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 10: Exception')
        print_exception()

    print('Startar test 1/11')
    try:
        res = sums([42, 43, 44, 45, 46, 47, 48, 49, 50])
        exp = [42, 85, 129, 174, 220, 267, 315, 364, 414]
        if res != exp:
            print("Fel i test 1/11: sums([42, 43, 44, 45, 46, 47, 48, 49, 50])")
            print("Korrekt svar: [42, 85, 129, 174, 220, 267, 315, 364, 414]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 11: Exception')
        print_exception()

    print('Startar test 1/12')
    try:
        res = sums([42, 43, 44, 45, 46, 47, 48, 49, 50, 51])
        exp = [42, 85, 129, 174, 220, 267, 315, 364, 414, 465]
        if res != exp:
            print("Fel i test 1/12: sums([42, 43, 44, 45, 46, 47, 48, 49, 50, 51])")
            print("Korrekt svar: [42, 85, 129, 174, 220, 267, 315, 364, 414, 465]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 12: Exception')
        print_exception()

    print('Startar test 1/13')
    try:
        res = sums([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52])
        exp = [42, 85, 129, 174, 220, 267, 315, 364, 414, 465, 517]
        if res != exp:
            print("Fel i test 1/13: sums([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52])")
            print("Korrekt svar: [42, 85, 129, 174, 220, 267, 315, 364, 414, 465, 517]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 13: Exception')
        print_exception()

    print('Startar test 1/14')
    try:
        res = sums([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53])
        exp = [42, 85, 129, 174, 220, 267, 315, 364, 414, 465, 517, 570]
        if res != exp:
            print("Fel i test 1/14: sums([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53])")
            print("Korrekt svar: [42, 85, 129, 174, 220, 267, 315, 364, 414, 465, 517, 570]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 14: Exception')
        print_exception()

    print('Startar test 1/15')
    try:
        res = sums([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54])
        exp = [42, 85, 129, 174, 220, 267, 315, 364, 414, 465, 517, 570, 624]
        if res != exp:
            print("Fel i test 1/15: sums([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54])")
            print("Korrekt svar: [42, 85, 129, 174, 220, 267, 315, 364, 414, 465, 517, 570, 624]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 15: Exception')
        print_exception()

    print('Startar test 1/16')
    try:
        res = sums([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55])
        exp = [42, 85, 129, 174, 220, 267, 315, 364, 414, 465, 517, 570, 624, 679]
        if res != exp:
            print("Fel i test 1/16: sums([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55])")
            print("Korrekt svar: [42, 85, 129, 174, 220, 267, 315, 364, 414, 465, 517, 570, 624, 679]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 16: Exception')
        print_exception()

    print('Startar test 1/17')
    try:
        res = sums([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56])
        exp = [42, 85, 129, 174, 220, 267, 315, 364, 414, 465, 517, 570, 624, 679, 735]
        if res != exp:
            print("Fel i test 1/17: sums([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56])")
            print("Korrekt svar: [42, 85, 129, 174, 220, 267, 315, 364, 414, 465, 517, 570, 624, 679, 735]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 17: Exception')
        print_exception()

    print('Startar test 1/18')
    try:
        res = sums([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57])
        exp = [42, 85, 129, 174, 220, 267, 315, 364, 414, 465, 517, 570, 624, 679, 735, 792]
        if res != exp:
            print("Fel i test 1/18: sums([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57])")
            print("Korrekt svar: [42, 85, 129, 174, 220, 267, 315, 364, 414, 465, 517, 570, 624, 679, 735, 792]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 18: Exception')
        print_exception()

    print('Startar test 1/19')
    try:
        res = sums([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58])
        exp = [42, 85, 129, 174, 220, 267, 315, 364, 414, 465, 517, 570, 624, 679, 735, 792, 850]
        if res != exp:
            print("Fel i test 1/19: sums([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58])")
            print("Korrekt svar: [42, 85, 129, 174, 220, 267, 315, 364, 414, 465, 517, 570, 624, 679, 735, 792, 850]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 19: Exception')
        print_exception()

    print('Startar test 1/20')
    try:
        res = sums([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59])
        exp = [42, 85, 129, 174, 220, 267, 315, 364, 414, 465, 517, 570, 624, 679, 735, 792, 850, 909]
        if res != exp:
            print("Fel i test 1/20: sums([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59])")
            print("Korrekt svar: [42, 85, 129, 174, 220, 267, 315, 364, 414, 465, 517, 570, 624, 679, 735, 792, 850, 909]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 20: Exception')
        print_exception()

    print('Startar test 1/21')
    try:
        res = sums([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60])
        exp = [42, 85, 129, 174, 220, 267, 315, 364, 414, 465, 517, 570, 624, 679, 735, 792, 850, 909, 969]
        if res != exp:
            print("Fel i test 1/21: sums([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60])")
            print("Korrekt svar: [42, 85, 129, 174, 220, 267, 315, 364, 414, 465, 517, 570, 624, 679, 735, 792, 850, 909, 969]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 21: Exception')
        print_exception()

    print('Startar test 1/22')
    try:
        res = sums([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61])
        exp = [42, 85, 129, 174, 220, 267, 315, 364, 414, 465, 517, 570, 624, 679, 735, 792, 850, 909, 969, 1030]
        if res != exp:
            print("Fel i test 1/22: sums([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61])")
            print("Korrekt svar: [42, 85, 129, 174, 220, 267, 315, 364, 414, 465, 517, 570, 624, 679, 735, 792, 850, 909, 969, 1030]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 22: Exception')
        print_exception()

    print('Startar test 1/23')
    try:
        res = sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
        exp = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435]
        if res != exp:
            print("Fel i test 1/23: sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])")
            print("Korrekt svar: [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 23: Exception')
        print_exception()

    print('Startar test 1/24')
    try:
        res = sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39])
        exp = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780]
        if res != exp:
            print("Fel i test 1/24: sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39])")
            print("Korrekt svar: [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 24: Exception')
        print_exception()

    print('Startar test 1/25')
    try:
        res = sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49])
        exp = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225]
        if res != exp:
            print("Fel i test 1/25: sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49])")
            print("Korrekt svar: [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 25: Exception')
        print_exception()

    print('Startar test 1/26')
    try:
        res = sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59])
        exp = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770]
        if res != exp:
            print("Fel i test 1/26: sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59])")
            print("Korrekt svar: [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 26: Exception')
        print_exception()

    print('Startar test 1/27')
    try:
        res = sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69])
        exp = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415]
        if res != exp:
            print("Fel i test 1/27: sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69])")
            print("Korrekt svar: [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 27: Exception')
        print_exception()

    print('Startar test 1/28')
    try:
        res = sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79])
        exp = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160]
        if res != exp:
            print("Fel i test 1/28: sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79])")
            print("Korrekt svar: [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 28: Exception')
        print_exception()

    print('Startar test 1/29')
    try:
        res = sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89])
        exp = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005]
        if res != exp:
            print("Fel i test 1/29: sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89])")
            print("Korrekt svar: [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 29: Exception')
        print_exception()

    print('Startar test 1/30')
    try:
        res = sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
        exp = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950]
        if res != exp:
            print("Fel i test 1/30: sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])")
            print("Korrekt svar: [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 30: Exception')
        print_exception()

    print('Startar test 1/31')
    try:
        res = sums([2, 7, 12, 17, 22, 27])
        exp = [2, 9, 21, 38, 60, 87]
        if res != exp:
            print("Fel i test 1/31: sums([2, 7, 12, 17, 22, 27])")
            print("Korrekt svar: [2, 9, 21, 38, 60, 87]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 31: Exception')
        print_exception()

    print('Startar test 1/32')
    try:
        res = sums([2, 7, 12, 17, 22, 27, 32, 37])
        exp = [2, 9, 21, 38, 60, 87, 119, 156]
        if res != exp:
            print("Fel i test 1/32: sums([2, 7, 12, 17, 22, 27, 32, 37])")
            print("Korrekt svar: [2, 9, 21, 38, 60, 87, 119, 156]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 32: Exception')
        print_exception()

    print('Startar test 1/33')
    try:
        res = sums([2, 7, 12, 17, 22, 27, 32, 37, 42, 47])
        exp = [2, 9, 21, 38, 60, 87, 119, 156, 198, 245]
        if res != exp:
            print("Fel i test 1/33: sums([2, 7, 12, 17, 22, 27, 32, 37, 42, 47])")
            print("Korrekt svar: [2, 9, 21, 38, 60, 87, 119, 156, 198, 245]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 33: Exception')
        print_exception()

    print('Startar test 1/34')
    try:
        res = sums([2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57])
        exp = [2, 9, 21, 38, 60, 87, 119, 156, 198, 245, 297, 354]
        if res != exp:
            print("Fel i test 1/34: sums([2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57])")
            print("Korrekt svar: [2, 9, 21, 38, 60, 87, 119, 156, 198, 245, 297, 354]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 34: Exception')
        print_exception()

    print('Startar test 1/35')
    try:
        res = sums([2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67])
        exp = [2, 9, 21, 38, 60, 87, 119, 156, 198, 245, 297, 354, 416, 483]
        if res != exp:
            print("Fel i test 1/35: sums([2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67])")
            print("Korrekt svar: [2, 9, 21, 38, 60, 87, 119, 156, 198, 245, 297, 354, 416, 483]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 35: Exception')
        print_exception()

    print('Startar test 1/36')
    try:
        res = sums([2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77])
        exp = [2, 9, 21, 38, 60, 87, 119, 156, 198, 245, 297, 354, 416, 483, 555, 632]
        if res != exp:
            print("Fel i test 1/36: sums([2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77])")
            print("Korrekt svar: [2, 9, 21, 38, 60, 87, 119, 156, 198, 245, 297, 354, 416, 483, 555, 632]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 36: Exception')
        print_exception()

    print('Startar test 1/37')
    try:
        res = sums([2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77, 82, 87])
        exp = [2, 9, 21, 38, 60, 87, 119, 156, 198, 245, 297, 354, 416, 483, 555, 632, 714, 801]
        if res != exp:
            print("Fel i test 1/37: sums([2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77, 82, 87])")
            print("Korrekt svar: [2, 9, 21, 38, 60, 87, 119, 156, 198, 245, 297, 354, 416, 483, 555, 632, 714, 801]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 37: Exception')
        print_exception()

    print('Startar test 1/38')
    try:
        res = sums([2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77, 82, 87, 92, 97])
        exp = [2, 9, 21, 38, 60, 87, 119, 156, 198, 245, 297, 354, 416, 483, 555, 632, 714, 801, 893, 990]
        if res != exp:
            print("Fel i test 1/38: sums([2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77, 82, 87, 92, 97])")
            print("Korrekt svar: [2, 9, 21, 38, 60, 87, 119, 156, 198, 245, 297, 354, 416, 483, 555, 632, 714, 801, 893, 990]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 38: Exception')
        print_exception()

    print('Startar test 1/39')
    try:
        res = sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199])
        exp = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950, 5050, 5151, 5253, 5356, 5460, 5565, 5671, 5778, 5886, 5995, 6105, 6216, 6328, 6441, 6555, 6670, 6786, 6903, 7021, 7140, 7260, 7381, 7503, 7626, 7750, 7875, 8001, 8128, 8256, 8385, 8515, 8646, 8778, 8911, 9045, 9180, 9316, 9453, 9591, 9730, 9870, 10011, 10153, 10296, 10440, 10585, 10731, 10878, 11026, 11175, 11325, 11476, 11628, 11781, 11935, 12090, 12246, 12403, 12561, 12720, 12880, 13041, 13203, 13366, 13530, 13695, 13861, 14028, 14196, 14365, 14535, 14706, 14878, 15051, 15225, 15400, 15576, 15753, 15931, 16110, 16290, 16471, 16653, 16836, 17020, 17205, 17391, 17578, 17766, 17955, 18145, 18336, 18528, 18721, 18915, 19110, 19306, 19503, 19701, 19900]
        if res != exp:
            print("Fel i test 1/39: sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199])")
            print("Korrekt svar: [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950, 5050, 5151, 5253, 5356, 5460, 5565, 5671, 5778, 5886, 5995, 6105, 6216, 6328, 6441, 6555, 6670, 6786, 6903, 7021, 7140, 7260, 7381, 7503, 7626, 7750, 7875, 8001, 8128, 8256, 8385, 8515, 8646, 8778, 8911, 9045, 9180, 9316, 9453, 9591, 9730, 9870, 10011, 10153, 10296, 10440, 10585, 10731, 10878, 11026, 11175, 11325, 11476, 11628, 11781, 11935, 12090, 12246, 12403, 12561, 12720, 12880, 13041, 13203, 13366, 13530, 13695, 13861, 14028, 14196, 14365, 14535, 14706, 14878, 15051, 15225, 15400, 15576, 15753, 15931, 16110, 16290, 16471, 16653, 16836, 17020, 17205, 17391, 17578, 17766, 17955, 18145, 18336, 18528, 18721, 18915, 19110, 19306, 19503, 19701, 19900]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 39: Exception')
        print_exception()

    print('Startar test 1/40')
    try:
        res = sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299])
        exp = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950, 5050, 5151, 5253, 5356, 5460, 5565, 5671, 5778, 5886, 5995, 6105, 6216, 6328, 6441, 6555, 6670, 6786, 6903, 7021, 7140, 7260, 7381, 7503, 7626, 7750, 7875, 8001, 8128, 8256, 8385, 8515, 8646, 8778, 8911, 9045, 9180, 9316, 9453, 9591, 9730, 9870, 10011, 10153, 10296, 10440, 10585, 10731, 10878, 11026, 11175, 11325, 11476, 11628, 11781, 11935, 12090, 12246, 12403, 12561, 12720, 12880, 13041, 13203, 13366, 13530, 13695, 13861, 14028, 14196, 14365, 14535, 14706, 14878, 15051, 15225, 15400, 15576, 15753, 15931, 16110, 16290, 16471, 16653, 16836, 17020, 17205, 17391, 17578, 17766, 17955, 18145, 18336, 18528, 18721, 18915, 19110, 19306, 19503, 19701, 19900, 20100, 20301, 20503, 20706, 20910, 21115, 21321, 21528, 21736, 21945, 22155, 22366, 22578, 22791, 23005, 23220, 23436, 23653, 23871, 24090, 24310, 24531, 24753, 24976, 25200, 25425, 25651, 25878, 26106, 26335, 26565, 26796, 27028, 27261, 27495, 27730, 27966, 28203, 28441, 28680, 28920, 29161, 29403, 29646, 29890, 30135, 30381, 30628, 30876, 31125, 31375, 31626, 31878, 32131, 32385, 32640, 32896, 33153, 33411, 33670, 33930, 34191, 34453, 34716, 34980, 35245, 35511, 35778, 36046, 36315, 36585, 36856, 37128, 37401, 37675, 37950, 38226, 38503, 38781, 39060, 39340, 39621, 39903, 40186, 40470, 40755, 41041, 41328, 41616, 41905, 42195, 42486, 42778, 43071, 43365, 43660, 43956, 44253, 44551, 44850]
        if res != exp:
            print("Fel i test 1/40: sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299])")
            print("Korrekt svar: [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950, 5050, 5151, 5253, 5356, 5460, 5565, 5671, 5778, 5886, 5995, 6105, 6216, 6328, 6441, 6555, 6670, 6786, 6903, 7021, 7140, 7260, 7381, 7503, 7626, 7750, 7875, 8001, 8128, 8256, 8385, 8515, 8646, 8778, 8911, 9045, 9180, 9316, 9453, 9591, 9730, 9870, 10011, 10153, 10296, 10440, 10585, 10731, 10878, 11026, 11175, 11325, 11476, 11628, 11781, 11935, 12090, 12246, 12403, 12561, 12720, 12880, 13041, 13203, 13366, 13530, 13695, 13861, 14028, 14196, 14365, 14535, 14706, 14878, 15051, 15225, 15400, 15576, 15753, 15931, 16110, 16290, 16471, 16653, 16836, 17020, 17205, 17391, 17578, 17766, 17955, 18145, 18336, 18528, 18721, 18915, 19110, 19306, 19503, 19701, 19900, 20100, 20301, 20503, 20706, 20910, 21115, 21321, 21528, 21736, 21945, 22155, 22366, 22578, 22791, 23005, 23220, 23436, 23653, 23871, 24090, 24310, 24531, 24753, 24976, 25200, 25425, 25651, 25878, 26106, 26335, 26565, 26796, 27028, 27261, 27495, 27730, 27966, 28203, 28441, 28680, 28920, 29161, 29403, 29646, 29890, 30135, 30381, 30628, 30876, 31125, 31375, 31626, 31878, 32131, 32385, 32640, 32896, 33153, 33411, 33670, 33930, 34191, 34453, 34716, 34980, 35245, 35511, 35778, 36046, 36315, 36585, 36856, 37128, 37401, 37675, 37950, 38226, 38503, 38781, 39060, 39340, 39621, 39903, 40186, 40470, 40755, 41041, 41328, 41616, 41905, 42195, 42486, 42778, 43071, 43365, 43660, 43956, 44253, 44551, 44850]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 40: Exception')
        print_exception()

    print('Startar test 1/41')
    try:
        res = sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399])
        exp = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950, 5050, 5151, 5253, 5356, 5460, 5565, 5671, 5778, 5886, 5995, 6105, 6216, 6328, 6441, 6555, 6670, 6786, 6903, 7021, 7140, 7260, 7381, 7503, 7626, 7750, 7875, 8001, 8128, 8256, 8385, 8515, 8646, 8778, 8911, 9045, 9180, 9316, 9453, 9591, 9730, 9870, 10011, 10153, 10296, 10440, 10585, 10731, 10878, 11026, 11175, 11325, 11476, 11628, 11781, 11935, 12090, 12246, 12403, 12561, 12720, 12880, 13041, 13203, 13366, 13530, 13695, 13861, 14028, 14196, 14365, 14535, 14706, 14878, 15051, 15225, 15400, 15576, 15753, 15931, 16110, 16290, 16471, 16653, 16836, 17020, 17205, 17391, 17578, 17766, 17955, 18145, 18336, 18528, 18721, 18915, 19110, 19306, 19503, 19701, 19900, 20100, 20301, 20503, 20706, 20910, 21115, 21321, 21528, 21736, 21945, 22155, 22366, 22578, 22791, 23005, 23220, 23436, 23653, 23871, 24090, 24310, 24531, 24753, 24976, 25200, 25425, 25651, 25878, 26106, 26335, 26565, 26796, 27028, 27261, 27495, 27730, 27966, 28203, 28441, 28680, 28920, 29161, 29403, 29646, 29890, 30135, 30381, 30628, 30876, 31125, 31375, 31626, 31878, 32131, 32385, 32640, 32896, 33153, 33411, 33670, 33930, 34191, 34453, 34716, 34980, 35245, 35511, 35778, 36046, 36315, 36585, 36856, 37128, 37401, 37675, 37950, 38226, 38503, 38781, 39060, 39340, 39621, 39903, 40186, 40470, 40755, 41041, 41328, 41616, 41905, 42195, 42486, 42778, 43071, 43365, 43660, 43956, 44253, 44551, 44850, 45150, 45451, 45753, 46056, 46360, 46665, 46971, 47278, 47586, 47895, 48205, 48516, 48828, 49141, 49455, 49770, 50086, 50403, 50721, 51040, 51360, 51681, 52003, 52326, 52650, 52975, 53301, 53628, 53956, 54285, 54615, 54946, 55278, 55611, 55945, 56280, 56616, 56953, 57291, 57630, 57970, 58311, 58653, 58996, 59340, 59685, 60031, 60378, 60726, 61075, 61425, 61776, 62128, 62481, 62835, 63190, 63546, 63903, 64261, 64620, 64980, 65341, 65703, 66066, 66430, 66795, 67161, 67528, 67896, 68265, 68635, 69006, 69378, 69751, 70125, 70500, 70876, 71253, 71631, 72010, 72390, 72771, 73153, 73536, 73920, 74305, 74691, 75078, 75466, 75855, 76245, 76636, 77028, 77421, 77815, 78210, 78606, 79003, 79401, 79800]
        if res != exp:
            print("Fel i test 1/41: sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399])")
            print("Korrekt svar: [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950, 5050, 5151, 5253, 5356, 5460, 5565, 5671, 5778, 5886, 5995, 6105, 6216, 6328, 6441, 6555, 6670, 6786, 6903, 7021, 7140, 7260, 7381, 7503, 7626, 7750, 7875, 8001, 8128, 8256, 8385, 8515, 8646, 8778, 8911, 9045, 9180, 9316, 9453, 9591, 9730, 9870, 10011, 10153, 10296, 10440, 10585, 10731, 10878, 11026, 11175, 11325, 11476, 11628, 11781, 11935, 12090, 12246, 12403, 12561, 12720, 12880, 13041, 13203, 13366, 13530, 13695, 13861, 14028, 14196, 14365, 14535, 14706, 14878, 15051, 15225, 15400, 15576, 15753, 15931, 16110, 16290, 16471, 16653, 16836, 17020, 17205, 17391, 17578, 17766, 17955, 18145, 18336, 18528, 18721, 18915, 19110, 19306, 19503, 19701, 19900, 20100, 20301, 20503, 20706, 20910, 21115, 21321, 21528, 21736, 21945, 22155, 22366, 22578, 22791, 23005, 23220, 23436, 23653, 23871, 24090, 24310, 24531, 24753, 24976, 25200, 25425, 25651, 25878, 26106, 26335, 26565, 26796, 27028, 27261, 27495, 27730, 27966, 28203, 28441, 28680, 28920, 29161, 29403, 29646, 29890, 30135, 30381, 30628, 30876, 31125, 31375, 31626, 31878, 32131, 32385, 32640, 32896, 33153, 33411, 33670, 33930, 34191, 34453, 34716, 34980, 35245, 35511, 35778, 36046, 36315, 36585, 36856, 37128, 37401, 37675, 37950, 38226, 38503, 38781, 39060, 39340, 39621, 39903, 40186, 40470, 40755, 41041, 41328, 41616, 41905, 42195, 42486, 42778, 43071, 43365, 43660, 43956, 44253, 44551, 44850, 45150, 45451, 45753, 46056, 46360, 46665, 46971, 47278, 47586, 47895, 48205, 48516, 48828, 49141, 49455, 49770, 50086, 50403, 50721, 51040, 51360, 51681, 52003, 52326, 52650, 52975, 53301, 53628, 53956, 54285, 54615, 54946, 55278, 55611, 55945, 56280, 56616, 56953, 57291, 57630, 57970, 58311, 58653, 58996, 59340, 59685, 60031, 60378, 60726, 61075, 61425, 61776, 62128, 62481, 62835, 63190, 63546, 63903, 64261, 64620, 64980, 65341, 65703, 66066, 66430, 66795, 67161, 67528, 67896, 68265, 68635, 69006, 69378, 69751, 70125, 70500, 70876, 71253, 71631, 72010, 72390, 72771, 73153, 73536, 73920, 74305, 74691, 75078, 75466, 75855, 76245, 76636, 77028, 77421, 77815, 78210, 78606, 79003, 79401, 79800]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 41: Exception')
        print_exception()

    print('Startar test 1/42')
    try:
        res = sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499])
        exp = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950, 5050, 5151, 5253, 5356, 5460, 5565, 5671, 5778, 5886, 5995, 6105, 6216, 6328, 6441, 6555, 6670, 6786, 6903, 7021, 7140, 7260, 7381, 7503, 7626, 7750, 7875, 8001, 8128, 8256, 8385, 8515, 8646, 8778, 8911, 9045, 9180, 9316, 9453, 9591, 9730, 9870, 10011, 10153, 10296, 10440, 10585, 10731, 10878, 11026, 11175, 11325, 11476, 11628, 11781, 11935, 12090, 12246, 12403, 12561, 12720, 12880, 13041, 13203, 13366, 13530, 13695, 13861, 14028, 14196, 14365, 14535, 14706, 14878, 15051, 15225, 15400, 15576, 15753, 15931, 16110, 16290, 16471, 16653, 16836, 17020, 17205, 17391, 17578, 17766, 17955, 18145, 18336, 18528, 18721, 18915, 19110, 19306, 19503, 19701, 19900, 20100, 20301, 20503, 20706, 20910, 21115, 21321, 21528, 21736, 21945, 22155, 22366, 22578, 22791, 23005, 23220, 23436, 23653, 23871, 24090, 24310, 24531, 24753, 24976, 25200, 25425, 25651, 25878, 26106, 26335, 26565, 26796, 27028, 27261, 27495, 27730, 27966, 28203, 28441, 28680, 28920, 29161, 29403, 29646, 29890, 30135, 30381, 30628, 30876, 31125, 31375, 31626, 31878, 32131, 32385, 32640, 32896, 33153, 33411, 33670, 33930, 34191, 34453, 34716, 34980, 35245, 35511, 35778, 36046, 36315, 36585, 36856, 37128, 37401, 37675, 37950, 38226, 38503, 38781, 39060, 39340, 39621, 39903, 40186, 40470, 40755, 41041, 41328, 41616, 41905, 42195, 42486, 42778, 43071, 43365, 43660, 43956, 44253, 44551, 44850, 45150, 45451, 45753, 46056, 46360, 46665, 46971, 47278, 47586, 47895, 48205, 48516, 48828, 49141, 49455, 49770, 50086, 50403, 50721, 51040, 51360, 51681, 52003, 52326, 52650, 52975, 53301, 53628, 53956, 54285, 54615, 54946, 55278, 55611, 55945, 56280, 56616, 56953, 57291, 57630, 57970, 58311, 58653, 58996, 59340, 59685, 60031, 60378, 60726, 61075, 61425, 61776, 62128, 62481, 62835, 63190, 63546, 63903, 64261, 64620, 64980, 65341, 65703, 66066, 66430, 66795, 67161, 67528, 67896, 68265, 68635, 69006, 69378, 69751, 70125, 70500, 70876, 71253, 71631, 72010, 72390, 72771, 73153, 73536, 73920, 74305, 74691, 75078, 75466, 75855, 76245, 76636, 77028, 77421, 77815, 78210, 78606, 79003, 79401, 79800, 80200, 80601, 81003, 81406, 81810, 82215, 82621, 83028, 83436, 83845, 84255, 84666, 85078, 85491, 85905, 86320, 86736, 87153, 87571, 87990, 88410, 88831, 89253, 89676, 90100, 90525, 90951, 91378, 91806, 92235, 92665, 93096, 93528, 93961, 94395, 94830, 95266, 95703, 96141, 96580, 97020, 97461, 97903, 98346, 98790, 99235, 99681, 100128, 100576, 101025, 101475, 101926, 102378, 102831, 103285, 103740, 104196, 104653, 105111, 105570, 106030, 106491, 106953, 107416, 107880, 108345, 108811, 109278, 109746, 110215, 110685, 111156, 111628, 112101, 112575, 113050, 113526, 114003, 114481, 114960, 115440, 115921, 116403, 116886, 117370, 117855, 118341, 118828, 119316, 119805, 120295, 120786, 121278, 121771, 122265, 122760, 123256, 123753, 124251, 124750]
        if res != exp:
            print("Fel i test 1/42: sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499])")
            print("Korrekt svar: [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950, 5050, 5151, 5253, 5356, 5460, 5565, 5671, 5778, 5886, 5995, 6105, 6216, 6328, 6441, 6555, 6670, 6786, 6903, 7021, 7140, 7260, 7381, 7503, 7626, 7750, 7875, 8001, 8128, 8256, 8385, 8515, 8646, 8778, 8911, 9045, 9180, 9316, 9453, 9591, 9730, 9870, 10011, 10153, 10296, 10440, 10585, 10731, 10878, 11026, 11175, 11325, 11476, 11628, 11781, 11935, 12090, 12246, 12403, 12561, 12720, 12880, 13041, 13203, 13366, 13530, 13695, 13861, 14028, 14196, 14365, 14535, 14706, 14878, 15051, 15225, 15400, 15576, 15753, 15931, 16110, 16290, 16471, 16653, 16836, 17020, 17205, 17391, 17578, 17766, 17955, 18145, 18336, 18528, 18721, 18915, 19110, 19306, 19503, 19701, 19900, 20100, 20301, 20503, 20706, 20910, 21115, 21321, 21528, 21736, 21945, 22155, 22366, 22578, 22791, 23005, 23220, 23436, 23653, 23871, 24090, 24310, 24531, 24753, 24976, 25200, 25425, 25651, 25878, 26106, 26335, 26565, 26796, 27028, 27261, 27495, 27730, 27966, 28203, 28441, 28680, 28920, 29161, 29403, 29646, 29890, 30135, 30381, 30628, 30876, 31125, 31375, 31626, 31878, 32131, 32385, 32640, 32896, 33153, 33411, 33670, 33930, 34191, 34453, 34716, 34980, 35245, 35511, 35778, 36046, 36315, 36585, 36856, 37128, 37401, 37675, 37950, 38226, 38503, 38781, 39060, 39340, 39621, 39903, 40186, 40470, 40755, 41041, 41328, 41616, 41905, 42195, 42486, 42778, 43071, 43365, 43660, 43956, 44253, 44551, 44850, 45150, 45451, 45753, 46056, 46360, 46665, 46971, 47278, 47586, 47895, 48205, 48516, 48828, 49141, 49455, 49770, 50086, 50403, 50721, 51040, 51360, 51681, 52003, 52326, 52650, 52975, 53301, 53628, 53956, 54285, 54615, 54946, 55278, 55611, 55945, 56280, 56616, 56953, 57291, 57630, 57970, 58311, 58653, 58996, 59340, 59685, 60031, 60378, 60726, 61075, 61425, 61776, 62128, 62481, 62835, 63190, 63546, 63903, 64261, 64620, 64980, 65341, 65703, 66066, 66430, 66795, 67161, 67528, 67896, 68265, 68635, 69006, 69378, 69751, 70125, 70500, 70876, 71253, 71631, 72010, 72390, 72771, 73153, 73536, 73920, 74305, 74691, 75078, 75466, 75855, 76245, 76636, 77028, 77421, 77815, 78210, 78606, 79003, 79401, 79800, 80200, 80601, 81003, 81406, 81810, 82215, 82621, 83028, 83436, 83845, 84255, 84666, 85078, 85491, 85905, 86320, 86736, 87153, 87571, 87990, 88410, 88831, 89253, 89676, 90100, 90525, 90951, 91378, 91806, 92235, 92665, 93096, 93528, 93961, 94395, 94830, 95266, 95703, 96141, 96580, 97020, 97461, 97903, 98346, 98790, 99235, 99681, 100128, 100576, 101025, 101475, 101926, 102378, 102831, 103285, 103740, 104196, 104653, 105111, 105570, 106030, 106491, 106953, 107416, 107880, 108345, 108811, 109278, 109746, 110215, 110685, 111156, 111628, 112101, 112575, 113050, 113526, 114003, 114481, 114960, 115440, 115921, 116403, 116886, 117370, 117855, 118341, 118828, 119316, 119805, 120295, 120786, 121278, 121771, 122265, 122760, 123256, 123753, 124251, 124750]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 42: Exception')
        print_exception()

    print('Startar test 1/43')
    try:
        res = sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599])
        exp = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950, 5050, 5151, 5253, 5356, 5460, 5565, 5671, 5778, 5886, 5995, 6105, 6216, 6328, 6441, 6555, 6670, 6786, 6903, 7021, 7140, 7260, 7381, 7503, 7626, 7750, 7875, 8001, 8128, 8256, 8385, 8515, 8646, 8778, 8911, 9045, 9180, 9316, 9453, 9591, 9730, 9870, 10011, 10153, 10296, 10440, 10585, 10731, 10878, 11026, 11175, 11325, 11476, 11628, 11781, 11935, 12090, 12246, 12403, 12561, 12720, 12880, 13041, 13203, 13366, 13530, 13695, 13861, 14028, 14196, 14365, 14535, 14706, 14878, 15051, 15225, 15400, 15576, 15753, 15931, 16110, 16290, 16471, 16653, 16836, 17020, 17205, 17391, 17578, 17766, 17955, 18145, 18336, 18528, 18721, 18915, 19110, 19306, 19503, 19701, 19900, 20100, 20301, 20503, 20706, 20910, 21115, 21321, 21528, 21736, 21945, 22155, 22366, 22578, 22791, 23005, 23220, 23436, 23653, 23871, 24090, 24310, 24531, 24753, 24976, 25200, 25425, 25651, 25878, 26106, 26335, 26565, 26796, 27028, 27261, 27495, 27730, 27966, 28203, 28441, 28680, 28920, 29161, 29403, 29646, 29890, 30135, 30381, 30628, 30876, 31125, 31375, 31626, 31878, 32131, 32385, 32640, 32896, 33153, 33411, 33670, 33930, 34191, 34453, 34716, 34980, 35245, 35511, 35778, 36046, 36315, 36585, 36856, 37128, 37401, 37675, 37950, 38226, 38503, 38781, 39060, 39340, 39621, 39903, 40186, 40470, 40755, 41041, 41328, 41616, 41905, 42195, 42486, 42778, 43071, 43365, 43660, 43956, 44253, 44551, 44850, 45150, 45451, 45753, 46056, 46360, 46665, 46971, 47278, 47586, 47895, 48205, 48516, 48828, 49141, 49455, 49770, 50086, 50403, 50721, 51040, 51360, 51681, 52003, 52326, 52650, 52975, 53301, 53628, 53956, 54285, 54615, 54946, 55278, 55611, 55945, 56280, 56616, 56953, 57291, 57630, 57970, 58311, 58653, 58996, 59340, 59685, 60031, 60378, 60726, 61075, 61425, 61776, 62128, 62481, 62835, 63190, 63546, 63903, 64261, 64620, 64980, 65341, 65703, 66066, 66430, 66795, 67161, 67528, 67896, 68265, 68635, 69006, 69378, 69751, 70125, 70500, 70876, 71253, 71631, 72010, 72390, 72771, 73153, 73536, 73920, 74305, 74691, 75078, 75466, 75855, 76245, 76636, 77028, 77421, 77815, 78210, 78606, 79003, 79401, 79800, 80200, 80601, 81003, 81406, 81810, 82215, 82621, 83028, 83436, 83845, 84255, 84666, 85078, 85491, 85905, 86320, 86736, 87153, 87571, 87990, 88410, 88831, 89253, 89676, 90100, 90525, 90951, 91378, 91806, 92235, 92665, 93096, 93528, 93961, 94395, 94830, 95266, 95703, 96141, 96580, 97020, 97461, 97903, 98346, 98790, 99235, 99681, 100128, 100576, 101025, 101475, 101926, 102378, 102831, 103285, 103740, 104196, 104653, 105111, 105570, 106030, 106491, 106953, 107416, 107880, 108345, 108811, 109278, 109746, 110215, 110685, 111156, 111628, 112101, 112575, 113050, 113526, 114003, 114481, 114960, 115440, 115921, 116403, 116886, 117370, 117855, 118341, 118828, 119316, 119805, 120295, 120786, 121278, 121771, 122265, 122760, 123256, 123753, 124251, 124750, 125250, 125751, 126253, 126756, 127260, 127765, 128271, 128778, 129286, 129795, 130305, 130816, 131328, 131841, 132355, 132870, 133386, 133903, 134421, 134940, 135460, 135981, 136503, 137026, 137550, 138075, 138601, 139128, 139656, 140185, 140715, 141246, 141778, 142311, 142845, 143380, 143916, 144453, 144991, 145530, 146070, 146611, 147153, 147696, 148240, 148785, 149331, 149878, 150426, 150975, 151525, 152076, 152628, 153181, 153735, 154290, 154846, 155403, 155961, 156520, 157080, 157641, 158203, 158766, 159330, 159895, 160461, 161028, 161596, 162165, 162735, 163306, 163878, 164451, 165025, 165600, 166176, 166753, 167331, 167910, 168490, 169071, 169653, 170236, 170820, 171405, 171991, 172578, 173166, 173755, 174345, 174936, 175528, 176121, 176715, 177310, 177906, 178503, 179101, 179700]
        if res != exp:
            print("Fel i test 1/43: sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599])")
            print("Korrekt svar: [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950, 5050, 5151, 5253, 5356, 5460, 5565, 5671, 5778, 5886, 5995, 6105, 6216, 6328, 6441, 6555, 6670, 6786, 6903, 7021, 7140, 7260, 7381, 7503, 7626, 7750, 7875, 8001, 8128, 8256, 8385, 8515, 8646, 8778, 8911, 9045, 9180, 9316, 9453, 9591, 9730, 9870, 10011, 10153, 10296, 10440, 10585, 10731, 10878, 11026, 11175, 11325, 11476, 11628, 11781, 11935, 12090, 12246, 12403, 12561, 12720, 12880, 13041, 13203, 13366, 13530, 13695, 13861, 14028, 14196, 14365, 14535, 14706, 14878, 15051, 15225, 15400, 15576, 15753, 15931, 16110, 16290, 16471, 16653, 16836, 17020, 17205, 17391, 17578, 17766, 17955, 18145, 18336, 18528, 18721, 18915, 19110, 19306, 19503, 19701, 19900, 20100, 20301, 20503, 20706, 20910, 21115, 21321, 21528, 21736, 21945, 22155, 22366, 22578, 22791, 23005, 23220, 23436, 23653, 23871, 24090, 24310, 24531, 24753, 24976, 25200, 25425, 25651, 25878, 26106, 26335, 26565, 26796, 27028, 27261, 27495, 27730, 27966, 28203, 28441, 28680, 28920, 29161, 29403, 29646, 29890, 30135, 30381, 30628, 30876, 31125, 31375, 31626, 31878, 32131, 32385, 32640, 32896, 33153, 33411, 33670, 33930, 34191, 34453, 34716, 34980, 35245, 35511, 35778, 36046, 36315, 36585, 36856, 37128, 37401, 37675, 37950, 38226, 38503, 38781, 39060, 39340, 39621, 39903, 40186, 40470, 40755, 41041, 41328, 41616, 41905, 42195, 42486, 42778, 43071, 43365, 43660, 43956, 44253, 44551, 44850, 45150, 45451, 45753, 46056, 46360, 46665, 46971, 47278, 47586, 47895, 48205, 48516, 48828, 49141, 49455, 49770, 50086, 50403, 50721, 51040, 51360, 51681, 52003, 52326, 52650, 52975, 53301, 53628, 53956, 54285, 54615, 54946, 55278, 55611, 55945, 56280, 56616, 56953, 57291, 57630, 57970, 58311, 58653, 58996, 59340, 59685, 60031, 60378, 60726, 61075, 61425, 61776, 62128, 62481, 62835, 63190, 63546, 63903, 64261, 64620, 64980, 65341, 65703, 66066, 66430, 66795, 67161, 67528, 67896, 68265, 68635, 69006, 69378, 69751, 70125, 70500, 70876, 71253, 71631, 72010, 72390, 72771, 73153, 73536, 73920, 74305, 74691, 75078, 75466, 75855, 76245, 76636, 77028, 77421, 77815, 78210, 78606, 79003, 79401, 79800, 80200, 80601, 81003, 81406, 81810, 82215, 82621, 83028, 83436, 83845, 84255, 84666, 85078, 85491, 85905, 86320, 86736, 87153, 87571, 87990, 88410, 88831, 89253, 89676, 90100, 90525, 90951, 91378, 91806, 92235, 92665, 93096, 93528, 93961, 94395, 94830, 95266, 95703, 96141, 96580, 97020, 97461, 97903, 98346, 98790, 99235, 99681, 100128, 100576, 101025, 101475, 101926, 102378, 102831, 103285, 103740, 104196, 104653, 105111, 105570, 106030, 106491, 106953, 107416, 107880, 108345, 108811, 109278, 109746, 110215, 110685, 111156, 111628, 112101, 112575, 113050, 113526, 114003, 114481, 114960, 115440, 115921, 116403, 116886, 117370, 117855, 118341, 118828, 119316, 119805, 120295, 120786, 121278, 121771, 122265, 122760, 123256, 123753, 124251, 124750, 125250, 125751, 126253, 126756, 127260, 127765, 128271, 128778, 129286, 129795, 130305, 130816, 131328, 131841, 132355, 132870, 133386, 133903, 134421, 134940, 135460, 135981, 136503, 137026, 137550, 138075, 138601, 139128, 139656, 140185, 140715, 141246, 141778, 142311, 142845, 143380, 143916, 144453, 144991, 145530, 146070, 146611, 147153, 147696, 148240, 148785, 149331, 149878, 150426, 150975, 151525, 152076, 152628, 153181, 153735, 154290, 154846, 155403, 155961, 156520, 157080, 157641, 158203, 158766, 159330, 159895, 160461, 161028, 161596, 162165, 162735, 163306, 163878, 164451, 165025, 165600, 166176, 166753, 167331, 167910, 168490, 169071, 169653, 170236, 170820, 171405, 171991, 172578, 173166, 173755, 174345, 174936, 175528, 176121, 176715, 177310, 177906, 178503, 179101, 179700]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 43: Exception')
        print_exception()

    print('Startar test 1/44')
    try:
        res = sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699])
        exp = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950, 5050, 5151, 5253, 5356, 5460, 5565, 5671, 5778, 5886, 5995, 6105, 6216, 6328, 6441, 6555, 6670, 6786, 6903, 7021, 7140, 7260, 7381, 7503, 7626, 7750, 7875, 8001, 8128, 8256, 8385, 8515, 8646, 8778, 8911, 9045, 9180, 9316, 9453, 9591, 9730, 9870, 10011, 10153, 10296, 10440, 10585, 10731, 10878, 11026, 11175, 11325, 11476, 11628, 11781, 11935, 12090, 12246, 12403, 12561, 12720, 12880, 13041, 13203, 13366, 13530, 13695, 13861, 14028, 14196, 14365, 14535, 14706, 14878, 15051, 15225, 15400, 15576, 15753, 15931, 16110, 16290, 16471, 16653, 16836, 17020, 17205, 17391, 17578, 17766, 17955, 18145, 18336, 18528, 18721, 18915, 19110, 19306, 19503, 19701, 19900, 20100, 20301, 20503, 20706, 20910, 21115, 21321, 21528, 21736, 21945, 22155, 22366, 22578, 22791, 23005, 23220, 23436, 23653, 23871, 24090, 24310, 24531, 24753, 24976, 25200, 25425, 25651, 25878, 26106, 26335, 26565, 26796, 27028, 27261, 27495, 27730, 27966, 28203, 28441, 28680, 28920, 29161, 29403, 29646, 29890, 30135, 30381, 30628, 30876, 31125, 31375, 31626, 31878, 32131, 32385, 32640, 32896, 33153, 33411, 33670, 33930, 34191, 34453, 34716, 34980, 35245, 35511, 35778, 36046, 36315, 36585, 36856, 37128, 37401, 37675, 37950, 38226, 38503, 38781, 39060, 39340, 39621, 39903, 40186, 40470, 40755, 41041, 41328, 41616, 41905, 42195, 42486, 42778, 43071, 43365, 43660, 43956, 44253, 44551, 44850, 45150, 45451, 45753, 46056, 46360, 46665, 46971, 47278, 47586, 47895, 48205, 48516, 48828, 49141, 49455, 49770, 50086, 50403, 50721, 51040, 51360, 51681, 52003, 52326, 52650, 52975, 53301, 53628, 53956, 54285, 54615, 54946, 55278, 55611, 55945, 56280, 56616, 56953, 57291, 57630, 57970, 58311, 58653, 58996, 59340, 59685, 60031, 60378, 60726, 61075, 61425, 61776, 62128, 62481, 62835, 63190, 63546, 63903, 64261, 64620, 64980, 65341, 65703, 66066, 66430, 66795, 67161, 67528, 67896, 68265, 68635, 69006, 69378, 69751, 70125, 70500, 70876, 71253, 71631, 72010, 72390, 72771, 73153, 73536, 73920, 74305, 74691, 75078, 75466, 75855, 76245, 76636, 77028, 77421, 77815, 78210, 78606, 79003, 79401, 79800, 80200, 80601, 81003, 81406, 81810, 82215, 82621, 83028, 83436, 83845, 84255, 84666, 85078, 85491, 85905, 86320, 86736, 87153, 87571, 87990, 88410, 88831, 89253, 89676, 90100, 90525, 90951, 91378, 91806, 92235, 92665, 93096, 93528, 93961, 94395, 94830, 95266, 95703, 96141, 96580, 97020, 97461, 97903, 98346, 98790, 99235, 99681, 100128, 100576, 101025, 101475, 101926, 102378, 102831, 103285, 103740, 104196, 104653, 105111, 105570, 106030, 106491, 106953, 107416, 107880, 108345, 108811, 109278, 109746, 110215, 110685, 111156, 111628, 112101, 112575, 113050, 113526, 114003, 114481, 114960, 115440, 115921, 116403, 116886, 117370, 117855, 118341, 118828, 119316, 119805, 120295, 120786, 121278, 121771, 122265, 122760, 123256, 123753, 124251, 124750, 125250, 125751, 126253, 126756, 127260, 127765, 128271, 128778, 129286, 129795, 130305, 130816, 131328, 131841, 132355, 132870, 133386, 133903, 134421, 134940, 135460, 135981, 136503, 137026, 137550, 138075, 138601, 139128, 139656, 140185, 140715, 141246, 141778, 142311, 142845, 143380, 143916, 144453, 144991, 145530, 146070, 146611, 147153, 147696, 148240, 148785, 149331, 149878, 150426, 150975, 151525, 152076, 152628, 153181, 153735, 154290, 154846, 155403, 155961, 156520, 157080, 157641, 158203, 158766, 159330, 159895, 160461, 161028, 161596, 162165, 162735, 163306, 163878, 164451, 165025, 165600, 166176, 166753, 167331, 167910, 168490, 169071, 169653, 170236, 170820, 171405, 171991, 172578, 173166, 173755, 174345, 174936, 175528, 176121, 176715, 177310, 177906, 178503, 179101, 179700, 180300, 180901, 181503, 182106, 182710, 183315, 183921, 184528, 185136, 185745, 186355, 186966, 187578, 188191, 188805, 189420, 190036, 190653, 191271, 191890, 192510, 193131, 193753, 194376, 195000, 195625, 196251, 196878, 197506, 198135, 198765, 199396, 200028, 200661, 201295, 201930, 202566, 203203, 203841, 204480, 205120, 205761, 206403, 207046, 207690, 208335, 208981, 209628, 210276, 210925, 211575, 212226, 212878, 213531, 214185, 214840, 215496, 216153, 216811, 217470, 218130, 218791, 219453, 220116, 220780, 221445, 222111, 222778, 223446, 224115, 224785, 225456, 226128, 226801, 227475, 228150, 228826, 229503, 230181, 230860, 231540, 232221, 232903, 233586, 234270, 234955, 235641, 236328, 237016, 237705, 238395, 239086, 239778, 240471, 241165, 241860, 242556, 243253, 243951, 244650]
        if res != exp:
            print("Fel i test 1/44: sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699])")
            print("Korrekt svar: [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950, 5050, 5151, 5253, 5356, 5460, 5565, 5671, 5778, 5886, 5995, 6105, 6216, 6328, 6441, 6555, 6670, 6786, 6903, 7021, 7140, 7260, 7381, 7503, 7626, 7750, 7875, 8001, 8128, 8256, 8385, 8515, 8646, 8778, 8911, 9045, 9180, 9316, 9453, 9591, 9730, 9870, 10011, 10153, 10296, 10440, 10585, 10731, 10878, 11026, 11175, 11325, 11476, 11628, 11781, 11935, 12090, 12246, 12403, 12561, 12720, 12880, 13041, 13203, 13366, 13530, 13695, 13861, 14028, 14196, 14365, 14535, 14706, 14878, 15051, 15225, 15400, 15576, 15753, 15931, 16110, 16290, 16471, 16653, 16836, 17020, 17205, 17391, 17578, 17766, 17955, 18145, 18336, 18528, 18721, 18915, 19110, 19306, 19503, 19701, 19900, 20100, 20301, 20503, 20706, 20910, 21115, 21321, 21528, 21736, 21945, 22155, 22366, 22578, 22791, 23005, 23220, 23436, 23653, 23871, 24090, 24310, 24531, 24753, 24976, 25200, 25425, 25651, 25878, 26106, 26335, 26565, 26796, 27028, 27261, 27495, 27730, 27966, 28203, 28441, 28680, 28920, 29161, 29403, 29646, 29890, 30135, 30381, 30628, 30876, 31125, 31375, 31626, 31878, 32131, 32385, 32640, 32896, 33153, 33411, 33670, 33930, 34191, 34453, 34716, 34980, 35245, 35511, 35778, 36046, 36315, 36585, 36856, 37128, 37401, 37675, 37950, 38226, 38503, 38781, 39060, 39340, 39621, 39903, 40186, 40470, 40755, 41041, 41328, 41616, 41905, 42195, 42486, 42778, 43071, 43365, 43660, 43956, 44253, 44551, 44850, 45150, 45451, 45753, 46056, 46360, 46665, 46971, 47278, 47586, 47895, 48205, 48516, 48828, 49141, 49455, 49770, 50086, 50403, 50721, 51040, 51360, 51681, 52003, 52326, 52650, 52975, 53301, 53628, 53956, 54285, 54615, 54946, 55278, 55611, 55945, 56280, 56616, 56953, 57291, 57630, 57970, 58311, 58653, 58996, 59340, 59685, 60031, 60378, 60726, 61075, 61425, 61776, 62128, 62481, 62835, 63190, 63546, 63903, 64261, 64620, 64980, 65341, 65703, 66066, 66430, 66795, 67161, 67528, 67896, 68265, 68635, 69006, 69378, 69751, 70125, 70500, 70876, 71253, 71631, 72010, 72390, 72771, 73153, 73536, 73920, 74305, 74691, 75078, 75466, 75855, 76245, 76636, 77028, 77421, 77815, 78210, 78606, 79003, 79401, 79800, 80200, 80601, 81003, 81406, 81810, 82215, 82621, 83028, 83436, 83845, 84255, 84666, 85078, 85491, 85905, 86320, 86736, 87153, 87571, 87990, 88410, 88831, 89253, 89676, 90100, 90525, 90951, 91378, 91806, 92235, 92665, 93096, 93528, 93961, 94395, 94830, 95266, 95703, 96141, 96580, 97020, 97461, 97903, 98346, 98790, 99235, 99681, 100128, 100576, 101025, 101475, 101926, 102378, 102831, 103285, 103740, 104196, 104653, 105111, 105570, 106030, 106491, 106953, 107416, 107880, 108345, 108811, 109278, 109746, 110215, 110685, 111156, 111628, 112101, 112575, 113050, 113526, 114003, 114481, 114960, 115440, 115921, 116403, 116886, 117370, 117855, 118341, 118828, 119316, 119805, 120295, 120786, 121278, 121771, 122265, 122760, 123256, 123753, 124251, 124750, 125250, 125751, 126253, 126756, 127260, 127765, 128271, 128778, 129286, 129795, 130305, 130816, 131328, 131841, 132355, 132870, 133386, 133903, 134421, 134940, 135460, 135981, 136503, 137026, 137550, 138075, 138601, 139128, 139656, 140185, 140715, 141246, 141778, 142311, 142845, 143380, 143916, 144453, 144991, 145530, 146070, 146611, 147153, 147696, 148240, 148785, 149331, 149878, 150426, 150975, 151525, 152076, 152628, 153181, 153735, 154290, 154846, 155403, 155961, 156520, 157080, 157641, 158203, 158766, 159330, 159895, 160461, 161028, 161596, 162165, 162735, 163306, 163878, 164451, 165025, 165600, 166176, 166753, 167331, 167910, 168490, 169071, 169653, 170236, 170820, 171405, 171991, 172578, 173166, 173755, 174345, 174936, 175528, 176121, 176715, 177310, 177906, 178503, 179101, 179700, 180300, 180901, 181503, 182106, 182710, 183315, 183921, 184528, 185136, 185745, 186355, 186966, 187578, 188191, 188805, 189420, 190036, 190653, 191271, 191890, 192510, 193131, 193753, 194376, 195000, 195625, 196251, 196878, 197506, 198135, 198765, 199396, 200028, 200661, 201295, 201930, 202566, 203203, 203841, 204480, 205120, 205761, 206403, 207046, 207690, 208335, 208981, 209628, 210276, 210925, 211575, 212226, 212878, 213531, 214185, 214840, 215496, 216153, 216811, 217470, 218130, 218791, 219453, 220116, 220780, 221445, 222111, 222778, 223446, 224115, 224785, 225456, 226128, 226801, 227475, 228150, 228826, 229503, 230181, 230860, 231540, 232221, 232903, 233586, 234270, 234955, 235641, 236328, 237016, 237705, 238395, 239086, 239778, 240471, 241165, 241860, 242556, 243253, 243951, 244650]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 44: Exception')
        print_exception()

    print('Startar test 1/45')
    try:
        res = sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799])
        exp = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950, 5050, 5151, 5253, 5356, 5460, 5565, 5671, 5778, 5886, 5995, 6105, 6216, 6328, 6441, 6555, 6670, 6786, 6903, 7021, 7140, 7260, 7381, 7503, 7626, 7750, 7875, 8001, 8128, 8256, 8385, 8515, 8646, 8778, 8911, 9045, 9180, 9316, 9453, 9591, 9730, 9870, 10011, 10153, 10296, 10440, 10585, 10731, 10878, 11026, 11175, 11325, 11476, 11628, 11781, 11935, 12090, 12246, 12403, 12561, 12720, 12880, 13041, 13203, 13366, 13530, 13695, 13861, 14028, 14196, 14365, 14535, 14706, 14878, 15051, 15225, 15400, 15576, 15753, 15931, 16110, 16290, 16471, 16653, 16836, 17020, 17205, 17391, 17578, 17766, 17955, 18145, 18336, 18528, 18721, 18915, 19110, 19306, 19503, 19701, 19900, 20100, 20301, 20503, 20706, 20910, 21115, 21321, 21528, 21736, 21945, 22155, 22366, 22578, 22791, 23005, 23220, 23436, 23653, 23871, 24090, 24310, 24531, 24753, 24976, 25200, 25425, 25651, 25878, 26106, 26335, 26565, 26796, 27028, 27261, 27495, 27730, 27966, 28203, 28441, 28680, 28920, 29161, 29403, 29646, 29890, 30135, 30381, 30628, 30876, 31125, 31375, 31626, 31878, 32131, 32385, 32640, 32896, 33153, 33411, 33670, 33930, 34191, 34453, 34716, 34980, 35245, 35511, 35778, 36046, 36315, 36585, 36856, 37128, 37401, 37675, 37950, 38226, 38503, 38781, 39060, 39340, 39621, 39903, 40186, 40470, 40755, 41041, 41328, 41616, 41905, 42195, 42486, 42778, 43071, 43365, 43660, 43956, 44253, 44551, 44850, 45150, 45451, 45753, 46056, 46360, 46665, 46971, 47278, 47586, 47895, 48205, 48516, 48828, 49141, 49455, 49770, 50086, 50403, 50721, 51040, 51360, 51681, 52003, 52326, 52650, 52975, 53301, 53628, 53956, 54285, 54615, 54946, 55278, 55611, 55945, 56280, 56616, 56953, 57291, 57630, 57970, 58311, 58653, 58996, 59340, 59685, 60031, 60378, 60726, 61075, 61425, 61776, 62128, 62481, 62835, 63190, 63546, 63903, 64261, 64620, 64980, 65341, 65703, 66066, 66430, 66795, 67161, 67528, 67896, 68265, 68635, 69006, 69378, 69751, 70125, 70500, 70876, 71253, 71631, 72010, 72390, 72771, 73153, 73536, 73920, 74305, 74691, 75078, 75466, 75855, 76245, 76636, 77028, 77421, 77815, 78210, 78606, 79003, 79401, 79800, 80200, 80601, 81003, 81406, 81810, 82215, 82621, 83028, 83436, 83845, 84255, 84666, 85078, 85491, 85905, 86320, 86736, 87153, 87571, 87990, 88410, 88831, 89253, 89676, 90100, 90525, 90951, 91378, 91806, 92235, 92665, 93096, 93528, 93961, 94395, 94830, 95266, 95703, 96141, 96580, 97020, 97461, 97903, 98346, 98790, 99235, 99681, 100128, 100576, 101025, 101475, 101926, 102378, 102831, 103285, 103740, 104196, 104653, 105111, 105570, 106030, 106491, 106953, 107416, 107880, 108345, 108811, 109278, 109746, 110215, 110685, 111156, 111628, 112101, 112575, 113050, 113526, 114003, 114481, 114960, 115440, 115921, 116403, 116886, 117370, 117855, 118341, 118828, 119316, 119805, 120295, 120786, 121278, 121771, 122265, 122760, 123256, 123753, 124251, 124750, 125250, 125751, 126253, 126756, 127260, 127765, 128271, 128778, 129286, 129795, 130305, 130816, 131328, 131841, 132355, 132870, 133386, 133903, 134421, 134940, 135460, 135981, 136503, 137026, 137550, 138075, 138601, 139128, 139656, 140185, 140715, 141246, 141778, 142311, 142845, 143380, 143916, 144453, 144991, 145530, 146070, 146611, 147153, 147696, 148240, 148785, 149331, 149878, 150426, 150975, 151525, 152076, 152628, 153181, 153735, 154290, 154846, 155403, 155961, 156520, 157080, 157641, 158203, 158766, 159330, 159895, 160461, 161028, 161596, 162165, 162735, 163306, 163878, 164451, 165025, 165600, 166176, 166753, 167331, 167910, 168490, 169071, 169653, 170236, 170820, 171405, 171991, 172578, 173166, 173755, 174345, 174936, 175528, 176121, 176715, 177310, 177906, 178503, 179101, 179700, 180300, 180901, 181503, 182106, 182710, 183315, 183921, 184528, 185136, 185745, 186355, 186966, 187578, 188191, 188805, 189420, 190036, 190653, 191271, 191890, 192510, 193131, 193753, 194376, 195000, 195625, 196251, 196878, 197506, 198135, 198765, 199396, 200028, 200661, 201295, 201930, 202566, 203203, 203841, 204480, 205120, 205761, 206403, 207046, 207690, 208335, 208981, 209628, 210276, 210925, 211575, 212226, 212878, 213531, 214185, 214840, 215496, 216153, 216811, 217470, 218130, 218791, 219453, 220116, 220780, 221445, 222111, 222778, 223446, 224115, 224785, 225456, 226128, 226801, 227475, 228150, 228826, 229503, 230181, 230860, 231540, 232221, 232903, 233586, 234270, 234955, 235641, 236328, 237016, 237705, 238395, 239086, 239778, 240471, 241165, 241860, 242556, 243253, 243951, 244650, 245350, 246051, 246753, 247456, 248160, 248865, 249571, 250278, 250986, 251695, 252405, 253116, 253828, 254541, 255255, 255970, 256686, 257403, 258121, 258840, 259560, 260281, 261003, 261726, 262450, 263175, 263901, 264628, 265356, 266085, 266815, 267546, 268278, 269011, 269745, 270480, 271216, 271953, 272691, 273430, 274170, 274911, 275653, 276396, 277140, 277885, 278631, 279378, 280126, 280875, 281625, 282376, 283128, 283881, 284635, 285390, 286146, 286903, 287661, 288420, 289180, 289941, 290703, 291466, 292230, 292995, 293761, 294528, 295296, 296065, 296835, 297606, 298378, 299151, 299925, 300700, 301476, 302253, 303031, 303810, 304590, 305371, 306153, 306936, 307720, 308505, 309291, 310078, 310866, 311655, 312445, 313236, 314028, 314821, 315615, 316410, 317206, 318003, 318801, 319600]
        if res != exp:
            print("Fel i test 1/45: sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799])")
            print("Korrekt svar: [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950, 5050, 5151, 5253, 5356, 5460, 5565, 5671, 5778, 5886, 5995, 6105, 6216, 6328, 6441, 6555, 6670, 6786, 6903, 7021, 7140, 7260, 7381, 7503, 7626, 7750, 7875, 8001, 8128, 8256, 8385, 8515, 8646, 8778, 8911, 9045, 9180, 9316, 9453, 9591, 9730, 9870, 10011, 10153, 10296, 10440, 10585, 10731, 10878, 11026, 11175, 11325, 11476, 11628, 11781, 11935, 12090, 12246, 12403, 12561, 12720, 12880, 13041, 13203, 13366, 13530, 13695, 13861, 14028, 14196, 14365, 14535, 14706, 14878, 15051, 15225, 15400, 15576, 15753, 15931, 16110, 16290, 16471, 16653, 16836, 17020, 17205, 17391, 17578, 17766, 17955, 18145, 18336, 18528, 18721, 18915, 19110, 19306, 19503, 19701, 19900, 20100, 20301, 20503, 20706, 20910, 21115, 21321, 21528, 21736, 21945, 22155, 22366, 22578, 22791, 23005, 23220, 23436, 23653, 23871, 24090, 24310, 24531, 24753, 24976, 25200, 25425, 25651, 25878, 26106, 26335, 26565, 26796, 27028, 27261, 27495, 27730, 27966, 28203, 28441, 28680, 28920, 29161, 29403, 29646, 29890, 30135, 30381, 30628, 30876, 31125, 31375, 31626, 31878, 32131, 32385, 32640, 32896, 33153, 33411, 33670, 33930, 34191, 34453, 34716, 34980, 35245, 35511, 35778, 36046, 36315, 36585, 36856, 37128, 37401, 37675, 37950, 38226, 38503, 38781, 39060, 39340, 39621, 39903, 40186, 40470, 40755, 41041, 41328, 41616, 41905, 42195, 42486, 42778, 43071, 43365, 43660, 43956, 44253, 44551, 44850, 45150, 45451, 45753, 46056, 46360, 46665, 46971, 47278, 47586, 47895, 48205, 48516, 48828, 49141, 49455, 49770, 50086, 50403, 50721, 51040, 51360, 51681, 52003, 52326, 52650, 52975, 53301, 53628, 53956, 54285, 54615, 54946, 55278, 55611, 55945, 56280, 56616, 56953, 57291, 57630, 57970, 58311, 58653, 58996, 59340, 59685, 60031, 60378, 60726, 61075, 61425, 61776, 62128, 62481, 62835, 63190, 63546, 63903, 64261, 64620, 64980, 65341, 65703, 66066, 66430, 66795, 67161, 67528, 67896, 68265, 68635, 69006, 69378, 69751, 70125, 70500, 70876, 71253, 71631, 72010, 72390, 72771, 73153, 73536, 73920, 74305, 74691, 75078, 75466, 75855, 76245, 76636, 77028, 77421, 77815, 78210, 78606, 79003, 79401, 79800, 80200, 80601, 81003, 81406, 81810, 82215, 82621, 83028, 83436, 83845, 84255, 84666, 85078, 85491, 85905, 86320, 86736, 87153, 87571, 87990, 88410, 88831, 89253, 89676, 90100, 90525, 90951, 91378, 91806, 92235, 92665, 93096, 93528, 93961, 94395, 94830, 95266, 95703, 96141, 96580, 97020, 97461, 97903, 98346, 98790, 99235, 99681, 100128, 100576, 101025, 101475, 101926, 102378, 102831, 103285, 103740, 104196, 104653, 105111, 105570, 106030, 106491, 106953, 107416, 107880, 108345, 108811, 109278, 109746, 110215, 110685, 111156, 111628, 112101, 112575, 113050, 113526, 114003, 114481, 114960, 115440, 115921, 116403, 116886, 117370, 117855, 118341, 118828, 119316, 119805, 120295, 120786, 121278, 121771, 122265, 122760, 123256, 123753, 124251, 124750, 125250, 125751, 126253, 126756, 127260, 127765, 128271, 128778, 129286, 129795, 130305, 130816, 131328, 131841, 132355, 132870, 133386, 133903, 134421, 134940, 135460, 135981, 136503, 137026, 137550, 138075, 138601, 139128, 139656, 140185, 140715, 141246, 141778, 142311, 142845, 143380, 143916, 144453, 144991, 145530, 146070, 146611, 147153, 147696, 148240, 148785, 149331, 149878, 150426, 150975, 151525, 152076, 152628, 153181, 153735, 154290, 154846, 155403, 155961, 156520, 157080, 157641, 158203, 158766, 159330, 159895, 160461, 161028, 161596, 162165, 162735, 163306, 163878, 164451, 165025, 165600, 166176, 166753, 167331, 167910, 168490, 169071, 169653, 170236, 170820, 171405, 171991, 172578, 173166, 173755, 174345, 174936, 175528, 176121, 176715, 177310, 177906, 178503, 179101, 179700, 180300, 180901, 181503, 182106, 182710, 183315, 183921, 184528, 185136, 185745, 186355, 186966, 187578, 188191, 188805, 189420, 190036, 190653, 191271, 191890, 192510, 193131, 193753, 194376, 195000, 195625, 196251, 196878, 197506, 198135, 198765, 199396, 200028, 200661, 201295, 201930, 202566, 203203, 203841, 204480, 205120, 205761, 206403, 207046, 207690, 208335, 208981, 209628, 210276, 210925, 211575, 212226, 212878, 213531, 214185, 214840, 215496, 216153, 216811, 217470, 218130, 218791, 219453, 220116, 220780, 221445, 222111, 222778, 223446, 224115, 224785, 225456, 226128, 226801, 227475, 228150, 228826, 229503, 230181, 230860, 231540, 232221, 232903, 233586, 234270, 234955, 235641, 236328, 237016, 237705, 238395, 239086, 239778, 240471, 241165, 241860, 242556, 243253, 243951, 244650, 245350, 246051, 246753, 247456, 248160, 248865, 249571, 250278, 250986, 251695, 252405, 253116, 253828, 254541, 255255, 255970, 256686, 257403, 258121, 258840, 259560, 260281, 261003, 261726, 262450, 263175, 263901, 264628, 265356, 266085, 266815, 267546, 268278, 269011, 269745, 270480, 271216, 271953, 272691, 273430, 274170, 274911, 275653, 276396, 277140, 277885, 278631, 279378, 280126, 280875, 281625, 282376, 283128, 283881, 284635, 285390, 286146, 286903, 287661, 288420, 289180, 289941, 290703, 291466, 292230, 292995, 293761, 294528, 295296, 296065, 296835, 297606, 298378, 299151, 299925, 300700, 301476, 302253, 303031, 303810, 304590, 305371, 306153, 306936, 307720, 308505, 309291, 310078, 310866, 311655, 312445, 313236, 314028, 314821, 315615, 316410, 317206, 318003, 318801, 319600]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 45: Exception')
        print_exception()

    print('Startar test 1/46')
    try:
        res = sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899])
        exp = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950, 5050, 5151, 5253, 5356, 5460, 5565, 5671, 5778, 5886, 5995, 6105, 6216, 6328, 6441, 6555, 6670, 6786, 6903, 7021, 7140, 7260, 7381, 7503, 7626, 7750, 7875, 8001, 8128, 8256, 8385, 8515, 8646, 8778, 8911, 9045, 9180, 9316, 9453, 9591, 9730, 9870, 10011, 10153, 10296, 10440, 10585, 10731, 10878, 11026, 11175, 11325, 11476, 11628, 11781, 11935, 12090, 12246, 12403, 12561, 12720, 12880, 13041, 13203, 13366, 13530, 13695, 13861, 14028, 14196, 14365, 14535, 14706, 14878, 15051, 15225, 15400, 15576, 15753, 15931, 16110, 16290, 16471, 16653, 16836, 17020, 17205, 17391, 17578, 17766, 17955, 18145, 18336, 18528, 18721, 18915, 19110, 19306, 19503, 19701, 19900, 20100, 20301, 20503, 20706, 20910, 21115, 21321, 21528, 21736, 21945, 22155, 22366, 22578, 22791, 23005, 23220, 23436, 23653, 23871, 24090, 24310, 24531, 24753, 24976, 25200, 25425, 25651, 25878, 26106, 26335, 26565, 26796, 27028, 27261, 27495, 27730, 27966, 28203, 28441, 28680, 28920, 29161, 29403, 29646, 29890, 30135, 30381, 30628, 30876, 31125, 31375, 31626, 31878, 32131, 32385, 32640, 32896, 33153, 33411, 33670, 33930, 34191, 34453, 34716, 34980, 35245, 35511, 35778, 36046, 36315, 36585, 36856, 37128, 37401, 37675, 37950, 38226, 38503, 38781, 39060, 39340, 39621, 39903, 40186, 40470, 40755, 41041, 41328, 41616, 41905, 42195, 42486, 42778, 43071, 43365, 43660, 43956, 44253, 44551, 44850, 45150, 45451, 45753, 46056, 46360, 46665, 46971, 47278, 47586, 47895, 48205, 48516, 48828, 49141, 49455, 49770, 50086, 50403, 50721, 51040, 51360, 51681, 52003, 52326, 52650, 52975, 53301, 53628, 53956, 54285, 54615, 54946, 55278, 55611, 55945, 56280, 56616, 56953, 57291, 57630, 57970, 58311, 58653, 58996, 59340, 59685, 60031, 60378, 60726, 61075, 61425, 61776, 62128, 62481, 62835, 63190, 63546, 63903, 64261, 64620, 64980, 65341, 65703, 66066, 66430, 66795, 67161, 67528, 67896, 68265, 68635, 69006, 69378, 69751, 70125, 70500, 70876, 71253, 71631, 72010, 72390, 72771, 73153, 73536, 73920, 74305, 74691, 75078, 75466, 75855, 76245, 76636, 77028, 77421, 77815, 78210, 78606, 79003, 79401, 79800, 80200, 80601, 81003, 81406, 81810, 82215, 82621, 83028, 83436, 83845, 84255, 84666, 85078, 85491, 85905, 86320, 86736, 87153, 87571, 87990, 88410, 88831, 89253, 89676, 90100, 90525, 90951, 91378, 91806, 92235, 92665, 93096, 93528, 93961, 94395, 94830, 95266, 95703, 96141, 96580, 97020, 97461, 97903, 98346, 98790, 99235, 99681, 100128, 100576, 101025, 101475, 101926, 102378, 102831, 103285, 103740, 104196, 104653, 105111, 105570, 106030, 106491, 106953, 107416, 107880, 108345, 108811, 109278, 109746, 110215, 110685, 111156, 111628, 112101, 112575, 113050, 113526, 114003, 114481, 114960, 115440, 115921, 116403, 116886, 117370, 117855, 118341, 118828, 119316, 119805, 120295, 120786, 121278, 121771, 122265, 122760, 123256, 123753, 124251, 124750, 125250, 125751, 126253, 126756, 127260, 127765, 128271, 128778, 129286, 129795, 130305, 130816, 131328, 131841, 132355, 132870, 133386, 133903, 134421, 134940, 135460, 135981, 136503, 137026, 137550, 138075, 138601, 139128, 139656, 140185, 140715, 141246, 141778, 142311, 142845, 143380, 143916, 144453, 144991, 145530, 146070, 146611, 147153, 147696, 148240, 148785, 149331, 149878, 150426, 150975, 151525, 152076, 152628, 153181, 153735, 154290, 154846, 155403, 155961, 156520, 157080, 157641, 158203, 158766, 159330, 159895, 160461, 161028, 161596, 162165, 162735, 163306, 163878, 164451, 165025, 165600, 166176, 166753, 167331, 167910, 168490, 169071, 169653, 170236, 170820, 171405, 171991, 172578, 173166, 173755, 174345, 174936, 175528, 176121, 176715, 177310, 177906, 178503, 179101, 179700, 180300, 180901, 181503, 182106, 182710, 183315, 183921, 184528, 185136, 185745, 186355, 186966, 187578, 188191, 188805, 189420, 190036, 190653, 191271, 191890, 192510, 193131, 193753, 194376, 195000, 195625, 196251, 196878, 197506, 198135, 198765, 199396, 200028, 200661, 201295, 201930, 202566, 203203, 203841, 204480, 205120, 205761, 206403, 207046, 207690, 208335, 208981, 209628, 210276, 210925, 211575, 212226, 212878, 213531, 214185, 214840, 215496, 216153, 216811, 217470, 218130, 218791, 219453, 220116, 220780, 221445, 222111, 222778, 223446, 224115, 224785, 225456, 226128, 226801, 227475, 228150, 228826, 229503, 230181, 230860, 231540, 232221, 232903, 233586, 234270, 234955, 235641, 236328, 237016, 237705, 238395, 239086, 239778, 240471, 241165, 241860, 242556, 243253, 243951, 244650, 245350, 246051, 246753, 247456, 248160, 248865, 249571, 250278, 250986, 251695, 252405, 253116, 253828, 254541, 255255, 255970, 256686, 257403, 258121, 258840, 259560, 260281, 261003, 261726, 262450, 263175, 263901, 264628, 265356, 266085, 266815, 267546, 268278, 269011, 269745, 270480, 271216, 271953, 272691, 273430, 274170, 274911, 275653, 276396, 277140, 277885, 278631, 279378, 280126, 280875, 281625, 282376, 283128, 283881, 284635, 285390, 286146, 286903, 287661, 288420, 289180, 289941, 290703, 291466, 292230, 292995, 293761, 294528, 295296, 296065, 296835, 297606, 298378, 299151, 299925, 300700, 301476, 302253, 303031, 303810, 304590, 305371, 306153, 306936, 307720, 308505, 309291, 310078, 310866, 311655, 312445, 313236, 314028, 314821, 315615, 316410, 317206, 318003, 318801, 319600, 320400, 321201, 322003, 322806, 323610, 324415, 325221, 326028, 326836, 327645, 328455, 329266, 330078, 330891, 331705, 332520, 333336, 334153, 334971, 335790, 336610, 337431, 338253, 339076, 339900, 340725, 341551, 342378, 343206, 344035, 344865, 345696, 346528, 347361, 348195, 349030, 349866, 350703, 351541, 352380, 353220, 354061, 354903, 355746, 356590, 357435, 358281, 359128, 359976, 360825, 361675, 362526, 363378, 364231, 365085, 365940, 366796, 367653, 368511, 369370, 370230, 371091, 371953, 372816, 373680, 374545, 375411, 376278, 377146, 378015, 378885, 379756, 380628, 381501, 382375, 383250, 384126, 385003, 385881, 386760, 387640, 388521, 389403, 390286, 391170, 392055, 392941, 393828, 394716, 395605, 396495, 397386, 398278, 399171, 400065, 400960, 401856, 402753, 403651, 404550]
        if res != exp:
            print("Fel i test 1/46: sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899])")
            print("Korrekt svar: [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950, 5050, 5151, 5253, 5356, 5460, 5565, 5671, 5778, 5886, 5995, 6105, 6216, 6328, 6441, 6555, 6670, 6786, 6903, 7021, 7140, 7260, 7381, 7503, 7626, 7750, 7875, 8001, 8128, 8256, 8385, 8515, 8646, 8778, 8911, 9045, 9180, 9316, 9453, 9591, 9730, 9870, 10011, 10153, 10296, 10440, 10585, 10731, 10878, 11026, 11175, 11325, 11476, 11628, 11781, 11935, 12090, 12246, 12403, 12561, 12720, 12880, 13041, 13203, 13366, 13530, 13695, 13861, 14028, 14196, 14365, 14535, 14706, 14878, 15051, 15225, 15400, 15576, 15753, 15931, 16110, 16290, 16471, 16653, 16836, 17020, 17205, 17391, 17578, 17766, 17955, 18145, 18336, 18528, 18721, 18915, 19110, 19306, 19503, 19701, 19900, 20100, 20301, 20503, 20706, 20910, 21115, 21321, 21528, 21736, 21945, 22155, 22366, 22578, 22791, 23005, 23220, 23436, 23653, 23871, 24090, 24310, 24531, 24753, 24976, 25200, 25425, 25651, 25878, 26106, 26335, 26565, 26796, 27028, 27261, 27495, 27730, 27966, 28203, 28441, 28680, 28920, 29161, 29403, 29646, 29890, 30135, 30381, 30628, 30876, 31125, 31375, 31626, 31878, 32131, 32385, 32640, 32896, 33153, 33411, 33670, 33930, 34191, 34453, 34716, 34980, 35245, 35511, 35778, 36046, 36315, 36585, 36856, 37128, 37401, 37675, 37950, 38226, 38503, 38781, 39060, 39340, 39621, 39903, 40186, 40470, 40755, 41041, 41328, 41616, 41905, 42195, 42486, 42778, 43071, 43365, 43660, 43956, 44253, 44551, 44850, 45150, 45451, 45753, 46056, 46360, 46665, 46971, 47278, 47586, 47895, 48205, 48516, 48828, 49141, 49455, 49770, 50086, 50403, 50721, 51040, 51360, 51681, 52003, 52326, 52650, 52975, 53301, 53628, 53956, 54285, 54615, 54946, 55278, 55611, 55945, 56280, 56616, 56953, 57291, 57630, 57970, 58311, 58653, 58996, 59340, 59685, 60031, 60378, 60726, 61075, 61425, 61776, 62128, 62481, 62835, 63190, 63546, 63903, 64261, 64620, 64980, 65341, 65703, 66066, 66430, 66795, 67161, 67528, 67896, 68265, 68635, 69006, 69378, 69751, 70125, 70500, 70876, 71253, 71631, 72010, 72390, 72771, 73153, 73536, 73920, 74305, 74691, 75078, 75466, 75855, 76245, 76636, 77028, 77421, 77815, 78210, 78606, 79003, 79401, 79800, 80200, 80601, 81003, 81406, 81810, 82215, 82621, 83028, 83436, 83845, 84255, 84666, 85078, 85491, 85905, 86320, 86736, 87153, 87571, 87990, 88410, 88831, 89253, 89676, 90100, 90525, 90951, 91378, 91806, 92235, 92665, 93096, 93528, 93961, 94395, 94830, 95266, 95703, 96141, 96580, 97020, 97461, 97903, 98346, 98790, 99235, 99681, 100128, 100576, 101025, 101475, 101926, 102378, 102831, 103285, 103740, 104196, 104653, 105111, 105570, 106030, 106491, 106953, 107416, 107880, 108345, 108811, 109278, 109746, 110215, 110685, 111156, 111628, 112101, 112575, 113050, 113526, 114003, 114481, 114960, 115440, 115921, 116403, 116886, 117370, 117855, 118341, 118828, 119316, 119805, 120295, 120786, 121278, 121771, 122265, 122760, 123256, 123753, 124251, 124750, 125250, 125751, 126253, 126756, 127260, 127765, 128271, 128778, 129286, 129795, 130305, 130816, 131328, 131841, 132355, 132870, 133386, 133903, 134421, 134940, 135460, 135981, 136503, 137026, 137550, 138075, 138601, 139128, 139656, 140185, 140715, 141246, 141778, 142311, 142845, 143380, 143916, 144453, 144991, 145530, 146070, 146611, 147153, 147696, 148240, 148785, 149331, 149878, 150426, 150975, 151525, 152076, 152628, 153181, 153735, 154290, 154846, 155403, 155961, 156520, 157080, 157641, 158203, 158766, 159330, 159895, 160461, 161028, 161596, 162165, 162735, 163306, 163878, 164451, 165025, 165600, 166176, 166753, 167331, 167910, 168490, 169071, 169653, 170236, 170820, 171405, 171991, 172578, 173166, 173755, 174345, 174936, 175528, 176121, 176715, 177310, 177906, 178503, 179101, 179700, 180300, 180901, 181503, 182106, 182710, 183315, 183921, 184528, 185136, 185745, 186355, 186966, 187578, 188191, 188805, 189420, 190036, 190653, 191271, 191890, 192510, 193131, 193753, 194376, 195000, 195625, 196251, 196878, 197506, 198135, 198765, 199396, 200028, 200661, 201295, 201930, 202566, 203203, 203841, 204480, 205120, 205761, 206403, 207046, 207690, 208335, 208981, 209628, 210276, 210925, 211575, 212226, 212878, 213531, 214185, 214840, 215496, 216153, 216811, 217470, 218130, 218791, 219453, 220116, 220780, 221445, 222111, 222778, 223446, 224115, 224785, 225456, 226128, 226801, 227475, 228150, 228826, 229503, 230181, 230860, 231540, 232221, 232903, 233586, 234270, 234955, 235641, 236328, 237016, 237705, 238395, 239086, 239778, 240471, 241165, 241860, 242556, 243253, 243951, 244650, 245350, 246051, 246753, 247456, 248160, 248865, 249571, 250278, 250986, 251695, 252405, 253116, 253828, 254541, 255255, 255970, 256686, 257403, 258121, 258840, 259560, 260281, 261003, 261726, 262450, 263175, 263901, 264628, 265356, 266085, 266815, 267546, 268278, 269011, 269745, 270480, 271216, 271953, 272691, 273430, 274170, 274911, 275653, 276396, 277140, 277885, 278631, 279378, 280126, 280875, 281625, 282376, 283128, 283881, 284635, 285390, 286146, 286903, 287661, 288420, 289180, 289941, 290703, 291466, 292230, 292995, 293761, 294528, 295296, 296065, 296835, 297606, 298378, 299151, 299925, 300700, 301476, 302253, 303031, 303810, 304590, 305371, 306153, 306936, 307720, 308505, 309291, 310078, 310866, 311655, 312445, 313236, 314028, 314821, 315615, 316410, 317206, 318003, 318801, 319600, 320400, 321201, 322003, 322806, 323610, 324415, 325221, 326028, 326836, 327645, 328455, 329266, 330078, 330891, 331705, 332520, 333336, 334153, 334971, 335790, 336610, 337431, 338253, 339076, 339900, 340725, 341551, 342378, 343206, 344035, 344865, 345696, 346528, 347361, 348195, 349030, 349866, 350703, 351541, 352380, 353220, 354061, 354903, 355746, 356590, 357435, 358281, 359128, 359976, 360825, 361675, 362526, 363378, 364231, 365085, 365940, 366796, 367653, 368511, 369370, 370230, 371091, 371953, 372816, 373680, 374545, 375411, 376278, 377146, 378015, 378885, 379756, 380628, 381501, 382375, 383250, 384126, 385003, 385881, 386760, 387640, 388521, 389403, 390286, 391170, 392055, 392941, 393828, 394716, 395605, 396495, 397386, 398278, 399171, 400065, 400960, 401856, 402753, 403651, 404550]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 46: Exception')
        print_exception()

    print('Startar test 1/47')
    try:
        res = sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999])
        exp = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950, 5050, 5151, 5253, 5356, 5460, 5565, 5671, 5778, 5886, 5995, 6105, 6216, 6328, 6441, 6555, 6670, 6786, 6903, 7021, 7140, 7260, 7381, 7503, 7626, 7750, 7875, 8001, 8128, 8256, 8385, 8515, 8646, 8778, 8911, 9045, 9180, 9316, 9453, 9591, 9730, 9870, 10011, 10153, 10296, 10440, 10585, 10731, 10878, 11026, 11175, 11325, 11476, 11628, 11781, 11935, 12090, 12246, 12403, 12561, 12720, 12880, 13041, 13203, 13366, 13530, 13695, 13861, 14028, 14196, 14365, 14535, 14706, 14878, 15051, 15225, 15400, 15576, 15753, 15931, 16110, 16290, 16471, 16653, 16836, 17020, 17205, 17391, 17578, 17766, 17955, 18145, 18336, 18528, 18721, 18915, 19110, 19306, 19503, 19701, 19900, 20100, 20301, 20503, 20706, 20910, 21115, 21321, 21528, 21736, 21945, 22155, 22366, 22578, 22791, 23005, 23220, 23436, 23653, 23871, 24090, 24310, 24531, 24753, 24976, 25200, 25425, 25651, 25878, 26106, 26335, 26565, 26796, 27028, 27261, 27495, 27730, 27966, 28203, 28441, 28680, 28920, 29161, 29403, 29646, 29890, 30135, 30381, 30628, 30876, 31125, 31375, 31626, 31878, 32131, 32385, 32640, 32896, 33153, 33411, 33670, 33930, 34191, 34453, 34716, 34980, 35245, 35511, 35778, 36046, 36315, 36585, 36856, 37128, 37401, 37675, 37950, 38226, 38503, 38781, 39060, 39340, 39621, 39903, 40186, 40470, 40755, 41041, 41328, 41616, 41905, 42195, 42486, 42778, 43071, 43365, 43660, 43956, 44253, 44551, 44850, 45150, 45451, 45753, 46056, 46360, 46665, 46971, 47278, 47586, 47895, 48205, 48516, 48828, 49141, 49455, 49770, 50086, 50403, 50721, 51040, 51360, 51681, 52003, 52326, 52650, 52975, 53301, 53628, 53956, 54285, 54615, 54946, 55278, 55611, 55945, 56280, 56616, 56953, 57291, 57630, 57970, 58311, 58653, 58996, 59340, 59685, 60031, 60378, 60726, 61075, 61425, 61776, 62128, 62481, 62835, 63190, 63546, 63903, 64261, 64620, 64980, 65341, 65703, 66066, 66430, 66795, 67161, 67528, 67896, 68265, 68635, 69006, 69378, 69751, 70125, 70500, 70876, 71253, 71631, 72010, 72390, 72771, 73153, 73536, 73920, 74305, 74691, 75078, 75466, 75855, 76245, 76636, 77028, 77421, 77815, 78210, 78606, 79003, 79401, 79800, 80200, 80601, 81003, 81406, 81810, 82215, 82621, 83028, 83436, 83845, 84255, 84666, 85078, 85491, 85905, 86320, 86736, 87153, 87571, 87990, 88410, 88831, 89253, 89676, 90100, 90525, 90951, 91378, 91806, 92235, 92665, 93096, 93528, 93961, 94395, 94830, 95266, 95703, 96141, 96580, 97020, 97461, 97903, 98346, 98790, 99235, 99681, 100128, 100576, 101025, 101475, 101926, 102378, 102831, 103285, 103740, 104196, 104653, 105111, 105570, 106030, 106491, 106953, 107416, 107880, 108345, 108811, 109278, 109746, 110215, 110685, 111156, 111628, 112101, 112575, 113050, 113526, 114003, 114481, 114960, 115440, 115921, 116403, 116886, 117370, 117855, 118341, 118828, 119316, 119805, 120295, 120786, 121278, 121771, 122265, 122760, 123256, 123753, 124251, 124750, 125250, 125751, 126253, 126756, 127260, 127765, 128271, 128778, 129286, 129795, 130305, 130816, 131328, 131841, 132355, 132870, 133386, 133903, 134421, 134940, 135460, 135981, 136503, 137026, 137550, 138075, 138601, 139128, 139656, 140185, 140715, 141246, 141778, 142311, 142845, 143380, 143916, 144453, 144991, 145530, 146070, 146611, 147153, 147696, 148240, 148785, 149331, 149878, 150426, 150975, 151525, 152076, 152628, 153181, 153735, 154290, 154846, 155403, 155961, 156520, 157080, 157641, 158203, 158766, 159330, 159895, 160461, 161028, 161596, 162165, 162735, 163306, 163878, 164451, 165025, 165600, 166176, 166753, 167331, 167910, 168490, 169071, 169653, 170236, 170820, 171405, 171991, 172578, 173166, 173755, 174345, 174936, 175528, 176121, 176715, 177310, 177906, 178503, 179101, 179700, 180300, 180901, 181503, 182106, 182710, 183315, 183921, 184528, 185136, 185745, 186355, 186966, 187578, 188191, 188805, 189420, 190036, 190653, 191271, 191890, 192510, 193131, 193753, 194376, 195000, 195625, 196251, 196878, 197506, 198135, 198765, 199396, 200028, 200661, 201295, 201930, 202566, 203203, 203841, 204480, 205120, 205761, 206403, 207046, 207690, 208335, 208981, 209628, 210276, 210925, 211575, 212226, 212878, 213531, 214185, 214840, 215496, 216153, 216811, 217470, 218130, 218791, 219453, 220116, 220780, 221445, 222111, 222778, 223446, 224115, 224785, 225456, 226128, 226801, 227475, 228150, 228826, 229503, 230181, 230860, 231540, 232221, 232903, 233586, 234270, 234955, 235641, 236328, 237016, 237705, 238395, 239086, 239778, 240471, 241165, 241860, 242556, 243253, 243951, 244650, 245350, 246051, 246753, 247456, 248160, 248865, 249571, 250278, 250986, 251695, 252405, 253116, 253828, 254541, 255255, 255970, 256686, 257403, 258121, 258840, 259560, 260281, 261003, 261726, 262450, 263175, 263901, 264628, 265356, 266085, 266815, 267546, 268278, 269011, 269745, 270480, 271216, 271953, 272691, 273430, 274170, 274911, 275653, 276396, 277140, 277885, 278631, 279378, 280126, 280875, 281625, 282376, 283128, 283881, 284635, 285390, 286146, 286903, 287661, 288420, 289180, 289941, 290703, 291466, 292230, 292995, 293761, 294528, 295296, 296065, 296835, 297606, 298378, 299151, 299925, 300700, 301476, 302253, 303031, 303810, 304590, 305371, 306153, 306936, 307720, 308505, 309291, 310078, 310866, 311655, 312445, 313236, 314028, 314821, 315615, 316410, 317206, 318003, 318801, 319600, 320400, 321201, 322003, 322806, 323610, 324415, 325221, 326028, 326836, 327645, 328455, 329266, 330078, 330891, 331705, 332520, 333336, 334153, 334971, 335790, 336610, 337431, 338253, 339076, 339900, 340725, 341551, 342378, 343206, 344035, 344865, 345696, 346528, 347361, 348195, 349030, 349866, 350703, 351541, 352380, 353220, 354061, 354903, 355746, 356590, 357435, 358281, 359128, 359976, 360825, 361675, 362526, 363378, 364231, 365085, 365940, 366796, 367653, 368511, 369370, 370230, 371091, 371953, 372816, 373680, 374545, 375411, 376278, 377146, 378015, 378885, 379756, 380628, 381501, 382375, 383250, 384126, 385003, 385881, 386760, 387640, 388521, 389403, 390286, 391170, 392055, 392941, 393828, 394716, 395605, 396495, 397386, 398278, 399171, 400065, 400960, 401856, 402753, 403651, 404550, 405450, 406351, 407253, 408156, 409060, 409965, 410871, 411778, 412686, 413595, 414505, 415416, 416328, 417241, 418155, 419070, 419986, 420903, 421821, 422740, 423660, 424581, 425503, 426426, 427350, 428275, 429201, 430128, 431056, 431985, 432915, 433846, 434778, 435711, 436645, 437580, 438516, 439453, 440391, 441330, 442270, 443211, 444153, 445096, 446040, 446985, 447931, 448878, 449826, 450775, 451725, 452676, 453628, 454581, 455535, 456490, 457446, 458403, 459361, 460320, 461280, 462241, 463203, 464166, 465130, 466095, 467061, 468028, 468996, 469965, 470935, 471906, 472878, 473851, 474825, 475800, 476776, 477753, 478731, 479710, 480690, 481671, 482653, 483636, 484620, 485605, 486591, 487578, 488566, 489555, 490545, 491536, 492528, 493521, 494515, 495510, 496506, 497503, 498501, 499500]
        if res != exp:
            print("Fel i test 1/47: sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999])")
            print("Korrekt svar: [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950, 5050, 5151, 5253, 5356, 5460, 5565, 5671, 5778, 5886, 5995, 6105, 6216, 6328, 6441, 6555, 6670, 6786, 6903, 7021, 7140, 7260, 7381, 7503, 7626, 7750, 7875, 8001, 8128, 8256, 8385, 8515, 8646, 8778, 8911, 9045, 9180, 9316, 9453, 9591, 9730, 9870, 10011, 10153, 10296, 10440, 10585, 10731, 10878, 11026, 11175, 11325, 11476, 11628, 11781, 11935, 12090, 12246, 12403, 12561, 12720, 12880, 13041, 13203, 13366, 13530, 13695, 13861, 14028, 14196, 14365, 14535, 14706, 14878, 15051, 15225, 15400, 15576, 15753, 15931, 16110, 16290, 16471, 16653, 16836, 17020, 17205, 17391, 17578, 17766, 17955, 18145, 18336, 18528, 18721, 18915, 19110, 19306, 19503, 19701, 19900, 20100, 20301, 20503, 20706, 20910, 21115, 21321, 21528, 21736, 21945, 22155, 22366, 22578, 22791, 23005, 23220, 23436, 23653, 23871, 24090, 24310, 24531, 24753, 24976, 25200, 25425, 25651, 25878, 26106, 26335, 26565, 26796, 27028, 27261, 27495, 27730, 27966, 28203, 28441, 28680, 28920, 29161, 29403, 29646, 29890, 30135, 30381, 30628, 30876, 31125, 31375, 31626, 31878, 32131, 32385, 32640, 32896, 33153, 33411, 33670, 33930, 34191, 34453, 34716, 34980, 35245, 35511, 35778, 36046, 36315, 36585, 36856, 37128, 37401, 37675, 37950, 38226, 38503, 38781, 39060, 39340, 39621, 39903, 40186, 40470, 40755, 41041, 41328, 41616, 41905, 42195, 42486, 42778, 43071, 43365, 43660, 43956, 44253, 44551, 44850, 45150, 45451, 45753, 46056, 46360, 46665, 46971, 47278, 47586, 47895, 48205, 48516, 48828, 49141, 49455, 49770, 50086, 50403, 50721, 51040, 51360, 51681, 52003, 52326, 52650, 52975, 53301, 53628, 53956, 54285, 54615, 54946, 55278, 55611, 55945, 56280, 56616, 56953, 57291, 57630, 57970, 58311, 58653, 58996, 59340, 59685, 60031, 60378, 60726, 61075, 61425, 61776, 62128, 62481, 62835, 63190, 63546, 63903, 64261, 64620, 64980, 65341, 65703, 66066, 66430, 66795, 67161, 67528, 67896, 68265, 68635, 69006, 69378, 69751, 70125, 70500, 70876, 71253, 71631, 72010, 72390, 72771, 73153, 73536, 73920, 74305, 74691, 75078, 75466, 75855, 76245, 76636, 77028, 77421, 77815, 78210, 78606, 79003, 79401, 79800, 80200, 80601, 81003, 81406, 81810, 82215, 82621, 83028, 83436, 83845, 84255, 84666, 85078, 85491, 85905, 86320, 86736, 87153, 87571, 87990, 88410, 88831, 89253, 89676, 90100, 90525, 90951, 91378, 91806, 92235, 92665, 93096, 93528, 93961, 94395, 94830, 95266, 95703, 96141, 96580, 97020, 97461, 97903, 98346, 98790, 99235, 99681, 100128, 100576, 101025, 101475, 101926, 102378, 102831, 103285, 103740, 104196, 104653, 105111, 105570, 106030, 106491, 106953, 107416, 107880, 108345, 108811, 109278, 109746, 110215, 110685, 111156, 111628, 112101, 112575, 113050, 113526, 114003, 114481, 114960, 115440, 115921, 116403, 116886, 117370, 117855, 118341, 118828, 119316, 119805, 120295, 120786, 121278, 121771, 122265, 122760, 123256, 123753, 124251, 124750, 125250, 125751, 126253, 126756, 127260, 127765, 128271, 128778, 129286, 129795, 130305, 130816, 131328, 131841, 132355, 132870, 133386, 133903, 134421, 134940, 135460, 135981, 136503, 137026, 137550, 138075, 138601, 139128, 139656, 140185, 140715, 141246, 141778, 142311, 142845, 143380, 143916, 144453, 144991, 145530, 146070, 146611, 147153, 147696, 148240, 148785, 149331, 149878, 150426, 150975, 151525, 152076, 152628, 153181, 153735, 154290, 154846, 155403, 155961, 156520, 157080, 157641, 158203, 158766, 159330, 159895, 160461, 161028, 161596, 162165, 162735, 163306, 163878, 164451, 165025, 165600, 166176, 166753, 167331, 167910, 168490, 169071, 169653, 170236, 170820, 171405, 171991, 172578, 173166, 173755, 174345, 174936, 175528, 176121, 176715, 177310, 177906, 178503, 179101, 179700, 180300, 180901, 181503, 182106, 182710, 183315, 183921, 184528, 185136, 185745, 186355, 186966, 187578, 188191, 188805, 189420, 190036, 190653, 191271, 191890, 192510, 193131, 193753, 194376, 195000, 195625, 196251, 196878, 197506, 198135, 198765, 199396, 200028, 200661, 201295, 201930, 202566, 203203, 203841, 204480, 205120, 205761, 206403, 207046, 207690, 208335, 208981, 209628, 210276, 210925, 211575, 212226, 212878, 213531, 214185, 214840, 215496, 216153, 216811, 217470, 218130, 218791, 219453, 220116, 220780, 221445, 222111, 222778, 223446, 224115, 224785, 225456, 226128, 226801, 227475, 228150, 228826, 229503, 230181, 230860, 231540, 232221, 232903, 233586, 234270, 234955, 235641, 236328, 237016, 237705, 238395, 239086, 239778, 240471, 241165, 241860, 242556, 243253, 243951, 244650, 245350, 246051, 246753, 247456, 248160, 248865, 249571, 250278, 250986, 251695, 252405, 253116, 253828, 254541, 255255, 255970, 256686, 257403, 258121, 258840, 259560, 260281, 261003, 261726, 262450, 263175, 263901, 264628, 265356, 266085, 266815, 267546, 268278, 269011, 269745, 270480, 271216, 271953, 272691, 273430, 274170, 274911, 275653, 276396, 277140, 277885, 278631, 279378, 280126, 280875, 281625, 282376, 283128, 283881, 284635, 285390, 286146, 286903, 287661, 288420, 289180, 289941, 290703, 291466, 292230, 292995, 293761, 294528, 295296, 296065, 296835, 297606, 298378, 299151, 299925, 300700, 301476, 302253, 303031, 303810, 304590, 305371, 306153, 306936, 307720, 308505, 309291, 310078, 310866, 311655, 312445, 313236, 314028, 314821, 315615, 316410, 317206, 318003, 318801, 319600, 320400, 321201, 322003, 322806, 323610, 324415, 325221, 326028, 326836, 327645, 328455, 329266, 330078, 330891, 331705, 332520, 333336, 334153, 334971, 335790, 336610, 337431, 338253, 339076, 339900, 340725, 341551, 342378, 343206, 344035, 344865, 345696, 346528, 347361, 348195, 349030, 349866, 350703, 351541, 352380, 353220, 354061, 354903, 355746, 356590, 357435, 358281, 359128, 359976, 360825, 361675, 362526, 363378, 364231, 365085, 365940, 366796, 367653, 368511, 369370, 370230, 371091, 371953, 372816, 373680, 374545, 375411, 376278, 377146, 378015, 378885, 379756, 380628, 381501, 382375, 383250, 384126, 385003, 385881, 386760, 387640, 388521, 389403, 390286, 391170, 392055, 392941, 393828, 394716, 395605, 396495, 397386, 398278, 399171, 400065, 400960, 401856, 402753, 403651, 404550, 405450, 406351, 407253, 408156, 409060, 409965, 410871, 411778, 412686, 413595, 414505, 415416, 416328, 417241, 418155, 419070, 419986, 420903, 421821, 422740, 423660, 424581, 425503, 426426, 427350, 428275, 429201, 430128, 431056, 431985, 432915, 433846, 434778, 435711, 436645, 437580, 438516, 439453, 440391, 441330, 442270, 443211, 444153, 445096, 446040, 446985, 447931, 448878, 449826, 450775, 451725, 452676, 453628, 454581, 455535, 456490, 457446, 458403, 459361, 460320, 461280, 462241, 463203, 464166, 465130, 466095, 467061, 468028, 468996, 469965, 470935, 471906, 472878, 473851, 474825, 475800, 476776, 477753, 478731, 479710, 480690, 481671, 482653, 483636, 484620, 485605, 486591, 487578, 488566, 489555, 490545, 491536, 492528, 493521, 494515, 495510, 496506, 497503, 498501, 499500]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 47: Exception')
        print_exception()

    print('Startar test 1/48')
    try:
        res = sums([29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        exp = [29, 57, 84, 110, 135, 159, 182, 204, 225, 245, 264, 282, 299, 315, 330, 344, 357, 369, 380, 390, 399, 407, 414, 420, 425, 429, 432, 434, 435, 435]
        if res != exp:
            print("Fel i test 1/48: sums([29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])")
            print("Korrekt svar: [29, 57, 84, 110, 135, 159, 182, 204, 225, 245, 264, 282, 299, 315, 330, 344, 357, 369, 380, 390, 399, 407, 414, 420, 425, 429, 432, 434, 435, 435]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 48: Exception')
        print_exception()

    print('Startar test 1/49')
    try:
        res = sums([39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        exp = [39, 77, 114, 150, 185, 219, 252, 284, 315, 345, 374, 402, 429, 455, 480, 504, 527, 549, 570, 590, 609, 627, 644, 660, 675, 689, 702, 714, 725, 735, 744, 752, 759, 765, 770, 774, 777, 779, 780, 780]
        if res != exp:
            print("Fel i test 1/49: sums([39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])")
            print("Korrekt svar: [39, 77, 114, 150, 185, 219, 252, 284, 315, 345, 374, 402, 429, 455, 480, 504, 527, 549, 570, 590, 609, 627, 644, 660, 675, 689, 702, 714, 725, 735, 744, 752, 759, 765, 770, 774, 777, 779, 780, 780]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 49: Exception')
        print_exception()

    print('Startar test 1/50')
    try:
        res = sums([49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        exp = [49, 97, 144, 190, 235, 279, 322, 364, 405, 445, 484, 522, 559, 595, 630, 664, 697, 729, 760, 790, 819, 847, 874, 900, 925, 949, 972, 994, 1015, 1035, 1054, 1072, 1089, 1105, 1120, 1134, 1147, 1159, 1170, 1180, 1189, 1197, 1204, 1210, 1215, 1219, 1222, 1224, 1225, 1225]
        if res != exp:
            print("Fel i test 1/50: sums([49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])")
            print("Korrekt svar: [49, 97, 144, 190, 235, 279, 322, 364, 405, 445, 484, 522, 559, 595, 630, 664, 697, 729, 760, 790, 819, 847, 874, 900, 925, 949, 972, 994, 1015, 1035, 1054, 1072, 1089, 1105, 1120, 1134, 1147, 1159, 1170, 1180, 1189, 1197, 1204, 1210, 1215, 1219, 1222, 1224, 1225, 1225]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 50: Exception')
        print_exception()

    print('Startar test 1/51')
    try:
        res = sums([59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        exp = [59, 117, 174, 230, 285, 339, 392, 444, 495, 545, 594, 642, 689, 735, 780, 824, 867, 909, 950, 990, 1029, 1067, 1104, 1140, 1175, 1209, 1242, 1274, 1305, 1335, 1364, 1392, 1419, 1445, 1470, 1494, 1517, 1539, 1560, 1580, 1599, 1617, 1634, 1650, 1665, 1679, 1692, 1704, 1715, 1725, 1734, 1742, 1749, 1755, 1760, 1764, 1767, 1769, 1770, 1770]
        if res != exp:
            print("Fel i test 1/51: sums([59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])")
            print("Korrekt svar: [59, 117, 174, 230, 285, 339, 392, 444, 495, 545, 594, 642, 689, 735, 780, 824, 867, 909, 950, 990, 1029, 1067, 1104, 1140, 1175, 1209, 1242, 1274, 1305, 1335, 1364, 1392, 1419, 1445, 1470, 1494, 1517, 1539, 1560, 1580, 1599, 1617, 1634, 1650, 1665, 1679, 1692, 1704, 1715, 1725, 1734, 1742, 1749, 1755, 1760, 1764, 1767, 1769, 1770, 1770]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 51: Exception')
        print_exception()

    print('Startar test 1/52')
    try:
        res = sums([69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        exp = [69, 137, 204, 270, 335, 399, 462, 524, 585, 645, 704, 762, 819, 875, 930, 984, 1037, 1089, 1140, 1190, 1239, 1287, 1334, 1380, 1425, 1469, 1512, 1554, 1595, 1635, 1674, 1712, 1749, 1785, 1820, 1854, 1887, 1919, 1950, 1980, 2009, 2037, 2064, 2090, 2115, 2139, 2162, 2184, 2205, 2225, 2244, 2262, 2279, 2295, 2310, 2324, 2337, 2349, 2360, 2370, 2379, 2387, 2394, 2400, 2405, 2409, 2412, 2414, 2415, 2415]
        if res != exp:
            print("Fel i test 1/52: sums([69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])")
            print("Korrekt svar: [69, 137, 204, 270, 335, 399, 462, 524, 585, 645, 704, 762, 819, 875, 930, 984, 1037, 1089, 1140, 1190, 1239, 1287, 1334, 1380, 1425, 1469, 1512, 1554, 1595, 1635, 1674, 1712, 1749, 1785, 1820, 1854, 1887, 1919, 1950, 1980, 2009, 2037, 2064, 2090, 2115, 2139, 2162, 2184, 2205, 2225, 2244, 2262, 2279, 2295, 2310, 2324, 2337, 2349, 2360, 2370, 2379, 2387, 2394, 2400, 2405, 2409, 2412, 2414, 2415, 2415]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 52: Exception')
        print_exception()

    print('Startar test 1/53')
    try:
        res = sums([79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        exp = [79, 157, 234, 310, 385, 459, 532, 604, 675, 745, 814, 882, 949, 1015, 1080, 1144, 1207, 1269, 1330, 1390, 1449, 1507, 1564, 1620, 1675, 1729, 1782, 1834, 1885, 1935, 1984, 2032, 2079, 2125, 2170, 2214, 2257, 2299, 2340, 2380, 2419, 2457, 2494, 2530, 2565, 2599, 2632, 2664, 2695, 2725, 2754, 2782, 2809, 2835, 2860, 2884, 2907, 2929, 2950, 2970, 2989, 3007, 3024, 3040, 3055, 3069, 3082, 3094, 3105, 3115, 3124, 3132, 3139, 3145, 3150, 3154, 3157, 3159, 3160, 3160]
        if res != exp:
            print("Fel i test 1/53: sums([79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])")
            print("Korrekt svar: [79, 157, 234, 310, 385, 459, 532, 604, 675, 745, 814, 882, 949, 1015, 1080, 1144, 1207, 1269, 1330, 1390, 1449, 1507, 1564, 1620, 1675, 1729, 1782, 1834, 1885, 1935, 1984, 2032, 2079, 2125, 2170, 2214, 2257, 2299, 2340, 2380, 2419, 2457, 2494, 2530, 2565, 2599, 2632, 2664, 2695, 2725, 2754, 2782, 2809, 2835, 2860, 2884, 2907, 2929, 2950, 2970, 2989, 3007, 3024, 3040, 3055, 3069, 3082, 3094, 3105, 3115, 3124, 3132, 3139, 3145, 3150, 3154, 3157, 3159, 3160, 3160]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 53: Exception')
        print_exception()

    print('Startar test 1/54')
    try:
        res = sums([89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        exp = [89, 177, 264, 350, 435, 519, 602, 684, 765, 845, 924, 1002, 1079, 1155, 1230, 1304, 1377, 1449, 1520, 1590, 1659, 1727, 1794, 1860, 1925, 1989, 2052, 2114, 2175, 2235, 2294, 2352, 2409, 2465, 2520, 2574, 2627, 2679, 2730, 2780, 2829, 2877, 2924, 2970, 3015, 3059, 3102, 3144, 3185, 3225, 3264, 3302, 3339, 3375, 3410, 3444, 3477, 3509, 3540, 3570, 3599, 3627, 3654, 3680, 3705, 3729, 3752, 3774, 3795, 3815, 3834, 3852, 3869, 3885, 3900, 3914, 3927, 3939, 3950, 3960, 3969, 3977, 3984, 3990, 3995, 3999, 4002, 4004, 4005, 4005]
        if res != exp:
            print("Fel i test 1/54: sums([89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])")
            print("Korrekt svar: [89, 177, 264, 350, 435, 519, 602, 684, 765, 845, 924, 1002, 1079, 1155, 1230, 1304, 1377, 1449, 1520, 1590, 1659, 1727, 1794, 1860, 1925, 1989, 2052, 2114, 2175, 2235, 2294, 2352, 2409, 2465, 2520, 2574, 2627, 2679, 2730, 2780, 2829, 2877, 2924, 2970, 3015, 3059, 3102, 3144, 3185, 3225, 3264, 3302, 3339, 3375, 3410, 3444, 3477, 3509, 3540, 3570, 3599, 3627, 3654, 3680, 3705, 3729, 3752, 3774, 3795, 3815, 3834, 3852, 3869, 3885, 3900, 3914, 3927, 3939, 3950, 3960, 3969, 3977, 3984, 3990, 3995, 3999, 4002, 4004, 4005, 4005]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 54: Exception')
        print_exception()

    print('Startar test 1/55')
    try:
        res = sums([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        exp = [99, 197, 294, 390, 485, 579, 672, 764, 855, 945, 1034, 1122, 1209, 1295, 1380, 1464, 1547, 1629, 1710, 1790, 1869, 1947, 2024, 2100, 2175, 2249, 2322, 2394, 2465, 2535, 2604, 2672, 2739, 2805, 2870, 2934, 2997, 3059, 3120, 3180, 3239, 3297, 3354, 3410, 3465, 3519, 3572, 3624, 3675, 3725, 3774, 3822, 3869, 3915, 3960, 4004, 4047, 4089, 4130, 4170, 4209, 4247, 4284, 4320, 4355, 4389, 4422, 4454, 4485, 4515, 4544, 4572, 4599, 4625, 4650, 4674, 4697, 4719, 4740, 4760, 4779, 4797, 4814, 4830, 4845, 4859, 4872, 4884, 4895, 4905, 4914, 4922, 4929, 4935, 4940, 4944, 4947, 4949, 4950, 4950]
        if res != exp:
            print("Fel i test 1/55: sums([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])")
            print("Korrekt svar: [99, 197, 294, 390, 485, 579, 672, 764, 855, 945, 1034, 1122, 1209, 1295, 1380, 1464, 1547, 1629, 1710, 1790, 1869, 1947, 2024, 2100, 2175, 2249, 2322, 2394, 2465, 2535, 2604, 2672, 2739, 2805, 2870, 2934, 2997, 3059, 3120, 3180, 3239, 3297, 3354, 3410, 3465, 3519, 3572, 3624, 3675, 3725, 3774, 3822, 3869, 3915, 3960, 4004, 4047, 4089, 4130, 4170, 4209, 4247, 4284, 4320, 4355, 4389, 4422, 4454, 4485, 4515, 4544, 4572, 4599, 4625, 4650, 4674, 4697, 4719, 4740, 4760, 4779, 4797, 4814, 4830, 4845, 4859, 4872, 4884, 4895, 4905, 4914, 4922, 4929, 4935, 4940, 4944, 4947, 4949, 4950, 4950]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 55: Exception')
        print_exception()

    print('Startar test 1/56')
    try:
        res = sums([6394, 250, 2750, 2232])
        exp = [6394, 6644, 9394, 11626]
        if res != exp:
            print("Fel i test 1/56: sums([6394, 250, 2750, 2232])")
            print("Korrekt svar: [6394, 6644, 9394, 11626]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 56: Exception')
        print_exception()

    print('Startar test 1/57')
    try:
        res = sums([7364, 6766, 8921, 869, 4219])
        exp = [7364, 14130, 23051, 23920, 28139]
        if res != exp:
            print("Fel i test 1/57: sums([7364, 6766, 8921, 869, 4219])")
            print("Korrekt svar: [7364, 14130, 23051, 23920, 28139]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 57: Exception')
        print_exception()

    print('Startar test 1/58')
    try:
        res = sums([297, 2186, 5053, 265, 1988, 6498])
        exp = [297, 2483, 7536, 7801, 9789, 16287]
        if res != exp:
            print("Fel i test 1/58: sums([297, 2186, 5053, 265, 1988, 6498])")
            print("Korrekt svar: [297, 2483, 7536, 7801, 9789, 16287]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 58: Exception')
        print_exception()

    print('Startar test 1/59')
    try:
        res = sums([5449, 2204, 5892, 8094, 64, 8058, 6981])
        exp = [5449, 7653, 13545, 21639, 21703, 29761, 36742]
        if res != exp:
            print("Fel i test 1/59: sums([5449, 2204, 5892, 8094, 64, 8058, 6981])")
            print("Korrekt svar: [5449, 7653, 13545, 21639, 21703, 29761, 36742]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 59: Exception')
        print_exception()

    print('Startar test 1/60')
    try:
        res = sums([3402, 1554, 9572, 3365, 927, 967, 8474, 6037])
        exp = [3402, 4956, 14528, 17893, 18820, 19787, 28261, 34298]
        if res != exp:
            print("Fel i test 1/60: sums([3402, 1554, 9572, 3365, 927, 967, 8474, 6037])")
            print("Korrekt svar: [3402, 4956, 14528, 17893, 18820, 19787, 28261, 34298]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 60: Exception')
        print_exception()

    print('Startar test 1/61')
    try:
        res = sums([8071, 7297, 5362, 9731, 3785, 5520, 8294, 6185, 8617])
        exp = [8071, 15368, 20730, 30461, 34246, 39766, 48060, 54245, 62862]
        if res != exp:
            print("Fel i test 1/61: sums([8071, 7297, 5362, 9731, 3785, 5520, 8294, 6185, 8617])")
            print("Korrekt svar: [8071, 15368, 20730, 30461, 34246, 39766, 48060, 54245, 62862]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 61: Exception')
        print_exception()

    print('Startar test 1/62')
    try:
        res = sums([5773, 7045, 458, 2278, 2893, 797, 2327, 1010, 2779, 6356])
        exp = [5773, 12818, 13276, 15554, 18447, 19244, 21571, 22581, 25360, 31716]
        if res != exp:
            print("Fel i test 1/62: sums([5773, 7045, 458, 2278, 2893, 797, 2327, 1010, 2779, 6356])")
            print("Korrekt svar: [5773, 12818, 13276, 15554, 18447, 19244, 21571, 22581, 25360, 31716]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 62: Exception')
        print_exception()

    print('Startar test 1/63')
    try:
        res = sums([3648, 3701, 2095, 2669, 9366, 6480, 6091, 1711, 7291, 1634, 3794])
        exp = [3648, 7349, 9444, 12113, 21479, 27959, 34050, 35761, 43052, 44686, 48480]
        if res != exp:
            print("Fel i test 1/63: sums([3648, 3701, 2095, 2669, 9366, 6480, 6091, 1711, 7291, 1634, 3794])")
            print("Korrekt svar: [3648, 7349, 9444, 12113, 21479, 27959, 34050, 35761, 43052, 44686, 48480]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 63: Exception')
        print_exception()

    print('Startar test 1/64')
    try:
        res = sums([1394, -4749, -2249, -2767])
        exp = [1394, -3355, -5604, -8371]
        if res != exp:
            print("Fel i test 1/64: sums([1394, -4749, -2249, -2767])")
            print("Korrekt svar: [1394, -3355, -5604, -8371]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 64: Exception')
        print_exception()

    print('Startar test 1/65')
    try:
        res = sums([2364, 1766, 3921, -4130, -780])
        exp = [2364, 4130, 8051, 3921, 3141]
        if res != exp:
            print("Fel i test 1/65: sums([2364, 1766, 3921, -4130, -780])")
            print("Korrekt svar: [2364, 4130, 8051, 3921, 3141]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 65: Exception')
        print_exception()

    print('Startar test 1/66')
    try:
        res = sums([-4702, -2813, 53, -4734, -3011, 1498])
        exp = [-4702, -7515, -7462, -12196, -15207, -13709]
        if res != exp:
            print("Fel i test 1/66: sums([-4702, -2813, 53, -4734, -3011, 1498])")
            print("Korrekt svar: [-4702, -7515, -7462, -12196, -15207, -13709]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 66: Exception')
        print_exception()

    print('Startar test 1/67')
    try:
        res = sums([449, -2795, 892, 3094, -4935, 3058, 1981])
        exp = [449, -2346, -1454, 1640, -3295, -237, 1744]
        if res != exp:
            print("Fel i test 1/67: sums([449, -2795, 892, 3094, -4935, 3058, 1981])")
            print("Korrekt svar: [449, -2346, -1454, 1640, -3295, -237, 1744]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 67: Exception')
        print_exception()

    print('Startar test 1/68')
    try:
        res = sums([-1597, -3445, 4572, -1634, -4072, -4032, 3474, 1037])
        exp = [-1597, -5042, -470, -2104, -6176, -10208, -6734, -5697]
        if res != exp:
            print("Fel i test 1/68: sums([-1597, -3445, 4572, -1634, -4072, -4032, 3474, 1037])")
            print("Korrekt svar: [-1597, -5042, -470, -2104, -6176, -10208, -6734, -5697]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 68: Exception')
        print_exception()

    print('Startar test 1/69')
    try:
        res = sums([3071, 2297, 362, 4731, -1214, 520, 3294, 1185, 3617])
        exp = [3071, 5368, 5730, 10461, 9247, 9767, 13061, 14246, 17863]
        if res != exp:
            print("Fel i test 1/69: sums([3071, 2297, 362, 4731, -1214, 520, 3294, 1185, 3617])")
            print("Korrekt svar: [3071, 5368, 5730, 10461, 9247, 9767, 13061, 14246, 17863]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 69: Exception')
        print_exception()

    print('Startar test 1/70')
    try:
        res = sums([773, 2045, -4541, -2721, -2106, -4202, -2672, -3989, -2220, 1356])
        exp = [773, 2818, -1723, -4444, -6550, -10752, -13424, -17413, -19633, -18277]
        if res != exp:
            print("Fel i test 1/70: sums([773, 2045, -4541, -2721, -2106, -4202, -2672, -3989, -2220, 1356])")
            print("Korrekt svar: [773, 2818, -1723, -4444, -6550, -10752, -13424, -17413, -19633, -18277]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 70: Exception')
        print_exception()

    print('Startar test 1/71')
    try:
        res = sums([-1351, -1298, -2904, -2330, 4366, 1480, 1091, -3288, 2291, -3365, -1205])
        exp = [-1351, -2649, -5553, -7883, -3517, -2037, -946, -4234, -1943, -5308, -6513]
        if res != exp:
            print("Fel i test 1/71: sums([-1351, -1298, -2904, -2330, 4366, 1480, 1091, -3288, 2291, -3365, -1205])")
            print("Korrekt svar: [-1351, -2649, -5553, -7883, -3517, -2037, -946, -4234, -1943, -5308, -6513]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 71: Exception')
        print_exception()

    print('Startar test 1/72')
    try:
        res = sums([1])
        exp = [1]
        if res != exp:
            print("Fel i test 1/72: sums([1])")
            print("Korrekt svar: [1]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 72: Exception')
        print_exception()

    print('Startar test 1/73')
    try:
        res = sums([1, 2, 3, 4, 5, 6, 7, 8])
        exp = [1, 3, 6, 10, 15, 21, 28, 36]
        if res != exp:
            print("Fel i test 1/73: sums([1, 2, 3, 4, 5, 6, 7, 8])")
            print("Korrekt svar: [1, 3, 6, 10, 15, 21, 28, 36]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 73: Exception')
        print_exception()

    print('Startar test 1/74')
    try:
        res = sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        exp = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120]
        if res != exp:
            print("Fel i test 1/74: sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])")
            print("Korrekt svar: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 74: Exception')
        print_exception()

    print('Startar test 1/75')
    try:
        res = sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
        exp = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253]
        if res != exp:
            print("Fel i test 1/75: sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])")
            print("Korrekt svar: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 75: Exception')
        print_exception()

    print('Startar test 1/76')
    try:
        res = sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
        exp = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435]
        if res != exp:
            print("Fel i test 1/76: sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])")
            print("Korrekt svar: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 76: Exception')
        print_exception()

    print('Startar test 1/77')
    try:
        res = sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36])
        exp = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666]
        if res != exp:
            print("Fel i test 1/77: sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36])")
            print("Korrekt svar: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 77: Exception')
        print_exception()

    print('Startar test 1/78')
    try:
        res = sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43])
        exp = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946]
        if res != exp:
            print("Fel i test 1/78: sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43])")
            print("Korrekt svar: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 78: Exception')
        print_exception()

    print('Startar test 1/79')
    try:
        res = sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])
        exp = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275]
        if res != exp:
            print("Fel i test 1/79: sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])")
            print("Korrekt svar: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 79: Exception')
        print_exception()

    print('Startar test 1/80')
    try:
        res = sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57])
        exp = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653]
        if res != exp:
            print("Fel i test 1/80: sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57])")
            print("Korrekt svar: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 80: Exception')
        print_exception()

    print('Startar test 1/81')
    try:
        res = sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64])
        exp = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080]
        if res != exp:
            print("Fel i test 1/81: sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64])")
            print("Korrekt svar: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 81: Exception')
        print_exception()

    print('Startar test 1/82')
    try:
        res = sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71])
        exp = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556]
        if res != exp:
            print("Fel i test 1/82: sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71])")
            print("Korrekt svar: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 82: Exception')
        print_exception()

    print('Startar test 1/83')
    try:
        res = sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78])
        exp = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081]
        if res != exp:
            print("Fel i test 1/83: sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78])")
            print("Korrekt svar: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 83: Exception')
        print_exception()

    print('Startar test 1/84')
    try:
        res = sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85])
        exp = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655]
        if res != exp:
            print("Fel i test 1/84: sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85])")
            print("Korrekt svar: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 84: Exception')
        print_exception()

    print('Startar test 1/85')
    try:
        res = sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92])
        exp = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278]
        if res != exp:
            print("Fel i test 1/85: sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92])")
            print("Korrekt svar: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 85: Exception')
        print_exception()

    print('Startar test 1/86')
    try:
        res = sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
        exp = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950]
        if res != exp:
            print("Fel i test 1/86: sums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])")
            print("Korrekt svar: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 86: Exception')
        print_exception()


    print('Klar med tester fÃ¶r uppgift 1')
    print()


# noinspection PyBroadException
def test_2():
    print('PÃ¥bÃ¶rjar tester fÃ¶r uppgift 2')

    print('Startar test 2/1')
    try:
        res = merge([], [1])
        exp = [1]
        if res != exp:
            print("Fel i test 2/1: merge([], [1])")
            print("Korrekt svar: [1]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 1: Exception')
        print_exception()

    print('Startar test 2/2')
    try:
        res = merge([1, 2, 5, 13], [3, 5, 21])
        exp = [1, 2, 3, 5, 5, 13, 21]
        if res != exp:
            print("Fel i test 2/2: merge([1, 2, 5, 13], [3, 5, 21])")
            print("Korrekt svar: [1, 2, 3, 5, 5, 13, 21]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2: Exception')
        print_exception()

    print('Startar test 2/3')
    try:
        res = merge(['a', 'c'], ['b', 'o'])
        exp = ['a', 'b', 'c', 'o']
        if res != exp:
            print("Fel i test 2/3: merge(['a', 'c'], ['b', 'o'])")
            print("Korrekt svar: ['a', 'b', 'c', 'o']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3: Exception')
        print_exception()

    print('Startar test 2/4')
    try:
        res = merge([], [])
        exp = []
        if res != exp:
            print("Fel i test 2/4: merge([], [])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4: Exception')
        print_exception()

    print('Startar test 2/5')
    try:
        res = merge([1], [])
        exp = [1]
        if res != exp:
            print("Fel i test 2/5: merge([1], [])")
            print("Korrekt svar: [1]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5: Exception')
        print_exception()

    print('Startar test 2/6')
    try:
        res = merge([1, 5, 6], [2, 4, 8])
        exp = [1, 2, 4, 5, 6, 8]
        if res != exp:
            print("Fel i test 2/6: merge([1, 5, 6], [2, 4, 8])")
            print("Korrekt svar: [1, 2, 4, 5, 6, 8]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 6: Exception')
        print_exception()

    print('Startar test 2/7')
    try:
        res = merge([1, 1], [1])
        exp = [1, 1, 1]
        if res != exp:
            print("Fel i test 2/7: merge([1, 1], [1])")
            print("Korrekt svar: [1, 1, 1]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 7: Exception')
        print_exception()

    print('Startar test 2/8')
    try:
        res = merge([3, 5], [3, 5])
        exp = [3, 3, 5, 5]
        if res != exp:
            print("Fel i test 2/8: merge([3, 5], [3, 5])")
            print("Korrekt svar: [3, 3, 5, 5]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 8: Exception')
        print_exception()

    print('Startar test 2/9')
    try:
        res = merge(['a', 'c'], ['b'])
        exp = ['a', 'b', 'c']
        if res != exp:
            print("Fel i test 2/9: merge(['a', 'c'], ['b'])")
            print("Korrekt svar: ['a', 'b', 'c']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 9: Exception')
        print_exception()

    print('Startar test 2/10')
    try:
        res = merge(['b'], ['a', 'c'])
        exp = ['a', 'b', 'c']
        if res != exp:
            print("Fel i test 2/10: merge(['b'], ['a', 'c'])")
            print("Korrekt svar: ['a', 'b', 'c']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 10: Exception')
        print_exception()

    print('Startar test 2/11')
    try:
        res = merge([3, 3], [5, 5])
        exp = [3, 3, 5, 5]
        if res != exp:
            print("Fel i test 2/11: merge([3, 3], [5, 5])")
            print("Korrekt svar: [3, 3, 5, 5]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 11: Exception')
        print_exception()

    print('Startar test 2/12')
    try:
        res = merge([3, 3, 3], [5, 5])
        exp = [3, 3, 3, 5, 5]
        if res != exp:
            print("Fel i test 2/12: merge([3, 3, 3], [5, 5])")
            print("Korrekt svar: [3, 3, 3, 5, 5]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 12: Exception')
        print_exception()

    print('Startar test 2/13')
    try:
        res = merge([1, 3, 3, 3], [5, 5])
        exp = [1, 3, 3, 3, 5, 5]
        if res != exp:
            print("Fel i test 2/13: merge([1, 3, 3, 3], [5, 5])")
            print("Korrekt svar: [1, 3, 3, 3, 5, 5]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 13: Exception')
        print_exception()

    print('Startar test 2/14')
    try:
        res = merge([1, 3, 3, 3, 8], [5, 5])
        exp = [1, 3, 3, 3, 5, 5, 8]
        if res != exp:
            print("Fel i test 2/14: merge([1, 3, 3, 3, 8], [5, 5])")
            print("Korrekt svar: [1, 3, 3, 3, 5, 5, 8]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 14: Exception')
        print_exception()

    print('Startar test 2/15')
    try:
        res = merge([1, 3, 3, 3, 8], [3, 5, 5])
        exp = [1, 3, 3, 3, 3, 5, 5, 8]
        if res != exp:
            print("Fel i test 2/15: merge([1, 3, 3, 3, 8], [3, 5, 5])")
            print("Korrekt svar: [1, 3, 3, 3, 3, 5, 5, 8]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 15: Exception')
        print_exception()

    print('Startar test 2/16')
    try:
        res = merge([3, 5, 5], [1, 3, 3, 3, 8])
        exp = [1, 3, 3, 3, 3, 5, 5, 8]
        if res != exp:
            print("Fel i test 2/16: merge([3, 5, 5], [1, 3, 3, 3, 8])")
            print("Korrekt svar: [1, 3, 3, 3, 3, 5, 5, 8]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 16: Exception')
        print_exception()

    print('Startar test 2/17')
    try:
        res = merge(['abc', 'cde'], ['bpq'])
        exp = ['abc', 'bpq', 'cde']
        if res != exp:
            print("Fel i test 2/17: merge(['abc', 'cde'], ['bpq'])")
            print("Korrekt svar: ['abc', 'bpq', 'cde']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 17: Exception')
        print_exception()

    print('Startar test 2/18')
    try:
        res = merge(['abc', 'cde'], ['aba', 'cdf'])
        exp = ['aba', 'abc', 'cde', 'cdf']
        if res != exp:
            print("Fel i test 2/18: merge(['abc', 'cde'], ['aba', 'cdf'])")
            print("Korrekt svar: ['aba', 'abc', 'cde', 'cdf']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 18: Exception')
        print_exception()

    print('Startar test 2/19')
    try:
        res = merge(['av', 'frÃ¥n', 'hav', 'i', 'laxmassor', 'lÃ¤ngd', 'nÃ¥gra', 'olika', 'strÃ¤ngar', 'totalfÃ¶rstÃ¶rt'], ['av', 'frÃ¥n', 'hav', 'i', 'laxmassor', 'lÃ¤ngd', 'nÃ¥gra', 'olika', 'strÃ¤ngar', 'totalfÃ¶rstÃ¶rt'])
        exp = ['av', 'av', 'frÃ¥n', 'frÃ¥n', 'hav', 'hav', 'i', 'i', 'laxmassor', 'laxmassor', 'lÃ¤ngd', 'lÃ¤ngd', 'nÃ¥gra', 'nÃ¥gra', 'olika', 'olika', 'strÃ¤ngar', 'strÃ¤ngar', 'totalfÃ¶rstÃ¶rt', 'totalfÃ¶rstÃ¶rt']
        if res != exp:
            print("Fel i test 2/19: merge(['av', 'frÃ¥n', 'hav', 'i', 'laxmassor', 'lÃ¤ngd', 'nÃ¥gra', 'olika', 'strÃ¤ngar', 'totalfÃ¶rstÃ¶rt'], ['av', 'frÃ¥n', 'hav', 'i', 'laxmassor', 'lÃ¤ngd', 'nÃ¥gra', 'olika', 'strÃ¤ngar', 'totalfÃ¶rstÃ¶rt'])")
            print("Korrekt svar: ['av', 'av', 'frÃ¥n', 'frÃ¥n', 'hav', 'hav', 'i', 'i', 'laxmassor', 'laxmassor', 'lÃ¤ngd', 'lÃ¤ngd', 'nÃ¥gra', 'nÃ¥gra', 'olika', 'olika', 'strÃ¤ngar', 'strÃ¤ngar', 'totalfÃ¶rstÃ¶rt', 'totalfÃ¶rstÃ¶rt']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 19: Exception')
        print_exception()

    print('Startar test 2/20')
    try:
        res = merge([(1, 2), (3, 4, 5), (4, 5), (4, 5), (4, 5)], [(2,), (2, 3, 4), (2, 5), (7, 8, 9)])
        exp = [(1, 2), (2,), (2, 3, 4), (2, 5), (3, 4, 5), (4, 5), (4, 5), (4, 5), (7, 8, 9)]
        if res != exp:
            print("Fel i test 2/20: merge([(1, 2), (3, 4, 5), (4, 5), (4, 5), (4, 5)], [(2,), (2, 3, 4), (2, 5), (7, 8, 9)])")
            print("Korrekt svar: [(1, 2), (2,), (2, 3, 4), (2, 5), (3, 4, 5), (4, 5), (4, 5), (4, 5), (7, 8, 9)]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 20: Exception')
        print_exception()

    print('Startar test 2/21')
    try:
        res = merge([3, 3, 5, 5, 7, 7], [3, 3, 5, 5, 7, 7, 7])
        exp = [3, 3, 3, 3, 5, 5, 5, 5, 7, 7, 7, 7, 7]
        if res != exp:
            print("Fel i test 2/21: merge([3, 3, 5, 5, 7, 7], [3, 3, 5, 5, 7, 7, 7])")
            print("Korrekt svar: [3, 3, 3, 3, 5, 5, 5, 5, 7, 7, 7, 7, 7]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 21: Exception')
        print_exception()

    print('Startar test 2/22')
    try:
        res = merge([1, 3, 3, 5, 5, 7, 7], [3, 3, 5, 5, 7, 7, 7])
        exp = [1, 3, 3, 3, 3, 5, 5, 5, 5, 7, 7, 7, 7, 7]
        if res != exp:
            print("Fel i test 2/22: merge([1, 3, 3, 5, 5, 7, 7], [3, 3, 5, 5, 7, 7, 7])")
            print("Korrekt svar: [1, 3, 3, 3, 3, 5, 5, 5, 5, 7, 7, 7, 7, 7]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 22: Exception')
        print_exception()

    print('Startar test 2/23')
    try:
        res = merge([1, 3, 3, 5, 5, 7, 7, 12], [3, 3, 5, 5, 7, 7, 7])
        exp = [1, 3, 3, 3, 3, 5, 5, 5, 5, 7, 7, 7, 7, 7, 12]
        if res != exp:
            print("Fel i test 2/23: merge([1, 3, 3, 5, 5, 7, 7, 12], [3, 3, 5, 5, 7, 7, 7])")
            print("Korrekt svar: [1, 3, 3, 3, 3, 5, 5, 5, 5, 7, 7, 7, 7, 7, 12]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 23: Exception')
        print_exception()

    print('Startar test 2/24')
    try:
        res = merge([1, 3, 3, 5, 5, 6, 7, 7, 12], [3, 3, 5, 5, 7, 7, 7])
        exp = [1, 3, 3, 3, 3, 5, 5, 5, 5, 6, 7, 7, 7, 7, 7, 12]
        if res != exp:
            print("Fel i test 2/24: merge([1, 3, 3, 5, 5, 6, 7, 7, 12], [3, 3, 5, 5, 7, 7, 7])")
            print("Korrekt svar: [1, 3, 3, 3, 3, 5, 5, 5, 5, 6, 7, 7, 7, 7, 7, 12]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 24: Exception')
        print_exception()

    print('Startar test 2/25')
    try:
        res = merge([(1, 2, 3), (4, 5), (12, 42)], [(1,), (7, 3), (15, 0, 7)])
        exp = [(1,), (1, 2, 3), (4, 5), (7, 3), (12, 42), (15, 0, 7)]
        if res != exp:
            print("Fel i test 2/25: merge([(1, 2, 3), (4, 5), (12, 42)], [(1,), (7, 3), (15, 0, 7)])")
            print("Korrekt svar: [(1,), (1, 2, 3), (4, 5), (7, 3), (12, 42), (15, 0, 7)]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 25: Exception')
        print_exception()

    print('Startar test 2/26')
    try:
        res = merge([42], [10])
        exp = [10, 42]
        if res != exp:
            print("Fel i test 2/26: merge([42], [10])")
            print("Korrekt svar: [10, 42]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 26: Exception')
        print_exception()

    print('Startar test 2/27')
    try:
        res = merge([42], [10, 11])
        exp = [10, 11, 42]
        if res != exp:
            print("Fel i test 2/27: merge([42], [10, 11])")
            print("Korrekt svar: [10, 11, 42]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 27: Exception')
        print_exception()

    print('Startar test 2/28')
    try:
        res = merge([42, 43], [10])
        exp = [10, 42, 43]
        if res != exp:
            print("Fel i test 2/28: merge([42, 43], [10])")
            print("Korrekt svar: [10, 42, 43]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 28: Exception')
        print_exception()

    print('Startar test 2/29')
    try:
        res = merge([42, 43], [10, 11])
        exp = [10, 11, 42, 43]
        if res != exp:
            print("Fel i test 2/29: merge([42, 43], [10, 11])")
            print("Korrekt svar: [10, 11, 42, 43]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 29: Exception')
        print_exception()

    print('Startar test 2/30')
    try:
        res = merge([42, 43, 44], [10])
        exp = [10, 42, 43, 44]
        if res != exp:
            print("Fel i test 2/30: merge([42, 43, 44], [10])")
            print("Korrekt svar: [10, 42, 43, 44]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 30: Exception')
        print_exception()

    print('Startar test 2/31')
    try:
        res = merge([42, 43, 44], [10, 11])
        exp = [10, 11, 42, 43, 44]
        if res != exp:
            print("Fel i test 2/31: merge([42, 43, 44], [10, 11])")
            print("Korrekt svar: [10, 11, 42, 43, 44]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 31: Exception')
        print_exception()

    print('Startar test 2/32')
    try:
        res = merge([42, 43, 44, 45], [10])
        exp = [10, 42, 43, 44, 45]
        if res != exp:
            print("Fel i test 2/32: merge([42, 43, 44, 45], [10])")
            print("Korrekt svar: [10, 42, 43, 44, 45]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 32: Exception')
        print_exception()

    print('Startar test 2/33')
    try:
        res = merge([42, 43, 44, 45], [10, 11])
        exp = [10, 11, 42, 43, 44, 45]
        if res != exp:
            print("Fel i test 2/33: merge([42, 43, 44, 45], [10, 11])")
            print("Korrekt svar: [10, 11, 42, 43, 44, 45]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 33: Exception')
        print_exception()

    print('Startar test 2/34')
    try:
        res = merge([42, 43, 44, 45, 46], [10])
        exp = [10, 42, 43, 44, 45, 46]
        if res != exp:
            print("Fel i test 2/34: merge([42, 43, 44, 45, 46], [10])")
            print("Korrekt svar: [10, 42, 43, 44, 45, 46]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 34: Exception')
        print_exception()

    print('Startar test 2/35')
    try:
        res = merge([42, 43, 44, 45, 46], [10, 11])
        exp = [10, 11, 42, 43, 44, 45, 46]
        if res != exp:
            print("Fel i test 2/35: merge([42, 43, 44, 45, 46], [10, 11])")
            print("Korrekt svar: [10, 11, 42, 43, 44, 45, 46]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 35: Exception')
        print_exception()

    print('Startar test 2/36')
    try:
        res = merge([42, 43, 44, 45, 46, 47], [10])
        exp = [10, 42, 43, 44, 45, 46, 47]
        if res != exp:
            print("Fel i test 2/36: merge([42, 43, 44, 45, 46, 47], [10])")
            print("Korrekt svar: [10, 42, 43, 44, 45, 46, 47]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 36: Exception')
        print_exception()

    print('Startar test 2/37')
    try:
        res = merge([42, 43, 44, 45, 46, 47], [10, 11])
        exp = [10, 11, 42, 43, 44, 45, 46, 47]
        if res != exp:
            print("Fel i test 2/37: merge([42, 43, 44, 45, 46, 47], [10, 11])")
            print("Korrekt svar: [10, 11, 42, 43, 44, 45, 46, 47]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 37: Exception')
        print_exception()

    print('Startar test 2/38')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48], [10])
        exp = [10, 42, 43, 44, 45, 46, 47, 48]
        if res != exp:
            print("Fel i test 2/38: merge([42, 43, 44, 45, 46, 47, 48], [10])")
            print("Korrekt svar: [10, 42, 43, 44, 45, 46, 47, 48]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 38: Exception')
        print_exception()

    print('Startar test 2/39')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48], [10, 11])
        exp = [10, 11, 42, 43, 44, 45, 46, 47, 48]
        if res != exp:
            print("Fel i test 2/39: merge([42, 43, 44, 45, 46, 47, 48], [10, 11])")
            print("Korrekt svar: [10, 11, 42, 43, 44, 45, 46, 47, 48]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 39: Exception')
        print_exception()

    print('Startar test 2/40')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48, 49], [10])
        exp = [10, 42, 43, 44, 45, 46, 47, 48, 49]
        if res != exp:
            print("Fel i test 2/40: merge([42, 43, 44, 45, 46, 47, 48, 49], [10])")
            print("Korrekt svar: [10, 42, 43, 44, 45, 46, 47, 48, 49]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 40: Exception')
        print_exception()

    print('Startar test 2/41')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48, 49], [10, 11])
        exp = [10, 11, 42, 43, 44, 45, 46, 47, 48, 49]
        if res != exp:
            print("Fel i test 2/41: merge([42, 43, 44, 45, 46, 47, 48, 49], [10, 11])")
            print("Korrekt svar: [10, 11, 42, 43, 44, 45, 46, 47, 48, 49]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 41: Exception')
        print_exception()

    print('Startar test 2/42')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48, 49, 50], [10])
        exp = [10, 42, 43, 44, 45, 46, 47, 48, 49, 50]
        if res != exp:
            print("Fel i test 2/42: merge([42, 43, 44, 45, 46, 47, 48, 49, 50], [10])")
            print("Korrekt svar: [10, 42, 43, 44, 45, 46, 47, 48, 49, 50]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 42: Exception')
        print_exception()

    print('Startar test 2/43')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48, 49, 50], [10, 11])
        exp = [10, 11, 42, 43, 44, 45, 46, 47, 48, 49, 50]
        if res != exp:
            print("Fel i test 2/43: merge([42, 43, 44, 45, 46, 47, 48, 49, 50], [10, 11])")
            print("Korrekt svar: [10, 11, 42, 43, 44, 45, 46, 47, 48, 49, 50]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 43: Exception')
        print_exception()

    print('Startar test 2/44')
    try:
        res = merge([42], [42])
        exp = [42, 42]
        if res != exp:
            print("Fel i test 2/44: merge([42], [42])")
            print("Korrekt svar: [42, 42]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 44: Exception')
        print_exception()

    print('Startar test 2/45')
    try:
        res = merge([42], [42, 43])
        exp = [42, 42, 43]
        if res != exp:
            print("Fel i test 2/45: merge([42], [42, 43])")
            print("Korrekt svar: [42, 42, 43]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 45: Exception')
        print_exception()

    print('Startar test 2/46')
    try:
        res = merge([42, 43], [42])
        exp = [42, 42, 43]
        if res != exp:
            print("Fel i test 2/46: merge([42, 43], [42])")
            print("Korrekt svar: [42, 42, 43]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 46: Exception')
        print_exception()

    print('Startar test 2/47')
    try:
        res = merge([42, 43], [42, 43])
        exp = [42, 42, 43, 43]
        if res != exp:
            print("Fel i test 2/47: merge([42, 43], [42, 43])")
            print("Korrekt svar: [42, 42, 43, 43]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 47: Exception')
        print_exception()

    print('Startar test 2/48')
    try:
        res = merge([42, 43, 44], [42])
        exp = [42, 42, 43, 44]
        if res != exp:
            print("Fel i test 2/48: merge([42, 43, 44], [42])")
            print("Korrekt svar: [42, 42, 43, 44]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 48: Exception')
        print_exception()

    print('Startar test 2/49')
    try:
        res = merge([42, 43, 44], [42, 43])
        exp = [42, 42, 43, 43, 44]
        if res != exp:
            print("Fel i test 2/49: merge([42, 43, 44], [42, 43])")
            print("Korrekt svar: [42, 42, 43, 43, 44]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 49: Exception')
        print_exception()

    print('Startar test 2/50')
    try:
        res = merge([42, 43, 44, 45], [42])
        exp = [42, 42, 43, 44, 45]
        if res != exp:
            print("Fel i test 2/50: merge([42, 43, 44, 45], [42])")
            print("Korrekt svar: [42, 42, 43, 44, 45]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 50: Exception')
        print_exception()

    print('Startar test 2/51')
    try:
        res = merge([42, 43, 44, 45], [42, 43])
        exp = [42, 42, 43, 43, 44, 45]
        if res != exp:
            print("Fel i test 2/51: merge([42, 43, 44, 45], [42, 43])")
            print("Korrekt svar: [42, 42, 43, 43, 44, 45]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 51: Exception')
        print_exception()

    print('Startar test 2/52')
    try:
        res = merge([42, 43, 44, 45, 46], [42])
        exp = [42, 42, 43, 44, 45, 46]
        if res != exp:
            print("Fel i test 2/52: merge([42, 43, 44, 45, 46], [42])")
            print("Korrekt svar: [42, 42, 43, 44, 45, 46]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 52: Exception')
        print_exception()

    print('Startar test 2/53')
    try:
        res = merge([42, 43, 44, 45, 46], [42, 43])
        exp = [42, 42, 43, 43, 44, 45, 46]
        if res != exp:
            print("Fel i test 2/53: merge([42, 43, 44, 45, 46], [42, 43])")
            print("Korrekt svar: [42, 42, 43, 43, 44, 45, 46]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 53: Exception')
        print_exception()

    print('Startar test 2/54')
    try:
        res = merge([42, 43, 44, 45, 46, 47], [42])
        exp = [42, 42, 43, 44, 45, 46, 47]
        if res != exp:
            print("Fel i test 2/54: merge([42, 43, 44, 45, 46, 47], [42])")
            print("Korrekt svar: [42, 42, 43, 44, 45, 46, 47]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 54: Exception')
        print_exception()

    print('Startar test 2/55')
    try:
        res = merge([42, 43, 44, 45, 46, 47], [42, 43])
        exp = [42, 42, 43, 43, 44, 45, 46, 47]
        if res != exp:
            print("Fel i test 2/55: merge([42, 43, 44, 45, 46, 47], [42, 43])")
            print("Korrekt svar: [42, 42, 43, 43, 44, 45, 46, 47]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 55: Exception')
        print_exception()

    print('Startar test 2/56')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48], [42])
        exp = [42, 42, 43, 44, 45, 46, 47, 48]
        if res != exp:
            print("Fel i test 2/56: merge([42, 43, 44, 45, 46, 47, 48], [42])")
            print("Korrekt svar: [42, 42, 43, 44, 45, 46, 47, 48]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 56: Exception')
        print_exception()

    print('Startar test 2/57')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48], [42, 43])
        exp = [42, 42, 43, 43, 44, 45, 46, 47, 48]
        if res != exp:
            print("Fel i test 2/57: merge([42, 43, 44, 45, 46, 47, 48], [42, 43])")
            print("Korrekt svar: [42, 42, 43, 43, 44, 45, 46, 47, 48]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 57: Exception')
        print_exception()

    print('Startar test 2/58')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48, 49], [42])
        exp = [42, 42, 43, 44, 45, 46, 47, 48, 49]
        if res != exp:
            print("Fel i test 2/58: merge([42, 43, 44, 45, 46, 47, 48, 49], [42])")
            print("Korrekt svar: [42, 42, 43, 44, 45, 46, 47, 48, 49]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 58: Exception')
        print_exception()

    print('Startar test 2/59')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48, 49], [42, 43])
        exp = [42, 42, 43, 43, 44, 45, 46, 47, 48, 49]
        if res != exp:
            print("Fel i test 2/59: merge([42, 43, 44, 45, 46, 47, 48, 49], [42, 43])")
            print("Korrekt svar: [42, 42, 43, 43, 44, 45, 46, 47, 48, 49]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 59: Exception')
        print_exception()

    print('Startar test 2/60')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48, 49, 50], [42])
        exp = [42, 42, 43, 44, 45, 46, 47, 48, 49, 50]
        if res != exp:
            print("Fel i test 2/60: merge([42, 43, 44, 45, 46, 47, 48, 49, 50], [42])")
            print("Korrekt svar: [42, 42, 43, 44, 45, 46, 47, 48, 49, 50]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 60: Exception')
        print_exception()

    print('Startar test 2/61')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48, 49, 50], [42, 43])
        exp = [42, 42, 43, 43, 44, 45, 46, 47, 48, 49, 50]
        if res != exp:
            print("Fel i test 2/61: merge([42, 43, 44, 45, 46, 47, 48, 49, 50], [42, 43])")
            print("Korrekt svar: [42, 42, 43, 43, 44, 45, 46, 47, 48, 49, 50]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 61: Exception')
        print_exception()

    print('Startar test 2/62')
    try:
        res = merge([42], [42])
        exp = [42, 42]
        if res != exp:
            print("Fel i test 2/62: merge([42], [42])")
            print("Korrekt svar: [42, 42]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 62: Exception')
        print_exception()

    print('Startar test 2/63')
    try:
        res = merge([42], [42, 43, 44, 45])
        exp = [42, 42, 43, 44, 45]
        if res != exp:
            print("Fel i test 2/63: merge([42], [42, 43, 44, 45])")
            print("Korrekt svar: [42, 42, 43, 44, 45]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 63: Exception')
        print_exception()

    print('Startar test 2/64')
    try:
        res = merge([42], [42, 43, 44, 45, 46, 47, 48])
        exp = [42, 42, 43, 44, 45, 46, 47, 48]
        if res != exp:
            print("Fel i test 2/64: merge([42], [42, 43, 44, 45, 46, 47, 48])")
            print("Korrekt svar: [42, 42, 43, 44, 45, 46, 47, 48]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 64: Exception')
        print_exception()

    print('Startar test 2/65')
    try:
        res = merge([42, 43], [42])
        exp = [42, 42, 43]
        if res != exp:
            print("Fel i test 2/65: merge([42, 43], [42])")
            print("Korrekt svar: [42, 42, 43]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 65: Exception')
        print_exception()

    print('Startar test 2/66')
    try:
        res = merge([42, 43], [42, 43, 44, 45])
        exp = [42, 42, 43, 43, 44, 45]
        if res != exp:
            print("Fel i test 2/66: merge([42, 43], [42, 43, 44, 45])")
            print("Korrekt svar: [42, 42, 43, 43, 44, 45]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 66: Exception')
        print_exception()

    print('Startar test 2/67')
    try:
        res = merge([42, 43], [42, 43, 44, 45, 46, 47, 48])
        exp = [42, 42, 43, 43, 44, 45, 46, 47, 48]
        if res != exp:
            print("Fel i test 2/67: merge([42, 43], [42, 43, 44, 45, 46, 47, 48])")
            print("Korrekt svar: [42, 42, 43, 43, 44, 45, 46, 47, 48]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 67: Exception')
        print_exception()

    print('Startar test 2/68')
    try:
        res = merge([42, 43, 44], [42])
        exp = [42, 42, 43, 44]
        if res != exp:
            print("Fel i test 2/68: merge([42, 43, 44], [42])")
            print("Korrekt svar: [42, 42, 43, 44]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 68: Exception')
        print_exception()

    print('Startar test 2/69')
    try:
        res = merge([42, 43, 44], [42, 43, 44, 45])
        exp = [42, 42, 43, 43, 44, 44, 45]
        if res != exp:
            print("Fel i test 2/69: merge([42, 43, 44], [42, 43, 44, 45])")
            print("Korrekt svar: [42, 42, 43, 43, 44, 44, 45]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 69: Exception')
        print_exception()

    print('Startar test 2/70')
    try:
        res = merge([42, 43, 44], [42, 43, 44, 45, 46, 47, 48])
        exp = [42, 42, 43, 43, 44, 44, 45, 46, 47, 48]
        if res != exp:
            print("Fel i test 2/70: merge([42, 43, 44], [42, 43, 44, 45, 46, 47, 48])")
            print("Korrekt svar: [42, 42, 43, 43, 44, 44, 45, 46, 47, 48]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 70: Exception')
        print_exception()

    print('Startar test 2/71')
    try:
        res = merge([42, 43, 44, 45], [42])
        exp = [42, 42, 43, 44, 45]
        if res != exp:
            print("Fel i test 2/71: merge([42, 43, 44, 45], [42])")
            print("Korrekt svar: [42, 42, 43, 44, 45]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 71: Exception')
        print_exception()

    print('Startar test 2/72')
    try:
        res = merge([42, 43, 44, 45], [42, 43, 44, 45])
        exp = [42, 42, 43, 43, 44, 44, 45, 45]
        if res != exp:
            print("Fel i test 2/72: merge([42, 43, 44, 45], [42, 43, 44, 45])")
            print("Korrekt svar: [42, 42, 43, 43, 44, 44, 45, 45]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 72: Exception')
        print_exception()

    print('Startar test 2/73')
    try:
        res = merge([42, 43, 44, 45], [42, 43, 44, 45, 46, 47, 48])
        exp = [42, 42, 43, 43, 44, 44, 45, 45, 46, 47, 48]
        if res != exp:
            print("Fel i test 2/73: merge([42, 43, 44, 45], [42, 43, 44, 45, 46, 47, 48])")
            print("Korrekt svar: [42, 42, 43, 43, 44, 44, 45, 45, 46, 47, 48]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 73: Exception')
        print_exception()

    print('Startar test 2/74')
    try:
        res = merge([42, 43, 44, 45, 46], [42])
        exp = [42, 42, 43, 44, 45, 46]
        if res != exp:
            print("Fel i test 2/74: merge([42, 43, 44, 45, 46], [42])")
            print("Korrekt svar: [42, 42, 43, 44, 45, 46]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 74: Exception')
        print_exception()

    print('Startar test 2/75')
    try:
        res = merge([42, 43, 44, 45, 46], [42, 43, 44, 45])
        exp = [42, 42, 43, 43, 44, 44, 45, 45, 46]
        if res != exp:
            print("Fel i test 2/75: merge([42, 43, 44, 45, 46], [42, 43, 44, 45])")
            print("Korrekt svar: [42, 42, 43, 43, 44, 44, 45, 45, 46]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 75: Exception')
        print_exception()

    print('Startar test 2/76')
    try:
        res = merge([42, 43, 44, 45, 46], [42, 43, 44, 45, 46, 47, 48])
        exp = [42, 42, 43, 43, 44, 44, 45, 45, 46, 46, 47, 48]
        if res != exp:
            print("Fel i test 2/76: merge([42, 43, 44, 45, 46], [42, 43, 44, 45, 46, 47, 48])")
            print("Korrekt svar: [42, 42, 43, 43, 44, 44, 45, 45, 46, 46, 47, 48]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 76: Exception')
        print_exception()

    print('Startar test 2/77')
    try:
        res = merge([42, 43, 44, 45, 46, 47], [42])
        exp = [42, 42, 43, 44, 45, 46, 47]
        if res != exp:
            print("Fel i test 2/77: merge([42, 43, 44, 45, 46, 47], [42])")
            print("Korrekt svar: [42, 42, 43, 44, 45, 46, 47]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 77: Exception')
        print_exception()

    print('Startar test 2/78')
    try:
        res = merge([42, 43, 44, 45, 46, 47], [42, 43, 44, 45])
        exp = [42, 42, 43, 43, 44, 44, 45, 45, 46, 47]
        if res != exp:
            print("Fel i test 2/78: merge([42, 43, 44, 45, 46, 47], [42, 43, 44, 45])")
            print("Korrekt svar: [42, 42, 43, 43, 44, 44, 45, 45, 46, 47]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 78: Exception')
        print_exception()

    print('Startar test 2/79')
    try:
        res = merge([42, 43, 44, 45, 46, 47], [42, 43, 44, 45, 46, 47, 48])
        exp = [42, 42, 43, 43, 44, 44, 45, 45, 46, 46, 47, 47, 48]
        if res != exp:
            print("Fel i test 2/79: merge([42, 43, 44, 45, 46, 47], [42, 43, 44, 45, 46, 47, 48])")
            print("Korrekt svar: [42, 42, 43, 43, 44, 44, 45, 45, 46, 46, 47, 47, 48]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 79: Exception')
        print_exception()

    print('Startar test 2/80')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48], [42])
        exp = [42, 42, 43, 44, 45, 46, 47, 48]
        if res != exp:
            print("Fel i test 2/80: merge([42, 43, 44, 45, 46, 47, 48], [42])")
            print("Korrekt svar: [42, 42, 43, 44, 45, 46, 47, 48]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 80: Exception')
        print_exception()

    print('Startar test 2/81')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48], [42, 43, 44, 45])
        exp = [42, 42, 43, 43, 44, 44, 45, 45, 46, 47, 48]
        if res != exp:
            print("Fel i test 2/81: merge([42, 43, 44, 45, 46, 47, 48], [42, 43, 44, 45])")
            print("Korrekt svar: [42, 42, 43, 43, 44, 44, 45, 45, 46, 47, 48]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 81: Exception')
        print_exception()

    print('Startar test 2/82')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48], [42, 43, 44, 45, 46, 47, 48])
        exp = [42, 42, 43, 43, 44, 44, 45, 45, 46, 46, 47, 47, 48, 48]
        if res != exp:
            print("Fel i test 2/82: merge([42, 43, 44, 45, 46, 47, 48], [42, 43, 44, 45, 46, 47, 48])")
            print("Korrekt svar: [42, 42, 43, 43, 44, 44, 45, 45, 46, 46, 47, 47, 48, 48]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 82: Exception')
        print_exception()

    print('Startar test 2/83')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48, 49], [42])
        exp = [42, 42, 43, 44, 45, 46, 47, 48, 49]
        if res != exp:
            print("Fel i test 2/83: merge([42, 43, 44, 45, 46, 47, 48, 49], [42])")
            print("Korrekt svar: [42, 42, 43, 44, 45, 46, 47, 48, 49]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 83: Exception')
        print_exception()

    print('Startar test 2/84')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48, 49], [42, 43, 44, 45])
        exp = [42, 42, 43, 43, 44, 44, 45, 45, 46, 47, 48, 49]
        if res != exp:
            print("Fel i test 2/84: merge([42, 43, 44, 45, 46, 47, 48, 49], [42, 43, 44, 45])")
            print("Korrekt svar: [42, 42, 43, 43, 44, 44, 45, 45, 46, 47, 48, 49]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 84: Exception')
        print_exception()

    print('Startar test 2/85')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48, 49], [42, 43, 44, 45, 46, 47, 48])
        exp = [42, 42, 43, 43, 44, 44, 45, 45, 46, 46, 47, 47, 48, 48, 49]
        if res != exp:
            print("Fel i test 2/85: merge([42, 43, 44, 45, 46, 47, 48, 49], [42, 43, 44, 45, 46, 47, 48])")
            print("Korrekt svar: [42, 42, 43, 43, 44, 44, 45, 45, 46, 46, 47, 47, 48, 48, 49]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 85: Exception')
        print_exception()

    print('Startar test 2/86')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48, 49, 50], [42])
        exp = [42, 42, 43, 44, 45, 46, 47, 48, 49, 50]
        if res != exp:
            print("Fel i test 2/86: merge([42, 43, 44, 45, 46, 47, 48, 49, 50], [42])")
            print("Korrekt svar: [42, 42, 43, 44, 45, 46, 47, 48, 49, 50]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 86: Exception')
        print_exception()

    print('Startar test 2/87')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48, 49, 50], [42, 43, 44, 45])
        exp = [42, 42, 43, 43, 44, 44, 45, 45, 46, 47, 48, 49, 50]
        if res != exp:
            print("Fel i test 2/87: merge([42, 43, 44, 45, 46, 47, 48, 49, 50], [42, 43, 44, 45])")
            print("Korrekt svar: [42, 42, 43, 43, 44, 44, 45, 45, 46, 47, 48, 49, 50]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 87: Exception')
        print_exception()

    print('Startar test 2/88')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48, 49, 50], [42, 43, 44, 45, 46, 47, 48])
        exp = [42, 42, 43, 43, 44, 44, 45, 45, 46, 46, 47, 47, 48, 48, 49, 50]
        if res != exp:
            print("Fel i test 2/88: merge([42, 43, 44, 45, 46, 47, 48, 49, 50], [42, 43, 44, 45, 46, 47, 48])")
            print("Korrekt svar: [42, 42, 43, 43, 44, 44, 45, 45, 46, 46, 47, 47, 48, 48, 49, 50]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 88: Exception')
        print_exception()

    print('Startar test 2/89')
    try:
        res = merge([42], [99])
        exp = [42, 99]
        if res != exp:
            print("Fel i test 2/89: merge([42], [99])")
            print("Korrekt svar: [42, 99]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 89: Exception')
        print_exception()

    print('Startar test 2/90')
    try:
        res = merge([42], [99, 100])
        exp = [42, 99, 100]
        if res != exp:
            print("Fel i test 2/90: merge([42], [99, 100])")
            print("Korrekt svar: [42, 99, 100]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 90: Exception')
        print_exception()

    print('Startar test 2/91')
    try:
        res = merge([42, 43], [99])
        exp = [42, 43, 99]
        if res != exp:
            print("Fel i test 2/91: merge([42, 43], [99])")
            print("Korrekt svar: [42, 43, 99]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 91: Exception')
        print_exception()

    print('Startar test 2/92')
    try:
        res = merge([42, 43], [99, 100])
        exp = [42, 43, 99, 100]
        if res != exp:
            print("Fel i test 2/92: merge([42, 43], [99, 100])")
            print("Korrekt svar: [42, 43, 99, 100]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 92: Exception')
        print_exception()

    print('Startar test 2/93')
    try:
        res = merge([42, 43, 44], [99])
        exp = [42, 43, 44, 99]
        if res != exp:
            print("Fel i test 2/93: merge([42, 43, 44], [99])")
            print("Korrekt svar: [42, 43, 44, 99]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 93: Exception')
        print_exception()

    print('Startar test 2/94')
    try:
        res = merge([42, 43, 44], [99, 100])
        exp = [42, 43, 44, 99, 100]
        if res != exp:
            print("Fel i test 2/94: merge([42, 43, 44], [99, 100])")
            print("Korrekt svar: [42, 43, 44, 99, 100]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 94: Exception')
        print_exception()

    print('Startar test 2/95')
    try:
        res = merge([42, 43, 44, 45], [99])
        exp = [42, 43, 44, 45, 99]
        if res != exp:
            print("Fel i test 2/95: merge([42, 43, 44, 45], [99])")
            print("Korrekt svar: [42, 43, 44, 45, 99]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 95: Exception')
        print_exception()

    print('Startar test 2/96')
    try:
        res = merge([42, 43, 44, 45], [99, 100])
        exp = [42, 43, 44, 45, 99, 100]
        if res != exp:
            print("Fel i test 2/96: merge([42, 43, 44, 45], [99, 100])")
            print("Korrekt svar: [42, 43, 44, 45, 99, 100]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 96: Exception')
        print_exception()

    print('Startar test 2/97')
    try:
        res = merge([42, 43, 44, 45, 46], [99])
        exp = [42, 43, 44, 45, 46, 99]
        if res != exp:
            print("Fel i test 2/97: merge([42, 43, 44, 45, 46], [99])")
            print("Korrekt svar: [42, 43, 44, 45, 46, 99]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 97: Exception')
        print_exception()

    print('Startar test 2/98')
    try:
        res = merge([42, 43, 44, 45, 46], [99, 100])
        exp = [42, 43, 44, 45, 46, 99, 100]
        if res != exp:
            print("Fel i test 2/98: merge([42, 43, 44, 45, 46], [99, 100])")
            print("Korrekt svar: [42, 43, 44, 45, 46, 99, 100]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 98: Exception')
        print_exception()

    print('Startar test 2/99')
    try:
        res = merge([42, 43, 44, 45, 46, 47], [99])
        exp = [42, 43, 44, 45, 46, 47, 99]
        if res != exp:
            print("Fel i test 2/99: merge([42, 43, 44, 45, 46, 47], [99])")
            print("Korrekt svar: [42, 43, 44, 45, 46, 47, 99]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 99: Exception')
        print_exception()

    print('Startar test 2/100')
    try:
        res = merge([42, 43, 44, 45, 46, 47], [99, 100])
        exp = [42, 43, 44, 45, 46, 47, 99, 100]
        if res != exp:
            print("Fel i test 2/100: merge([42, 43, 44, 45, 46, 47], [99, 100])")
            print("Korrekt svar: [42, 43, 44, 45, 46, 47, 99, 100]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 100: Exception')
        print_exception()

    print('Startar test 2/101')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48], [99])
        exp = [42, 43, 44, 45, 46, 47, 48, 99]
        if res != exp:
            print("Fel i test 2/101: merge([42, 43, 44, 45, 46, 47, 48], [99])")
            print("Korrekt svar: [42, 43, 44, 45, 46, 47, 48, 99]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 101: Exception')
        print_exception()

    print('Startar test 2/102')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48], [99, 100])
        exp = [42, 43, 44, 45, 46, 47, 48, 99, 100]
        if res != exp:
            print("Fel i test 2/102: merge([42, 43, 44, 45, 46, 47, 48], [99, 100])")
            print("Korrekt svar: [42, 43, 44, 45, 46, 47, 48, 99, 100]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 102: Exception')
        print_exception()

    print('Startar test 2/103')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48, 49], [99])
        exp = [42, 43, 44, 45, 46, 47, 48, 49, 99]
        if res != exp:
            print("Fel i test 2/103: merge([42, 43, 44, 45, 46, 47, 48, 49], [99])")
            print("Korrekt svar: [42, 43, 44, 45, 46, 47, 48, 49, 99]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 103: Exception')
        print_exception()

    print('Startar test 2/104')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48, 49], [99, 100])
        exp = [42, 43, 44, 45, 46, 47, 48, 49, 99, 100]
        if res != exp:
            print("Fel i test 2/104: merge([42, 43, 44, 45, 46, 47, 48, 49], [99, 100])")
            print("Korrekt svar: [42, 43, 44, 45, 46, 47, 48, 49, 99, 100]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 104: Exception')
        print_exception()

    print('Startar test 2/105')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48, 49, 50], [99])
        exp = [42, 43, 44, 45, 46, 47, 48, 49, 50, 99]
        if res != exp:
            print("Fel i test 2/105: merge([42, 43, 44, 45, 46, 47, 48, 49, 50], [99])")
            print("Korrekt svar: [42, 43, 44, 45, 46, 47, 48, 49, 50, 99]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 105: Exception')
        print_exception()

    print('Startar test 2/106')
    try:
        res = merge([42, 43, 44, 45, 46, 47, 48, 49, 50], [99, 100])
        exp = [42, 43, 44, 45, 46, 47, 48, 49, 50, 99, 100]
        if res != exp:
            print("Fel i test 2/106: merge([42, 43, 44, 45, 46, 47, 48, 49, 50], [99, 100])")
            print("Korrekt svar: [42, 43, 44, 45, 46, 47, 48, 49, 50, 99, 100]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 106: Exception')
        print_exception()

    print('Startar test 2/107')
    try:
        res = merge([[1, 2], [3, 4, 5], [4, 5], [4, 5], [4, 5]], [[2], [2, 3, 4], [2, 5], [7, 8, 9]])
        exp = [[1, 2], [2], [2, 3, 4], [2, 5], [3, 4, 5], [4, 5], [4, 5], [4, 5], [7, 8, 9]]
        if res != exp:
            print("Fel i test 2/107: merge([[1, 2], [3, 4, 5], [4, 5], [4, 5], [4, 5]], [[2], [2, 3, 4], [2, 5], [7, 8, 9]])")
            print("Korrekt svar: [[1, 2], [2], [2, 3, 4], [2, 5], [3, 4, 5], [4, 5], [4, 5], [4, 5], [7, 8, 9]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 107: Exception')
        print_exception()

    print('Startar test 2/108')
    try:
        res = merge([[1, 2, 3], [4, 5], [12, 42]], [[1], [7, 3], [15, 0, 7]])
        exp = [[1], [1, 2, 3], [4, 5], [7, 3], [12, 42], [15, 0, 7]]
        if res != exp:
            print("Fel i test 2/108: merge([[1, 2, 3], [4, 5], [12, 42]], [[1], [7, 3], [15, 0, 7]])")
            print("Korrekt svar: [[1], [1, 2, 3], [4, 5], [7, 3], [12, 42], [15, 0, 7]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 108: Exception')
        print_exception()

    print('Startar test 2/109')
    try:
        res = merge([1, 2, 3, 17, 17, 17], [4, 5, 6, 17, 17, 17])
        exp = [1, 2, 3, 4, 5, 6, 17, 17, 17, 17, 17, 17]
        if res != exp:
            print("Fel i test 2/109: merge([1, 2, 3, 17, 17, 17], [4, 5, 6, 17, 17, 17])")
            print("Korrekt svar: [1, 2, 3, 4, 5, 6, 17, 17, 17, 17, 17, 17]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 109: Exception')
        print_exception()

    print('Startar test 2/110')
    try:
        res = merge([1, 2, 3, 17, 17, 17], [4, 5, 6, 17, 17, 18])
        exp = [1, 2, 3, 4, 5, 6, 17, 17, 17, 17, 17, 18]
        if res != exp:
            print("Fel i test 2/110: merge([1, 2, 3, 17, 17, 17], [4, 5, 6, 17, 17, 18])")
            print("Korrekt svar: [1, 2, 3, 4, 5, 6, 17, 17, 17, 17, 17, 18]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 110: Exception')
        print_exception()


    print('Klar med tester fÃ¶r uppgift 2')
    print()


# noinspection PyBroadException
def test_3():
    print('PÃ¥bÃ¶rjar tester fÃ¶r uppgift 3')

    print('Startar test 3/1')
    try:
        res = without([[1], [[2]], [[[3]]], [[[[4]]]]], [1, 3])
        exp = [[], [[2]], [[[]]], [[[[4]]]]]
        if res != exp:
            print("Fel i test 3/1: without([[1], [[2]], [[[3]]], [[[[4]]]]], [1, 3])")
            print("Korrekt svar: [[], [[2]], [[[]]], [[[[4]]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 1: Exception')
        print_exception()

    print('Startar test 3/2')
    try:
        res = without([[[[[[[[[[10]]]]]]]]]], [10])
        exp = [[[[[[[[[[]]]]]]]]]]
        if res != exp:
            print("Fel i test 3/2: without([[[[[[[[[[10]]]]]]]]]], [10])")
            print("Korrekt svar: [[[[[[[[[[]]]]]]]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2: Exception')
        print_exception()

    print('Startar test 3/3')
    try:
        res = without([[[[[[[[[[10]]]]]]]]]], [5])
        exp = [[[[[[[[[[10]]]]]]]]]]
        if res != exp:
            print("Fel i test 3/3: without([[[[[[[[[[10]]]]]]]]]], [5])")
            print("Korrekt svar: [[[[[[[[[[10]]]]]]]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3: Exception')
        print_exception()

    print('Startar test 3/4')
    try:
        res = without([[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]], [1, None])
        exp = [[(1, 2)], [['b']], [[[]]], [[[[42.5]]]]]
        if res != exp:
            print("Fel i test 3/4: without([[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]], [1, None])")
            print("Korrekt svar: [[(1, 2)], [['b']], [[[]]], [[[[42.5]]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4: Exception')
        print_exception()

    print('Startar test 3/5')
    try:
        res = without([], [])
        exp = []
        if res != exp:
            print("Fel i test 3/5: without([], [])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5: Exception')
        print_exception()

    print('Startar test 3/6')
    try:
        res = without([[]], [])
        exp = [[]]
        if res != exp:
            print("Fel i test 3/6: without([[]], [])")
            print("Korrekt svar: [[]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 6: Exception')
        print_exception()

    print('Startar test 3/7')
    try:
        res = without([[[]]], [])
        exp = [[[]]]
        if res != exp:
            print("Fel i test 3/7: without([[[]]], [])")
            print("Korrekt svar: [[[]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 7: Exception')
        print_exception()

    print('Startar test 3/8')
    try:
        res = without([[], []], [])
        exp = [[], []]
        if res != exp:
            print("Fel i test 3/8: without([[], []], [])")
            print("Korrekt svar: [[], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 8: Exception')
        print_exception()

    print('Startar test 3/9')
    try:
        res = without([[[]], []], [])
        exp = [[[]], []]
        if res != exp:
            print("Fel i test 3/9: without([[[]], []], [])")
            print("Korrekt svar: [[[]], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 9: Exception')
        print_exception()

    print('Startar test 3/10')
    try:
        res = without([[], []], [])
        exp = [[], []]
        if res != exp:
            print("Fel i test 3/10: without([[], []], [])")
            print("Korrekt svar: [[], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 10: Exception')
        print_exception()

    print('Startar test 3/11')
    try:
        res = without([[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]], [])
        exp = [[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]]
        if res != exp:
            print("Fel i test 3/11: without([[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]], [])")
            print("Korrekt svar: [[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 11: Exception')
        print_exception()

    print('Startar test 3/12')
    try:
        res = without([[[3, 3, [], [], 3, []]], []], [])
        exp = [[[3, 3, [], [], 3, []]], []]
        if res != exp:
            print("Fel i test 3/12: without([[[3, 3, [], [], 3, []]], []], [])")
            print("Korrekt svar: [[[3, 3, [], [], 3, []]], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 12: Exception')
        print_exception()

    print('Startar test 3/13')
    try:
        res = without(['', [''], ''], [])
        exp = ['', [''], '']
        if res != exp:
            print("Fel i test 3/13: without(['', [''], ''], [])")
            print("Korrekt svar: ['', [''], '']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 13: Exception')
        print_exception()

    print('Startar test 3/14')
    try:
        res = without([2, 6, [7, 'att', []], 3], [])
        exp = [2, 6, [7, 'att', []], 3]
        if res != exp:
            print("Fel i test 3/14: without([2, 6, [7, 'att', []], 3], [])")
            print("Korrekt svar: [2, 6, [7, 'att', []], 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 14: Exception')
        print_exception()

    print('Startar test 3/15')
    try:
        res = without(['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta'], [])
        exp = ['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta']
        if res != exp:
            print("Fel i test 3/15: without(['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta'], [])")
            print("Korrekt svar: ['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 15: Exception')
        print_exception()

    print('Startar test 3/16')
    try:
        res = without([1, 2, 3], [])
        exp = [1, 2, 3]
        if res != exp:
            print("Fel i test 3/16: without([1, 2, 3], [])")
            print("Korrekt svar: [1, 2, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 16: Exception')
        print_exception()

    print('Startar test 3/17')
    try:
        res = without([-1, [2, 3], ['Hi', 4, [1]]], [])
        exp = [-1, [2, 3], ['Hi', 4, [1]]]
        if res != exp:
            print("Fel i test 3/17: without([-1, [2, 3], ['Hi', 4, [1]]], [])")
            print("Korrekt svar: [-1, [2, 3], ['Hi', 4, [1]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 17: Exception')
        print_exception()

    print('Startar test 3/18')
    try:
        res = without([-1, [2, 3], ('Hi', 4, 1)], [])
        exp = [-1, [2, 3], ('Hi', 4, 1)]
        if res != exp:
            print("Fel i test 3/18: without([-1, [2, 3], ('Hi', 4, 1)], [])")
            print("Korrekt svar: [-1, [2, 3], ('Hi', 4, 1)]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 18: Exception')
        print_exception()

    print('Startar test 3/19')
    try:
        res = without([], [1])
        exp = []
        if res != exp:
            print("Fel i test 3/19: without([], [1])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 19: Exception')
        print_exception()

    print('Startar test 3/20')
    try:
        res = without([[]], [1])
        exp = [[]]
        if res != exp:
            print("Fel i test 3/20: without([[]], [1])")
            print("Korrekt svar: [[]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 20: Exception')
        print_exception()

    print('Startar test 3/21')
    try:
        res = without([[[]]], [1])
        exp = [[[]]]
        if res != exp:
            print("Fel i test 3/21: without([[[]]], [1])")
            print("Korrekt svar: [[[]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 21: Exception')
        print_exception()

    print('Startar test 3/22')
    try:
        res = without([[], []], [1])
        exp = [[], []]
        if res != exp:
            print("Fel i test 3/22: without([[], []], [1])")
            print("Korrekt svar: [[], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 22: Exception')
        print_exception()

    print('Startar test 3/23')
    try:
        res = without([[[]], []], [1])
        exp = [[[]], []]
        if res != exp:
            print("Fel i test 3/23: without([[[]], []], [1])")
            print("Korrekt svar: [[[]], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 23: Exception')
        print_exception()

    print('Startar test 3/24')
    try:
        res = without([[], []], [1])
        exp = [[], []]
        if res != exp:
            print("Fel i test 3/24: without([[], []], [1])")
            print("Korrekt svar: [[], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 24: Exception')
        print_exception()

    print('Startar test 3/25')
    try:
        res = without([[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]], [1])
        exp = [[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]]
        if res != exp:
            print("Fel i test 3/25: without([[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]], [1])")
            print("Korrekt svar: [[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 25: Exception')
        print_exception()

    print('Startar test 3/26')
    try:
        res = without([[[3, 3, [], [], 3, []]], []], [1])
        exp = [[[3, 3, [], [], 3, []]], []]
        if res != exp:
            print("Fel i test 3/26: without([[[3, 3, [], [], 3, []]], []], [1])")
            print("Korrekt svar: [[[3, 3, [], [], 3, []]], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 26: Exception')
        print_exception()

    print('Startar test 3/27')
    try:
        res = without(['', [''], ''], [1])
        exp = ['', [''], '']
        if res != exp:
            print("Fel i test 3/27: without(['', [''], ''], [1])")
            print("Korrekt svar: ['', [''], '']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 27: Exception')
        print_exception()

    print('Startar test 3/28')
    try:
        res = without([2, 6, [7, 'att', []], 3], [1])
        exp = [2, 6, [7, 'att', []], 3]
        if res != exp:
            print("Fel i test 3/28: without([2, 6, [7, 'att', []], 3], [1])")
            print("Korrekt svar: [2, 6, [7, 'att', []], 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 28: Exception')
        print_exception()

    print('Startar test 3/29')
    try:
        res = without(['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta'], [1])
        exp = ['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta']
        if res != exp:
            print("Fel i test 3/29: without(['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta'], [1])")
            print("Korrekt svar: ['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 29: Exception')
        print_exception()

    print('Startar test 3/30')
    try:
        res = without([1, 2, 3], [1])
        exp = [2, 3]
        if res != exp:
            print("Fel i test 3/30: without([1, 2, 3], [1])")
            print("Korrekt svar: [2, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 30: Exception')
        print_exception()

    print('Startar test 3/31')
    try:
        res = without([-1, [2, 3], ['Hi', 4, [1]]], [1])
        exp = [-1, [2, 3], ['Hi', 4, []]]
        if res != exp:
            print("Fel i test 3/31: without([-1, [2, 3], ['Hi', 4, [1]]], [1])")
            print("Korrekt svar: [-1, [2, 3], ['Hi', 4, []]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 31: Exception')
        print_exception()

    print('Startar test 3/32')
    try:
        res = without([-1, [2, 3], ('Hi', 4, 1)], [1])
        exp = [-1, [2, 3], ('Hi', 4, 1)]
        if res != exp:
            print("Fel i test 3/32: without([-1, [2, 3], ('Hi', 4, 1)], [1])")
            print("Korrekt svar: [-1, [2, 3], ('Hi', 4, 1)]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 32: Exception')
        print_exception()

    print('Startar test 3/33')
    try:
        res = without([], [1, 2])
        exp = []
        if res != exp:
            print("Fel i test 3/33: without([], [1, 2])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 33: Exception')
        print_exception()

    print('Startar test 3/34')
    try:
        res = without([[]], [1, 2])
        exp = [[]]
        if res != exp:
            print("Fel i test 3/34: without([[]], [1, 2])")
            print("Korrekt svar: [[]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 34: Exception')
        print_exception()

    print('Startar test 3/35')
    try:
        res = without([[[]]], [1, 2])
        exp = [[[]]]
        if res != exp:
            print("Fel i test 3/35: without([[[]]], [1, 2])")
            print("Korrekt svar: [[[]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 35: Exception')
        print_exception()

    print('Startar test 3/36')
    try:
        res = without([[], []], [1, 2])
        exp = [[], []]
        if res != exp:
            print("Fel i test 3/36: without([[], []], [1, 2])")
            print("Korrekt svar: [[], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 36: Exception')
        print_exception()

    print('Startar test 3/37')
    try:
        res = without([[[]], []], [1, 2])
        exp = [[[]], []]
        if res != exp:
            print("Fel i test 3/37: without([[[]], []], [1, 2])")
            print("Korrekt svar: [[[]], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 37: Exception')
        print_exception()

    print('Startar test 3/38')
    try:
        res = without([[], []], [1, 2])
        exp = [[], []]
        if res != exp:
            print("Fel i test 3/38: without([[], []], [1, 2])")
            print("Korrekt svar: [[], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 38: Exception')
        print_exception()

    print('Startar test 3/39')
    try:
        res = without([[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]], [1, 2])
        exp = [[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]]
        if res != exp:
            print("Fel i test 3/39: without([[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]], [1, 2])")
            print("Korrekt svar: [[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 39: Exception')
        print_exception()

    print('Startar test 3/40')
    try:
        res = without([[[3, 3, [], [], 3, []]], []], [1, 2])
        exp = [[[3, 3, [], [], 3, []]], []]
        if res != exp:
            print("Fel i test 3/40: without([[[3, 3, [], [], 3, []]], []], [1, 2])")
            print("Korrekt svar: [[[3, 3, [], [], 3, []]], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 40: Exception')
        print_exception()

    print('Startar test 3/41')
    try:
        res = without(['', [''], ''], [1, 2])
        exp = ['', [''], '']
        if res != exp:
            print("Fel i test 3/41: without(['', [''], ''], [1, 2])")
            print("Korrekt svar: ['', [''], '']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 41: Exception')
        print_exception()

    print('Startar test 3/42')
    try:
        res = without([2, 6, [7, 'att', []], 3], [1, 2])
        exp = [6, [7, 'att', []], 3]
        if res != exp:
            print("Fel i test 3/42: without([2, 6, [7, 'att', []], 3], [1, 2])")
            print("Korrekt svar: [6, [7, 'att', []], 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 42: Exception')
        print_exception()

    print('Startar test 3/43')
    try:
        res = without(['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta'], [1, 2])
        exp = ['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta']
        if res != exp:
            print("Fel i test 3/43: without(['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta'], [1, 2])")
            print("Korrekt svar: ['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 43: Exception')
        print_exception()

    print('Startar test 3/44')
    try:
        res = without([1, 2, 3], [1, 2])
        exp = [3]
        if res != exp:
            print("Fel i test 3/44: without([1, 2, 3], [1, 2])")
            print("Korrekt svar: [3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 44: Exception')
        print_exception()

    print('Startar test 3/45')
    try:
        res = without([-1, [2, 3], ['Hi', 4, [1]]], [1, 2])
        exp = [-1, [3], ['Hi', 4, []]]
        if res != exp:
            print("Fel i test 3/45: without([-1, [2, 3], ['Hi', 4, [1]]], [1, 2])")
            print("Korrekt svar: [-1, [3], ['Hi', 4, []]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 45: Exception')
        print_exception()

    print('Startar test 3/46')
    try:
        res = without([-1, [2, 3], ('Hi', 4, 1)], [1, 2])
        exp = [-1, [3], ('Hi', 4, 1)]
        if res != exp:
            print("Fel i test 3/46: without([-1, [2, 3], ('Hi', 4, 1)], [1, 2])")
            print("Korrekt svar: [-1, [3], ('Hi', 4, 1)]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 46: Exception')
        print_exception()

    print('Startar test 3/47')
    try:
        res = without([], ['a', 42])
        exp = []
        if res != exp:
            print("Fel i test 3/47: without([], ['a', 42])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 47: Exception')
        print_exception()

    print('Startar test 3/48')
    try:
        res = without([[]], ['a', 42])
        exp = [[]]
        if res != exp:
            print("Fel i test 3/48: without([[]], ['a', 42])")
            print("Korrekt svar: [[]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 48: Exception')
        print_exception()

    print('Startar test 3/49')
    try:
        res = without([[[]]], ['a', 42])
        exp = [[[]]]
        if res != exp:
            print("Fel i test 3/49: without([[[]]], ['a', 42])")
            print("Korrekt svar: [[[]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 49: Exception')
        print_exception()

    print('Startar test 3/50')
    try:
        res = without([[], []], ['a', 42])
        exp = [[], []]
        if res != exp:
            print("Fel i test 3/50: without([[], []], ['a', 42])")
            print("Korrekt svar: [[], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 50: Exception')
        print_exception()

    print('Startar test 3/51')
    try:
        res = without([[[]], []], ['a', 42])
        exp = [[[]], []]
        if res != exp:
            print("Fel i test 3/51: without([[[]], []], ['a', 42])")
            print("Korrekt svar: [[[]], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 51: Exception')
        print_exception()

    print('Startar test 3/52')
    try:
        res = without([[], []], ['a', 42])
        exp = [[], []]
        if res != exp:
            print("Fel i test 3/52: without([[], []], ['a', 42])")
            print("Korrekt svar: [[], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 52: Exception')
        print_exception()

    print('Startar test 3/53')
    try:
        res = without([[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]], ['a', 42])
        exp = [[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]]
        if res != exp:
            print("Fel i test 3/53: without([[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]], ['a', 42])")
            print("Korrekt svar: [[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 53: Exception')
        print_exception()

    print('Startar test 3/54')
    try:
        res = without([[[3, 3, [], [], 3, []]], []], ['a', 42])
        exp = [[[3, 3, [], [], 3, []]], []]
        if res != exp:
            print("Fel i test 3/54: without([[[3, 3, [], [], 3, []]], []], ['a', 42])")
            print("Korrekt svar: [[[3, 3, [], [], 3, []]], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 54: Exception')
        print_exception()

    print('Startar test 3/55')
    try:
        res = without(['', [''], ''], ['a', 42])
        exp = ['', [''], '']
        if res != exp:
            print("Fel i test 3/55: without(['', [''], ''], ['a', 42])")
            print("Korrekt svar: ['', [''], '']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 55: Exception')
        print_exception()

    print('Startar test 3/56')
    try:
        res = without([2, 6, [7, 'att', []], 3], ['a', 42])
        exp = [2, 6, [7, 'att', []], 3]
        if res != exp:
            print("Fel i test 3/56: without([2, 6, [7, 'att', []], 3], ['a', 42])")
            print("Korrekt svar: [2, 6, [7, 'att', []], 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 56: Exception')
        print_exception()

    print('Startar test 3/57')
    try:
        res = without(['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta'], ['a', 42])
        exp = ['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta']
        if res != exp:
            print("Fel i test 3/57: without(['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta'], ['a', 42])")
            print("Korrekt svar: ['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 57: Exception')
        print_exception()

    print('Startar test 3/58')
    try:
        res = without([1, 2, 3], ['a', 42])
        exp = [1, 2, 3]
        if res != exp:
            print("Fel i test 3/58: without([1, 2, 3], ['a', 42])")
            print("Korrekt svar: [1, 2, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 58: Exception')
        print_exception()

    print('Startar test 3/59')
    try:
        res = without([-1, [2, 3], ['Hi', 4, [1]]], ['a', 42])
        exp = [-1, [2, 3], ['Hi', 4, [1]]]
        if res != exp:
            print("Fel i test 3/59: without([-1, [2, 3], ['Hi', 4, [1]]], ['a', 42])")
            print("Korrekt svar: [-1, [2, 3], ['Hi', 4, [1]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 59: Exception')
        print_exception()

    print('Startar test 3/60')
    try:
        res = without([-1, [2, 3], ('Hi', 4, 1)], ['a', 42])
        exp = [-1, [2, 3], ('Hi', 4, 1)]
        if res != exp:
            print("Fel i test 3/60: without([-1, [2, 3], ('Hi', 4, 1)], ['a', 42])")
            print("Korrekt svar: [-1, [2, 3], ('Hi', 4, 1)]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 60: Exception')
        print_exception()

    print('Startar test 3/61')
    try:
        res = without([], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
        exp = []
        if res != exp:
            print("Fel i test 3/61: without([], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 61: Exception')
        print_exception()

    print('Startar test 3/62')
    try:
        res = without([[]], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
        exp = [[]]
        if res != exp:
            print("Fel i test 3/62: without([[]], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])")
            print("Korrekt svar: [[]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 62: Exception')
        print_exception()

    print('Startar test 3/63')
    try:
        res = without([[[]]], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
        exp = [[[]]]
        if res != exp:
            print("Fel i test 3/63: without([[[]]], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])")
            print("Korrekt svar: [[[]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 63: Exception')
        print_exception()

    print('Startar test 3/64')
    try:
        res = without([[], []], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
        exp = [[], []]
        if res != exp:
            print("Fel i test 3/64: without([[], []], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])")
            print("Korrekt svar: [[], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 64: Exception')
        print_exception()

    print('Startar test 3/65')
    try:
        res = without([[[]], []], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
        exp = [[[]], []]
        if res != exp:
            print("Fel i test 3/65: without([[[]], []], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])")
            print("Korrekt svar: [[[]], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 65: Exception')
        print_exception()

    print('Startar test 3/66')
    try:
        res = without([[], []], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
        exp = [[], []]
        if res != exp:
            print("Fel i test 3/66: without([[], []], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])")
            print("Korrekt svar: [[], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 66: Exception')
        print_exception()

    print('Startar test 3/67')
    try:
        res = without([[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
        exp = [[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]]
        if res != exp:
            print("Fel i test 3/67: without([[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])")
            print("Korrekt svar: [[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 67: Exception')
        print_exception()

    print('Startar test 3/68')
    try:
        res = without([[[3, 3, [], [], 3, []]], []], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
        exp = [[[[], [], []]], []]
        if res != exp:
            print("Fel i test 3/68: without([[[3, 3, [], [], 3, []]], []], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])")
            print("Korrekt svar: [[[[], [], []]], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 68: Exception')
        print_exception()

    print('Startar test 3/69')
    try:
        res = without(['', [''], ''], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
        exp = ['', [''], '']
        if res != exp:
            print("Fel i test 3/69: without(['', [''], ''], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])")
            print("Korrekt svar: ['', [''], '']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 69: Exception')
        print_exception()

    print('Startar test 3/70')
    try:
        res = without([2, 6, [7, 'att', []], 3], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
        exp = [['att', []]]
        if res != exp:
            print("Fel i test 3/70: without([2, 6, [7, 'att', []], 3], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])")
            print("Korrekt svar: [['att', []]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 70: Exception')
        print_exception()

    print('Startar test 3/71')
    try:
        res = without(['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta'], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
        exp = ['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta']
        if res != exp:
            print("Fel i test 3/71: without(['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta'], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])")
            print("Korrekt svar: ['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 71: Exception')
        print_exception()

    print('Startar test 3/72')
    try:
        res = without([1, 2, 3], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
        exp = []
        if res != exp:
            print("Fel i test 3/72: without([1, 2, 3], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 72: Exception')
        print_exception()

    print('Startar test 3/73')
    try:
        res = without([-1, [2, 3], ['Hi', 4, [1]]], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
        exp = [-1, [], ['Hi', []]]
        if res != exp:
            print("Fel i test 3/73: without([-1, [2, 3], ['Hi', 4, [1]]], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])")
            print("Korrekt svar: [-1, [], ['Hi', []]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 73: Exception')
        print_exception()

    print('Startar test 3/74')
    try:
        res = without([-1, [2, 3], ('Hi', 4, 1)], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
        exp = [-1, [], ('Hi', 4, 1)]
        if res != exp:
            print("Fel i test 3/74: without([-1, [2, 3], ('Hi', 4, 1)], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])")
            print("Korrekt svar: [-1, [], ('Hi', 4, 1)]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 74: Exception')
        print_exception()

    print('Startar test 3/75')
    try:
        res = without([], [(1, 2), None])
        exp = []
        if res != exp:
            print("Fel i test 3/75: without([], [(1, 2), None])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 75: Exception')
        print_exception()

    print('Startar test 3/76')
    try:
        res = without([[]], [(1, 2), None])
        exp = [[]]
        if res != exp:
            print("Fel i test 3/76: without([[]], [(1, 2), None])")
            print("Korrekt svar: [[]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 76: Exception')
        print_exception()

    print('Startar test 3/77')
    try:
        res = without([[[]]], [(1, 2), None])
        exp = [[[]]]
        if res != exp:
            print("Fel i test 3/77: without([[[]]], [(1, 2), None])")
            print("Korrekt svar: [[[]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 77: Exception')
        print_exception()

    print('Startar test 3/78')
    try:
        res = without([[], []], [(1, 2), None])
        exp = [[], []]
        if res != exp:
            print("Fel i test 3/78: without([[], []], [(1, 2), None])")
            print("Korrekt svar: [[], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 78: Exception')
        print_exception()

    print('Startar test 3/79')
    try:
        res = without([[[]], []], [(1, 2), None])
        exp = [[[]], []]
        if res != exp:
            print("Fel i test 3/79: without([[[]], []], [(1, 2), None])")
            print("Korrekt svar: [[[]], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 79: Exception')
        print_exception()

    print('Startar test 3/80')
    try:
        res = without([[], []], [(1, 2), None])
        exp = [[], []]
        if res != exp:
            print("Fel i test 3/80: without([[], []], [(1, 2), None])")
            print("Korrekt svar: [[], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 80: Exception')
        print_exception()

    print('Startar test 3/81')
    try:
        res = without([[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]], [(1, 2), None])
        exp = [[], [['b']], [[[]]], [[[[42.5]]]]]
        if res != exp:
            print("Fel i test 3/81: without([[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]], [(1, 2), None])")
            print("Korrekt svar: [[], [['b']], [[[]]], [[[[42.5]]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 81: Exception')
        print_exception()

    print('Startar test 3/82')
    try:
        res = without([[[3, 3, [], [], 3, []]], []], [(1, 2), None])
        exp = [[[3, 3, [], [], 3, []]], []]
        if res != exp:
            print("Fel i test 3/82: without([[[3, 3, [], [], 3, []]], []], [(1, 2), None])")
            print("Korrekt svar: [[[3, 3, [], [], 3, []]], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 82: Exception')
        print_exception()

    print('Startar test 3/83')
    try:
        res = without(['', [''], ''], [(1, 2), None])
        exp = ['', [''], '']
        if res != exp:
            print("Fel i test 3/83: without(['', [''], ''], [(1, 2), None])")
            print("Korrekt svar: ['', [''], '']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 83: Exception')
        print_exception()

    print('Startar test 3/84')
    try:
        res = without([2, 6, [7, 'att', []], 3], [(1, 2), None])
        exp = [2, 6, [7, 'att', []], 3]
        if res != exp:
            print("Fel i test 3/84: without([2, 6, [7, 'att', []], 3], [(1, 2), None])")
            print("Korrekt svar: [2, 6, [7, 'att', []], 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 84: Exception')
        print_exception()

    print('Startar test 3/85')
    try:
        res = without(['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta'], [(1, 2), None])
        exp = ['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta']
        if res != exp:
            print("Fel i test 3/85: without(['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta'], [(1, 2), None])")
            print("Korrekt svar: ['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 85: Exception')
        print_exception()

    print('Startar test 3/86')
    try:
        res = without([1, 2, 3], [(1, 2), None])
        exp = [1, 2, 3]
        if res != exp:
            print("Fel i test 3/86: without([1, 2, 3], [(1, 2), None])")
            print("Korrekt svar: [1, 2, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 86: Exception')
        print_exception()

    print('Startar test 3/87')
    try:
        res = without([-1, [2, 3], ['Hi', 4, [1]]], [(1, 2), None])
        exp = [-1, [2, 3], ['Hi', 4, [1]]]
        if res != exp:
            print("Fel i test 3/87: without([-1, [2, 3], ['Hi', 4, [1]]], [(1, 2), None])")
            print("Korrekt svar: [-1, [2, 3], ['Hi', 4, [1]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 87: Exception')
        print_exception()

    print('Startar test 3/88')
    try:
        res = without([-1, [2, 3], ('Hi', 4, 1)], [(1, 2), None])
        exp = [-1, [2, 3], ('Hi', 4, 1)]
        if res != exp:
            print("Fel i test 3/88: without([-1, [2, 3], ('Hi', 4, 1)], [(1, 2), None])")
            print("Korrekt svar: [-1, [2, 3], ('Hi', 4, 1)]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 88: Exception')
        print_exception()

    print('Startar test 3/89')
    try:
        res = without([], [0])
        exp = []
        if res != exp:
            print("Fel i test 3/89: without([], [0])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 89: Exception')
        print_exception()

    print('Startar test 3/90')
    try:
        res = without([[]], [0])
        exp = [[]]
        if res != exp:
            print("Fel i test 3/90: without([[]], [0])")
            print("Korrekt svar: [[]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 90: Exception')
        print_exception()

    print('Startar test 3/91')
    try:
        res = without([[[]]], [0])
        exp = [[[]]]
        if res != exp:
            print("Fel i test 3/91: without([[[]]], [0])")
            print("Korrekt svar: [[[]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 91: Exception')
        print_exception()

    print('Startar test 3/92')
    try:
        res = without([[], []], [0])
        exp = [[], []]
        if res != exp:
            print("Fel i test 3/92: without([[], []], [0])")
            print("Korrekt svar: [[], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 92: Exception')
        print_exception()

    print('Startar test 3/93')
    try:
        res = without([[[]], []], [0])
        exp = [[[]], []]
        if res != exp:
            print("Fel i test 3/93: without([[[]], []], [0])")
            print("Korrekt svar: [[[]], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 93: Exception')
        print_exception()

    print('Startar test 3/94')
    try:
        res = without([[], []], [0])
        exp = [[], []]
        if res != exp:
            print("Fel i test 3/94: without([[], []], [0])")
            print("Korrekt svar: [[], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 94: Exception')
        print_exception()

    print('Startar test 3/95')
    try:
        res = without([[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]], [0])
        exp = [[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]]
        if res != exp:
            print("Fel i test 3/95: without([[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]], [0])")
            print("Korrekt svar: [[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 95: Exception')
        print_exception()

    print('Startar test 3/96')
    try:
        res = without([[[3, 3, [], [], 3, []]], []], [0])
        exp = [[[3, 3, [], [], 3, []]], []]
        if res != exp:
            print("Fel i test 3/96: without([[[3, 3, [], [], 3, []]], []], [0])")
            print("Korrekt svar: [[[3, 3, [], [], 3, []]], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 96: Exception')
        print_exception()

    print('Startar test 3/97')
    try:
        res = without(['', [''], ''], [0])
        exp = ['', [''], '']
        if res != exp:
            print("Fel i test 3/97: without(['', [''], ''], [0])")
            print("Korrekt svar: ['', [''], '']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 97: Exception')
        print_exception()

    print('Startar test 3/98')
    try:
        res = without([2, 6, [7, 'att', []], 3], [0])
        exp = [2, 6, [7, 'att', []], 3]
        if res != exp:
            print("Fel i test 3/98: without([2, 6, [7, 'att', []], 3], [0])")
            print("Korrekt svar: [2, 6, [7, 'att', []], 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 98: Exception')
        print_exception()

    print('Startar test 3/99')
    try:
        res = without(['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta'], [0])
        exp = ['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta']
        if res != exp:
            print("Fel i test 3/99: without(['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta'], [0])")
            print("Korrekt svar: ['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 99: Exception')
        print_exception()

    print('Startar test 3/100')
    try:
        res = without([1, 2, 3], [0])
        exp = [1, 2, 3]
        if res != exp:
            print("Fel i test 3/100: without([1, 2, 3], [0])")
            print("Korrekt svar: [1, 2, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 100: Exception')
        print_exception()

    print('Startar test 3/101')
    try:
        res = without([-1, [2, 3], ['Hi', 4, [1]]], [0])
        exp = [-1, [2, 3], ['Hi', 4, [1]]]
        if res != exp:
            print("Fel i test 3/101: without([-1, [2, 3], ['Hi', 4, [1]]], [0])")
            print("Korrekt svar: [-1, [2, 3], ['Hi', 4, [1]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 101: Exception')
        print_exception()

    print('Startar test 3/102')
    try:
        res = without([-1, [2, 3], ('Hi', 4, 1)], [0])
        exp = [-1, [2, 3], ('Hi', 4, 1)]
        if res != exp:
            print("Fel i test 3/102: without([-1, [2, 3], ('Hi', 4, 1)], [0])")
            print("Korrekt svar: [-1, [2, 3], ('Hi', 4, 1)]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 102: Exception')
        print_exception()

    print('Startar test 3/103')
    try:
        res = without([], ['lycka'])
        exp = []
        if res != exp:
            print("Fel i test 3/103: without([], ['lycka'])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 103: Exception')
        print_exception()

    print('Startar test 3/104')
    try:
        res = without([[]], ['lycka'])
        exp = [[]]
        if res != exp:
            print("Fel i test 3/104: without([[]], ['lycka'])")
            print("Korrekt svar: [[]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 104: Exception')
        print_exception()

    print('Startar test 3/105')
    try:
        res = without([[[]]], ['lycka'])
        exp = [[[]]]
        if res != exp:
            print("Fel i test 3/105: without([[[]]], ['lycka'])")
            print("Korrekt svar: [[[]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 105: Exception')
        print_exception()

    print('Startar test 3/106')
    try:
        res = without([[], []], ['lycka'])
        exp = [[], []]
        if res != exp:
            print("Fel i test 3/106: without([[], []], ['lycka'])")
            print("Korrekt svar: [[], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 106: Exception')
        print_exception()

    print('Startar test 3/107')
    try:
        res = without([[[]], []], ['lycka'])
        exp = [[[]], []]
        if res != exp:
            print("Fel i test 3/107: without([[[]], []], ['lycka'])")
            print("Korrekt svar: [[[]], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 107: Exception')
        print_exception()

    print('Startar test 3/108')
    try:
        res = without([[], []], ['lycka'])
        exp = [[], []]
        if res != exp:
            print("Fel i test 3/108: without([[], []], ['lycka'])")
            print("Korrekt svar: [[], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 108: Exception')
        print_exception()

    print('Startar test 3/109')
    try:
        res = without([[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]], ['lycka'])
        exp = [[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]]
        if res != exp:
            print("Fel i test 3/109: without([[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]], ['lycka'])")
            print("Korrekt svar: [[(1, 2)], [['b']], [[[None]]], [[[[42.5]]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 109: Exception')
        print_exception()

    print('Startar test 3/110')
    try:
        res = without([[[3, 3, [], [], 3, []]], []], ['lycka'])
        exp = [[[3, 3, [], [], 3, []]], []]
        if res != exp:
            print("Fel i test 3/110: without([[[3, 3, [], [], 3, []]], []], ['lycka'])")
            print("Korrekt svar: [[[3, 3, [], [], 3, []]], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 110: Exception')
        print_exception()

    print('Startar test 3/111')
    try:
        res = without(['', [''], ''], ['lycka'])
        exp = ['', [''], '']
        if res != exp:
            print("Fel i test 3/111: without(['', [''], ''], ['lycka'])")
            print("Korrekt svar: ['', [''], '']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 111: Exception')
        print_exception()

    print('Startar test 3/112')
    try:
        res = without([2, 6, [7, 'att', []], 3], ['lycka'])
        exp = [2, 6, [7, 'att', []], 3]
        if res != exp:
            print("Fel i test 3/112: without([2, 6, [7, 'att', []], 3], ['lycka'])")
            print("Korrekt svar: [2, 6, [7, 'att', []], 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 112: Exception')
        print_exception()

    print('Startar test 3/113')
    try:
        res = without(['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta'], ['lycka'])
        exp = [' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta']
        if res != exp:
            print("Fel i test 3/113: without(['lycka', ' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta'], ['lycka'])")
            print("Korrekt svar: [' ', 'Ã¤r', ['kanske', ' ', 'att', []], 'tenta']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 113: Exception')
        print_exception()

    print('Startar test 3/114')
    try:
        res = without([1, 2, 3], ['lycka'])
        exp = [1, 2, 3]
        if res != exp:
            print("Fel i test 3/114: without([1, 2, 3], ['lycka'])")
            print("Korrekt svar: [1, 2, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 114: Exception')
        print_exception()

    print('Startar test 3/115')
    try:
        res = without([-1, [2, 3], ['Hi', 4, [1]]], ['lycka'])
        exp = [-1, [2, 3], ['Hi', 4, [1]]]
        if res != exp:
            print("Fel i test 3/115: without([-1, [2, 3], ['Hi', 4, [1]]], ['lycka'])")
            print("Korrekt svar: [-1, [2, 3], ['Hi', 4, [1]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 115: Exception')
        print_exception()

    print('Startar test 3/116')
    try:
        res = without([-1, [2, 3], ('Hi', 4, 1)], ['lycka'])
        exp = [-1, [2, 3], ('Hi', 4, 1)]
        if res != exp:
            print("Fel i test 3/116: without([-1, [2, 3], ('Hi', 4, 1)], ['lycka'])")
            print("Korrekt svar: [-1, [2, 3], ('Hi', 4, 1)]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 116: Exception')
        print_exception()

    print('Startar test 3/117')
    try:
        res = without([1], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = []
        if res != exp:
            print("Fel i test 3/117: without([1], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 117: Exception')
        print_exception()

    print('Startar test 3/118')
    try:
        res = without(['a'], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = ['a']
        if res != exp:
            print("Fel i test 3/118: without(['a'], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: ['a']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 118: Exception')
        print_exception()

    print('Startar test 3/119')
    try:
        res = without([0.1], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [0.1]
        if res != exp:
            print("Fel i test 3/119: without([0.1], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [0.1]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 119: Exception')
        print_exception()

    print('Startar test 3/120')
    try:
        res = without([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
        if res != exp:
            print("Fel i test 3/120: without([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 120: Exception')
        print_exception()

    print('Startar test 3/121')
    try:
        res = without([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 3, 4, 6, 7, 8, 9]
        if res != exp:
            print("Fel i test 3/121: without([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 3, 4, 6, 7, 8, 9]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 121: Exception')
        print_exception()

    print('Startar test 3/122')
    try:
        res = without([5, 467, 123, 4567, 878, 345, 89, 90, 78], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [467, 123, 4567, 878, 345, 89, 90, 78]
        if res != exp:
            print("Fel i test 3/122: without([5, 467, 123, 4567, 878, 345, 89, 90, 78], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [467, 123, 4567, 878, 345, 89, 90, 78]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 122: Exception')
        print_exception()

    print('Startar test 3/123')
    try:
        res = without([0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [0]
        if res != exp:
            print("Fel i test 3/123: without([0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 123: Exception')
        print_exception()

    print('Startar test 3/124')
    try:
        res = without([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [0, 3, 4, 6, 7, 8, 9]
        if res != exp:
            print("Fel i test 3/124: without([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [0, 3, 4, 6, 7, 8, 9]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 124: Exception')
        print_exception()

    print('Startar test 3/125')
    try:
        res = without([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
        if res != exp:
            print("Fel i test 3/125: without([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 125: Exception')
        print_exception()

    print('Startar test 3/126')
    try:
        res = without([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [10, 9, 8, 7, 6, 4, 3, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
        if res != exp:
            print("Fel i test 3/126: without([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [10, 9, 8, 7, 6, 4, 3, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 126: Exception')
        print_exception()

    print('Startar test 3/127')
    try:
        res = without(['1', '2', '3', '4', '5'], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = ['1', '2', '4', '5']
        if res != exp:
            print("Fel i test 3/127: without(['1', '2', '3', '4', '5'], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: ['1', '2', '4', '5']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 127: Exception')
        print_exception()

    print('Startar test 3/128')
    try:
        res = without(['Ã¥', 'Ã¤', 'Ã¶', 'Ã¢', 'Ã´', 'Ãª', 'Ã¡', 'Ã³', 'Ã©'], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = ['Ã¥', 'Ã¤', 'Ã¢', 'Ã´', 'Ãª', 'Ã¡', 'Ã³', 'Ã©']
        if res != exp:
            print("Fel i test 3/128: without(['Ã¥', 'Ã¤', 'Ã¶', 'Ã¢', 'Ã´', 'Ãª', 'Ã¡', 'Ã³', 'Ã©'], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: ['Ã¥', 'Ã¤', 'Ã¢', 'Ã´', 'Ãª', 'Ã¡', 'Ã³', 'Ã©']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 128: Exception')
        print_exception()

    print('Startar test 3/129')
    try:
        res = without(['', '', '', ''], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = ['', '', '', '']
        if res != exp:
            print("Fel i test 3/129: without(['', '', '', ''], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: ['', '', '', '']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 129: Exception')
        print_exception()

    print('Startar test 3/130')
    try:
        res = without([' ', '', ' ', ''], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [' ', '', ' ', '']
        if res != exp:
            print("Fel i test 3/130: without([' ', '', ' ', ''], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [' ', '', ' ', '']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 130: Exception')
        print_exception()

    print('Startar test 3/131')
    try:
        res = without(['nÃ¥gra', 'strÃ¤ngar', 'av', 'olika', 'lÃ¤ngd', 'i', 'hav', 'totalfÃ¶rstÃ¶rt', 'frÃ¥n', 'laxmassor'], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = ['nÃ¥gra', 'strÃ¤ngar', 'av', 'olika', 'lÃ¤ngd', 'i', 'hav', 'totalfÃ¶rstÃ¶rt', 'frÃ¥n', 'laxmassor']
        if res != exp:
            print("Fel i test 3/131: without(['nÃ¥gra', 'strÃ¤ngar', 'av', 'olika', 'lÃ¤ngd', 'i', 'hav', 'totalfÃ¶rstÃ¶rt', 'frÃ¥n', 'laxmassor'], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: ['nÃ¥gra', 'strÃ¤ngar', 'av', 'olika', 'lÃ¤ngd', 'i', 'hav', 'totalfÃ¶rstÃ¶rt', 'frÃ¥n', 'laxmassor']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 131: Exception')
        print_exception()

    print('Startar test 3/132')
    try:
        res = without([' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', ''], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '']
        if res != exp:
            print("Fel i test 3/132: without([' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', ''], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 132: Exception')
        print_exception()

    print('Startar test 3/133')
    try:
        res = without(['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '\x7f', '\x80', '\x81', '\x82', '\x83', '\x84', '\x85', '\x86', '\x87', '\x88', '\x89', '\x8a', '\x8b', '\x8c', '\x8d', '\x8e', '\x8f', '\x90', '\x91', '\x92', '\x93', '\x94', '\x95'], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = ['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '\x7f', '\x80', '\x81', '\x82', '\x83', '\x84', '\x85', '\x86', '\x87', '\x88', '\x89', '\x8a', '\x8b', '\x8c', '\x8d', '\x8e', '\x8f', '\x90', '\x91', '\x92', '\x93', '\x94', '\x95']
        if res != exp:
            print("Fel i test 3/133: without([\'\\x00\', \'\\x01\', \'\\x02\', \'\\x03\', \'\\x04\', \'\\x05\', \'\\x06\', \'\\x07\', \'\\x08\', \'\\t\', \'\\n\', \'\\x0b\', \'\\x0c\', \'\\r\', \'\\x0e\', \'\\x0f\', \'\\x10\', \'\\x11\', \'\\x12\', \'\\x13\', \'\\x14\', \'\\x15\', \'\\x16\', \'\\x17\', \'\\x18\', \'\\x19\', \'\\x1a\', \'\\x1b\', \'\\x1c\', \'\\x1d\', \'\\x1e\', \'\\x1f\', \' \', \'!\', \'\"\', \'#\', \'$\', \'%\', \'&\', \"\'\", \'(\', \')\', \'*\', \'+\', \',\', \'-\', \'.\', \'/\', \'0\', \'1\', \'2\', \'3\', \'4\', \'5\', \'6\', \'7\', \'8\', \'9\', \':\', \';\', \'<\', \'=\', \'>\', \'?\', \'@\', \'A\', \'B\', \'C\', \'D\', \'E\', \'F\', \'G\', \'H\', \'I\', \'J\', \'K\', \'L\', \'M\', \'N\', \'O\', \'P\', \'Q\', \'R\', \'S\', \'T\', \'U\', \'V\', \'W\', \'X\', \'Y\', \'Z\', \'[\', \'\\\\\', \']\', \'^\', \'_\', \'`\', \'a\', \'b\', \'c\', \'d\', \'e\', \'f\', \'g\', \'h\', \'i\', \'j\', \'k\', \'l\', \'m\', \'n\', \'o\', \'p\', \'q\', \'r\', \'s\', \'t\', \'u\', \'v\', \'w\', \'x\', \'y\', \'z\', \'{\', \'|\', \'}\', \'~\', \'\\x7f\', \'\\x80\', \'\\x81\', \'\\x82\', \'\\x83\', \'\\x84\', \'\\x85\', \'\\x86\', \'\\x87\', \'\\x88\', \'\\x89\', \'\\x8a\', \'\\x8b\', \'\\x8c\', \'\\x8d\', \'\\x8e\', \'\\x8f\', \'\\x90\', \'\\x91\', \'\\x92\', \'\\x93\', \'\\x94\', \'\\x95\'], [1, 2, 5, \'3\', \'Ã¶\', 1.0, \'Hello\'])")
            print("Korrekt svar: ['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', ' ', '!', '\"', '#', '$', '%', '&', \"'\", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '\x7f', '\x80', '\x81', '\x82', '\x83', '\x84', '\x85', '\x86', '\x87', '\x88', '\x89', '\x8a', '\x8b', '\x8c', '\x8d', '\x8e', '\x8f', '\x90', '\x91', '\x92', '\x93', '\x94', '\x95']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 133: Exception')
        print_exception()

    print('Startar test 3/134')
    try:
        res = without([0.0, 1.0, 2.0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [0.0]
        if res != exp:
            print("Fel i test 3/134: without([0.0, 1.0, 2.0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [0.0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 134: Exception')
        print_exception()

    print('Startar test 3/135')
    try:
        res = without([-25.0, -24.0, -23.0, -22.0, -21.0, -20.0, -19.0, -18.0, -17.0, -16.0, -15.0, -14.0, -13.0, -12.0, -11.0, -10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [-25.0, -24.0, -23.0, -22.0, -21.0, -20.0, -19.0, -18.0, -17.0, -16.0, -15.0, -14.0, -13.0, -12.0, -11.0, -10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 3.0, 4.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0]
        if res != exp:
            print("Fel i test 3/135: without([-25.0, -24.0, -23.0, -22.0, -21.0, -20.0, -19.0, -18.0, -17.0, -16.0, -15.0, -14.0, -13.0, -12.0, -11.0, -10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [-25.0, -24.0, -23.0, -22.0, -21.0, -20.0, -19.0, -18.0, -17.0, -16.0, -15.0, -14.0, -13.0, -12.0, -11.0, -10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 3.0, 4.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 135: Exception')
        print_exception()

    print('Startar test 3/136')
    try:
        res = without([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0, 33.5, 34.0, 34.5, 35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0, 42.5, 43.0, 43.5, 44.0, 44.5, 45.0, 45.5, 46.0, 46.5, 47.0, 47.5, 48.0, 48.5, 49.0, 49.5, 50.0, 50.5, 51.0, 51.5, 52.0, 52.5, 53.0, 53.5, 54.0, 54.5, 55.0, 55.5, 56.0, 56.5, 57.0, 57.5, 58.0, 58.5, 59.0, 59.5, 60.0, 60.5, 61.0, 61.5, 62.0, 62.5, 63.0, 63.5, 64.0, 64.5, 65.0, 65.5, 66.0, 66.5, 67.0, 67.5, 68.0, 68.5, 69.0, 69.5, 70.0, 70.5, 71.0, 71.5, 72.0, 72.5, 73.0, 73.5, 74.0, 74.5], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [0.0, 0.5, 1.5, 2.5, 3.0, 3.5, 4.0, 4.5, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0, 33.5, 34.0, 34.5, 35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0, 42.5, 43.0, 43.5, 44.0, 44.5, 45.0, 45.5, 46.0, 46.5, 47.0, 47.5, 48.0, 48.5, 49.0, 49.5, 50.0, 50.5, 51.0, 51.5, 52.0, 52.5, 53.0, 53.5, 54.0, 54.5, 55.0, 55.5, 56.0, 56.5, 57.0, 57.5, 58.0, 58.5, 59.0, 59.5, 60.0, 60.5, 61.0, 61.5, 62.0, 62.5, 63.0, 63.5, 64.0, 64.5, 65.0, 65.5, 66.0, 66.5, 67.0, 67.5, 68.0, 68.5, 69.0, 69.5, 70.0, 70.5, 71.0, 71.5, 72.0, 72.5, 73.0, 73.5, 74.0, 74.5]
        if res != exp:
            print("Fel i test 3/136: without([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0, 33.5, 34.0, 34.5, 35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0, 42.5, 43.0, 43.5, 44.0, 44.5, 45.0, 45.5, 46.0, 46.5, 47.0, 47.5, 48.0, 48.5, 49.0, 49.5, 50.0, 50.5, 51.0, 51.5, 52.0, 52.5, 53.0, 53.5, 54.0, 54.5, 55.0, 55.5, 56.0, 56.5, 57.0, 57.5, 58.0, 58.5, 59.0, 59.5, 60.0, 60.5, 61.0, 61.5, 62.0, 62.5, 63.0, 63.5, 64.0, 64.5, 65.0, 65.5, 66.0, 66.5, 67.0, 67.5, 68.0, 68.5, 69.0, 69.5, 70.0, 70.5, 71.0, 71.5, 72.0, 72.5, 73.0, 73.5, 74.0, 74.5], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [0.0, 0.5, 1.5, 2.5, 3.0, 3.5, 4.0, 4.5, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0, 33.5, 34.0, 34.5, 35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0, 42.5, 43.0, 43.5, 44.0, 44.5, 45.0, 45.5, 46.0, 46.5, 47.0, 47.5, 48.0, 48.5, 49.0, 49.5, 50.0, 50.5, 51.0, 51.5, 52.0, 52.5, 53.0, 53.5, 54.0, 54.5, 55.0, 55.5, 56.0, 56.5, 57.0, 57.5, 58.0, 58.5, 59.0, 59.5, 60.0, 60.5, 61.0, 61.5, 62.0, 62.5, 63.0, 63.5, 64.0, 64.5, 65.0, 65.5, 66.0, 66.5, 67.0, 67.5, 68.0, 68.5, 69.0, 69.5, 70.0, 70.5, 71.0, 71.5, 72.0, 72.5, 73.0, 73.5, 74.0, 74.5]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 136: Exception')
        print_exception()

    print('Startar test 3/137')
    try:
        res = without([7.6, 7.7, 7, 7.0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [7.6, 7.7, 7, 7.0]
        if res != exp:
            print("Fel i test 3/137: without([7.6, 7.7, 7, 7.0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [7.6, 7.7, 7, 7.0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 137: Exception')
        print_exception()

    print('Startar test 3/138')
    try:
        res = without([1, 1.0, 1, 1.0, 1, 1, 1.0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = []
        if res != exp:
            print("Fel i test 3/138: without([1, 1.0, 1, 1.0, 1, 1, 1.0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 138: Exception')
        print_exception()

    print('Startar test 3/139')
    try:
        res = without(['0', 1.0, 2, '3', 4.0, 5, '6', 7.0, 8, '9', 10.0, 11, '12', 13.0, 14, '15', 16.0, 17, '18', 19.0, 20, '21', 22.0, 23, '24', 25.0, 26, '27', 28.0, 29, '30', 31.0, 32, '33', 34.0, 35, '36', 37.0, 38, '39', 40.0, 41, '42', 43.0, 44, '45', 46.0, 47, '48', 49.0, 50, '51', 52.0, 53, '54', 55.0, 56, '57', 58.0, 59, '60', 61.0, 62, '63', 64.0, 65, '66', 67.0, 68, '69', 70.0, 71, '72', 73.0, 74, '75', 76.0, 77, '78', 79.0, 80, '81', 82.0, 83, '84', 85.0, 86, '87', 88.0, 89, '90', 91.0, 92, '93', 94.0, 95, '96', 97.0, 98, '99', 100.0, 101, '102', 103.0, 104, '105', 106.0, 107, '108', 109.0, 110, '111', 112.0, 113, '114', 115.0, 116, '117', 118.0, 119, '120', 121.0, 122, '123', 124.0, 125, '126', 127.0, 128, '129', 130.0, 131, '132', 133.0, 134, '135', 136.0, 137, '138', 139.0, 140, '141', 142.0, 143, '144', 145.0, 146, '147', 148.0, 149], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = ['0', 4.0, '6', 7.0, 8, '9', 10.0, 11, '12', 13.0, 14, '15', 16.0, 17, '18', 19.0, 20, '21', 22.0, 23, '24', 25.0, 26, '27', 28.0, 29, '30', 31.0, 32, '33', 34.0, 35, '36', 37.0, 38, '39', 40.0, 41, '42', 43.0, 44, '45', 46.0, 47, '48', 49.0, 50, '51', 52.0, 53, '54', 55.0, 56, '57', 58.0, 59, '60', 61.0, 62, '63', 64.0, 65, '66', 67.0, 68, '69', 70.0, 71, '72', 73.0, 74, '75', 76.0, 77, '78', 79.0, 80, '81', 82.0, 83, '84', 85.0, 86, '87', 88.0, 89, '90', 91.0, 92, '93', 94.0, 95, '96', 97.0, 98, '99', 100.0, 101, '102', 103.0, 104, '105', 106.0, 107, '108', 109.0, 110, '111', 112.0, 113, '114', 115.0, 116, '117', 118.0, 119, '120', 121.0, 122, '123', 124.0, 125, '126', 127.0, 128, '129', 130.0, 131, '132', 133.0, 134, '135', 136.0, 137, '138', 139.0, 140, '141', 142.0, 143, '144', 145.0, 146, '147', 148.0, 149]
        if res != exp:
            print("Fel i test 3/139: without(['0', 1.0, 2, '3', 4.0, 5, '6', 7.0, 8, '9', 10.0, 11, '12', 13.0, 14, '15', 16.0, 17, '18', 19.0, 20, '21', 22.0, 23, '24', 25.0, 26, '27', 28.0, 29, '30', 31.0, 32, '33', 34.0, 35, '36', 37.0, 38, '39', 40.0, 41, '42', 43.0, 44, '45', 46.0, 47, '48', 49.0, 50, '51', 52.0, 53, '54', 55.0, 56, '57', 58.0, 59, '60', 61.0, 62, '63', 64.0, 65, '66', 67.0, 68, '69', 70.0, 71, '72', 73.0, 74, '75', 76.0, 77, '78', 79.0, 80, '81', 82.0, 83, '84', 85.0, 86, '87', 88.0, 89, '90', 91.0, 92, '93', 94.0, 95, '96', 97.0, 98, '99', 100.0, 101, '102', 103.0, 104, '105', 106.0, 107, '108', 109.0, 110, '111', 112.0, 113, '114', 115.0, 116, '117', 118.0, 119, '120', 121.0, 122, '123', 124.0, 125, '126', 127.0, 128, '129', 130.0, 131, '132', 133.0, 134, '135', 136.0, 137, '138', 139.0, 140, '141', 142.0, 143, '144', 145.0, 146, '147', 148.0, 149], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: ['0', 4.0, '6', 7.0, 8, '9', 10.0, 11, '12', 13.0, 14, '15', 16.0, 17, '18', 19.0, 20, '21', 22.0, 23, '24', 25.0, 26, '27', 28.0, 29, '30', 31.0, 32, '33', 34.0, 35, '36', 37.0, 38, '39', 40.0, 41, '42', 43.0, 44, '45', 46.0, 47, '48', 49.0, 50, '51', 52.0, 53, '54', 55.0, 56, '57', 58.0, 59, '60', 61.0, 62, '63', 64.0, 65, '66', 67.0, 68, '69', 70.0, 71, '72', 73.0, 74, '75', 76.0, 77, '78', 79.0, 80, '81', 82.0, 83, '84', 85.0, 86, '87', 88.0, 89, '90', 91.0, 92, '93', 94.0, 95, '96', 97.0, 98, '99', 100.0, 101, '102', 103.0, 104, '105', 106.0, 107, '108', 109.0, 110, '111', 112.0, 113, '114', 115.0, 116, '117', 118.0, 119, '120', 121.0, 122, '123', 124.0, 125, '126', 127.0, 128, '129', 130.0, 131, '132', 133.0, 134, '135', 136.0, 137, '138', 139.0, 140, '141', 142.0, 143, '144', 145.0, 146, '147', 148.0, 149]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 139: Exception')
        print_exception()

    print('Startar test 3/140')
    try:
        res = without(['1', 1, 2, '2', '3', '3', 4, 4], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = ['1', '2', 4, 4]
        if res != exp:
            print("Fel i test 3/140: without(['1', 1, 2, '2', '3', '3', 4, 4], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: ['1', '2', 4, 4]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 140: Exception')
        print_exception()

    print('Startar test 3/141')
    try:
        res = without([], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = []
        if res != exp:
            print("Fel i test 3/141: without([], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 141: Exception')
        print_exception()

    print('Startar test 3/142')
    try:
        res = without([[[[]]]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [[[[]]]]
        if res != exp:
            print("Fel i test 3/142: without([[[[]]]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [[[[]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 142: Exception')
        print_exception()

    print('Startar test 3/143')
    try:
        res = without([[]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [[]]
        if res != exp:
            print("Fel i test 3/143: without([[]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [[]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 143: Exception')
        print_exception()

    print('Startar test 3/144')
    try:
        res = without([[], [[]]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [[], [[]]]
        if res != exp:
            print("Fel i test 3/144: without([[], [[]]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [[], [[]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 144: Exception')
        print_exception()

    print('Startar test 3/145')
    try:
        res = without([[[[[]]]], [], [[]]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [[[[[]]]], [], [[]]]
        if res != exp:
            print("Fel i test 3/145: without([[[[[]]]], [], [[]]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [[[[[]]]], [], [[]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 145: Exception')
        print_exception()

    print('Startar test 3/146')
    try:
        res = without([[[[5]]]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [[[[]]]]
        if res != exp:
            print("Fel i test 3/146: without([[[[5]]]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [[[[]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 146: Exception')
        print_exception()

    print('Startar test 3/147')
    try:
        res = without([[1], [2]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [[], []]
        if res != exp:
            print("Fel i test 3/147: without([[1], [2]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [[], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 147: Exception')
        print_exception()

    print('Startar test 3/148')
    try:
        res = without([[1], [[2]], [[[3]]], [[[[4]]]]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [[], [[]], [[[3]]], [[[[4]]]]]
        if res != exp:
            print("Fel i test 3/148: without([[1], [[2]], [[[3]]], [[[[4]]]]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [[], [[]], [[[3]]], [[[[4]]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 148: Exception')
        print_exception()

    print('Startar test 3/149')
    try:
        res = without([[-1], [[[2]]], 33, [[[[78]]]], [[[-123]]]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [[-1], [[[]]], 33, [[[[78]]]], [[[-123]]]]
        if res != exp:
            print("Fel i test 3/149: without([[-1], [[[2]]], 33, [[[[78]]]], [[[-123]]]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [[-1], [[[]]], 33, [[[[78]]]], [[[-123]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 149: Exception')
        print_exception()

    print('Startar test 3/150')
    try:
        res = without([[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12], [0, 4, 8, 12, 16]], [[0, 0, 0, 0, 0], [0, 2, 4, 6, 8], [0, 4, 8, 12, 16], [0, 6, 12, 18, 24], [0, 8, 16, 24, 32]], [[0, 0, 0, 0, 0], [0, 3, 6, 9, 12], [0, 6, 12, 18, 24], [0, 9, 18, 27, 36], [0, 12, 24, 36, 48]], [[0, 0, 0, 0, 0], [0, 4, 8, 12, 16], [0, 8, 16, 24, 32], [0, 12, 24, 36, 48], [0, 16, 32, 48, 64]]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 3, 4], [0, 4, 6, 8], [0, 3, 6, 9, 12], [0, 4, 8, 12, 16]], [[0, 0, 0, 0, 0], [0, 4, 6, 8], [0, 4, 8, 12, 16], [0, 6, 12, 18, 24], [0, 8, 16, 24, 32]], [[0, 0, 0, 0, 0], [0, 3, 6, 9, 12], [0, 6, 12, 18, 24], [0, 9, 18, 27, 36], [0, 12, 24, 36, 48]], [[0, 0, 0, 0, 0], [0, 4, 8, 12, 16], [0, 8, 16, 24, 32], [0, 12, 24, 36, 48], [0, 16, 32, 48, 64]]]
        if res != exp:
            print("Fel i test 3/150: without([[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12], [0, 4, 8, 12, 16]], [[0, 0, 0, 0, 0], [0, 2, 4, 6, 8], [0, 4, 8, 12, 16], [0, 6, 12, 18, 24], [0, 8, 16, 24, 32]], [[0, 0, 0, 0, 0], [0, 3, 6, 9, 12], [0, 6, 12, 18, 24], [0, 9, 18, 27, 36], [0, 12, 24, 36, 48]], [[0, 0, 0, 0, 0], [0, 4, 8, 12, 16], [0, 8, 16, 24, 32], [0, 12, 24, 36, 48], [0, 16, 32, 48, 64]]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 3, 4], [0, 4, 6, 8], [0, 3, 6, 9, 12], [0, 4, 8, 12, 16]], [[0, 0, 0, 0, 0], [0, 4, 6, 8], [0, 4, 8, 12, 16], [0, 6, 12, 18, 24], [0, 8, 16, 24, 32]], [[0, 0, 0, 0, 0], [0, 3, 6, 9, 12], [0, 6, 12, 18, 24], [0, 9, 18, 27, 36], [0, 12, 24, 36, 48]], [[0, 0, 0, 0, 0], [0, 4, 8, 12, 16], [0, 8, 16, 24, 32], [0, 12, 24, 36, 48], [0, 16, 32, 48, 64]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 150: Exception')
        print_exception()

    print('Startar test 3/151')
    try:
        res = without([[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, -1, -2, -3, -4], [0, -2, -4, -6, -8], [0, -3, -6, -9, -12], [0, -4, -8, -12, -16]], [[0, 0, 0, 0, 0], [0, -2, -4, -6, -8], [0, -4, -8, -12, -16], [0, -6, -12, -18, -24], [0, -8, -16, -24, -32]], [[0, 0, 0, 0, 0], [0, -3, -6, -9, -12], [0, -6, -12, -18, -24], [0, -9, -18, -27, -36], [0, -12, -24, -36, -48]], [[0, 0, 0, 0, 0], [0, -4, -8, -12, -16], [0, -8, -16, -24, -32], [0, -12, -24, -36, -48], [0, -16, -32, -48, -64]]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, -1, -2, -3, -4], [0, -2, -4, -6, -8], [0, -3, -6, -9, -12], [0, -4, -8, -12, -16]], [[0, 0, 0, 0, 0], [0, -2, -4, -6, -8], [0, -4, -8, -12, -16], [0, -6, -12, -18, -24], [0, -8, -16, -24, -32]], [[0, 0, 0, 0, 0], [0, -3, -6, -9, -12], [0, -6, -12, -18, -24], [0, -9, -18, -27, -36], [0, -12, -24, -36, -48]], [[0, 0, 0, 0, 0], [0, -4, -8, -12, -16], [0, -8, -16, -24, -32], [0, -12, -24, -36, -48], [0, -16, -32, -48, -64]]]
        if res != exp:
            print("Fel i test 3/151: without([[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, -1, -2, -3, -4], [0, -2, -4, -6, -8], [0, -3, -6, -9, -12], [0, -4, -8, -12, -16]], [[0, 0, 0, 0, 0], [0, -2, -4, -6, -8], [0, -4, -8, -12, -16], [0, -6, -12, -18, -24], [0, -8, -16, -24, -32]], [[0, 0, 0, 0, 0], [0, -3, -6, -9, -12], [0, -6, -12, -18, -24], [0, -9, -18, -27, -36], [0, -12, -24, -36, -48]], [[0, 0, 0, 0, 0], [0, -4, -8, -12, -16], [0, -8, -16, -24, -32], [0, -12, -24, -36, -48], [0, -16, -32, -48, -64]]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, -1, -2, -3, -4], [0, -2, -4, -6, -8], [0, -3, -6, -9, -12], [0, -4, -8, -12, -16]], [[0, 0, 0, 0, 0], [0, -2, -4, -6, -8], [0, -4, -8, -12, -16], [0, -6, -12, -18, -24], [0, -8, -16, -24, -32]], [[0, 0, 0, 0, 0], [0, -3, -6, -9, -12], [0, -6, -12, -18, -24], [0, -9, -18, -27, -36], [0, -12, -24, -36, -48]], [[0, 0, 0, 0, 0], [0, -4, -8, -12, -16], [0, -8, -16, -24, -32], [0, -12, -24, -36, -48], [0, -16, -32, -48, -64]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 151: Exception')
        print_exception()

    print('Startar test 3/152')
    try:
        res = without([[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [[], [0], [0], [0], [0, 3], [0, 3, 4], [0, 3, 4], [0, 3, 4, 6], [0, 3, 4, 6, 7], [0, 3, 4, 6, 7, 8], [0, 3, 4, 6, 7, 8, 9], [0, 3, 4, 6, 7, 8, 9, 10], [0, 3, 4, 6, 7, 8, 9, 10, 11], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]]
        if res != exp:
            print("Fel i test 3/152: without([[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [[], [0], [0], [0], [0, 3], [0, 3, 4], [0, 3, 4], [0, 3, 4, 6], [0, 3, 4, 6, 7], [0, 3, 4, 6, 7, 8], [0, 3, 4, 6, 7, 8, 9], [0, 3, 4, 6, 7, 8, 9, 10], [0, 3, 4, 6, 7, 8, 9, 10, 11], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 152: Exception')
        print_exception()

    print('Startar test 3/153')
    try:
        res = without([[], [[0]], [[0], [1], [0], [1]], [[0], [1], [2], [0], [1], [2], [0], [1], [2]], [[0], [1], [2], [3], [0], [1], [2], [3], [0], [1], [2], [3], [0], [1], [2], [3]], [[0], [1], [2], [3], [4], [0], [1], [2], [3], [4], [0], [1], [2], [3], [4], [0], [1], [2], [3], [4], [0], [1], [2], [3], [4]], [[0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5]], [[0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6]], [[0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7]], [[0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8]]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [[], [[0]], [[0], [], [0], []], [[0], [], [], [0], [], [], [0], [], []], [[0], [], [], [3], [0], [], [], [3], [0], [], [], [3], [0], [], [], [3]], [[0], [], [], [3], [4], [0], [], [], [3], [4], [0], [], [], [3], [4], [0], [], [], [3], [4], [0], [], [], [3], [4]], [[0], [], [], [3], [4], [], [0], [], [], [3], [4], [], [0], [], [], [3], [4], [], [0], [], [], [3], [4], [], [0], [], [], [3], [4], [], [0], [], [], [3], [4], []], [[0], [], [], [3], [4], [], [6], [0], [], [], [3], [4], [], [6], [0], [], [], [3], [4], [], [6], [0], [], [], [3], [4], [], [6], [0], [], [], [3], [4], [], [6], [0], [], [], [3], [4], [], [6], [0], [], [], [3], [4], [], [6]], [[0], [], [], [3], [4], [], [6], [7], [0], [], [], [3], [4], [], [6], [7], [0], [], [], [3], [4], [], [6], [7], [0], [], [], [3], [4], [], [6], [7], [0], [], [], [3], [4], [], [6], [7], [0], [], [], [3], [4], [], [6], [7], [0], [], [], [3], [4], [], [6], [7], [0], [], [], [3], [4], [], [6], [7]], [[0], [], [], [3], [4], [], [6], [7], [8], [0], [], [], [3], [4], [], [6], [7], [8], [0], [], [], [3], [4], [], [6], [7], [8], [0], [], [], [3], [4], [], [6], [7], [8], [0], [], [], [3], [4], [], [6], [7], [8], [0], [], [], [3], [4], [], [6], [7], [8], [0], [], [], [3], [4], [], [6], [7], [8], [0], [], [], [3], [4], [], [6], [7], [8], [0], [], [], [3], [4], [], [6], [7], [8]]]
        if res != exp:
            print("Fel i test 3/153: without([[], [[0]], [[0], [1], [0], [1]], [[0], [1], [2], [0], [1], [2], [0], [1], [2]], [[0], [1], [2], [3], [0], [1], [2], [3], [0], [1], [2], [3], [0], [1], [2], [3]], [[0], [1], [2], [3], [4], [0], [1], [2], [3], [4], [0], [1], [2], [3], [4], [0], [1], [2], [3], [4], [0], [1], [2], [3], [4]], [[0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5]], [[0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6]], [[0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7]], [[0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8]]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [[], [[0]], [[0], [], [0], []], [[0], [], [], [0], [], [], [0], [], []], [[0], [], [], [3], [0], [], [], [3], [0], [], [], [3], [0], [], [], [3]], [[0], [], [], [3], [4], [0], [], [], [3], [4], [0], [], [], [3], [4], [0], [], [], [3], [4], [0], [], [], [3], [4]], [[0], [], [], [3], [4], [], [0], [], [], [3], [4], [], [0], [], [], [3], [4], [], [0], [], [], [3], [4], [], [0], [], [], [3], [4], [], [0], [], [], [3], [4], []], [[0], [], [], [3], [4], [], [6], [0], [], [], [3], [4], [], [6], [0], [], [], [3], [4], [], [6], [0], [], [], [3], [4], [], [6], [0], [], [], [3], [4], [], [6], [0], [], [], [3], [4], [], [6], [0], [], [], [3], [4], [], [6]], [[0], [], [], [3], [4], [], [6], [7], [0], [], [], [3], [4], [], [6], [7], [0], [], [], [3], [4], [], [6], [7], [0], [], [], [3], [4], [], [6], [7], [0], [], [], [3], [4], [], [6], [7], [0], [], [], [3], [4], [], [6], [7], [0], [], [], [3], [4], [], [6], [7], [0], [], [], [3], [4], [], [6], [7]], [[0], [], [], [3], [4], [], [6], [7], [8], [0], [], [], [3], [4], [], [6], [7], [8], [0], [], [], [3], [4], [], [6], [7], [8], [0], [], [], [3], [4], [], [6], [7], [8], [0], [], [], [3], [4], [], [6], [7], [8], [0], [], [], [3], [4], [], [6], [7], [8], [0], [], [], [3], [4], [], [6], [7], [8], [0], [], [], [3], [4], [], [6], [7], [8], [0], [], [], [3], [4], [], [6], [7], [8]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 153: Exception')
        print_exception()

    print('Startar test 3/154')
    try:
        res = without([tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple()], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple()]
        if res != exp:
            print("Fel i test 3/154: without([tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple()], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [(), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ()]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 154: Exception')
        print_exception()

    print('Startar test 3/155')
    try:
        res = without([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        if res != exp:
            print("Fel i test 3/155: without([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 155: Exception')
        print_exception()

    print('Startar test 3/156')
    try:
        res = without([[1, 2, 3], '123'], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [[3], '123']
        if res != exp:
            print("Fel i test 3/156: without([[1, 2, 3], '123'], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [[3], '123']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 156: Exception')
        print_exception()

    print('Startar test 3/157')
    try:
        res = without([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399]
        if res != exp:
            print("Fel i test 3/157: without([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 157: Exception')
        print_exception()

    print('Startar test 3/158')
    try:
        res = without([-400, -399, -398, -397, -396, -395, -394, -393, -392, -391, -390, -389, -388, -387, -386, -385, -384, -383, -382, -381, -380, -379, -378, -377, -376, -375, -374, -373, -372, -371, -370, -369, -368, -367, -366, -365, -364, -363, -362, -361, -360, -359, -358, -357, -356, -355, -354, -353, -352, -351, -350, -349, -348, -347, -346, -345, -344, -343, -342, -341, -340, -339, -338, -337, -336, -335, -334, -333, -332, -331, -330, -329, -328, -327, -326, -325, -324, -323, -322, -321, -320, -319, -318, -317, -316, -315, -314, -313, -312, -311, -310, -309, -308, -307, -306, -305, -304, -303, -302, -301, -300, -299, -298, -297, -296, -295, -294, -293, -292, -291, -290, -289, -288, -287, -286, -285, -284, -283, -282, -281, -280, -279, -278, -277, -276, -275, -274, -273, -272, -271, -270, -269, -268, -267, -266, -265, -264, -263, -262, -261, -260, -259, -258, -257, -256, -255, -254, -253, -252, -251, -250, -249, -248, -247, -246, -245, -244, -243, -242, -241, -240, -239, -238, -237, -236, -235, -234, -233, -232, -231, -230, -229, -228, -227, -226, -225, -224, -223, -222, -221, -220, -219, -218, -217, -216, -215, -214, -213, -212, -211, -210, -209, -208, -207, -206, -205, -204, -203, -202, -201, -200, -199, -198, -197, -196, -195, -194, -193, -192, -191, -190, -189, -188, -187, -186, -185, -184, -183, -182, -181, -180, -179, -178, -177, -176, -175, -174, -173, -172, -171, -170, -169, -168, -167, -166, -165, -164, -163, -162, -161, -160, -159, -158, -157, -156, -155, -154, -153, -152, -151, -150, -149, -148, -147, -146, -145, -144, -143, -142, -141, -140, -139, -138, -137, -136, -135, -134, -133, -132, -131, -130, -129, -128, -127, -126, -125, -124, -123, -122, -121, -120, -119, -118, -117, -116, -115, -114, -113, -112, -111, -110, -109, -108, -107, -106, -105, -104, -103, -102, -101, -100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [-400, -399, -398, -397, -396, -395, -394, -393, -392, -391, -390, -389, -388, -387, -386, -385, -384, -383, -382, -381, -380, -379, -378, -377, -376, -375, -374, -373, -372, -371, -370, -369, -368, -367, -366, -365, -364, -363, -362, -361, -360, -359, -358, -357, -356, -355, -354, -353, -352, -351, -350, -349, -348, -347, -346, -345, -344, -343, -342, -341, -340, -339, -338, -337, -336, -335, -334, -333, -332, -331, -330, -329, -328, -327, -326, -325, -324, -323, -322, -321, -320, -319, -318, -317, -316, -315, -314, -313, -312, -311, -310, -309, -308, -307, -306, -305, -304, -303, -302, -301, -300, -299, -298, -297, -296, -295, -294, -293, -292, -291, -290, -289, -288, -287, -286, -285, -284, -283, -282, -281, -280, -279, -278, -277, -276, -275, -274, -273, -272, -271, -270, -269, -268, -267, -266, -265, -264, -263, -262, -261, -260, -259, -258, -257, -256, -255, -254, -253, -252, -251, -250, -249, -248, -247, -246, -245, -244, -243, -242, -241, -240, -239, -238, -237, -236, -235, -234, -233, -232, -231, -230, -229, -228, -227, -226, -225, -224, -223, -222, -221, -220, -219, -218, -217, -216, -215, -214, -213, -212, -211, -210, -209, -208, -207, -206, -205, -204, -203, -202, -201, -200, -199, -198, -197, -196, -195, -194, -193, -192, -191, -190, -189, -188, -187, -186, -185, -184, -183, -182, -181, -180, -179, -178, -177, -176, -175, -174, -173, -172, -171, -170, -169, -168, -167, -166, -165, -164, -163, -162, -161, -160, -159, -158, -157, -156, -155, -154, -153, -152, -151, -150, -149, -148, -147, -146, -145, -144, -143, -142, -141, -140, -139, -138, -137, -136, -135, -134, -133, -132, -131, -130, -129, -128, -127, -126, -125, -124, -123, -122, -121, -120, -119, -118, -117, -116, -115, -114, -113, -112, -111, -110, -109, -108, -107, -106, -105, -104, -103, -102, -101, -100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399]
        if res != exp:
            print("Fel i test 3/158: without([-400, -399, -398, -397, -396, -395, -394, -393, -392, -391, -390, -389, -388, -387, -386, -385, -384, -383, -382, -381, -380, -379, -378, -377, -376, -375, -374, -373, -372, -371, -370, -369, -368, -367, -366, -365, -364, -363, -362, -361, -360, -359, -358, -357, -356, -355, -354, -353, -352, -351, -350, -349, -348, -347, -346, -345, -344, -343, -342, -341, -340, -339, -338, -337, -336, -335, -334, -333, -332, -331, -330, -329, -328, -327, -326, -325, -324, -323, -322, -321, -320, -319, -318, -317, -316, -315, -314, -313, -312, -311, -310, -309, -308, -307, -306, -305, -304, -303, -302, -301, -300, -299, -298, -297, -296, -295, -294, -293, -292, -291, -290, -289, -288, -287, -286, -285, -284, -283, -282, -281, -280, -279, -278, -277, -276, -275, -274, -273, -272, -271, -270, -269, -268, -267, -266, -265, -264, -263, -262, -261, -260, -259, -258, -257, -256, -255, -254, -253, -252, -251, -250, -249, -248, -247, -246, -245, -244, -243, -242, -241, -240, -239, -238, -237, -236, -235, -234, -233, -232, -231, -230, -229, -228, -227, -226, -225, -224, -223, -222, -221, -220, -219, -218, -217, -216, -215, -214, -213, -212, -211, -210, -209, -208, -207, -206, -205, -204, -203, -202, -201, -200, -199, -198, -197, -196, -195, -194, -193, -192, -191, -190, -189, -188, -187, -186, -185, -184, -183, -182, -181, -180, -179, -178, -177, -176, -175, -174, -173, -172, -171, -170, -169, -168, -167, -166, -165, -164, -163, -162, -161, -160, -159, -158, -157, -156, -155, -154, -153, -152, -151, -150, -149, -148, -147, -146, -145, -144, -143, -142, -141, -140, -139, -138, -137, -136, -135, -134, -133, -132, -131, -130, -129, -128, -127, -126, -125, -124, -123, -122, -121, -120, -119, -118, -117, -116, -115, -114, -113, -112, -111, -110, -109, -108, -107, -106, -105, -104, -103, -102, -101, -100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [-400, -399, -398, -397, -396, -395, -394, -393, -392, -391, -390, -389, -388, -387, -386, -385, -384, -383, -382, -381, -380, -379, -378, -377, -376, -375, -374, -373, -372, -371, -370, -369, -368, -367, -366, -365, -364, -363, -362, -361, -360, -359, -358, -357, -356, -355, -354, -353, -352, -351, -350, -349, -348, -347, -346, -345, -344, -343, -342, -341, -340, -339, -338, -337, -336, -335, -334, -333, -332, -331, -330, -329, -328, -327, -326, -325, -324, -323, -322, -321, -320, -319, -318, -317, -316, -315, -314, -313, -312, -311, -310, -309, -308, -307, -306, -305, -304, -303, -302, -301, -300, -299, -298, -297, -296, -295, -294, -293, -292, -291, -290, -289, -288, -287, -286, -285, -284, -283, -282, -281, -280, -279, -278, -277, -276, -275, -274, -273, -272, -271, -270, -269, -268, -267, -266, -265, -264, -263, -262, -261, -260, -259, -258, -257, -256, -255, -254, -253, -252, -251, -250, -249, -248, -247, -246, -245, -244, -243, -242, -241, -240, -239, -238, -237, -236, -235, -234, -233, -232, -231, -230, -229, -228, -227, -226, -225, -224, -223, -222, -221, -220, -219, -218, -217, -216, -215, -214, -213, -212, -211, -210, -209, -208, -207, -206, -205, -204, -203, -202, -201, -200, -199, -198, -197, -196, -195, -194, -193, -192, -191, -190, -189, -188, -187, -186, -185, -184, -183, -182, -181, -180, -179, -178, -177, -176, -175, -174, -173, -172, -171, -170, -169, -168, -167, -166, -165, -164, -163, -162, -161, -160, -159, -158, -157, -156, -155, -154, -153, -152, -151, -150, -149, -148, -147, -146, -145, -144, -143, -142, -141, -140, -139, -138, -137, -136, -135, -134, -133, -132, -131, -130, -129, -128, -127, -126, -125, -124, -123, -122, -121, -120, -119, -118, -117, -116, -115, -114, -113, -112, -111, -110, -109, -108, -107, -106, -105, -104, -103, -102, -101, -100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 158: Exception')
        print_exception()

    print('Startar test 3/159')
    try:
        res = without([2, 2.0, 3, 3.0, 3, 5, 3.0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [3, 3.0, 3, 3.0]
        if res != exp:
            print("Fel i test 3/159: without([2, 2.0, 3, 3.0, 3, 5, 3.0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [3, 3.0, 3, 3.0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 159: Exception')
        print_exception()

    print('Startar test 3/160')
    try:
        res = without([2, 2.0, 3, [3.0, 3, 5], 3.0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [3, [3.0, 3], 3.0]
        if res != exp:
            print("Fel i test 3/160: without([2, 2.0, 3, [3.0, 3, 5], 3.0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [3, [3.0, 3], 3.0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 160: Exception')
        print_exception()

    print('Startar test 3/161')
    try:
        res = without([2, 2.5, [14, 8.5]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [2.5, [14, 8.5]]
        if res != exp:
            print("Fel i test 3/161: without([2, 2.5, [14, 8.5]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [2.5, [14, 8.5]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 161: Exception')
        print_exception()

    print('Startar test 3/162')
    try:
        res = without([2, 2.5, [14, 8]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [2.5, [14, 8]]
        if res != exp:
            print("Fel i test 3/162: without([2, 2.5, [14, 8]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [2.5, [14, 8]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 162: Exception')
        print_exception()

    print('Startar test 3/163')
    try:
        res = without([2, 2, [14, 8.5]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [[14, 8.5]]
        if res != exp:
            print("Fel i test 3/163: without([2, 2, [14, 8.5]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [[14, 8.5]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 163: Exception')
        print_exception()

    print('Startar test 3/164')
    try:
        res = without([2, 2, 14, 8.5], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [14, 8.5]
        if res != exp:
            print("Fel i test 3/164: without([2, 2, 14, 8.5], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [14, 8.5]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 164: Exception')
        print_exception()

    print('Startar test 3/165')
    try:
        res = without([2, 4.0, [14, 12.0]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [4.0, [14, 12.0]]
        if res != exp:
            print("Fel i test 3/165: without([2, 4.0, [14, 12.0]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [4.0, [14, 12.0]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 165: Exception')
        print_exception()

    print('Startar test 3/166')
    try:
        res = without([2, 4.0, [14, 12]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [4.0, [14, 12]]
        if res != exp:
            print("Fel i test 3/166: without([2, 4.0, [14, 12]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [4.0, [14, 12]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 166: Exception')
        print_exception()

    print('Startar test 3/167')
    try:
        res = without([2, 4, [14, 12.0]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [4, [14, 12.0]]
        if res != exp:
            print("Fel i test 3/167: without([2, 4, [14, 12.0]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [4, [14, 12.0]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 167: Exception')
        print_exception()

    print('Startar test 3/168')
    try:
        res = without([2, 4, 14, 12.0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [4, 14, 12.0]
        if res != exp:
            print("Fel i test 3/168: without([2, 4, 14, 12.0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [4, 14, 12.0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 168: Exception')
        print_exception()

    print('Startar test 3/169')
    try:
        res = without([2, 5.0, [14, 11.0]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [[14, 11.0]]
        if res != exp:
            print("Fel i test 3/169: without([2, 5.0, [14, 11.0]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [[14, 11.0]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 169: Exception')
        print_exception()

    print('Startar test 3/170')
    try:
        res = without([2, 5.0, [14, 11]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [[14, 11]]
        if res != exp:
            print("Fel i test 3/170: without([2, 5.0, [14, 11]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [[14, 11]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 170: Exception')
        print_exception()

    print('Startar test 3/171')
    try:
        res = without([2, 4, [14, 11.0]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [4, [14, 11.0]]
        if res != exp:
            print("Fel i test 3/171: without([2, 4, [14, 11.0]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [4, [14, 11.0]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 171: Exception')
        print_exception()

    print('Startar test 3/172')
    try:
        res = without([2, 4, 14, 11.0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [4, 14, 11.0]
        if res != exp:
            print("Fel i test 3/172: without([2, 4, 14, 11.0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [4, 14, 11.0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 172: Exception')
        print_exception()

    print('Startar test 3/173')
    try:
        res = without([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [3, 3, 3, 3, 3]
        if res != exp:
            print("Fel i test 3/173: without([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [3, 3, 3, 3, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 173: Exception')
        print_exception()

    print('Startar test 3/174')
    try:
        res = without([0, 5, 5, 0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [0, 0]
        if res != exp:
            print("Fel i test 3/174: without([0, 5, 5, 0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [0, 0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 174: Exception')
        print_exception()

    print('Startar test 3/175')
    try:
        res = without([0, 5, 5, 5, 0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [0, 0]
        if res != exp:
            print("Fel i test 3/175: without([0, 5, 5, 5, 0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [0, 0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 175: Exception')
        print_exception()

    print('Startar test 3/176')
    try:
        res = without([0, 5, 5, 5, 0, 5, 5, 0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [0, 0, 0]
        if res != exp:
            print("Fel i test 3/176: without([0, 5, 5, 5, 0, 5, 5, 0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [0, 0, 0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 176: Exception')
        print_exception()

    print('Startar test 3/177')
    try:
        res = without([5, 5, 0, 5, 5, 0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [0, 0]
        if res != exp:
            print("Fel i test 3/177: without([5, 5, 0, 5, 5, 0], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [0, 0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 177: Exception')
        print_exception()

    print('Startar test 3/178')
    try:
        res = without([0, 5, 5, 0, 5, 5, 5], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [0, 0]
        if res != exp:
            print("Fel i test 3/178: without([0, 5, 5, 0, 5, 5, 5], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [0, 0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 178: Exception')
        print_exception()

    print('Startar test 3/179')
    try:
        res = without([[0, 5, 5, 0]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [[0, 0]]
        if res != exp:
            print("Fel i test 3/179: without([[0, 5, 5, 0]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [[0, 0]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 179: Exception')
        print_exception()

    print('Startar test 3/180')
    try:
        res = without([[0, 5, 5, 5, 0]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [[0, 0]]
        if res != exp:
            print("Fel i test 3/180: without([[0, 5, 5, 5, 0]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [[0, 0]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 180: Exception')
        print_exception()

    print('Startar test 3/181')
    try:
        res = without([[0, 5, 5, 5, 0, 5, 5, 0]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [[0, 0, 0]]
        if res != exp:
            print("Fel i test 3/181: without([[0, 5, 5, 5, 0, 5, 5, 0]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [[0, 0, 0]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 181: Exception')
        print_exception()

    print('Startar test 3/182')
    try:
        res = without([[5, 5, 0, 5, 5, 0]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [[0, 0]]
        if res != exp:
            print("Fel i test 3/182: without([[5, 5, 0, 5, 5, 0]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [[0, 0]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 182: Exception')
        print_exception()

    print('Startar test 3/183')
    try:
        res = without([[0, 5, 5, 0, 5, 5, 5]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])
        exp = [[0, 0]]
        if res != exp:
            print("Fel i test 3/183: without([[0, 5, 5, 0, 5, 5, 5]], [1, 2, 5, '3', 'Ã¶', 1.0, 'Hello'])")
            print("Korrekt svar: [[0, 0]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 183: Exception')
        print_exception()

    print('Startar test 3/184')
    try:
        res = without([1, 2, 3], [])
        exp = [1, 2, 3]
        if res != exp:
            print("Fel i test 3/184: without([1, 2, 3], [])")
            print("Korrekt svar: [1, 2, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 184: Exception')
        print_exception()

    print('Startar test 3/185')
    try:
        res = without([1, 2, 3], [1])
        exp = [2, 3]
        if res != exp:
            print("Fel i test 3/185: without([1, 2, 3], [1])")
            print("Korrekt svar: [2, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 185: Exception')
        print_exception()

    print('Startar test 3/186')
    try:
        res = without([1, 2, 3], [2])
        exp = [1, 3]
        if res != exp:
            print("Fel i test 3/186: without([1, 2, 3], [2])")
            print("Korrekt svar: [1, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 186: Exception')
        print_exception()

    print('Startar test 3/187')
    try:
        res = without([1, 2, 3], [3])
        exp = [1, 2]
        if res != exp:
            print("Fel i test 3/187: without([1, 2, 3], [3])")
            print("Korrekt svar: [1, 2]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 187: Exception')
        print_exception()

    print('Startar test 3/188')
    try:
        res = without([1, 2, 3], [1, 2, 3])
        exp = []
        if res != exp:
            print("Fel i test 3/188: without([1, 2, 3], [1, 2, 3])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 188: Exception')
        print_exception()

    print('Startar test 3/189')
    try:
        res = without([], [])
        exp = []
        if res != exp:
            print("Fel i test 3/189: without([], [])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 189: Exception')
        print_exception()

    print('Startar test 3/190')
    try:
        res = without([], [1])
        exp = []
        if res != exp:
            print("Fel i test 3/190: without([], [1])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 190: Exception')
        print_exception()

    print('Startar test 3/191')
    try:
        res = without([[1], 2, 3], [1, 2, 3])
        exp = [[]]
        if res != exp:
            print("Fel i test 3/191: without([[1], 2, 3], [1, 2, 3])")
            print("Korrekt svar: [[]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 191: Exception')
        print_exception()

    print('Startar test 3/192')
    try:
        res = without([1, [2], 3], [1, 2, 3])
        exp = [[]]
        if res != exp:
            print("Fel i test 3/192: without([1, [2], 3], [1, 2, 3])")
            print("Korrekt svar: [[]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 192: Exception')
        print_exception()

    print('Startar test 3/193')
    try:
        res = without([1, 2, [3]], [1, 2, 3])
        exp = [[]]
        if res != exp:
            print("Fel i test 3/193: without([1, 2, [3]], [1, 2, 3])")
            print("Korrekt svar: [[]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 193: Exception')
        print_exception()

    print('Startar test 3/194')
    try:
        res = without([1], ['lycka'])
        exp = [1]
        if res != exp:
            print("Fel i test 3/194: without([1], ['lycka'])")
            print("Korrekt svar: [1]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 194: Exception')
        print_exception()

    print('Startar test 3/195')
    try:
        res = without(['a'], ['lycka'])
        exp = ['a']
        if res != exp:
            print("Fel i test 3/195: without(['a'], ['lycka'])")
            print("Korrekt svar: ['a']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 195: Exception')
        print_exception()

    print('Startar test 3/196')
    try:
        res = without([0.1], ['lycka'])
        exp = [0.1]
        if res != exp:
            print("Fel i test 3/196: without([0.1], ['lycka'])")
            print("Korrekt svar: [0.1]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 196: Exception')
        print_exception()

    print('Startar test 3/197')
    try:
        res = without([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], ['lycka'])
        exp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
        if res != exp:
            print("Fel i test 3/197: without([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], ['lycka'])")
            print("Korrekt svar: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 197: Exception')
        print_exception()

    print('Startar test 3/198')
    try:
        res = without([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], ['lycka'])
        exp = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if res != exp:
            print("Fel i test 3/198: without([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], ['lycka'])")
            print("Korrekt svar: [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 198: Exception')
        print_exception()

    print('Startar test 3/199')
    try:
        res = without([5, 467, 123, 4567, 878, 345, 89, 90, 78], ['lycka'])
        exp = [5, 467, 123, 4567, 878, 345, 89, 90, 78]
        if res != exp:
            print("Fel i test 3/199: without([5, 467, 123, 4567, 878, 345, 89, 90, 78], ['lycka'])")
            print("Korrekt svar: [5, 467, 123, 4567, 878, 345, 89, 90, 78]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 199: Exception')
        print_exception()

    print('Startar test 3/200')
    try:
        res = without([0], ['lycka'])
        exp = [0]
        if res != exp:
            print("Fel i test 3/200: without([0], ['lycka'])")
            print("Korrekt svar: [0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 200: Exception')
        print_exception()

    print('Startar test 3/201')
    try:
        res = without([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], ['lycka'])
        exp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if res != exp:
            print("Fel i test 3/201: without([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], ['lycka'])")
            print("Korrekt svar: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 201: Exception')
        print_exception()

    print('Startar test 3/202')
    try:
        res = without([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], ['lycka'])
        exp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
        if res != exp:
            print("Fel i test 3/202: without([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], ['lycka'])")
            print("Korrekt svar: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 202: Exception')
        print_exception()

    print('Startar test 3/203')
    try:
        res = without([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], ['lycka'])
        exp = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
        if res != exp:
            print("Fel i test 3/203: without([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], ['lycka'])")
            print("Korrekt svar: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 203: Exception')
        print_exception()

    print('Startar test 3/204')
    try:
        res = without(['1', '2', '3', '4', '5'], ['lycka'])
        exp = ['1', '2', '3', '4', '5']
        if res != exp:
            print("Fel i test 3/204: without(['1', '2', '3', '4', '5'], ['lycka'])")
            print("Korrekt svar: ['1', '2', '3', '4', '5']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 204: Exception')
        print_exception()

    print('Startar test 3/205')
    try:
        res = without(['Ã¥', 'Ã¤', 'Ã¶', 'Ã¢', 'Ã´', 'Ãª', 'Ã¡', 'Ã³', 'Ã©'], ['lycka'])
        exp = ['Ã¥', 'Ã¤', 'Ã¶', 'Ã¢', 'Ã´', 'Ãª', 'Ã¡', 'Ã³', 'Ã©']
        if res != exp:
            print("Fel i test 3/205: without(['Ã¥', 'Ã¤', 'Ã¶', 'Ã¢', 'Ã´', 'Ãª', 'Ã¡', 'Ã³', 'Ã©'], ['lycka'])")
            print("Korrekt svar: ['Ã¥', 'Ã¤', 'Ã¶', 'Ã¢', 'Ã´', 'Ãª', 'Ã¡', 'Ã³', 'Ã©']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 205: Exception')
        print_exception()

    print('Startar test 3/206')
    try:
        res = without(['', '', '', ''], ['lycka'])
        exp = ['', '', '', '']
        if res != exp:
            print("Fel i test 3/206: without(['', '', '', ''], ['lycka'])")
            print("Korrekt svar: ['', '', '', '']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 206: Exception')
        print_exception()

    print('Startar test 3/207')
    try:
        res = without([' ', '', ' ', ''], ['lycka'])
        exp = [' ', '', ' ', '']
        if res != exp:
            print("Fel i test 3/207: without([' ', '', ' ', ''], ['lycka'])")
            print("Korrekt svar: [' ', '', ' ', '']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 207: Exception')
        print_exception()

    print('Startar test 3/208')
    try:
        res = without(['nÃ¥gra', 'strÃ¤ngar', 'av', 'olika', 'lÃ¤ngd', 'i', 'hav', 'totalfÃ¶rstÃ¶rt', 'frÃ¥n', 'laxmassor'], ['lycka'])
        exp = ['nÃ¥gra', 'strÃ¤ngar', 'av', 'olika', 'lÃ¤ngd', 'i', 'hav', 'totalfÃ¶rstÃ¶rt', 'frÃ¥n', 'laxmassor']
        if res != exp:
            print("Fel i test 3/208: without(['nÃ¥gra', 'strÃ¤ngar', 'av', 'olika', 'lÃ¤ngd', 'i', 'hav', 'totalfÃ¶rstÃ¶rt', 'frÃ¥n', 'laxmassor'], ['lycka'])")
            print("Korrekt svar: ['nÃ¥gra', 'strÃ¤ngar', 'av', 'olika', 'lÃ¤ngd', 'i', 'hav', 'totalfÃ¶rstÃ¶rt', 'frÃ¥n', 'laxmassor']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 208: Exception')
        print_exception()

    print('Startar test 3/209')
    try:
        res = without([' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', ''], ['lycka'])
        exp = [' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '']
        if res != exp:
            print("Fel i test 3/209: without([' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', ''], ['lycka'])")
            print("Korrekt svar: [' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 209: Exception')
        print_exception()

    print('Startar test 3/210')
    try:
        res = without(['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '\x7f', '\x80', '\x81', '\x82', '\x83', '\x84', '\x85', '\x86', '\x87', '\x88', '\x89', '\x8a', '\x8b', '\x8c', '\x8d', '\x8e', '\x8f', '\x90', '\x91', '\x92', '\x93', '\x94', '\x95'], ['lycka'])
        exp = ['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '\x7f', '\x80', '\x81', '\x82', '\x83', '\x84', '\x85', '\x86', '\x87', '\x88', '\x89', '\x8a', '\x8b', '\x8c', '\x8d', '\x8e', '\x8f', '\x90', '\x91', '\x92', '\x93', '\x94', '\x95']
        if res != exp:
            print("Fel i test 3/210: without([\'\\x00\', \'\\x01\', \'\\x02\', \'\\x03\', \'\\x04\', \'\\x05\', \'\\x06\', \'\\x07\', \'\\x08\', \'\\t\', \'\\n\', \'\\x0b\', \'\\x0c\', \'\\r\', \'\\x0e\', \'\\x0f\', \'\\x10\', \'\\x11\', \'\\x12\', \'\\x13\', \'\\x14\', \'\\x15\', \'\\x16\', \'\\x17\', \'\\x18\', \'\\x19\', \'\\x1a\', \'\\x1b\', \'\\x1c\', \'\\x1d\', \'\\x1e\', \'\\x1f\', \' \', \'!\', \'\"\', \'#\', \'$\', \'%\', \'&\', \"\'\", \'(\', \')\', \'*\', \'+\', \',\', \'-\', \'.\', \'/\', \'0\', \'1\', \'2\', \'3\', \'4\', \'5\', \'6\', \'7\', \'8\', \'9\', \':\', \';\', \'<\', \'=\', \'>\', \'?\', \'@\', \'A\', \'B\', \'C\', \'D\', \'E\', \'F\', \'G\', \'H\', \'I\', \'J\', \'K\', \'L\', \'M\', \'N\', \'O\', \'P\', \'Q\', \'R\', \'S\', \'T\', \'U\', \'V\', \'W\', \'X\', \'Y\', \'Z\', \'[\', \'\\\\\', \']\', \'^\', \'_\', \'`\', \'a\', \'b\', \'c\', \'d\', \'e\', \'f\', \'g\', \'h\', \'i\', \'j\', \'k\', \'l\', \'m\', \'n\', \'o\', \'p\', \'q\', \'r\', \'s\', \'t\', \'u\', \'v\', \'w\', \'x\', \'y\', \'z\', \'{\', \'|\', \'}\', \'~\', \'\\x7f\', \'\\x80\', \'\\x81\', \'\\x82\', \'\\x83\', \'\\x84\', \'\\x85\', \'\\x86\', \'\\x87\', \'\\x88\', \'\\x89\', \'\\x8a\', \'\\x8b\', \'\\x8c\', \'\\x8d\', \'\\x8e\', \'\\x8f\', \'\\x90\', \'\\x91\', \'\\x92\', \'\\x93\', \'\\x94\', \'\\x95\'], [\'lycka\'])")
            print("Korrekt svar: ['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', ' ', '!', '\"', '#', '$', '%', '&', \"'\", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '\x7f', '\x80', '\x81', '\x82', '\x83', '\x84', '\x85', '\x86', '\x87', '\x88', '\x89', '\x8a', '\x8b', '\x8c', '\x8d', '\x8e', '\x8f', '\x90', '\x91', '\x92', '\x93', '\x94', '\x95']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 210: Exception')
        print_exception()

    print('Startar test 3/211')
    try:
        res = without([0.0, 1.0, 2.0], ['lycka'])
        exp = [0.0, 1.0, 2.0]
        if res != exp:
            print("Fel i test 3/211: without([0.0, 1.0, 2.0], ['lycka'])")
            print("Korrekt svar: [0.0, 1.0, 2.0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 211: Exception')
        print_exception()

    print('Startar test 3/212')
    try:
        res = without([-25.0, -24.0, -23.0, -22.0, -21.0, -20.0, -19.0, -18.0, -17.0, -16.0, -15.0, -14.0, -13.0, -12.0, -11.0, -10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0], ['lycka'])
        exp = [-25.0, -24.0, -23.0, -22.0, -21.0, -20.0, -19.0, -18.0, -17.0, -16.0, -15.0, -14.0, -13.0, -12.0, -11.0, -10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0]
        if res != exp:
            print("Fel i test 3/212: without([-25.0, -24.0, -23.0, -22.0, -21.0, -20.0, -19.0, -18.0, -17.0, -16.0, -15.0, -14.0, -13.0, -12.0, -11.0, -10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0], ['lycka'])")
            print("Korrekt svar: [-25.0, -24.0, -23.0, -22.0, -21.0, -20.0, -19.0, -18.0, -17.0, -16.0, -15.0, -14.0, -13.0, -12.0, -11.0, -10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 212: Exception')
        print_exception()

    print('Startar test 3/213')
    try:
        res = without([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0, 33.5, 34.0, 34.5, 35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0, 42.5, 43.0, 43.5, 44.0, 44.5, 45.0, 45.5, 46.0, 46.5, 47.0, 47.5, 48.0, 48.5, 49.0, 49.5, 50.0, 50.5, 51.0, 51.5, 52.0, 52.5, 53.0, 53.5, 54.0, 54.5, 55.0, 55.5, 56.0, 56.5, 57.0, 57.5, 58.0, 58.5, 59.0, 59.5, 60.0, 60.5, 61.0, 61.5, 62.0, 62.5, 63.0, 63.5, 64.0, 64.5, 65.0, 65.5, 66.0, 66.5, 67.0, 67.5, 68.0, 68.5, 69.0, 69.5, 70.0, 70.5, 71.0, 71.5, 72.0, 72.5, 73.0, 73.5, 74.0, 74.5], ['lycka'])
        exp = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0, 33.5, 34.0, 34.5, 35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0, 42.5, 43.0, 43.5, 44.0, 44.5, 45.0, 45.5, 46.0, 46.5, 47.0, 47.5, 48.0, 48.5, 49.0, 49.5, 50.0, 50.5, 51.0, 51.5, 52.0, 52.5, 53.0, 53.5, 54.0, 54.5, 55.0, 55.5, 56.0, 56.5, 57.0, 57.5, 58.0, 58.5, 59.0, 59.5, 60.0, 60.5, 61.0, 61.5, 62.0, 62.5, 63.0, 63.5, 64.0, 64.5, 65.0, 65.5, 66.0, 66.5, 67.0, 67.5, 68.0, 68.5, 69.0, 69.5, 70.0, 70.5, 71.0, 71.5, 72.0, 72.5, 73.0, 73.5, 74.0, 74.5]
        if res != exp:
            print("Fel i test 3/213: without([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0, 33.5, 34.0, 34.5, 35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0, 42.5, 43.0, 43.5, 44.0, 44.5, 45.0, 45.5, 46.0, 46.5, 47.0, 47.5, 48.0, 48.5, 49.0, 49.5, 50.0, 50.5, 51.0, 51.5, 52.0, 52.5, 53.0, 53.5, 54.0, 54.5, 55.0, 55.5, 56.0, 56.5, 57.0, 57.5, 58.0, 58.5, 59.0, 59.5, 60.0, 60.5, 61.0, 61.5, 62.0, 62.5, 63.0, 63.5, 64.0, 64.5, 65.0, 65.5, 66.0, 66.5, 67.0, 67.5, 68.0, 68.5, 69.0, 69.5, 70.0, 70.5, 71.0, 71.5, 72.0, 72.5, 73.0, 73.5, 74.0, 74.5], ['lycka'])")
            print("Korrekt svar: [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0, 33.5, 34.0, 34.5, 35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0, 42.5, 43.0, 43.5, 44.0, 44.5, 45.0, 45.5, 46.0, 46.5, 47.0, 47.5, 48.0, 48.5, 49.0, 49.5, 50.0, 50.5, 51.0, 51.5, 52.0, 52.5, 53.0, 53.5, 54.0, 54.5, 55.0, 55.5, 56.0, 56.5, 57.0, 57.5, 58.0, 58.5, 59.0, 59.5, 60.0, 60.5, 61.0, 61.5, 62.0, 62.5, 63.0, 63.5, 64.0, 64.5, 65.0, 65.5, 66.0, 66.5, 67.0, 67.5, 68.0, 68.5, 69.0, 69.5, 70.0, 70.5, 71.0, 71.5, 72.0, 72.5, 73.0, 73.5, 74.0, 74.5]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 213: Exception')
        print_exception()

    print('Startar test 3/214')
    try:
        res = without([7.6, 7.7, 7, 7.0], ['lycka'])
        exp = [7.6, 7.7, 7, 7.0]
        if res != exp:
            print("Fel i test 3/214: without([7.6, 7.7, 7, 7.0], ['lycka'])")
            print("Korrekt svar: [7.6, 7.7, 7, 7.0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 214: Exception')
        print_exception()

    print('Startar test 3/215')
    try:
        res = without([1, 1.0, 1, 1.0, 1, 1, 1.0], ['lycka'])
        exp = [1, 1.0, 1, 1.0, 1, 1, 1.0]
        if res != exp:
            print("Fel i test 3/215: without([1, 1.0, 1, 1.0, 1, 1, 1.0], ['lycka'])")
            print("Korrekt svar: [1, 1.0, 1, 1.0, 1, 1, 1.0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 215: Exception')
        print_exception()

    print('Startar test 3/216')
    try:
        res = without(['0', 1.0, 2, '3', 4.0, 5, '6', 7.0, 8, '9', 10.0, 11, '12', 13.0, 14, '15', 16.0, 17, '18', 19.0, 20, '21', 22.0, 23, '24', 25.0, 26, '27', 28.0, 29, '30', 31.0, 32, '33', 34.0, 35, '36', 37.0, 38, '39', 40.0, 41, '42', 43.0, 44, '45', 46.0, 47, '48', 49.0, 50, '51', 52.0, 53, '54', 55.0, 56, '57', 58.0, 59, '60', 61.0, 62, '63', 64.0, 65, '66', 67.0, 68, '69', 70.0, 71, '72', 73.0, 74, '75', 76.0, 77, '78', 79.0, 80, '81', 82.0, 83, '84', 85.0, 86, '87', 88.0, 89, '90', 91.0, 92, '93', 94.0, 95, '96', 97.0, 98, '99', 100.0, 101, '102', 103.0, 104, '105', 106.0, 107, '108', 109.0, 110, '111', 112.0, 113, '114', 115.0, 116, '117', 118.0, 119, '120', 121.0, 122, '123', 124.0, 125, '126', 127.0, 128, '129', 130.0, 131, '132', 133.0, 134, '135', 136.0, 137, '138', 139.0, 140, '141', 142.0, 143, '144', 145.0, 146, '147', 148.0, 149], ['lycka'])
        exp = ['0', 1.0, 2, '3', 4.0, 5, '6', 7.0, 8, '9', 10.0, 11, '12', 13.0, 14, '15', 16.0, 17, '18', 19.0, 20, '21', 22.0, 23, '24', 25.0, 26, '27', 28.0, 29, '30', 31.0, 32, '33', 34.0, 35, '36', 37.0, 38, '39', 40.0, 41, '42', 43.0, 44, '45', 46.0, 47, '48', 49.0, 50, '51', 52.0, 53, '54', 55.0, 56, '57', 58.0, 59, '60', 61.0, 62, '63', 64.0, 65, '66', 67.0, 68, '69', 70.0, 71, '72', 73.0, 74, '75', 76.0, 77, '78', 79.0, 80, '81', 82.0, 83, '84', 85.0, 86, '87', 88.0, 89, '90', 91.0, 92, '93', 94.0, 95, '96', 97.0, 98, '99', 100.0, 101, '102', 103.0, 104, '105', 106.0, 107, '108', 109.0, 110, '111', 112.0, 113, '114', 115.0, 116, '117', 118.0, 119, '120', 121.0, 122, '123', 124.0, 125, '126', 127.0, 128, '129', 130.0, 131, '132', 133.0, 134, '135', 136.0, 137, '138', 139.0, 140, '141', 142.0, 143, '144', 145.0, 146, '147', 148.0, 149]
        if res != exp:
            print("Fel i test 3/216: without(['0', 1.0, 2, '3', 4.0, 5, '6', 7.0, 8, '9', 10.0, 11, '12', 13.0, 14, '15', 16.0, 17, '18', 19.0, 20, '21', 22.0, 23, '24', 25.0, 26, '27', 28.0, 29, '30', 31.0, 32, '33', 34.0, 35, '36', 37.0, 38, '39', 40.0, 41, '42', 43.0, 44, '45', 46.0, 47, '48', 49.0, 50, '51', 52.0, 53, '54', 55.0, 56, '57', 58.0, 59, '60', 61.0, 62, '63', 64.0, 65, '66', 67.0, 68, '69', 70.0, 71, '72', 73.0, 74, '75', 76.0, 77, '78', 79.0, 80, '81', 82.0, 83, '84', 85.0, 86, '87', 88.0, 89, '90', 91.0, 92, '93', 94.0, 95, '96', 97.0, 98, '99', 100.0, 101, '102', 103.0, 104, '105', 106.0, 107, '108', 109.0, 110, '111', 112.0, 113, '114', 115.0, 116, '117', 118.0, 119, '120', 121.0, 122, '123', 124.0, 125, '126', 127.0, 128, '129', 130.0, 131, '132', 133.0, 134, '135', 136.0, 137, '138', 139.0, 140, '141', 142.0, 143, '144', 145.0, 146, '147', 148.0, 149], ['lycka'])")
            print("Korrekt svar: ['0', 1.0, 2, '3', 4.0, 5, '6', 7.0, 8, '9', 10.0, 11, '12', 13.0, 14, '15', 16.0, 17, '18', 19.0, 20, '21', 22.0, 23, '24', 25.0, 26, '27', 28.0, 29, '30', 31.0, 32, '33', 34.0, 35, '36', 37.0, 38, '39', 40.0, 41, '42', 43.0, 44, '45', 46.0, 47, '48', 49.0, 50, '51', 52.0, 53, '54', 55.0, 56, '57', 58.0, 59, '60', 61.0, 62, '63', 64.0, 65, '66', 67.0, 68, '69', 70.0, 71, '72', 73.0, 74, '75', 76.0, 77, '78', 79.0, 80, '81', 82.0, 83, '84', 85.0, 86, '87', 88.0, 89, '90', 91.0, 92, '93', 94.0, 95, '96', 97.0, 98, '99', 100.0, 101, '102', 103.0, 104, '105', 106.0, 107, '108', 109.0, 110, '111', 112.0, 113, '114', 115.0, 116, '117', 118.0, 119, '120', 121.0, 122, '123', 124.0, 125, '126', 127.0, 128, '129', 130.0, 131, '132', 133.0, 134, '135', 136.0, 137, '138', 139.0, 140, '141', 142.0, 143, '144', 145.0, 146, '147', 148.0, 149]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 216: Exception')
        print_exception()

    print('Startar test 3/217')
    try:
        res = without(['1', 1, 2, '2', '3', '3', 4, 4], ['lycka'])
        exp = ['1', 1, 2, '2', '3', '3', 4, 4]
        if res != exp:
            print("Fel i test 3/217: without(['1', 1, 2, '2', '3', '3', 4, 4], ['lycka'])")
            print("Korrekt svar: ['1', 1, 2, '2', '3', '3', 4, 4]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 217: Exception')
        print_exception()

    print('Startar test 3/218')
    try:
        res = without([], ['lycka'])
        exp = []
        if res != exp:
            print("Fel i test 3/218: without([], ['lycka'])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 218: Exception')
        print_exception()

    print('Startar test 3/219')
    try:
        res = without([[[[]]]], ['lycka'])
        exp = [[[[]]]]
        if res != exp:
            print("Fel i test 3/219: without([[[[]]]], ['lycka'])")
            print("Korrekt svar: [[[[]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 219: Exception')
        print_exception()

    print('Startar test 3/220')
    try:
        res = without([[]], ['lycka'])
        exp = [[]]
        if res != exp:
            print("Fel i test 3/220: without([[]], ['lycka'])")
            print("Korrekt svar: [[]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 220: Exception')
        print_exception()

    print('Startar test 3/221')
    try:
        res = without([[], [[]]], ['lycka'])
        exp = [[], [[]]]
        if res != exp:
            print("Fel i test 3/221: without([[], [[]]], ['lycka'])")
            print("Korrekt svar: [[], [[]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 221: Exception')
        print_exception()

    print('Startar test 3/222')
    try:
        res = without([[[[[]]]], [], [[]]], ['lycka'])
        exp = [[[[[]]]], [], [[]]]
        if res != exp:
            print("Fel i test 3/222: without([[[[[]]]], [], [[]]], ['lycka'])")
            print("Korrekt svar: [[[[[]]]], [], [[]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 222: Exception')
        print_exception()

    print('Startar test 3/223')
    try:
        res = without([[[[5]]]], ['lycka'])
        exp = [[[[5]]]]
        if res != exp:
            print("Fel i test 3/223: without([[[[5]]]], ['lycka'])")
            print("Korrekt svar: [[[[5]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 223: Exception')
        print_exception()

    print('Startar test 3/224')
    try:
        res = without([[1], [2]], ['lycka'])
        exp = [[1], [2]]
        if res != exp:
            print("Fel i test 3/224: without([[1], [2]], ['lycka'])")
            print("Korrekt svar: [[1], [2]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 224: Exception')
        print_exception()

    print('Startar test 3/225')
    try:
        res = without([[1], [[2]], [[[3]]], [[[[4]]]]], ['lycka'])
        exp = [[1], [[2]], [[[3]]], [[[[4]]]]]
        if res != exp:
            print("Fel i test 3/225: without([[1], [[2]], [[[3]]], [[[[4]]]]], ['lycka'])")
            print("Korrekt svar: [[1], [[2]], [[[3]]], [[[[4]]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 225: Exception')
        print_exception()

    print('Startar test 3/226')
    try:
        res = without([[-1], [[[2]]], 33, [[[[78]]]], [[[-123]]]], ['lycka'])
        exp = [[-1], [[[2]]], 33, [[[[78]]]], [[[-123]]]]
        if res != exp:
            print("Fel i test 3/226: without([[-1], [[[2]]], 33, [[[[78]]]], [[[-123]]]], ['lycka'])")
            print("Korrekt svar: [[-1], [[[2]]], 33, [[[[78]]]], [[[-123]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 226: Exception')
        print_exception()

    print('Startar test 3/227')
    try:
        res = without([[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12], [0, 4, 8, 12, 16]], [[0, 0, 0, 0, 0], [0, 2, 4, 6, 8], [0, 4, 8, 12, 16], [0, 6, 12, 18, 24], [0, 8, 16, 24, 32]], [[0, 0, 0, 0, 0], [0, 3, 6, 9, 12], [0, 6, 12, 18, 24], [0, 9, 18, 27, 36], [0, 12, 24, 36, 48]], [[0, 0, 0, 0, 0], [0, 4, 8, 12, 16], [0, 8, 16, 24, 32], [0, 12, 24, 36, 48], [0, 16, 32, 48, 64]]], ['lycka'])
        exp = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12], [0, 4, 8, 12, 16]], [[0, 0, 0, 0, 0], [0, 2, 4, 6, 8], [0, 4, 8, 12, 16], [0, 6, 12, 18, 24], [0, 8, 16, 24, 32]], [[0, 0, 0, 0, 0], [0, 3, 6, 9, 12], [0, 6, 12, 18, 24], [0, 9, 18, 27, 36], [0, 12, 24, 36, 48]], [[0, 0, 0, 0, 0], [0, 4, 8, 12, 16], [0, 8, 16, 24, 32], [0, 12, 24, 36, 48], [0, 16, 32, 48, 64]]]
        if res != exp:
            print("Fel i test 3/227: without([[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12], [0, 4, 8, 12, 16]], [[0, 0, 0, 0, 0], [0, 2, 4, 6, 8], [0, 4, 8, 12, 16], [0, 6, 12, 18, 24], [0, 8, 16, 24, 32]], [[0, 0, 0, 0, 0], [0, 3, 6, 9, 12], [0, 6, 12, 18, 24], [0, 9, 18, 27, 36], [0, 12, 24, 36, 48]], [[0, 0, 0, 0, 0], [0, 4, 8, 12, 16], [0, 8, 16, 24, 32], [0, 12, 24, 36, 48], [0, 16, 32, 48, 64]]], ['lycka'])")
            print("Korrekt svar: [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12], [0, 4, 8, 12, 16]], [[0, 0, 0, 0, 0], [0, 2, 4, 6, 8], [0, 4, 8, 12, 16], [0, 6, 12, 18, 24], [0, 8, 16, 24, 32]], [[0, 0, 0, 0, 0], [0, 3, 6, 9, 12], [0, 6, 12, 18, 24], [0, 9, 18, 27, 36], [0, 12, 24, 36, 48]], [[0, 0, 0, 0, 0], [0, 4, 8, 12, 16], [0, 8, 16, 24, 32], [0, 12, 24, 36, 48], [0, 16, 32, 48, 64]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 227: Exception')
        print_exception()

    print('Startar test 3/228')
    try:
        res = without([[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, -1, -2, -3, -4], [0, -2, -4, -6, -8], [0, -3, -6, -9, -12], [0, -4, -8, -12, -16]], [[0, 0, 0, 0, 0], [0, -2, -4, -6, -8], [0, -4, -8, -12, -16], [0, -6, -12, -18, -24], [0, -8, -16, -24, -32]], [[0, 0, 0, 0, 0], [0, -3, -6, -9, -12], [0, -6, -12, -18, -24], [0, -9, -18, -27, -36], [0, -12, -24, -36, -48]], [[0, 0, 0, 0, 0], [0, -4, -8, -12, -16], [0, -8, -16, -24, -32], [0, -12, -24, -36, -48], [0, -16, -32, -48, -64]]], ['lycka'])
        exp = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, -1, -2, -3, -4], [0, -2, -4, -6, -8], [0, -3, -6, -9, -12], [0, -4, -8, -12, -16]], [[0, 0, 0, 0, 0], [0, -2, -4, -6, -8], [0, -4, -8, -12, -16], [0, -6, -12, -18, -24], [0, -8, -16, -24, -32]], [[0, 0, 0, 0, 0], [0, -3, -6, -9, -12], [0, -6, -12, -18, -24], [0, -9, -18, -27, -36], [0, -12, -24, -36, -48]], [[0, 0, 0, 0, 0], [0, -4, -8, -12, -16], [0, -8, -16, -24, -32], [0, -12, -24, -36, -48], [0, -16, -32, -48, -64]]]
        if res != exp:
            print("Fel i test 3/228: without([[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, -1, -2, -3, -4], [0, -2, -4, -6, -8], [0, -3, -6, -9, -12], [0, -4, -8, -12, -16]], [[0, 0, 0, 0, 0], [0, -2, -4, -6, -8], [0, -4, -8, -12, -16], [0, -6, -12, -18, -24], [0, -8, -16, -24, -32]], [[0, 0, 0, 0, 0], [0, -3, -6, -9, -12], [0, -6, -12, -18, -24], [0, -9, -18, -27, -36], [0, -12, -24, -36, -48]], [[0, 0, 0, 0, 0], [0, -4, -8, -12, -16], [0, -8, -16, -24, -32], [0, -12, -24, -36, -48], [0, -16, -32, -48, -64]]], ['lycka'])")
            print("Korrekt svar: [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, -1, -2, -3, -4], [0, -2, -4, -6, -8], [0, -3, -6, -9, -12], [0, -4, -8, -12, -16]], [[0, 0, 0, 0, 0], [0, -2, -4, -6, -8], [0, -4, -8, -12, -16], [0, -6, -12, -18, -24], [0, -8, -16, -24, -32]], [[0, 0, 0, 0, 0], [0, -3, -6, -9, -12], [0, -6, -12, -18, -24], [0, -9, -18, -27, -36], [0, -12, -24, -36, -48]], [[0, 0, 0, 0, 0], [0, -4, -8, -12, -16], [0, -8, -16, -24, -32], [0, -12, -24, -36, -48], [0, -16, -32, -48, -64]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 228: Exception')
        print_exception()

    print('Startar test 3/229')
    try:
        res = without([[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]], ['lycka'])
        exp = [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]]
        if res != exp:
            print("Fel i test 3/229: without([[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]], ['lycka'])")
            print("Korrekt svar: [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 229: Exception')
        print_exception()

    print('Startar test 3/230')
    try:
        res = without([[], [[0]], [[0], [1], [0], [1]], [[0], [1], [2], [0], [1], [2], [0], [1], [2]], [[0], [1], [2], [3], [0], [1], [2], [3], [0], [1], [2], [3], [0], [1], [2], [3]], [[0], [1], [2], [3], [4], [0], [1], [2], [3], [4], [0], [1], [2], [3], [4], [0], [1], [2], [3], [4], [0], [1], [2], [3], [4]], [[0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5]], [[0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6]], [[0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7]], [[0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8]]], ['lycka'])
        exp = [[], [[0]], [[0], [1], [0], [1]], [[0], [1], [2], [0], [1], [2], [0], [1], [2]], [[0], [1], [2], [3], [0], [1], [2], [3], [0], [1], [2], [3], [0], [1], [2], [3]], [[0], [1], [2], [3], [4], [0], [1], [2], [3], [4], [0], [1], [2], [3], [4], [0], [1], [2], [3], [4], [0], [1], [2], [3], [4]], [[0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5]], [[0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6]], [[0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7]], [[0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8]]]
        if res != exp:
            print("Fel i test 3/230: without([[], [[0]], [[0], [1], [0], [1]], [[0], [1], [2], [0], [1], [2], [0], [1], [2]], [[0], [1], [2], [3], [0], [1], [2], [3], [0], [1], [2], [3], [0], [1], [2], [3]], [[0], [1], [2], [3], [4], [0], [1], [2], [3], [4], [0], [1], [2], [3], [4], [0], [1], [2], [3], [4], [0], [1], [2], [3], [4]], [[0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5]], [[0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6]], [[0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7]], [[0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8]]], ['lycka'])")
            print("Korrekt svar: [[], [[0]], [[0], [1], [0], [1]], [[0], [1], [2], [0], [1], [2], [0], [1], [2]], [[0], [1], [2], [3], [0], [1], [2], [3], [0], [1], [2], [3], [0], [1], [2], [3]], [[0], [1], [2], [3], [4], [0], [1], [2], [3], [4], [0], [1], [2], [3], [4], [0], [1], [2], [3], [4], [0], [1], [2], [3], [4]], [[0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5]], [[0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6]], [[0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7]], [[0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 230: Exception')
        print_exception()

    print('Startar test 3/231')
    try:
        res = without([tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple()], ['lycka'])
        exp = [tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple()]
        if res != exp:
            print("Fel i test 3/231: without([tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple(), tuple()], ['lycka'])")
            print("Korrekt svar: [(), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ()]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 231: Exception')
        print_exception()

    print('Startar test 3/232')
    try:
        res = without([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)], ['lycka'])
        exp = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        if res != exp:
            print("Fel i test 3/232: without([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)], ['lycka'])")
            print("Korrekt svar: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 232: Exception')
        print_exception()

    print('Startar test 3/233')
    try:
        res = without([[1, 2, 3], '123'], ['lycka'])
        exp = [[1, 2, 3], '123']
        if res != exp:
            print("Fel i test 3/233: without([[1, 2, 3], '123'], ['lycka'])")
            print("Korrekt svar: [[1, 2, 3], '123']")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 233: Exception')
        print_exception()

    print('Startar test 3/234')
    try:
        res = without([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399], ['lycka'])
        exp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399]
        if res != exp:
            print("Fel i test 3/234: without([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399], ['lycka'])")
            print("Korrekt svar: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 234: Exception')
        print_exception()

    print('Startar test 3/235')
    try:
        res = without([-400, -399, -398, -397, -396, -395, -394, -393, -392, -391, -390, -389, -388, -387, -386, -385, -384, -383, -382, -381, -380, -379, -378, -377, -376, -375, -374, -373, -372, -371, -370, -369, -368, -367, -366, -365, -364, -363, -362, -361, -360, -359, -358, -357, -356, -355, -354, -353, -352, -351, -350, -349, -348, -347, -346, -345, -344, -343, -342, -341, -340, -339, -338, -337, -336, -335, -334, -333, -332, -331, -330, -329, -328, -327, -326, -325, -324, -323, -322, -321, -320, -319, -318, -317, -316, -315, -314, -313, -312, -311, -310, -309, -308, -307, -306, -305, -304, -303, -302, -301, -300, -299, -298, -297, -296, -295, -294, -293, -292, -291, -290, -289, -288, -287, -286, -285, -284, -283, -282, -281, -280, -279, -278, -277, -276, -275, -274, -273, -272, -271, -270, -269, -268, -267, -266, -265, -264, -263, -262, -261, -260, -259, -258, -257, -256, -255, -254, -253, -252, -251, -250, -249, -248, -247, -246, -245, -244, -243, -242, -241, -240, -239, -238, -237, -236, -235, -234, -233, -232, -231, -230, -229, -228, -227, -226, -225, -224, -223, -222, -221, -220, -219, -218, -217, -216, -215, -214, -213, -212, -211, -210, -209, -208, -207, -206, -205, -204, -203, -202, -201, -200, -199, -198, -197, -196, -195, -194, -193, -192, -191, -190, -189, -188, -187, -186, -185, -184, -183, -182, -181, -180, -179, -178, -177, -176, -175, -174, -173, -172, -171, -170, -169, -168, -167, -166, -165, -164, -163, -162, -161, -160, -159, -158, -157, -156, -155, -154, -153, -152, -151, -150, -149, -148, -147, -146, -145, -144, -143, -142, -141, -140, -139, -138, -137, -136, -135, -134, -133, -132, -131, -130, -129, -128, -127, -126, -125, -124, -123, -122, -121, -120, -119, -118, -117, -116, -115, -114, -113, -112, -111, -110, -109, -108, -107, -106, -105, -104, -103, -102, -101, -100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399], ['lycka'])
        exp = [-400, -399, -398, -397, -396, -395, -394, -393, -392, -391, -390, -389, -388, -387, -386, -385, -384, -383, -382, -381, -380, -379, -378, -377, -376, -375, -374, -373, -372, -371, -370, -369, -368, -367, -366, -365, -364, -363, -362, -361, -360, -359, -358, -357, -356, -355, -354, -353, -352, -351, -350, -349, -348, -347, -346, -345, -344, -343, -342, -341, -340, -339, -338, -337, -336, -335, -334, -333, -332, -331, -330, -329, -328, -327, -326, -325, -324, -323, -322, -321, -320, -319, -318, -317, -316, -315, -314, -313, -312, -311, -310, -309, -308, -307, -306, -305, -304, -303, -302, -301, -300, -299, -298, -297, -296, -295, -294, -293, -292, -291, -290, -289, -288, -287, -286, -285, -284, -283, -282, -281, -280, -279, -278, -277, -276, -275, -274, -273, -272, -271, -270, -269, -268, -267, -266, -265, -264, -263, -262, -261, -260, -259, -258, -257, -256, -255, -254, -253, -252, -251, -250, -249, -248, -247, -246, -245, -244, -243, -242, -241, -240, -239, -238, -237, -236, -235, -234, -233, -232, -231, -230, -229, -228, -227, -226, -225, -224, -223, -222, -221, -220, -219, -218, -217, -216, -215, -214, -213, -212, -211, -210, -209, -208, -207, -206, -205, -204, -203, -202, -201, -200, -199, -198, -197, -196, -195, -194, -193, -192, -191, -190, -189, -188, -187, -186, -185, -184, -183, -182, -181, -180, -179, -178, -177, -176, -175, -174, -173, -172, -171, -170, -169, -168, -167, -166, -165, -164, -163, -162, -161, -160, -159, -158, -157, -156, -155, -154, -153, -152, -151, -150, -149, -148, -147, -146, -145, -144, -143, -142, -141, -140, -139, -138, -137, -136, -135, -134, -133, -132, -131, -130, -129, -128, -127, -126, -125, -124, -123, -122, -121, -120, -119, -118, -117, -116, -115, -114, -113, -112, -111, -110, -109, -108, -107, -106, -105, -104, -103, -102, -101, -100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399]
        if res != exp:
            print("Fel i test 3/235: without([-400, -399, -398, -397, -396, -395, -394, -393, -392, -391, -390, -389, -388, -387, -386, -385, -384, -383, -382, -381, -380, -379, -378, -377, -376, -375, -374, -373, -372, -371, -370, -369, -368, -367, -366, -365, -364, -363, -362, -361, -360, -359, -358, -357, -356, -355, -354, -353, -352, -351, -350, -349, -348, -347, -346, -345, -344, -343, -342, -341, -340, -339, -338, -337, -336, -335, -334, -333, -332, -331, -330, -329, -328, -327, -326, -325, -324, -323, -322, -321, -320, -319, -318, -317, -316, -315, -314, -313, -312, -311, -310, -309, -308, -307, -306, -305, -304, -303, -302, -301, -300, -299, -298, -297, -296, -295, -294, -293, -292, -291, -290, -289, -288, -287, -286, -285, -284, -283, -282, -281, -280, -279, -278, -277, -276, -275, -274, -273, -272, -271, -270, -269, -268, -267, -266, -265, -264, -263, -262, -261, -260, -259, -258, -257, -256, -255, -254, -253, -252, -251, -250, -249, -248, -247, -246, -245, -244, -243, -242, -241, -240, -239, -238, -237, -236, -235, -234, -233, -232, -231, -230, -229, -228, -227, -226, -225, -224, -223, -222, -221, -220, -219, -218, -217, -216, -215, -214, -213, -212, -211, -210, -209, -208, -207, -206, -205, -204, -203, -202, -201, -200, -199, -198, -197, -196, -195, -194, -193, -192, -191, -190, -189, -188, -187, -186, -185, -184, -183, -182, -181, -180, -179, -178, -177, -176, -175, -174, -173, -172, -171, -170, -169, -168, -167, -166, -165, -164, -163, -162, -161, -160, -159, -158, -157, -156, -155, -154, -153, -152, -151, -150, -149, -148, -147, -146, -145, -144, -143, -142, -141, -140, -139, -138, -137, -136, -135, -134, -133, -132, -131, -130, -129, -128, -127, -126, -125, -124, -123, -122, -121, -120, -119, -118, -117, -116, -115, -114, -113, -112, -111, -110, -109, -108, -107, -106, -105, -104, -103, -102, -101, -100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399], ['lycka'])")
            print("Korrekt svar: [-400, -399, -398, -397, -396, -395, -394, -393, -392, -391, -390, -389, -388, -387, -386, -385, -384, -383, -382, -381, -380, -379, -378, -377, -376, -375, -374, -373, -372, -371, -370, -369, -368, -367, -366, -365, -364, -363, -362, -361, -360, -359, -358, -357, -356, -355, -354, -353, -352, -351, -350, -349, -348, -347, -346, -345, -344, -343, -342, -341, -340, -339, -338, -337, -336, -335, -334, -333, -332, -331, -330, -329, -328, -327, -326, -325, -324, -323, -322, -321, -320, -319, -318, -317, -316, -315, -314, -313, -312, -311, -310, -309, -308, -307, -306, -305, -304, -303, -302, -301, -300, -299, -298, -297, -296, -295, -294, -293, -292, -291, -290, -289, -288, -287, -286, -285, -284, -283, -282, -281, -280, -279, -278, -277, -276, -275, -274, -273, -272, -271, -270, -269, -268, -267, -266, -265, -264, -263, -262, -261, -260, -259, -258, -257, -256, -255, -254, -253, -252, -251, -250, -249, -248, -247, -246, -245, -244, -243, -242, -241, -240, -239, -238, -237, -236, -235, -234, -233, -232, -231, -230, -229, -228, -227, -226, -225, -224, -223, -222, -221, -220, -219, -218, -217, -216, -215, -214, -213, -212, -211, -210, -209, -208, -207, -206, -205, -204, -203, -202, -201, -200, -199, -198, -197, -196, -195, -194, -193, -192, -191, -190, -189, -188, -187, -186, -185, -184, -183, -182, -181, -180, -179, -178, -177, -176, -175, -174, -173, -172, -171, -170, -169, -168, -167, -166, -165, -164, -163, -162, -161, -160, -159, -158, -157, -156, -155, -154, -153, -152, -151, -150, -149, -148, -147, -146, -145, -144, -143, -142, -141, -140, -139, -138, -137, -136, -135, -134, -133, -132, -131, -130, -129, -128, -127, -126, -125, -124, -123, -122, -121, -120, -119, -118, -117, -116, -115, -114, -113, -112, -111, -110, -109, -108, -107, -106, -105, -104, -103, -102, -101, -100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 235: Exception')
        print_exception()

    print('Startar test 3/236')
    try:
        res = without([2, 2.0, 3, 3.0, 3, 5, 3.0], ['lycka'])
        exp = [2, 2.0, 3, 3.0, 3, 5, 3.0]
        if res != exp:
            print("Fel i test 3/236: without([2, 2.0, 3, 3.0, 3, 5, 3.0], ['lycka'])")
            print("Korrekt svar: [2, 2.0, 3, 3.0, 3, 5, 3.0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 236: Exception')
        print_exception()

    print('Startar test 3/237')
    try:
        res = without([2, 2.0, 3, [3.0, 3, 5], 3.0], ['lycka'])
        exp = [2, 2.0, 3, [3.0, 3, 5], 3.0]
        if res != exp:
            print("Fel i test 3/237: without([2, 2.0, 3, [3.0, 3, 5], 3.0], ['lycka'])")
            print("Korrekt svar: [2, 2.0, 3, [3.0, 3, 5], 3.0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 237: Exception')
        print_exception()

    print('Startar test 3/238')
    try:
        res = without([2, 2.5, [14, 8.5]], ['lycka'])
        exp = [2, 2.5, [14, 8.5]]
        if res != exp:
            print("Fel i test 3/238: without([2, 2.5, [14, 8.5]], ['lycka'])")
            print("Korrekt svar: [2, 2.5, [14, 8.5]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 238: Exception')
        print_exception()

    print('Startar test 3/239')
    try:
        res = without([2, 2.5, [14, 8]], ['lycka'])
        exp = [2, 2.5, [14, 8]]
        if res != exp:
            print("Fel i test 3/239: without([2, 2.5, [14, 8]], ['lycka'])")
            print("Korrekt svar: [2, 2.5, [14, 8]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 239: Exception')
        print_exception()

    print('Startar test 3/240')
    try:
        res = without([2, 2, [14, 8.5]], ['lycka'])
        exp = [2, 2, [14, 8.5]]
        if res != exp:
            print("Fel i test 3/240: without([2, 2, [14, 8.5]], ['lycka'])")
            print("Korrekt svar: [2, 2, [14, 8.5]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 240: Exception')
        print_exception()

    print('Startar test 3/241')
    try:
        res = without([2, 2, 14, 8.5], ['lycka'])
        exp = [2, 2, 14, 8.5]
        if res != exp:
            print("Fel i test 3/241: without([2, 2, 14, 8.5], ['lycka'])")
            print("Korrekt svar: [2, 2, 14, 8.5]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 241: Exception')
        print_exception()

    print('Startar test 3/242')
    try:
        res = without([2, 4.0, [14, 12.0]], ['lycka'])
        exp = [2, 4.0, [14, 12.0]]
        if res != exp:
            print("Fel i test 3/242: without([2, 4.0, [14, 12.0]], ['lycka'])")
            print("Korrekt svar: [2, 4.0, [14, 12.0]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 242: Exception')
        print_exception()

    print('Startar test 3/243')
    try:
        res = without([2, 4.0, [14, 12]], ['lycka'])
        exp = [2, 4.0, [14, 12]]
        if res != exp:
            print("Fel i test 3/243: without([2, 4.0, [14, 12]], ['lycka'])")
            print("Korrekt svar: [2, 4.0, [14, 12]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 243: Exception')
        print_exception()

    print('Startar test 3/244')
    try:
        res = without([2, 4, [14, 12.0]], ['lycka'])
        exp = [2, 4, [14, 12.0]]
        if res != exp:
            print("Fel i test 3/244: without([2, 4, [14, 12.0]], ['lycka'])")
            print("Korrekt svar: [2, 4, [14, 12.0]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 244: Exception')
        print_exception()

    print('Startar test 3/245')
    try:
        res = without([2, 4, 14, 12.0], ['lycka'])
        exp = [2, 4, 14, 12.0]
        if res != exp:
            print("Fel i test 3/245: without([2, 4, 14, 12.0], ['lycka'])")
            print("Korrekt svar: [2, 4, 14, 12.0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 245: Exception')
        print_exception()

    print('Startar test 3/246')
    try:
        res = without([2, 5.0, [14, 11.0]], ['lycka'])
        exp = [2, 5.0, [14, 11.0]]
        if res != exp:
            print("Fel i test 3/246: without([2, 5.0, [14, 11.0]], ['lycka'])")
            print("Korrekt svar: [2, 5.0, [14, 11.0]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 246: Exception')
        print_exception()

    print('Startar test 3/247')
    try:
        res = without([2, 5.0, [14, 11]], ['lycka'])
        exp = [2, 5.0, [14, 11]]
        if res != exp:
            print("Fel i test 3/247: without([2, 5.0, [14, 11]], ['lycka'])")
            print("Korrekt svar: [2, 5.0, [14, 11]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 247: Exception')
        print_exception()

    print('Startar test 3/248')
    try:
        res = without([2, 4, [14, 11.0]], ['lycka'])
        exp = [2, 4, [14, 11.0]]
        if res != exp:
            print("Fel i test 3/248: without([2, 4, [14, 11.0]], ['lycka'])")
            print("Korrekt svar: [2, 4, [14, 11.0]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 248: Exception')
        print_exception()

    print('Startar test 3/249')
    try:
        res = without([2, 4, 14, 11.0], ['lycka'])
        exp = [2, 4, 14, 11.0]
        if res != exp:
            print("Fel i test 3/249: without([2, 4, 14, 11.0], ['lycka'])")
            print("Korrekt svar: [2, 4, 14, 11.0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 249: Exception')
        print_exception()

    print('Startar test 3/250')
    try:
        res = without([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3], ['lycka'])
        exp = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
        if res != exp:
            print("Fel i test 3/250: without([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3], ['lycka'])")
            print("Korrekt svar: [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 250: Exception')
        print_exception()

    print('Startar test 3/251')
    try:
        res = without([0, 5, 5, 0], ['lycka'])
        exp = [0, 5, 5, 0]
        if res != exp:
            print("Fel i test 3/251: without([0, 5, 5, 0], ['lycka'])")
            print("Korrekt svar: [0, 5, 5, 0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 251: Exception')
        print_exception()

    print('Startar test 3/252')
    try:
        res = without([0, 5, 5, 5, 0], ['lycka'])
        exp = [0, 5, 5, 5, 0]
        if res != exp:
            print("Fel i test 3/252: without([0, 5, 5, 5, 0], ['lycka'])")
            print("Korrekt svar: [0, 5, 5, 5, 0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 252: Exception')
        print_exception()

    print('Startar test 3/253')
    try:
        res = without([0, 5, 5, 5, 0, 5, 5, 0], ['lycka'])
        exp = [0, 5, 5, 5, 0, 5, 5, 0]
        if res != exp:
            print("Fel i test 3/253: without([0, 5, 5, 5, 0, 5, 5, 0], ['lycka'])")
            print("Korrekt svar: [0, 5, 5, 5, 0, 5, 5, 0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 253: Exception')
        print_exception()

    print('Startar test 3/254')
    try:
        res = without([5, 5, 0, 5, 5, 0], ['lycka'])
        exp = [5, 5, 0, 5, 5, 0]
        if res != exp:
            print("Fel i test 3/254: without([5, 5, 0, 5, 5, 0], ['lycka'])")
            print("Korrekt svar: [5, 5, 0, 5, 5, 0]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 254: Exception')
        print_exception()

    print('Startar test 3/255')
    try:
        res = without([0, 5, 5, 0, 5, 5, 5], ['lycka'])
        exp = [0, 5, 5, 0, 5, 5, 5]
        if res != exp:
            print("Fel i test 3/255: without([0, 5, 5, 0, 5, 5, 5], ['lycka'])")
            print("Korrekt svar: [0, 5, 5, 0, 5, 5, 5]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 255: Exception')
        print_exception()

    print('Startar test 3/256')
    try:
        res = without([[0, 5, 5, 0]], ['lycka'])
        exp = [[0, 5, 5, 0]]
        if res != exp:
            print("Fel i test 3/256: without([[0, 5, 5, 0]], ['lycka'])")
            print("Korrekt svar: [[0, 5, 5, 0]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 256: Exception')
        print_exception()

    print('Startar test 3/257')
    try:
        res = without([[0, 5, 5, 5, 0]], ['lycka'])
        exp = [[0, 5, 5, 5, 0]]
        if res != exp:
            print("Fel i test 3/257: without([[0, 5, 5, 5, 0]], ['lycka'])")
            print("Korrekt svar: [[0, 5, 5, 5, 0]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 257: Exception')
        print_exception()

    print('Startar test 3/258')
    try:
        res = without([[0, 5, 5, 5, 0, 5, 5, 0]], ['lycka'])
        exp = [[0, 5, 5, 5, 0, 5, 5, 0]]
        if res != exp:
            print("Fel i test 3/258: without([[0, 5, 5, 5, 0, 5, 5, 0]], ['lycka'])")
            print("Korrekt svar: [[0, 5, 5, 5, 0, 5, 5, 0]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 258: Exception')
        print_exception()

    print('Startar test 3/259')
    try:
        res = without([[5, 5, 0, 5, 5, 0]], ['lycka'])
        exp = [[5, 5, 0, 5, 5, 0]]
        if res != exp:
            print("Fel i test 3/259: without([[5, 5, 0, 5, 5, 0]], ['lycka'])")
            print("Korrekt svar: [[5, 5, 0, 5, 5, 0]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 259: Exception')
        print_exception()

    print('Startar test 3/260')
    try:
        res = without([[0, 5, 5, 0, 5, 5, 5]], ['lycka'])
        exp = [[0, 5, 5, 0, 5, 5, 5]]
        if res != exp:
            print("Fel i test 3/260: without([[0, 5, 5, 0, 5, 5, 5]], ['lycka'])")
            print("Korrekt svar: [[0, 5, 5, 0, 5, 5, 5]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 260: Exception')
        print_exception()

    print('Startar test 3/261')
    try:
        res = without([1, 2, 3], [])
        exp = [1, 2, 3]
        if res != exp:
            print("Fel i test 3/261: without([1, 2, 3], [])")
            print("Korrekt svar: [1, 2, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 261: Exception')
        print_exception()

    print('Startar test 3/262')
    try:
        res = without([1, 2, 3], [1])
        exp = [2, 3]
        if res != exp:
            print("Fel i test 3/262: without([1, 2, 3], [1])")
            print("Korrekt svar: [2, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 262: Exception')
        print_exception()

    print('Startar test 3/263')
    try:
        res = without([1, 2, 3], [2])
        exp = [1, 3]
        if res != exp:
            print("Fel i test 3/263: without([1, 2, 3], [2])")
            print("Korrekt svar: [1, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 263: Exception')
        print_exception()

    print('Startar test 3/264')
    try:
        res = without([1, 2, 3], [3])
        exp = [1, 2]
        if res != exp:
            print("Fel i test 3/264: without([1, 2, 3], [3])")
            print("Korrekt svar: [1, 2]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 264: Exception')
        print_exception()

    print('Startar test 3/265')
    try:
        res = without([1, 2, 3], [1, 2, 3])
        exp = []
        if res != exp:
            print("Fel i test 3/265: without([1, 2, 3], [1, 2, 3])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 265: Exception')
        print_exception()

    print('Startar test 3/266')
    try:
        res = without([], [])
        exp = []
        if res != exp:
            print("Fel i test 3/266: without([], [])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 266: Exception')
        print_exception()

    print('Startar test 3/267')
    try:
        res = without([], [1])
        exp = []
        if res != exp:
            print("Fel i test 3/267: without([], [1])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 267: Exception')
        print_exception()

    print('Startar test 3/268')
    try:
        res = without([[1], 2, 3], [1, 2, 3])
        exp = [[]]
        if res != exp:
            print("Fel i test 3/268: without([[1], 2, 3], [1, 2, 3])")
            print("Korrekt svar: [[]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 268: Exception')
        print_exception()

    print('Startar test 3/269')
    try:
        res = without([1, [2], 3], [1, 2, 3])
        exp = [[]]
        if res != exp:
            print("Fel i test 3/269: without([1, [2], 3], [1, 2, 3])")
            print("Korrekt svar: [[]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 269: Exception')
        print_exception()

    print('Startar test 3/270')
    try:
        res = without([1, 2, [3]], [1, 2, 3])
        exp = [[]]
        if res != exp:
            print("Fel i test 3/270: without([1, 2, [3]], [1, 2, 3])")
            print("Korrekt svar: [[]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 270: Exception')
        print_exception()


    print('Klar med tester fÃ¶r uppgift 3')
    print()


# noinspection PyBroadException
def test_4a():
    print('PÃ¥bÃ¶rjar tester fÃ¶r uppgift 4a')

    print('Startar test 4a/1')
    try:
        res = split_at([2, 3, 4, 2, 5], is_two)
        exp = [[], [3, 4], [5]]
        if res != exp:
            print("Fel i test 4a/1: split_at([2, 3, 4, 2, 5], is_two)")
            print("Korrekt svar: [[], [3, 4], [5]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 1: Exception')
        print_exception()

    print('Startar test 4a/2')
    try:
        res = split_at([1, 2, 3, 4, 2], is_two)
        exp = [[1], [3, 4], []]
        if res != exp:
            print("Fel i test 4a/2: split_at([1, 2, 3, 4, 2], is_two)")
            print("Korrekt svar: [[1], [3, 4], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2: Exception')
        print_exception()

    print('Startar test 4a/3')
    try:
        res = split_at([1, 2, 2, 3, 4, 2, 5], is_two)
        exp = [[1], [], [3, 4], [5]]
        if res != exp:
            print("Fel i test 4a/3: split_at([1, 2, 2, 3, 4, 2, 5], is_two)")
            print("Korrekt svar: [[1], [], [3, 4], [5]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3: Exception')
        print_exception()

    print('Startar test 4a/4')
    try:
        res = split_at('abcdeba', is_b)
        exp = [['a'], ['c', 'd', 'e'], ['a']]
        if res != exp:
            print("Fel i test 4a/4: split_at('abcdeba', is_b)")
            print("Korrekt svar: [['a'], ['c', 'd', 'e'], ['a']]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4: Exception')
        print_exception()

    print('Startar test 4a/5')
    try:
        res = split_at([1, 2, 3, 4, 5], is_even)
        exp = [[1], [3], [5]]
        if res != exp:
            print("Fel i test 4a/5: split_at([1, 2, 3, 4, 5], is_even)")
            print("Korrekt svar: [[1], [3], [5]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5: Exception')
        print_exception()

    print('Startar test 4a/6')
    try:
        res = split_at([1, 2, 3], is_four)
        exp = [[1, 2, 3]]
        if res != exp:
            print("Fel i test 4a/6: split_at([1, 2, 3], is_four)")
            print("Korrekt svar: [[1, 2, 3]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 6: Exception')
        print_exception()

    print('Startar test 4a/7')
    try:
        res = split_at([1, 2, 3, [4, 5]], is_four)
        exp = [[1, 2, 3, [4, 5]]]
        if res != exp:
            print("Fel i test 4a/7: split_at([1, 2, 3, [4, 5]], is_four)")
            print("Korrekt svar: [[1, 2, 3, [4, 5]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 7: Exception')
        print_exception()

    print('Startar test 4a/8')
    try:
        res = split_at([1, 2, [3, [4, 5]]], is_two)
        exp = [[1], [[3, [4, 5]]]]
        if res != exp:
            print("Fel i test 4a/8: split_at([1, 2, [3, [4, 5]]], is_two)")
            print("Korrekt svar: [[1], [[3, [4, 5]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 8: Exception')
        print_exception()

    print('Startar test 4a/9')
    try:
        res = split_at([], always_false)
        exp = [[]]
        if res != exp:
            print("Fel i test 4a/9: split_at([], always_false)")
            print("Korrekt svar: [[]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 9: Exception')
        print_exception()

    print('Startar test 4a/10')
    try:
        res = split_at([42], always_false)
        exp = [[42]]
        if res != exp:
            print("Fel i test 4a/10: split_at([42], always_false)")
            print("Korrekt svar: [[42]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 10: Exception')
        print_exception()

    print('Startar test 4a/11')
    try:
        res = split_at([42, 42], always_false)
        exp = [[42, 42]]
        if res != exp:
            print("Fel i test 4a/11: split_at([42, 42], always_false)")
            print("Korrekt svar: [[42, 42]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 11: Exception')
        print_exception()

    print('Startar test 4a/12')
    try:
        res = split_at([42, 42, 42], always_false)
        exp = [[42, 42, 42]]
        if res != exp:
            print("Fel i test 4a/12: split_at([42, 42, 42], always_false)")
            print("Korrekt svar: [[42, 42, 42]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 12: Exception')
        print_exception()

    print('Startar test 4a/13')
    try:
        res = split_at([0], is_zero)
        exp = [[], []]
        if res != exp:
            print("Fel i test 4a/13: split_at([0], is_zero)")
            print("Korrekt svar: [[], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 13: Exception')
        print_exception()

    print('Startar test 4a/14')
    try:
        res = split_at([0, 1], is_zero)
        exp = [[], [1]]
        if res != exp:
            print("Fel i test 4a/14: split_at([0, 1], is_zero)")
            print("Korrekt svar: [[], [1]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 14: Exception')
        print_exception()

    print('Startar test 4a/15')
    try:
        res = split_at([1, 0], is_zero)
        exp = [[1], []]
        if res != exp:
            print("Fel i test 4a/15: split_at([1, 0], is_zero)")
            print("Korrekt svar: [[1], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 15: Exception')
        print_exception()

    print('Startar test 4a/16')
    try:
        res = split_at([0, 1, 1], is_zero)
        exp = [[], [1, 1]]
        if res != exp:
            print("Fel i test 4a/16: split_at([0, 1, 1], is_zero)")
            print("Korrekt svar: [[], [1, 1]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 16: Exception')
        print_exception()

    print('Startar test 4a/17')
    try:
        res = split_at([1, 0, 1], is_zero)
        exp = [[1], [1]]
        if res != exp:
            print("Fel i test 4a/17: split_at([1, 0, 1], is_zero)")
            print("Korrekt svar: [[1], [1]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 17: Exception')
        print_exception()

    print('Startar test 4a/18')
    try:
        res = split_at([1, 1, 0], is_zero)
        exp = [[1, 1], []]
        if res != exp:
            print("Fel i test 4a/18: split_at([1, 1, 0], is_zero)")
            print("Korrekt svar: [[1, 1], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 18: Exception')
        print_exception()

    print('Startar test 4a/19')
    try:
        res = split_at([0, 1, 1, 1], is_zero)
        exp = [[], [1, 1, 1]]
        if res != exp:
            print("Fel i test 4a/19: split_at([0, 1, 1, 1], is_zero)")
            print("Korrekt svar: [[], [1, 1, 1]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 19: Exception')
        print_exception()

    print('Startar test 4a/20')
    try:
        res = split_at([1, 0, 1, 1], is_zero)
        exp = [[1], [1, 1]]
        if res != exp:
            print("Fel i test 4a/20: split_at([1, 0, 1, 1], is_zero)")
            print("Korrekt svar: [[1], [1, 1]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 20: Exception')
        print_exception()

    print('Startar test 4a/21')
    try:
        res = split_at([1, 1, 0, 1], is_zero)
        exp = [[1, 1], [1]]
        if res != exp:
            print("Fel i test 4a/21: split_at([1, 1, 0, 1], is_zero)")
            print("Korrekt svar: [[1, 1], [1]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 21: Exception')
        print_exception()

    print('Startar test 4a/22')
    try:
        res = split_at([1, 1, 1, 0], is_zero)
        exp = [[1, 1, 1], []]
        if res != exp:
            print("Fel i test 4a/22: split_at([1, 1, 1, 0], is_zero)")
            print("Korrekt svar: [[1, 1, 1], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 22: Exception')
        print_exception()

    print('Startar test 4a/23')
    try:
        res = split_at([0, 0], is_zero)
        exp = [[], [], []]
        if res != exp:
            print("Fel i test 4a/23: split_at([0, 0], is_zero)")
            print("Korrekt svar: [[], [], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 23: Exception')
        print_exception()

    print('Startar test 4a/24')
    try:
        res = split_at([0, 0, 0], is_zero)
        exp = [[], [], [], []]
        if res != exp:
            print("Fel i test 4a/24: split_at([0, 0, 0], is_zero)")
            print("Korrekt svar: [[], [], [], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 24: Exception')
        print_exception()

    print('Startar test 4a/25')
    try:
        res = split_at([0, 0, 0, 0], is_zero)
        exp = [[], [], [], [], []]
        if res != exp:
            print("Fel i test 4a/25: split_at([0, 0, 0, 0], is_zero)")
            print("Korrekt svar: [[], [], [], [], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 25: Exception')
        print_exception()

    print('Startar test 4a/26')
    try:
        res = split_at([0, 0, 0, 0, 0], is_zero)
        exp = [[], [], [], [], [], []]
        if res != exp:
            print("Fel i test 4a/26: split_at([0, 0, 0, 0, 0], is_zero)")
            print("Korrekt svar: [[], [], [], [], [], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 26: Exception')
        print_exception()

    print('Startar test 4a/27')
    try:
        res = split_at([2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 2, 5], is_even)
        exp = [[], [3], [], [], [], [], [], [], [], [], [5]]
        if res != exp:
            print("Fel i test 4a/27: split_at([2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 2, 5], is_even)")
            print("Korrekt svar: [[], [3], [], [], [], [], [], [], [], [], [5]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 27: Exception')
        print_exception()

    print('Startar test 4a/28')
    try:
        res = split_at([2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 1, 5], is_even)
        exp = [[], [3], [], [], [], [], [], [], [], [1, 5]]
        if res != exp:
            print("Fel i test 4a/28: split_at([2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 1, 5], is_even)")
            print("Korrekt svar: [[], [3], [], [], [], [], [], [], [], [1, 5]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 28: Exception')
        print_exception()

    print('Startar test 4a/29')
    try:
        res = split_at([2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 1, 4, 5], is_even)
        exp = [[], [3], [], [], [], [], [], [], [], [1], [5]]
        if res != exp:
            print("Fel i test 4a/29: split_at([2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 1, 4, 5], is_even)")
            print("Korrekt svar: [[], [3], [], [], [], [], [], [], [], [1], [5]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 29: Exception')
        print_exception()

    print('Startar test 4a/30')
    try:
        res = split_at(['abc', 14, 23, (1, 2, 3)], is_even_int)
        exp = [['abc'], [23, (1, 2, 3)]]
        if res != exp:
            print("Fel i test 4a/30: split_at(['abc', 14, 23, (1, 2, 3)], is_even_int)")
            print("Korrekt svar: [['abc'], [23, (1, 2, 3)]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 30: Exception')
        print_exception()

    print('Startar test 4a/31')
    try:
        res = split_at([], is_even)
        exp = [[]]
        if res != exp:
            print("Fel i test 4a/31: split_at([], is_even)")
            print("Korrekt svar: [[]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 31: Exception')
        print_exception()

    print('Startar test 4a/32')
    try:
        res = split_at('abcdeba', always_false)
        exp = [['a', 'b', 'c', 'd', 'e', 'b', 'a']]
        if res != exp:
            print("Fel i test 4a/32: split_at('abcdeba', always_false)")
            print("Korrekt svar: [['a', 'b', 'c', 'd', 'e', 'b', 'a']]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 32: Exception')
        print_exception()

    print('Startar test 4a/33')
    try:
        res = split_at('krokofant', always_true)
        exp = [[], [], [], [], [], [], [], [], [], []]
        if res != exp:
            print("Fel i test 4a/33: split_at('krokofant', always_true)")
            print("Korrekt svar: [[], [], [], [], [], [], [], [], [], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 33: Exception')
        print_exception()

    print('Startar test 4a/34')
    try:
        res = split_at((2, 3, 4, 2, 5), is_two)
        exp = [[], [3, 4], [5]]
        if res != exp:
            print("Fel i test 4a/34: split_at((2, 3, 4, 2, 5), is_two)")
            print("Korrekt svar: [[], [3, 4], [5]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 34: Exception')
        print_exception()

    print('Startar test 4a/35')
    try:
        res = split_at((1, 2, 3, 4, 2), is_two)
        exp = [[1], [3, 4], []]
        if res != exp:
            print("Fel i test 4a/35: split_at((1, 2, 3, 4, 2), is_two)")
            print("Korrekt svar: [[1], [3, 4], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 35: Exception')
        print_exception()

    print('Startar test 4a/36')
    try:
        res = split_at((1, 2, 2, 3, 4, 2, 5), is_two)
        exp = [[1], [], [3, 4], [5]]
        if res != exp:
            print("Fel i test 4a/36: split_at((1, 2, 2, 3, 4, 2, 5), is_two)")
            print("Korrekt svar: [[1], [], [3, 4], [5]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 36: Exception')
        print_exception()

    print('Startar test 4a/37')
    try:
        res = split_at((1, 2, 3, 4, 5), is_even)
        exp = [[1], [3], [5]]
        if res != exp:
            print("Fel i test 4a/37: split_at((1, 2, 3, 4, 5), is_even)")
            print("Korrekt svar: [[1], [3], [5]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 37: Exception')
        print_exception()

    print('Startar test 4a/38')
    try:
        res = split_at([1, 0, 0], is_zero)
        exp = [[1], [], []]
        if res != exp:
            print("Fel i test 4a/38: split_at([1, 0, 0], is_zero)")
            print("Korrekt svar: [[1], [], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 38: Exception')
        print_exception()

    print('Startar test 4a/39')
    try:
        res = split_at((1, 2, 3, 4, 2), is_even)
        exp = [[1], [3], [], []]
        if res != exp:
            print("Fel i test 4a/39: split_at((1, 2, 3, 4, 2), is_even)")
            print("Korrekt svar: [[1], [3], [], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 39: Exception')
        print_exception()

    print('Startar test 4a/40')
    try:
        res = split_at((1, 2, 2, 2, 2), is_two)
        exp = [[1], [], [], [], []]
        if res != exp:
            print("Fel i test 4a/40: split_at((1, 2, 2, 2, 2), is_two)")
            print("Korrekt svar: [[1], [], [], [], []]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 40: Exception')
        print_exception()


    print('Klar med tester fÃ¶r uppgift 4a')
    print()


# noinspection PyBroadException
def test_4b():
    print('PÃ¥bÃ¶rjar tester fÃ¶r uppgift 4b')

    print('Startar test 4b/1')
    try:
        res = add_for_each([1, 2, 3, 4], squared)
        exp = 30
        if res != exp:
            print("Fel i test 4b/1: add_for_each([1, 2, 3, 4], squared)")
            print("Korrekt svar: 30")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 1: Exception')
        print_exception()

    print('Startar test 4b/2')
    try:
        res = add_for_each([], squared)
        exp = 0
        if res != exp:
            print("Fel i test 4b/2: add_for_each([], squared)")
            print("Korrekt svar: 0")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2: Exception')
        print_exception()

    print('Startar test 4b/3')
    try:
        res = add_for_each([[1, 2, 3], [1], [1, 2, 3, 4]], len)
        exp = 8
        if res != exp:
            print("Fel i test 4b/3: add_for_each([[1, 2, 3], [1], [1, 2, 3, 4]], len)")
            print("Korrekt svar: 8")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3: Exception')
        print_exception()

    print('Startar test 4b/4')
    try:
        res = add_for_each([12], squared)
        exp = 144
        if res != exp:
            print("Fel i test 4b/4: add_for_each([12], squared)")
            print("Korrekt svar: 144")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4: Exception')
        print_exception()

    print('Startar test 4b/5')
    try:
        res = add_for_each([12, 34], squared)
        exp = 1300
        if res != exp:
            print("Fel i test 4b/5: add_for_each([12, 34], squared)")
            print("Korrekt svar: 1300")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5: Exception')
        print_exception()

    print('Startar test 4b/6')
    try:
        res = add_for_each([12, 34, 56], squared)
        exp = 4436
        if res != exp:
            print("Fel i test 4b/6: add_for_each([12, 34, 56], squared)")
            print("Korrekt svar: 4436")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 6: Exception')
        print_exception()

    print('Startar test 4b/7')
    try:
        res = add_for_each([12, 34, 56, 78], squared)
        exp = 10520
        if res != exp:
            print("Fel i test 4b/7: add_for_each([12, 34, 56, 78], squared)")
            print("Korrekt svar: 10520")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 7: Exception')
        print_exception()

    print('Startar test 4b/8')
    try:
        res = add_for_each([12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78], squared)
        exp = 315600
        if res != exp:
            print("Fel i test 4b/8: add_for_each([12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78, 12, 34, 56, 78], squared)")
            print("Korrekt svar: 315600")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 8: Exception')
        print_exception()

    print('Startar test 4b/9')
    try:
        res = add_for_each([1, 2, 3, 4], half)
        exp = 5.0
        if res != exp:
            print("Fel i test 4b/9: add_for_each([1, 2, 3, 4], half)")
            print("Korrekt svar: 5.0")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 9: Exception')
        print_exception()


    print('Klar med tester fÃ¶r uppgift 4b')
    print()


# noinspection PyBroadException
def test_5a():
    print('PÃ¥bÃ¶rjar tester fÃ¶r uppgift 5a')

    print('Startar test 5a/1')
    try:
        if is_prime(1):
            print("Fel i test 5a/1: is_prime(1)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1: Exception')
        print_exception()

    print('Startar test 5a/2')
    try:
        if not is_prime(2):
            print("Fel i test 5a/2: is_prime(2)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 2: Exception')
        print_exception()

    print('Startar test 5a/3')
    try:
        if not is_prime(3):
            print("Fel i test 5a/3: is_prime(3)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 3: Exception')
        print_exception()

    print('Startar test 5a/4')
    try:
        if is_prime(4):
            print("Fel i test 5a/4: is_prime(4)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 4: Exception')
        print_exception()

    print('Startar test 5a/5')
    try:
        if not is_prime(5):
            print("Fel i test 5a/5: is_prime(5)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5: Exception')
        print_exception()

    print('Startar test 5a/6')
    try:
        if is_prime(6):
            print("Fel i test 5a/6: is_prime(6)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 6: Exception')
        print_exception()

    print('Startar test 5a/7')
    try:
        if not is_prime(7):
            print("Fel i test 5a/7: is_prime(7)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 7: Exception')
        print_exception()

    print('Startar test 5a/8')
    try:
        if is_prime(8):
            print("Fel i test 5a/8: is_prime(8)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 8: Exception')
        print_exception()

    print('Startar test 5a/9')
    try:
        if is_prime(9):
            print("Fel i test 5a/9: is_prime(9)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 9: Exception')
        print_exception()

    print('Startar test 5a/10')
    try:
        if is_prime(10):
            print("Fel i test 5a/10: is_prime(10)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 10: Exception')
        print_exception()

    print('Startar test 5a/11')
    try:
        if not is_prime(11):
            print("Fel i test 5a/11: is_prime(11)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 11: Exception')
        print_exception()

    print('Startar test 5a/12')
    try:
        if is_prime(12):
            print("Fel i test 5a/12: is_prime(12)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 12: Exception')
        print_exception()

    print('Startar test 5a/13')
    try:
        if not is_prime(13):
            print("Fel i test 5a/13: is_prime(13)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 13: Exception')
        print_exception()

    print('Startar test 5a/14')
    try:
        if is_prime(14):
            print("Fel i test 5a/14: is_prime(14)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 14: Exception')
        print_exception()

    print('Startar test 5a/15')
    try:
        if is_prime(15):
            print("Fel i test 5a/15: is_prime(15)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 15: Exception')
        print_exception()

    print('Startar test 5a/16')
    try:
        if is_prime(16):
            print("Fel i test 5a/16: is_prime(16)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 16: Exception')
        print_exception()

    print('Startar test 5a/17')
    try:
        if not is_prime(17):
            print("Fel i test 5a/17: is_prime(17)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 17: Exception')
        print_exception()

    print('Startar test 5a/18')
    try:
        if is_prime(18):
            print("Fel i test 5a/18: is_prime(18)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 18: Exception')
        print_exception()

    print('Startar test 5a/19')
    try:
        if not is_prime(19):
            print("Fel i test 5a/19: is_prime(19)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 19: Exception')
        print_exception()

    print('Startar test 5a/20')
    try:
        if is_prime(20):
            print("Fel i test 5a/20: is_prime(20)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 20: Exception')
        print_exception()

    print('Startar test 5a/21')
    try:
        if is_prime(21):
            print("Fel i test 5a/21: is_prime(21)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 21: Exception')
        print_exception()

    print('Startar test 5a/22')
    try:
        if is_prime(22):
            print("Fel i test 5a/22: is_prime(22)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 22: Exception')
        print_exception()

    print('Startar test 5a/23')
    try:
        if not is_prime(23):
            print("Fel i test 5a/23: is_prime(23)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 23: Exception')
        print_exception()

    print('Startar test 5a/24')
    try:
        if is_prime(24):
            print("Fel i test 5a/24: is_prime(24)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 24: Exception')
        print_exception()

    print('Startar test 5a/25')
    try:
        if is_prime(25):
            print("Fel i test 5a/25: is_prime(25)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 25: Exception')
        print_exception()

    print('Startar test 5a/26')
    try:
        if is_prime(26):
            print("Fel i test 5a/26: is_prime(26)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 26: Exception')
        print_exception()

    print('Startar test 5a/27')
    try:
        if is_prime(27):
            print("Fel i test 5a/27: is_prime(27)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 27: Exception')
        print_exception()

    print('Startar test 5a/28')
    try:
        if is_prime(28):
            print("Fel i test 5a/28: is_prime(28)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 28: Exception')
        print_exception()

    print('Startar test 5a/29')
    try:
        if not is_prime(29):
            print("Fel i test 5a/29: is_prime(29)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 29: Exception')
        print_exception()

    print('Startar test 5a/30')
    try:
        if is_prime(30):
            print("Fel i test 5a/30: is_prime(30)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 30: Exception')
        print_exception()

    print('Startar test 5a/31')
    try:
        if not is_prime(31):
            print("Fel i test 5a/31: is_prime(31)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 31: Exception')
        print_exception()

    print('Startar test 5a/32')
    try:
        if is_prime(32):
            print("Fel i test 5a/32: is_prime(32)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 32: Exception')
        print_exception()

    print('Startar test 5a/33')
    try:
        if is_prime(33):
            print("Fel i test 5a/33: is_prime(33)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 33: Exception')
        print_exception()

    print('Startar test 5a/34')
    try:
        if is_prime(34):
            print("Fel i test 5a/34: is_prime(34)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 34: Exception')
        print_exception()

    print('Startar test 5a/35')
    try:
        if is_prime(35):
            print("Fel i test 5a/35: is_prime(35)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 35: Exception')
        print_exception()

    print('Startar test 5a/36')
    try:
        if is_prime(36):
            print("Fel i test 5a/36: is_prime(36)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 36: Exception')
        print_exception()

    print('Startar test 5a/37')
    try:
        if not is_prime(37):
            print("Fel i test 5a/37: is_prime(37)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 37: Exception')
        print_exception()

    print('Startar test 5a/38')
    try:
        if is_prime(38):
            print("Fel i test 5a/38: is_prime(38)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 38: Exception')
        print_exception()

    print('Startar test 5a/39')
    try:
        if is_prime(39):
            print("Fel i test 5a/39: is_prime(39)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 39: Exception')
        print_exception()

    print('Startar test 5a/40')
    try:
        if is_prime(77):
            print("Fel i test 5a/40: is_prime(77)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 40: Exception')
        print_exception()

    print('Startar test 5a/41')
    try:
        if is_prime(121):
            print("Fel i test 5a/41: is_prime(121)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 41: Exception')
        print_exception()

    print('Startar test 5a/42')
    try:
        if is_prime(143):
            print("Fel i test 5a/42: is_prime(143)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 42: Exception')
        print_exception()

    print('Startar test 5a/43')
    try:
        if is_prime(169):
            print("Fel i test 5a/43: is_prime(169)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 43: Exception')
        print_exception()

    print('Startar test 5a/44')
    try:
        if is_prime(221):
            print("Fel i test 5a/44: is_prime(221)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 44: Exception')
        print_exception()

    print('Startar test 5a/45')
    try:
        if is_prime(289):
            print("Fel i test 5a/45: is_prime(289)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 45: Exception')
        print_exception()

    print('Startar test 5a/46')
    try:
        if is_prime(323):
            print("Fel i test 5a/46: is_prime(323)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 46: Exception')
        print_exception()

    print('Startar test 5a/47')
    try:
        if not is_prime(1000003):
            print("Fel i test 5a/47: is_prime(1000003)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 47: Exception')
        print_exception()

    print('Startar test 5a/48')
    try:
        if not is_prime(10000019):
            print("Fel i test 5a/48: is_prime(10000019)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 48: Exception')
        print_exception()

    print('Startar test 5a/49')
    try:
        if not is_prime(100000073):
            print("Fel i test 5a/49: is_prime(100000073)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 49: Exception')
        print_exception()

    print('Startar test 5a/50')
    try:
        if not is_prime(1000000007):
            print("Fel i test 5a/50: is_prime(1000000007)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 50: Exception')
        print_exception()

    print('Startar test 5a/51')
    try:
        if not is_prime(10000000019):
            print("Fel i test 5a/51: is_prime(10000000019)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 51: Exception')
        print_exception()

    print('Startar test 5a/52')
    try:
        if is_prime(256):
            print("Fel i test 5a/52: is_prime(256)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 52: Exception')
        print_exception()

    print('Startar test 5a/53')
    try:
        if is_prime(65536):
            print("Fel i test 5a/53: is_prime(65536)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 53: Exception')
        print_exception()

    print('Startar test 5a/54')
    try:
        if is_prime(16777216):
            print("Fel i test 5a/54: is_prime(16777216)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 54: Exception')
        print_exception()


    print('Klar med tester fÃ¶r uppgift 5a')
    print()


# noinspection PyBroadException
def test_5b():
    print('PÃ¥bÃ¶rjar tester fÃ¶r uppgift 5b')

    print('Startar test 5b/1')
    try:
        res = sorted(prime_factors(2))
        exp = [2]
        if res != exp:
            print("Fel i test 5b/1: prime_factors(2)")
            print("Korrekt svar: [2]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 1: Exception')
        print_exception()

    print('Startar test 5b/2')
    try:
        res = sorted(prime_factors(3))
        exp = [3]
        if res != exp:
            print("Fel i test 5b/2: prime_factors(3)")
            print("Korrekt svar: [3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2: Exception')
        print_exception()

    print('Startar test 5b/3')
    try:
        res = sorted(prime_factors(4))
        exp = [2, 2]
        if res != exp:
            print("Fel i test 5b/3: prime_factors(4)")
            print("Korrekt svar: [2, 2]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3: Exception')
        print_exception()

    print('Startar test 5b/4')
    try:
        res = sorted(prime_factors(5))
        exp = [5]
        if res != exp:
            print("Fel i test 5b/4: prime_factors(5)")
            print("Korrekt svar: [5]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4: Exception')
        print_exception()

    print('Startar test 5b/5')
    try:
        res = sorted(prime_factors(6))
        exp = [2, 3]
        if res != exp:
            print("Fel i test 5b/5: prime_factors(6)")
            print("Korrekt svar: [2, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5: Exception')
        print_exception()

    print('Startar test 5b/6')
    try:
        res = sorted(prime_factors(7))
        exp = [7]
        if res != exp:
            print("Fel i test 5b/6: prime_factors(7)")
            print("Korrekt svar: [7]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 6: Exception')
        print_exception()

    print('Startar test 5b/7')
    try:
        res = sorted(prime_factors(8))
        exp = [2, 2, 2]
        if res != exp:
            print("Fel i test 5b/7: prime_factors(8)")
            print("Korrekt svar: [2, 2, 2]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 7: Exception')
        print_exception()

    print('Startar test 5b/8')
    try:
        res = sorted(prime_factors(9))
        exp = [3, 3]
        if res != exp:
            print("Fel i test 5b/8: prime_factors(9)")
            print("Korrekt svar: [3, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 8: Exception')
        print_exception()

    print('Startar test 5b/9')
    try:
        res = sorted(prime_factors(10))
        exp = [2, 5]
        if res != exp:
            print("Fel i test 5b/9: prime_factors(10)")
            print("Korrekt svar: [2, 5]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 9: Exception')
        print_exception()

    print('Startar test 5b/10')
    try:
        res = sorted(prime_factors(11))
        exp = [11]
        if res != exp:
            print("Fel i test 5b/10: prime_factors(11)")
            print("Korrekt svar: [11]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 10: Exception')
        print_exception()

    print('Startar test 5b/11')
    try:
        res = sorted(prime_factors(12))
        exp = [2, 2, 3]
        if res != exp:
            print("Fel i test 5b/11: prime_factors(12)")
            print("Korrekt svar: [2, 2, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 11: Exception')
        print_exception()

    print('Startar test 5b/12')
    try:
        res = sorted(prime_factors(13))
        exp = [13]
        if res != exp:
            print("Fel i test 5b/12: prime_factors(13)")
            print("Korrekt svar: [13]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 12: Exception')
        print_exception()

    print('Startar test 5b/13')
    try:
        res = sorted(prime_factors(14))
        exp = [2, 7]
        if res != exp:
            print("Fel i test 5b/13: prime_factors(14)")
            print("Korrekt svar: [2, 7]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 13: Exception')
        print_exception()

    print('Startar test 5b/14')
    try:
        res = sorted(prime_factors(15))
        exp = [3, 5]
        if res != exp:
            print("Fel i test 5b/14: prime_factors(15)")
            print("Korrekt svar: [3, 5]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 14: Exception')
        print_exception()

    print('Startar test 5b/15')
    try:
        res = sorted(prime_factors(16))
        exp = [2, 2, 2, 2]
        if res != exp:
            print("Fel i test 5b/15: prime_factors(16)")
            print("Korrekt svar: [2, 2, 2, 2]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 15: Exception')
        print_exception()

    print('Startar test 5b/16')
    try:
        res = sorted(prime_factors(17))
        exp = [17]
        if res != exp:
            print("Fel i test 5b/16: prime_factors(17)")
            print("Korrekt svar: [17]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 16: Exception')
        print_exception()

    print('Startar test 5b/17')
    try:
        res = sorted(prime_factors(18))
        exp = [2, 3, 3]
        if res != exp:
            print("Fel i test 5b/17: prime_factors(18)")
            print("Korrekt svar: [2, 3, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 17: Exception')
        print_exception()

    print('Startar test 5b/18')
    try:
        res = sorted(prime_factors(19))
        exp = [19]
        if res != exp:
            print("Fel i test 5b/18: prime_factors(19)")
            print("Korrekt svar: [19]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 18: Exception')
        print_exception()

    print('Startar test 5b/19')
    try:
        res = sorted(prime_factors(20))
        exp = [2, 2, 5]
        if res != exp:
            print("Fel i test 5b/19: prime_factors(20)")
            print("Korrekt svar: [2, 2, 5]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 19: Exception')
        print_exception()

    print('Startar test 5b/20')
    try:
        res = sorted(prime_factors(21))
        exp = [3, 7]
        if res != exp:
            print("Fel i test 5b/20: prime_factors(21)")
            print("Korrekt svar: [3, 7]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 20: Exception')
        print_exception()

    print('Startar test 5b/21')
    try:
        res = sorted(prime_factors(22))
        exp = [2, 11]
        if res != exp:
            print("Fel i test 5b/21: prime_factors(22)")
            print("Korrekt svar: [2, 11]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 21: Exception')
        print_exception()

    print('Startar test 5b/22')
    try:
        res = sorted(prime_factors(23))
        exp = [23]
        if res != exp:
            print("Fel i test 5b/22: prime_factors(23)")
            print("Korrekt svar: [23]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 22: Exception')
        print_exception()

    print('Startar test 5b/23')
    try:
        res = sorted(prime_factors(24))
        exp = [2, 2, 2, 3]
        if res != exp:
            print("Fel i test 5b/23: prime_factors(24)")
            print("Korrekt svar: [2, 2, 2, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 23: Exception')
        print_exception()

    print('Startar test 5b/24')
    try:
        res = sorted(prime_factors(25))
        exp = [5, 5]
        if res != exp:
            print("Fel i test 5b/24: prime_factors(25)")
            print("Korrekt svar: [5, 5]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 24: Exception')
        print_exception()

    print('Startar test 5b/25')
    try:
        res = sorted(prime_factors(26))
        exp = [2, 13]
        if res != exp:
            print("Fel i test 5b/25: prime_factors(26)")
            print("Korrekt svar: [2, 13]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 25: Exception')
        print_exception()

    print('Startar test 5b/26')
    try:
        res = sorted(prime_factors(27))
        exp = [3, 3, 3]
        if res != exp:
            print("Fel i test 5b/26: prime_factors(27)")
            print("Korrekt svar: [3, 3, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 26: Exception')
        print_exception()

    print('Startar test 5b/27')
    try:
        res = sorted(prime_factors(28))
        exp = [2, 2, 7]
        if res != exp:
            print("Fel i test 5b/27: prime_factors(28)")
            print("Korrekt svar: [2, 2, 7]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 27: Exception')
        print_exception()

    print('Startar test 5b/28')
    try:
        res = sorted(prime_factors(29))
        exp = [29]
        if res != exp:
            print("Fel i test 5b/28: prime_factors(29)")
            print("Korrekt svar: [29]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 28: Exception')
        print_exception()

    print('Startar test 5b/29')
    try:
        res = sorted(prime_factors(30))
        exp = [2, 3, 5]
        if res != exp:
            print("Fel i test 5b/29: prime_factors(30)")
            print("Korrekt svar: [2, 3, 5]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 29: Exception')
        print_exception()

    print('Startar test 5b/30')
    try:
        res = sorted(prime_factors(31))
        exp = [31]
        if res != exp:
            print("Fel i test 5b/30: prime_factors(31)")
            print("Korrekt svar: [31]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 30: Exception')
        print_exception()

    print('Startar test 5b/31')
    try:
        res = sorted(prime_factors(32))
        exp = [2, 2, 2, 2, 2]
        if res != exp:
            print("Fel i test 5b/31: prime_factors(32)")
            print("Korrekt svar: [2, 2, 2, 2, 2]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 31: Exception')
        print_exception()

    print('Startar test 5b/32')
    try:
        res = sorted(prime_factors(33))
        exp = [3, 11]
        if res != exp:
            print("Fel i test 5b/32: prime_factors(33)")
            print("Korrekt svar: [3, 11]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 32: Exception')
        print_exception()

    print('Startar test 5b/33')
    try:
        res = sorted(prime_factors(34))
        exp = [2, 17]
        if res != exp:
            print("Fel i test 5b/33: prime_factors(34)")
            print("Korrekt svar: [2, 17]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 33: Exception')
        print_exception()

    print('Startar test 5b/34')
    try:
        res = sorted(prime_factors(35))
        exp = [5, 7]
        if res != exp:
            print("Fel i test 5b/34: prime_factors(35)")
            print("Korrekt svar: [5, 7]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 34: Exception')
        print_exception()

    print('Startar test 5b/35')
    try:
        res = sorted(prime_factors(36))
        exp = [2, 2, 3, 3]
        if res != exp:
            print("Fel i test 5b/35: prime_factors(36)")
            print("Korrekt svar: [2, 2, 3, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 35: Exception')
        print_exception()

    print('Startar test 5b/36')
    try:
        res = sorted(prime_factors(37))
        exp = [37]
        if res != exp:
            print("Fel i test 5b/36: prime_factors(37)")
            print("Korrekt svar: [37]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 36: Exception')
        print_exception()

    print('Startar test 5b/37')
    try:
        res = sorted(prime_factors(38))
        exp = [2, 19]
        if res != exp:
            print("Fel i test 5b/37: prime_factors(38)")
            print("Korrekt svar: [2, 19]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 37: Exception')
        print_exception()

    print('Startar test 5b/38')
    try:
        res = sorted(prime_factors(39))
        exp = [3, 13]
        if res != exp:
            print("Fel i test 5b/38: prime_factors(39)")
            print("Korrekt svar: [3, 13]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 38: Exception')
        print_exception()

    print('Startar test 5b/39')
    try:
        res = sorted(prime_factors(40))
        exp = [2, 2, 2, 5]
        if res != exp:
            print("Fel i test 5b/39: prime_factors(40)")
            print("Korrekt svar: [2, 2, 2, 5]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 39: Exception')
        print_exception()

    print('Startar test 5b/40')
    try:
        res = sorted(prime_factors(41))
        exp = [41]
        if res != exp:
            print("Fel i test 5b/40: prime_factors(41)")
            print("Korrekt svar: [41]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 40: Exception')
        print_exception()

    print('Startar test 5b/41')
    try:
        res = sorted(prime_factors(42))
        exp = [2, 3, 7]
        if res != exp:
            print("Fel i test 5b/41: prime_factors(42)")
            print("Korrekt svar: [2, 3, 7]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 41: Exception')
        print_exception()

    print('Startar test 5b/42')
    try:
        res = sorted(prime_factors(43))
        exp = [43]
        if res != exp:
            print("Fel i test 5b/42: prime_factors(43)")
            print("Korrekt svar: [43]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 42: Exception')
        print_exception()

    print('Startar test 5b/43')
    try:
        res = sorted(prime_factors(44))
        exp = [2, 2, 11]
        if res != exp:
            print("Fel i test 5b/43: prime_factors(44)")
            print("Korrekt svar: [2, 2, 11]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 43: Exception')
        print_exception()

    print('Startar test 5b/44')
    try:
        res = sorted(prime_factors(45))
        exp = [3, 3, 5]
        if res != exp:
            print("Fel i test 5b/44: prime_factors(45)")
            print("Korrekt svar: [3, 3, 5]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 44: Exception')
        print_exception()

    print('Startar test 5b/45')
    try:
        res = sorted(prime_factors(46))
        exp = [2, 23]
        if res != exp:
            print("Fel i test 5b/45: prime_factors(46)")
            print("Korrekt svar: [2, 23]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 45: Exception')
        print_exception()

    print('Startar test 5b/46')
    try:
        res = sorted(prime_factors(47))
        exp = [47]
        if res != exp:
            print("Fel i test 5b/46: prime_factors(47)")
            print("Korrekt svar: [47]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 46: Exception')
        print_exception()

    print('Startar test 5b/47')
    try:
        res = sorted(prime_factors(48))
        exp = [2, 2, 2, 2, 3]
        if res != exp:
            print("Fel i test 5b/47: prime_factors(48)")
            print("Korrekt svar: [2, 2, 2, 2, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 47: Exception')
        print_exception()

    print('Startar test 5b/48')
    try:
        res = sorted(prime_factors(49))
        exp = [7, 7]
        if res != exp:
            print("Fel i test 5b/48: prime_factors(49)")
            print("Korrekt svar: [7, 7]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 48: Exception')
        print_exception()

    print('Startar test 5b/49')
    try:
        res = sorted(prime_factors(100))
        exp = [2, 2, 5, 5]
        if res != exp:
            print("Fel i test 5b/49: prime_factors(100)")
            print("Korrekt svar: [2, 2, 5, 5]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 49: Exception')
        print_exception()

    print('Startar test 5b/50')
    try:
        res = sorted(prime_factors(101))
        exp = [101]
        if res != exp:
            print("Fel i test 5b/50: prime_factors(101)")
            print("Korrekt svar: [101]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 50: Exception')
        print_exception()

    print('Startar test 5b/51')
    try:
        res = sorted(prime_factors(150))
        exp = [2, 3, 5, 5]
        if res != exp:
            print("Fel i test 5b/51: prime_factors(150)")
            print("Korrekt svar: [2, 3, 5, 5]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 51: Exception')
        print_exception()

    print('Startar test 5b/52')
    try:
        res = sorted(prime_factors(151))
        exp = [151]
        if res != exp:
            print("Fel i test 5b/52: prime_factors(151)")
            print("Korrekt svar: [151]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 52: Exception')
        print_exception()

    print('Startar test 5b/53')
    try:
        res = sorted(prime_factors(200))
        exp = [2, 2, 2, 5, 5]
        if res != exp:
            print("Fel i test 5b/53: prime_factors(200)")
            print("Korrekt svar: [2, 2, 2, 5, 5]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 53: Exception')
        print_exception()

    print('Startar test 5b/54')
    try:
        res = sorted(prime_factors(211))
        exp = [211]
        if res != exp:
            print("Fel i test 5b/54: prime_factors(211)")
            print("Korrekt svar: [211]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 54: Exception')
        print_exception()

    print('Startar test 5b/55')
    try:
        res = sorted(prime_factors(256))
        exp = [2, 2, 2, 2, 2, 2, 2, 2]
        if res != exp:
            print("Fel i test 5b/55: prime_factors(256)")
            print("Korrekt svar: [2, 2, 2, 2, 2, 2, 2, 2]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 55: Exception')
        print_exception()

    print('Startar test 5b/56')
    try:
        res = sorted(prime_factors(743))
        exp = [743]
        if res != exp:
            print("Fel i test 5b/56: prime_factors(743)")
            print("Korrekt svar: [743]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 56: Exception')
        print_exception()

    print('Startar test 5b/57')
    try:
        res = sorted(prime_factors(6561))
        exp = [3, 3, 3, 3, 3, 3, 3, 3]
        if res != exp:
            print("Fel i test 5b/57: prime_factors(6561)")
            print("Korrekt svar: [3, 3, 3, 3, 3, 3, 3, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 57: Exception')
        print_exception()

    print('Startar test 5b/58')
    try:
        res = sorted(prime_factors(3019))
        exp = [3019]
        if res != exp:
            print("Fel i test 5b/58: prime_factors(3019)")
            print("Korrekt svar: [3019]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 58: Exception')
        print_exception()

    print('Startar test 5b/59')
    try:
        res = sorted(prime_factors(121))
        exp = [11, 11]
        if res != exp:
            print("Fel i test 5b/59: prime_factors(121)")
            print("Korrekt svar: [11, 11]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 59: Exception')
        print_exception()

    print('Startar test 5b/60')
    try:
        res = sorted(prime_factors(289))
        exp = [17, 17]
        if res != exp:
            print("Fel i test 5b/60: prime_factors(289)")
            print("Korrekt svar: [17, 17]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 60: Exception')
        print_exception()

    print('Startar test 5b/61')
    try:
        res = sorted(prime_factors(529))
        exp = [23, 23]
        if res != exp:
            print("Fel i test 5b/61: prime_factors(529)")
            print("Korrekt svar: [23, 23]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 61: Exception')
        print_exception()

    print('Startar test 5b/62')
    try:
        res = sorted(prime_factors(108))
        exp = [2, 2, 3, 3, 3]
        if res != exp:
            print("Fel i test 5b/62: prime_factors(108)")
            print("Korrekt svar: [2, 2, 3, 3, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 62: Exception')
        print_exception()

    print('Startar test 5b/63')
    try:
        res = sorted(prime_factors(11021))
        exp = [103, 107]
        if res != exp:
            print("Fel i test 5b/63: prime_factors(11021)")
            print("Korrekt svar: [103, 107]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 63: Exception')
        print_exception()

    print('Startar test 5b/64')
    try:
        res = sorted(prime_factors(3113))
        exp = [11, 283]
        if res != exp:
            print("Fel i test 5b/64: prime_factors(3113)")
            print("Korrekt svar: [11, 283]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 64: Exception')
        print_exception()


    print('Klar med tester fÃ¶r uppgift 5b')
    print()


# noinspection PyBroadException
def test_5c():
    print('PÃ¥bÃ¶rjar tester fÃ¶r uppgift 5c')

    print('Startar test 5c/1')
    try:
        if is_attractive(16):
            print("Fel i test 5c/1: is_attractive(16)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1: Exception')
        print_exception()

    print('Startar test 5c/2')
    try:
        if not is_attractive(20):
            print("Fel i test 5c/2: is_attractive(20)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 2: Exception')
        print_exception()

    print('Startar test 5c/3')
    try:
        if not is_attractive(21):
            print("Fel i test 5c/3: is_attractive(21)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 3: Exception')
        print_exception()

    print('Startar test 5c/4')
    try:
        if not is_attractive(22):
            print("Fel i test 5c/4: is_attractive(22)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 4: Exception')
        print_exception()

    print('Startar test 5c/5')
    try:
        if is_attractive(23):
            print("Fel i test 5c/5: is_attractive(23)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5: Exception')
        print_exception()

    print('Startar test 5c/6')
    try:
        if is_attractive(24):
            print("Fel i test 5c/6: is_attractive(24)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 6: Exception')
        print_exception()

    print('Startar test 5c/7')
    try:
        if not is_attractive(55):
            print("Fel i test 5c/7: is_attractive(55)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 7: Exception')
        print_exception()

    print('Startar test 5c/8')
    try:
        if is_attractive(100):
            print("Fel i test 5c/8: is_attractive(100)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 8: Exception')
        print_exception()

    print('Startar test 5c/9')
    try:
        if is_attractive(101):
            print("Fel i test 5c/9: is_attractive(101)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 9: Exception')
        print_exception()

    print('Startar test 5c/10')
    try:
        if not is_attractive(102):
            print("Fel i test 5c/10: is_attractive(102)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 10: Exception')
        print_exception()

    print('Startar test 5c/11')
    try:
        if is_attractive(103):
            print("Fel i test 5c/11: is_attractive(103)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 11: Exception')
        print_exception()

    print('Startar test 5c/12')
    try:
        if is_attractive(104):
            print("Fel i test 5c/12: is_attractive(104)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 12: Exception')
        print_exception()

    print('Startar test 5c/13')
    try:
        if not is_attractive(105):
            print("Fel i test 5c/13: is_attractive(105)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 13: Exception')
        print_exception()

    print('Startar test 5c/14')
    try:
        if not is_attractive(106):
            print("Fel i test 5c/14: is_attractive(106)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 14: Exception')
        print_exception()

    print('Startar test 5c/15')
    try:
        if is_attractive(107):
            print("Fel i test 5c/15: is_attractive(107)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 15: Exception')
        print_exception()

    print('Startar test 5c/16')
    try:
        if not is_attractive(108):
            print("Fel i test 5c/16: is_attractive(108)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 16: Exception')
        print_exception()

    print('Startar test 5c/17')
    try:
        if is_attractive(109):
            print("Fel i test 5c/17: is_attractive(109)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 17: Exception')
        print_exception()

    print('Startar test 5c/18')
    try:
        if not is_attractive(110):
            print("Fel i test 5c/18: is_attractive(110)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 18: Exception')
        print_exception()

    print('Startar test 5c/19')
    try:
        if not is_attractive(111):
            print("Fel i test 5c/19: is_attractive(111)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 19: Exception')
        print_exception()

    print('Startar test 5c/20')
    try:
        if not is_attractive(112):
            print("Fel i test 5c/20: is_attractive(112)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 20: Exception')
        print_exception()

    print('Startar test 5c/21')
    try:
        if is_attractive(113):
            print("Fel i test 5c/21: is_attractive(113)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 21: Exception')
        print_exception()

    print('Startar test 5c/22')
    try:
        if not is_attractive(114):
            print("Fel i test 5c/22: is_attractive(114)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 22: Exception')
        print_exception()

    print('Startar test 5c/23')
    try:
        if not is_attractive(115):
            print("Fel i test 5c/23: is_attractive(115)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 23: Exception')
        print_exception()

    print('Startar test 5c/24')
    try:
        if not is_attractive(116):
            print("Fel i test 5c/24: is_attractive(116)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 24: Exception')
        print_exception()

    print('Startar test 5c/25')
    try:
        if not is_attractive(117):
            print("Fel i test 5c/25: is_attractive(117)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 25: Exception')
        print_exception()

    print('Startar test 5c/26')
    try:
        if not is_attractive(118):
            print("Fel i test 5c/26: is_attractive(118)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 26: Exception')
        print_exception()

    print('Startar test 5c/27')
    try:
        if not is_attractive(119):
            print("Fel i test 5c/27: is_attractive(119)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 27: Exception')
        print_exception()

    print('Startar test 5c/28')
    try:
        if not is_attractive(120):
            print("Fel i test 5c/28: is_attractive(120)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 28: Exception')
        print_exception()

    print('Startar test 5c/29')
    try:
        if not is_attractive(121):
            print("Fel i test 5c/29: is_attractive(121)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 29: Exception')
        print_exception()

    print('Startar test 5c/30')
    try:
        if not is_attractive(122):
            print("Fel i test 5c/30: is_attractive(122)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 30: Exception')
        print_exception()

    print('Startar test 5c/31')
    try:
        if not is_attractive(123):
            print("Fel i test 5c/31: is_attractive(123)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 31: Exception')
        print_exception()

    print('Startar test 5c/32')
    try:
        if not is_attractive(124):
            print("Fel i test 5c/32: is_attractive(124)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 32: Exception')
        print_exception()

    print('Startar test 5c/33')
    try:
        if not is_attractive(125):
            print("Fel i test 5c/33: is_attractive(125)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 33: Exception')
        print_exception()

    print('Startar test 5c/34')
    try:
        if is_attractive(126):
            print("Fel i test 5c/34: is_attractive(126)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 34: Exception')
        print_exception()

    print('Startar test 5c/35')
    try:
        if is_attractive(127):
            print("Fel i test 5c/35: is_attractive(127)")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 35: Exception')
        print_exception()

    print('Startar test 5c/36')
    try:
        if not is_attractive(128):
            print("Fel i test 5c/36: is_attractive(128)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 36: Exception')
        print_exception()

    print('Startar test 5c/37')
    try:
        if not is_attractive(129):
            print("Fel i test 5c/37: is_attractive(129)")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 37: Exception')
        print_exception()


    print('Klar med tester fÃ¶r uppgift 5c')
    print()


# noinspection PyBroadException
def test_6a():
    print('PÃ¥bÃ¶rjar tester fÃ¶r uppgift 6a')

    print('Startar test 6a/1')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        create_trie()
    except:
        print(f'Fel i test 1: Exception')
        print_exception()

    print('Startar test 6a/2')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {}), 'hello')
    except:
        print(f'Fel i test 2: Exception')
        print_exception()

    print('Startar test 6a/3')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})})}), 'hello')
    except:
        print(f'Fel i test 3: Exception')
        print_exception()

    print('Startar test 6a/4')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})})}), 'hello')
    except:
        print(f'Fel i test 4: Exception')
        print_exception()

    print('Startar test 6a/5')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})})}), 'ace')
    except:
        print(f'Fel i test 5: Exception')
        print_exception()

    print('Startar test 6a/6')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {})})})}), 'aced')
    except:
        print(f'Fel i test 6: Exception')
        print_exception()

    print('Startar test 6a/7')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {})})})})}), 'aces')
    except:
        print(f'Fel i test 7: Exception')
        print_exception()

    print('Startar test 6a/8')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})})})})}), 'acre')
    except:
        print(f'Fel i test 8: Exception')
        print_exception()

    print('Startar test 6a/9')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {})})})})}), 'acres')
    except:
        print(f'Fel i test 9: Exception')
        print_exception()

    print('Startar test 6a/10')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'act')
    except:
        print(f'Fel i test 10: Exception')
        print_exception()

    print('Startar test 6a/11')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {})})})}), 'acted')
    except:
        print(f'Fel i test 11: Exception')
        print_exception()

    print('Startar test 6a/12')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})})})})})}), 'acting')
    except:
        print(f'Fel i test 12: Exception')
        print_exception()

    print('Startar test 6a/13')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})})})})}), 'acts')
    except:
        print(f'Fel i test 13: Exception')
        print_exception()

    print('Startar test 6a/14')
    try:
        if not word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'ace'):
            print("Fel i test 6a/14: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'ace')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 14: Exception')
        print_exception()

    print('Startar test 6a/15')
    try:
        if not word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'aced'):
            print("Fel i test 6a/15: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'aced')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 15: Exception')
        print_exception()

    print('Startar test 6a/16')
    try:
        if not word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'aces'):
            print("Fel i test 6a/16: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'aces')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 16: Exception')
        print_exception()

    print('Startar test 6a/17')
    try:
        if not word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acre'):
            print("Fel i test 6a/17: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acre')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 17: Exception')
        print_exception()

    print('Startar test 6a/18')
    try:
        if not word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acres'):
            print("Fel i test 6a/18: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acres')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 18: Exception')
        print_exception()

    print('Startar test 6a/19')
    try:
        if not word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'act'):
            print("Fel i test 6a/19: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'act')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 19: Exception')
        print_exception()

    print('Startar test 6a/20')
    try:
        if not word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acted'):
            print("Fel i test 6a/20: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acted')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 20: Exception')
        print_exception()

    print('Startar test 6a/21')
    try:
        if not word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acting'):
            print("Fel i test 6a/21: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acting')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 21: Exception')
        print_exception()

    print('Startar test 6a/22')
    try:
        if not word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acts'):
            print("Fel i test 6a/22: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acts')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 22: Exception')
        print_exception()

    print('Startar test 6a/23')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'ac'):
            print("Fel i test 6a/23: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'ac')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 23: Exception')
        print_exception()

    print('Startar test 6a/24')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acr'):
            print("Fel i test 6a/24: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acr')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 24: Exception')
        print_exception()

    print('Startar test 6a/25')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acte'):
            print("Fel i test 6a/25: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acte')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 25: Exception')
        print_exception()

    print('Startar test 6a/26')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acti'):
            print("Fel i test 6a/26: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acti')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 26: Exception')
        print_exception()

    print('Startar test 6a/27')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'actin'):
            print("Fel i test 6a/27: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'actin')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 27: Exception')
        print_exception()

    print('Startar test 6a/28')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'actinga'):
            print("Fel i test 6a/28: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'actinga')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 28: Exception')
        print_exception()

    print('Startar test 6a/29')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acreses'):
            print("Fel i test 6a/29: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acreses')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 29: Exception')
        print_exception()

    print('Startar test 6a/30')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'actz'):
            print("Fel i test 6a/30: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'actz')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 30: Exception')
        print_exception()

    print('Startar test 6a/31')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'actt'):
            print("Fel i test 6a/31: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'actt')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 31: Exception')
        print_exception()

    print('Startar test 6a/32')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'at'):
            print("Fel i test 6a/32: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'at')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 32: Exception')
        print_exception()

    print('Startar test 6a/33')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acd'):
            print("Fel i test 6a/33: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acd')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 33: Exception')
        print_exception()

    print('Startar test 6a/34')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'ated'):
            print("Fel i test 6a/34: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'ated')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 34: Exception')
        print_exception()

    print('Startar test 6a/35')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'atng'):
            print("Fel i test 6a/35: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'atng')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 35: Exception')
        print_exception()

    print('Startar test 6a/36')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'ta'):
            print("Fel i test 6a/36: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'ta')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 36: Exception')
        print_exception()

    print('Startar test 6a/37')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'dac'):
            print("Fel i test 6a/37: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'dac')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 37: Exception')
        print_exception()

    print('Startar test 6a/38')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acser'):
            print("Fel i test 6a/38: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acser')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 38: Exception')
        print_exception()

    print('Startar test 6a/39')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'En'):
            print("Fel i test 6a/39: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'En')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 39: Exception')
        print_exception()

    print('Startar test 6a/40')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'Trie'):
            print("Fel i test 6a/40: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'Trie')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 40: Exception')
        print_exception()

    print('Startar test 6a/41')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'Ã¤r'):
            print("Fel i test 6a/41: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'Ã¤r')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 41: Exception')
        print_exception()

    print('Startar test 6a/42')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'en'):
            print("Fel i test 6a/42: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'en')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 42: Exception')
        print_exception()

    print('Startar test 6a/43')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'effektiv'):
            print("Fel i test 6a/43: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'effektiv')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 43: Exception')
        print_exception()

    print('Startar test 6a/44')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'datastruktur'):
            print("Fel i test 6a/44: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'datastruktur')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 44: Exception')
        print_exception()

    print('Startar test 6a/45')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'fÃ¶r'):
            print("Fel i test 6a/45: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'fÃ¶r')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 45: Exception')
        print_exception()

    print('Startar test 6a/46')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'att'):
            print("Fel i test 6a/46: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'att')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 46: Exception')
        print_exception()

    print('Startar test 6a/47')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'lagra'):
            print("Fel i test 6a/47: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'lagra')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 47: Exception')
        print_exception()

    print('Startar test 6a/48')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'en'):
            print("Fel i test 6a/48: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'en')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 48: Exception')
        print_exception()

    print('Startar test 6a/49')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'mÃ¤ngd'):
            print("Fel i test 6a/49: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'mÃ¤ngd')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 49: Exception')
        print_exception()

    print('Startar test 6a/50')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'strÃ¤ngar'):
            print("Fel i test 6a/50: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'strÃ¤ngar')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 50: Exception')
        print_exception()

    print('Startar test 6a/51')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {}), 'acts')
    except:
        print(f'Fel i test 51: Exception')
        print_exception()

    print('Startar test 6a/52')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'a': (False, {'c': (False, {'t': (False, {'s': (True, {})})})})}), 'aced')
    except:
        print(f'Fel i test 52: Exception')
        print_exception()

    print('Startar test 6a/53')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'a': (False, {'c': (False, {'t': (False, {'s': (True, {})}), 'e': (False, {'d': (True, {})})})})}), 'act')
    except:
        print(f'Fel i test 53: Exception')
        print_exception()

    print('Startar test 6a/54')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {})}), 'e': (False, {'d': (True, {})})})})}), 'acre')
    except:
        print(f'Fel i test 54: Exception')
        print_exception()

    print('Startar test 6a/55')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {})}), 'e': (False, {'d': (True, {})}), 'r': (False, {'e': (True, {})})})})}), 'acres')
    except:
        print(f'Fel i test 55: Exception')
        print_exception()

    print('Startar test 6a/56')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {})}), 'e': (False, {'d': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'ace')
    except:
        print(f'Fel i test 56: Exception')
        print_exception()

    print('Startar test 6a/57')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {})}), 'e': (True, {'d': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'acted')
    except:
        print(f'Fel i test 57: Exception')
        print_exception()

    print('Startar test 6a/58')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})})}), 'e': (True, {'d': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'aces')
    except:
        print(f'Fel i test 58: Exception')
        print_exception()

    print('Startar test 6a/59')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'acting')
    except:
        print(f'Fel i test 59: Exception')
        print_exception()

    print('Startar test 6a/60')
    try:
        if not word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'ace'):
            print("Fel i test 6a/60: word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'ace')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 60: Exception')
        print_exception()

    print('Startar test 6a/61')
    try:
        if not word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'aced'):
            print("Fel i test 6a/61: word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'aced')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 61: Exception')
        print_exception()

    print('Startar test 6a/62')
    try:
        if not word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'aces'):
            print("Fel i test 6a/62: word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'aces')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 62: Exception')
        print_exception()

    print('Startar test 6a/63')
    try:
        if not word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'acre'):
            print("Fel i test 6a/63: word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'acre')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 63: Exception')
        print_exception()

    print('Startar test 6a/64')
    try:
        if not word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'acres'):
            print("Fel i test 6a/64: word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'acres')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 64: Exception')
        print_exception()

    print('Startar test 6a/65')
    try:
        if not word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'act'):
            print("Fel i test 6a/65: word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'act')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 65: Exception')
        print_exception()

    print('Startar test 6a/66')
    try:
        if not word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'acted'):
            print("Fel i test 6a/66: word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'acted')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 66: Exception')
        print_exception()

    print('Startar test 6a/67')
    try:
        if not word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'acting'):
            print("Fel i test 6a/67: word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'acting')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 67: Exception')
        print_exception()

    print('Startar test 6a/68')
    try:
        if not word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'acts'):
            print("Fel i test 6a/68: word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'acts')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 68: Exception')
        print_exception()

    print('Startar test 6a/69')
    try:
        if word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'En'):
            print("Fel i test 6a/69: word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'En')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 69: Exception')
        print_exception()

    print('Startar test 6a/70')
    try:
        if word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'Trie'):
            print("Fel i test 6a/70: word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'Trie')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 70: Exception')
        print_exception()

    print('Startar test 6a/71')
    try:
        if word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'Ã¤r'):
            print("Fel i test 6a/71: word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'Ã¤r')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 71: Exception')
        print_exception()

    print('Startar test 6a/72')
    try:
        if word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'en'):
            print("Fel i test 6a/72: word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'en')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 72: Exception')
        print_exception()

    print('Startar test 6a/73')
    try:
        if word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'effektiv'):
            print("Fel i test 6a/73: word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'effektiv')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 73: Exception')
        print_exception()

    print('Startar test 6a/74')
    try:
        if word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'datastruktur'):
            print("Fel i test 6a/74: word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'datastruktur')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 74: Exception')
        print_exception()

    print('Startar test 6a/75')
    try:
        if word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'fÃ¶r'):
            print("Fel i test 6a/75: word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'fÃ¶r')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 75: Exception')
        print_exception()

    print('Startar test 6a/76')
    try:
        if word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'att'):
            print("Fel i test 6a/76: word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'att')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 76: Exception')
        print_exception()

    print('Startar test 6a/77')
    try:
        if word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'lagra'):
            print("Fel i test 6a/77: word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'lagra')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 77: Exception')
        print_exception()

    print('Startar test 6a/78')
    try:
        if word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'en'):
            print("Fel i test 6a/78: word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'en')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 78: Exception')
        print_exception()

    print('Startar test 6a/79')
    try:
        if word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'mÃ¤ngd'):
            print("Fel i test 6a/79: word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'mÃ¤ngd')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 79: Exception')
        print_exception()

    print('Startar test 6a/80')
    try:
        if word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'strÃ¤ngar'):
            print("Fel i test 6a/80: word_in_trie((False, {'a': (False, {'c': (False, {'t': (True, {'s': (True, {}), 'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})}), 'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'strÃ¤ngar')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 80: Exception')
        print_exception()

    print('Startar test 6a/81')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {}), 'trierarchies')
    except:
        print(f'Fel i test 81: Exception')
        print_exception()

    print('Startar test 6a/82')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (False, {'i': (False, {'e': (False, {'s': (True, {})})})})})})})})})})})})}), 'triennially')
    except:
        print(f'Fel i test 82: Exception')
        print_exception()

    print('Startar test 6a/83')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (False, {'i': (False, {'e': (False, {'s': (True, {})})})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (False, {'l': (False, {'l': (False, {'y': (True, {})})})})})})})})})})})}), 'trierarchy')
    except:
        print(f'Fel i test 83: Exception')
        print_exception()

    print('Startar test 6a/84')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (False, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (False, {'l': (False, {'l': (False, {'y': (True, {})})})})})})})})})})})}), 'trienniums')
    except:
        print(f'Fel i test 84: Exception')
        print_exception()

    print('Startar test 6a/85')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (False, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (False, {'l': (False, {'l': (False, {'y': (True, {})})})}), 'u': (False, {'m': (False, {'s': (True, {})})})})})})})})})})}), 'triennials')
    except:
        print(f'Fel i test 85: Exception')
        print_exception()

    print('Startar test 6a/86')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (False, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (False, {'l': (False, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (False, {'s': (True, {})})})})})})})})})})}), 'trierarchs')
    except:
        print(f'Fel i test 86: Exception')
        print_exception()

    print('Startar test 6a/87')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (False, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (False, {'l': (False, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (False, {'s': (True, {})})})})})})})})})})}), 'triennial')
    except:
        print(f'Fel i test 87: Exception')
        print_exception()

    print('Startar test 6a/88')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (False, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (False, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (False, {'s': (True, {})})})})})})})})})})}), 'triennium')
    except:
        print(f'Fel i test 88: Exception')
        print_exception()

    print('Startar test 6a/89')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (False, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (False, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})})})})})})})}), 'trierarch')
    except:
        print(f'Fel i test 89: Exception')
        print_exception()

    print('Startar test 6a/90')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (False, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})})})})})})})}), 'trientes')
    except:
        print(f'Fel i test 90: Exception')
        print_exception()

    print('Startar test 6a/91')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (False, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})})})})})})})}), 'triennia')
    except:
        print(f'Fel i test 91: Exception')
        print_exception()

    print('Startar test 6a/92')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})})})})})})})}), 'triethyl')
    except:
        print(f'Fel i test 92: Exception')
        print_exception()

    print('Startar test 6a/93')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})})})})})})}), 'trienes')
    except:
        print(f'Fel i test 93: Exception')
        print_exception()

    print('Startar test 6a/94')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (False, {'s': (True, {})})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})})})})})})}), 'triene')
    except:
        print(f'Fel i test 94: Exception')
        print_exception()

    print('Startar test 6a/95')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})})})})})})}), 'triens')
    except:
        print(f'Fel i test 95: Exception')
        print_exception()

    print('Startar test 6a/96')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})})})})})})}), 'triers')
    except:
        print(f'Fel i test 96: Exception')
        print_exception()

    print('Startar test 6a/97')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})})})})})})}), 'tried')
    except:
        print(f'Fel i test 97: Exception')
        print_exception()

    print('Startar test 6a/98')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {})})})})})}), 'tries')
    except:
        print(f'Fel i test 98: Exception')
        print_exception()

    print('Startar test 6a/99')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trier')
    except:
        print(f'Fel i test 99: Exception')
        print_exception()

    print('Startar test 6a/100')
    try:
        if word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'ace'):
            print("Fel i test 6a/100: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'ace')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 100: Exception')
        print_exception()

    print('Startar test 6a/101')
    try:
        if word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'aced'):
            print("Fel i test 6a/101: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'aced')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 101: Exception')
        print_exception()

    print('Startar test 6a/102')
    try:
        if word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'aces'):
            print("Fel i test 6a/102: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'aces')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 102: Exception')
        print_exception()

    print('Startar test 6a/103')
    try:
        if word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'acre'):
            print("Fel i test 6a/103: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'acre')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 103: Exception')
        print_exception()

    print('Startar test 6a/104')
    try:
        if word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'acres'):
            print("Fel i test 6a/104: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'acres')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 104: Exception')
        print_exception()

    print('Startar test 6a/105')
    try:
        if word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'act'):
            print("Fel i test 6a/105: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'act')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 105: Exception')
        print_exception()

    print('Startar test 6a/106')
    try:
        if word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'acted'):
            print("Fel i test 6a/106: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'acted')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 106: Exception')
        print_exception()

    print('Startar test 6a/107')
    try:
        if word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'acting'):
            print("Fel i test 6a/107: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'acting')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 107: Exception')
        print_exception()

    print('Startar test 6a/108')
    try:
        if word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'acts'):
            print("Fel i test 6a/108: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'acts')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 108: Exception')
        print_exception()

    print('Startar test 6a/109')
    try:
        if not word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trierarchies'):
            print("Fel i test 6a/109: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trierarchies')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 109: Exception')
        print_exception()

    print('Startar test 6a/110')
    try:
        if not word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'triennially'):
            print("Fel i test 6a/110: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'triennially')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 110: Exception')
        print_exception()

    print('Startar test 6a/111')
    try:
        if not word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trierarchy'):
            print("Fel i test 6a/111: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trierarchy')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 111: Exception')
        print_exception()

    print('Startar test 6a/112')
    try:
        if not word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trienniums'):
            print("Fel i test 6a/112: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trienniums')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 112: Exception')
        print_exception()

    print('Startar test 6a/113')
    try:
        if not word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'triennials'):
            print("Fel i test 6a/113: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'triennials')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 113: Exception')
        print_exception()

    print('Startar test 6a/114')
    try:
        if not word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trierarchs'):
            print("Fel i test 6a/114: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trierarchs')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 114: Exception')
        print_exception()

    print('Startar test 6a/115')
    try:
        if not word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'triennial'):
            print("Fel i test 6a/115: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'triennial')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 115: Exception')
        print_exception()

    print('Startar test 6a/116')
    try:
        if not word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'triennium'):
            print("Fel i test 6a/116: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'triennium')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 116: Exception')
        print_exception()

    print('Startar test 6a/117')
    try:
        if not word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trierarch'):
            print("Fel i test 6a/117: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trierarch')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 117: Exception')
        print_exception()

    print('Startar test 6a/118')
    try:
        if not word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trientes'):
            print("Fel i test 6a/118: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trientes')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 118: Exception')
        print_exception()

    print('Startar test 6a/119')
    try:
        if not word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'triennia'):
            print("Fel i test 6a/119: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'triennia')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 119: Exception')
        print_exception()

    print('Startar test 6a/120')
    try:
        if not word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'triethyl'):
            print("Fel i test 6a/120: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'triethyl')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 120: Exception')
        print_exception()

    print('Startar test 6a/121')
    try:
        if not word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trienes'):
            print("Fel i test 6a/121: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trienes')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 121: Exception')
        print_exception()

    print('Startar test 6a/122')
    try:
        if not word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'triene'):
            print("Fel i test 6a/122: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'triene')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 122: Exception')
        print_exception()

    print('Startar test 6a/123')
    try:
        if not word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'triens'):
            print("Fel i test 6a/123: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'triens')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 123: Exception')
        print_exception()

    print('Startar test 6a/124')
    try:
        if not word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'triers'):
            print("Fel i test 6a/124: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'triers')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 124: Exception')
        print_exception()

    print('Startar test 6a/125')
    try:
        if not word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'tried'):
            print("Fel i test 6a/125: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'tried')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 125: Exception')
        print_exception()

    print('Startar test 6a/126')
    try:
        if not word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'tries'):
            print("Fel i test 6a/126: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'tries')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 126: Exception')
        print_exception()

    print('Startar test 6a/127')
    try:
        if not word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trier'):
            print("Fel i test 6a/127: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trier')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 127: Exception')
        print_exception()

    print('Startar test 6a/128')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {}), 'En')
    except:
        print(f'Fel i test 128: Exception')
        print_exception()

    print('Startar test 6a/129')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})})}), 'Trie')
    except:
        print(f'Fel i test 129: Exception')
        print_exception()

    print('Startar test 6a/130')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})})}), 'Ã¤r')
    except:
        print(f'Fel i test 130: Exception')
        print_exception()

    print('Startar test 6a/131')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})})}), 'en')
    except:
        print(f'Fel i test 131: Exception')
        print_exception()

    print('Startar test 6a/132')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {})})}), 'effektiv')
    except:
        print(f'Fel i test 132: Exception')
        print_exception()

    print('Startar test 6a/133')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})})}), 'datastruktur')
    except:
        print(f'Fel i test 133: Exception')
        print_exception()

    print('Startar test 6a/134')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})})}), 'fÃ¶r')
    except:
        print(f'Fel i test 134: Exception')
        print_exception()

    print('Startar test 6a/135')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})})}), 'att')
    except:
        print(f'Fel i test 135: Exception')
        print_exception()

    print('Startar test 6a/136')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})})}), 'lagra')
    except:
        print(f'Fel i test 136: Exception')
        print_exception()

    print('Startar test 6a/137')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})})}), 'en')
    except:
        print(f'Fel i test 137: Exception')
        print_exception()

    print('Startar test 6a/138')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})})}), 'mÃ¤ngd')
    except:
        print(f'Fel i test 138: Exception')
        print_exception()

    print('Startar test 6a/139')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})})}), 'strÃ¤ngar')
    except:
        print(f'Fel i test 139: Exception')
        print_exception()

    print('Startar test 6a/140')
    try:
        if word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'ace'):
            print("Fel i test 6a/140: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'ace')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 140: Exception')
        print_exception()

    print('Startar test 6a/141')
    try:
        if word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'aced'):
            print("Fel i test 6a/141: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'aced')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 141: Exception')
        print_exception()

    print('Startar test 6a/142')
    try:
        if word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'aces'):
            print("Fel i test 6a/142: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'aces')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 142: Exception')
        print_exception()

    print('Startar test 6a/143')
    try:
        if word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'acre'):
            print("Fel i test 6a/143: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'acre')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 143: Exception')
        print_exception()

    print('Startar test 6a/144')
    try:
        if word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'acres'):
            print("Fel i test 6a/144: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'acres')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 144: Exception')
        print_exception()

    print('Startar test 6a/145')
    try:
        if word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'act'):
            print("Fel i test 6a/145: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'act')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 145: Exception')
        print_exception()

    print('Startar test 6a/146')
    try:
        if word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'acted'):
            print("Fel i test 6a/146: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'acted')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 146: Exception')
        print_exception()

    print('Startar test 6a/147')
    try:
        if word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'acting'):
            print("Fel i test 6a/147: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'acting')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 147: Exception')
        print_exception()

    print('Startar test 6a/148')
    try:
        if word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'acts'):
            print("Fel i test 6a/148: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'acts')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 148: Exception')
        print_exception()

    print('Startar test 6a/149')
    try:
        if not word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'En'):
            print("Fel i test 6a/149: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'En')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 149: Exception')
        print_exception()

    print('Startar test 6a/150')
    try:
        if not word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'Trie'):
            print("Fel i test 6a/150: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'Trie')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 150: Exception')
        print_exception()

    print('Startar test 6a/151')
    try:
        if not word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'Ã¤r'):
            print("Fel i test 6a/151: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'Ã¤r')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 151: Exception')
        print_exception()

    print('Startar test 6a/152')
    try:
        if not word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'en'):
            print("Fel i test 6a/152: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'en')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 152: Exception')
        print_exception()

    print('Startar test 6a/153')
    try:
        if not word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'effektiv'):
            print("Fel i test 6a/153: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'effektiv')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 153: Exception')
        print_exception()

    print('Startar test 6a/154')
    try:
        if not word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'datastruktur'):
            print("Fel i test 6a/154: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'datastruktur')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 154: Exception')
        print_exception()

    print('Startar test 6a/155')
    try:
        if not word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'fÃ¶r'):
            print("Fel i test 6a/155: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'fÃ¶r')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 155: Exception')
        print_exception()

    print('Startar test 6a/156')
    try:
        if not word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'att'):
            print("Fel i test 6a/156: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'att')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 156: Exception')
        print_exception()

    print('Startar test 6a/157')
    try:
        if not word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'lagra'):
            print("Fel i test 6a/157: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'lagra')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 157: Exception')
        print_exception()

    print('Startar test 6a/158')
    try:
        if not word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'en'):
            print("Fel i test 6a/158: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'en')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 158: Exception')
        print_exception()

    print('Startar test 6a/159')
    try:
        if not word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'mÃ¤ngd'):
            print("Fel i test 6a/159: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'mÃ¤ngd')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 159: Exception')
        print_exception()

    print('Startar test 6a/160')
    try:
        if not word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'strÃ¤ngar'):
            print("Fel i test 6a/160: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'strÃ¤ngar')")
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 160: Exception')
        print_exception()

    print('Startar test 6a/161')
    try:
        if word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'E'):
            print("Fel i test 6a/161: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'E')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 161: Exception')
        print_exception()

    print('Startar test 6a/162')
    try:
        if word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'Tri'):
            print("Fel i test 6a/162: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'Tri')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 162: Exception')
        print_exception()

    print('Startar test 6a/163')
    try:
        if word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'Ã¤rr'):
            print("Fel i test 6a/163: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'Ã¤rr')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 163: Exception')
        print_exception()

    print('Startar test 6a/164')
    try:
        if word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'e'):
            print("Fel i test 6a/164: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'e')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 164: Exception')
        print_exception()

    print('Startar test 6a/165')
    try:
        if word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'effekti'):
            print("Fel i test 6a/165: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'effekti')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 165: Exception')
        print_exception()

    print('Startar test 6a/166')
    try:
        if word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'datastruk'):
            print("Fel i test 6a/166: word_in_trie((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'datastruk')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 166: Exception')
        print_exception()

    print('Startar test 6a/167')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acred'):
            print("Fel i test 6a/167: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acred')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 167: Exception')
        print_exception()

    print('Startar test 6a/168')
    try:
        if word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'actes'):
            print("Fel i test 6a/168: word_in_trie((False, {'h': (False, {'e': (False, {'l': (False, {'l': (False, {'o': (True, {})})})})}), 'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'actes')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 168: Exception')
        print_exception()

    print('Startar test 6a/169')
    try:
        if word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trarchs'):
            print("Fel i test 6a/169: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trarchs')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 169: Exception')
        print_exception()

    print('Startar test 6a/170')
    try:
        if word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trietrietriene'):
            print("Fel i test 6a/170: word_in_trie((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trietrietriene')")
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 170: Exception')
        print_exception()


    print('Klar med tester fÃ¶r uppgift 6a')
    print()


# noinspection PyBroadException
def test_6b():
    print('PÃ¥bÃ¶rjar tester fÃ¶r uppgift 6b')

    print('Startar test 6b/1')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {}), 'ace')
    except:
        print(f'Fel i test 1: Exception')
        print_exception()

    print('Startar test 6b/2')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'a': (False, {'c': (False, {'e': (True, {})})})}), 'aced')
    except:
        print(f'Fel i test 2: Exception')
        print_exception()

    print('Startar test 6b/3')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {})})})})}), 'aces')
    except:
        print(f'Fel i test 3: Exception')
        print_exception()

    print('Startar test 6b/4')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})})})})}), 'acre')
    except:
        print(f'Fel i test 4: Exception')
        print_exception()

    print('Startar test 6b/5')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {})})})})}), 'acres')
    except:
        print(f'Fel i test 5: Exception')
        print_exception()

    print('Startar test 6b/6')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})})})})}), 'act')
    except:
        print(f'Fel i test 6: Exception')
        print_exception()

    print('Startar test 6b/7')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {})})})}), 'acted')
    except:
        print(f'Fel i test 7: Exception')
        print_exception()

    print('Startar test 6b/8')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})})})})})}), 'acting')
    except:
        print(f'Fel i test 8: Exception')
        print_exception()

    print('Startar test 6b/9')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})})})})})}), 'acts')
    except:
        print(f'Fel i test 9: Exception')
        print_exception()

    print('Startar test 6b/10')
    try:
        res = find_all_matches((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'ace')
        exp = {'ace', 'aced', 'aces'}
        if res != exp:
            print("Fel i test 6b/10: find_all_matches((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'ace')")
            print("Korrekt svar: {'ace', 'aced', 'aces'}")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 10: Exception')
        print_exception()

    print('Startar test 6b/11')
    try:
        res = find_all_matches((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acre')
        exp = {'acre', 'acres'}
        if res != exp:
            print("Fel i test 6b/11: find_all_matches((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acre')")
            print("Korrekt svar: {'acre', 'acres'}")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 11: Exception')
        print_exception()

    print('Startar test 6b/12')
    try:
        res = find_all_matches((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'act')
        exp = {'acted', 'acts', 'acting', 'act'}
        if res != exp:
            print("Fel i test 6b/12: find_all_matches((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'act')")
            print("Korrekt svar: {'acted', 'acts', 'acting', 'act'}")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 12: Exception')
        print_exception()

    print('Startar test 6b/13')
    try:
        res = find_all_matches((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acts')
        exp = {'acts'}
        if res != exp:
            print("Fel i test 6b/13: find_all_matches((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acts')")
            print("Korrekt svar: {'acts'}")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 13: Exception')
        print_exception()

    print('Startar test 6b/14')
    try:
        res = find_all_matches((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'actss')
        exp = set()
        if res != exp:
            print("Fel i test 6b/14: find_all_matches((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'actss')")
            print("Korrekt svar: set()")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 14: Exception')
        print_exception()

    print('Startar test 6b/15')
    try:
        res = find_all_matches((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'actz')
        exp = set()
        if res != exp:
            print("Fel i test 6b/15: find_all_matches((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'actz')")
            print("Korrekt svar: set()")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 15: Exception')
        print_exception()

    print('Startar test 6b/16')
    try:
        res = find_all_matches((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'actsor')
        exp = set()
        if res != exp:
            print("Fel i test 6b/16: find_all_matches((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'actsor')")
            print("Korrekt svar: set()")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 16: Exception')
        print_exception()

    print('Startar test 6b/17')
    try:
        res = find_all_matches((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acetone')
        exp = set()
        if res != exp:
            print("Fel i test 6b/17: find_all_matches((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'acetone')")
            print("Korrekt svar: set()")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 17: Exception')
        print_exception()

    print('Startar test 6b/18')
    try:
        res = find_all_matches((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'after')
        exp = set()
        if res != exp:
            print("Fel i test 6b/18: find_all_matches((False, {'a': (False, {'c': (False, {'e': (True, {'d': (True, {}), 's': (True, {})}), 'r': (False, {'e': (True, {'s': (True, {})})}), 't': (True, {'e': (False, {'d': (True, {})}), 'i': (False, {'n': (False, {'g': (True, {})})}), 's': (True, {})})})})}), 'after')")
            print("Korrekt svar: set()")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 18: Exception')
        print_exception()

    print('Startar test 6b/19')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {}), 'trierarchies')
    except:
        print(f'Fel i test 19: Exception')
        print_exception()

    print('Startar test 6b/20')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (False, {'i': (False, {'e': (False, {'s': (True, {})})})})})})})})})})})})}), 'triennially')
    except:
        print(f'Fel i test 20: Exception')
        print_exception()

    print('Startar test 6b/21')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (False, {'i': (False, {'e': (False, {'s': (True, {})})})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (False, {'l': (False, {'l': (False, {'y': (True, {})})})})})})})})})})})}), 'trierarchy')
    except:
        print(f'Fel i test 21: Exception')
        print_exception()

    print('Startar test 6b/22')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (False, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (False, {'l': (False, {'l': (False, {'y': (True, {})})})})})})})})})})})}), 'trienniums')
    except:
        print(f'Fel i test 22: Exception')
        print_exception()

    print('Startar test 6b/23')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (False, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (False, {'l': (False, {'l': (False, {'y': (True, {})})})}), 'u': (False, {'m': (False, {'s': (True, {})})})})})})})})})})}), 'triennials')
    except:
        print(f'Fel i test 23: Exception')
        print_exception()

    print('Startar test 6b/24')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (False, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (False, {'l': (False, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (False, {'s': (True, {})})})})})})})})})})}), 'trierarchs')
    except:
        print(f'Fel i test 24: Exception')
        print_exception()

    print('Startar test 6b/25')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (False, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (False, {'l': (False, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (False, {'s': (True, {})})})})})})})})})})}), 'triennial')
    except:
        print(f'Fel i test 25: Exception')
        print_exception()

    print('Startar test 6b/26')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (False, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (False, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (False, {'s': (True, {})})})})})})})})})})}), 'triennium')
    except:
        print(f'Fel i test 26: Exception')
        print_exception()

    print('Startar test 6b/27')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (False, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (False, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})})})})})})})}), 'trierarch')
    except:
        print(f'Fel i test 27: Exception')
        print_exception()

    print('Startar test 6b/28')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (False, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})})})})})})})}), 'trientes')
    except:
        print(f'Fel i test 28: Exception')
        print_exception()

    print('Startar test 6b/29')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (False, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})})})})})})})}), 'triennia')
    except:
        print(f'Fel i test 29: Exception')
        print_exception()

    print('Startar test 6b/30')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})})})})})})})}), 'triethyl')
    except:
        print(f'Fel i test 30: Exception')
        print_exception()

    print('Startar test 6b/31')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})})})})})})}), 'trienes')
    except:
        print(f'Fel i test 31: Exception')
        print_exception()

    print('Startar test 6b/32')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (False, {'s': (True, {})})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})})})})})})}), 'triene')
    except:
        print(f'Fel i test 32: Exception')
        print_exception()

    print('Startar test 6b/33')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})})})})})})}), 'triens')
    except:
        print(f'Fel i test 33: Exception')
        print_exception()

    print('Startar test 6b/34')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})})})})})})}), 'triers')
    except:
        print(f'Fel i test 34: Exception')
        print_exception()

    print('Startar test 6b/35')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})})})})})})}), 'tried')
    except:
        print(f'Fel i test 35: Exception')
        print_exception()

    print('Startar test 6b/36')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {})})})})})}), 'tries')
    except:
        print(f'Fel i test 36: Exception')
        print_exception()

    print('Startar test 6b/37')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (False, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trier')
    except:
        print(f'Fel i test 37: Exception')
        print_exception()

    print('Startar test 6b/38')
    try:
        res = find_all_matches((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'ace')
        exp = set()
        if res != exp:
            print("Fel i test 6b/38: find_all_matches((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'ace')")
            print("Korrekt svar: set()")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 38: Exception')
        print_exception()

    print('Startar test 6b/39')
    try:
        res = find_all_matches((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'z')
        exp = set()
        if res != exp:
            print("Fel i test 6b/39: find_all_matches((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'z')")
            print("Korrekt svar: set()")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 39: Exception')
        print_exception()

    print('Startar test 6b/40')
    try:
        res = find_all_matches((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'triesfoo')
        exp = set()
        if res != exp:
            print("Fel i test 6b/40: find_all_matches((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'triesfoo')")
            print("Korrekt svar: set()")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 40: Exception')
        print_exception()

    print('Startar test 6b/41')
    try:
        res = find_all_matches((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trierarchasdf')
        exp = set()
        if res != exp:
            print("Fel i test 6b/41: find_all_matches((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trierarchasdf')")
            print("Korrekt svar: set()")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 41: Exception')
        print_exception()

    print('Startar test 6b/42')
    try:
        res = find_all_matches((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trieneasdf')
        exp = set()
        if res != exp:
            print("Fel i test 6b/42: find_all_matches((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trieneasdf')")
            print("Korrekt svar: set()")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 42: Exception')
        print_exception()

    print('Startar test 6b/43')
    try:
        res = find_all_matches((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trien')
        exp = {'trientes', 'trienes', 'triennial', 'triens', 'triennially', 'trienniums', 'triennium', 'triennia', 'triennials', 'triene'}
        if res != exp:
            print("Fel i test 6b/43: find_all_matches((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trien')")
            print("Korrekt svar: {'trientes', 'trienes', 'triennial', 'triens', 'triennially', 'trienniums', 'triennium', 'triennia', 'triennials', 'triene'}")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 43: Exception')
        print_exception()

    print('Startar test 6b/44')
    try:
        res = find_all_matches((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trienn')
        exp = {'triennially', 'trienniums', 'triennium', 'triennia', 'triennials', 'triennial'}
        if res != exp:
            print("Fel i test 6b/44: find_all_matches((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'trienn')")
            print("Korrekt svar: {'triennially', 'trienniums', 'triennium', 'triennia', 'triennials', 'triennial'}")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 44: Exception')
        print_exception()

    print('Startar test 6b/45')
    try:
        res = find_all_matches((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'triennia')
        exp = {'triennia', 'triennials', 'triennial', 'triennially'}
        if res != exp:
            print("Fel i test 6b/45: find_all_matches((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'triennia')")
            print("Korrekt svar: {'triennia', 'triennials', 'triennial', 'triennially'}")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 45: Exception')
        print_exception()

    print('Startar test 6b/46')
    try:
        res = find_all_matches((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'triennial')
        exp = {'triennials', 'triennial', 'triennially'}
        if res != exp:
            print("Fel i test 6b/46: find_all_matches((False, {'t': (False, {'r': (False, {'i': (False, {'e': (False, {'r': (True, {'a': (False, {'r': (False, {'c': (False, {'h': (True, {'i': (False, {'e': (False, {'s': (True, {})})}), 'y': (True, {}), 's': (True, {})})})})}), 's': (True, {})}), 'n': (False, {'n': (False, {'i': (False, {'a': (True, {'l': (True, {'l': (False, {'y': (True, {})}), 's': (True, {})})}), 'u': (False, {'m': (True, {'s': (True, {})})})})}), 't': (False, {'e': (False, {'s': (True, {})})}), 'e': (True, {'s': (True, {})}), 's': (True, {})}), 't': (False, {'h': (False, {'y': (False, {'l': (True, {})})})}), 'd': (True, {}), 's': (True, {})})})})})}), 'triennial')")
            print("Korrekt svar: {'triennials', 'triennial', 'triennially'}")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 46: Exception')
        print_exception()

    print('Startar test 6b/47')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {}), 'En')
    except:
        print(f'Fel i test 47: Exception')
        print_exception()

    print('Startar test 6b/48')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})})}), 'Trie')
    except:
        print(f'Fel i test 48: Exception')
        print_exception()

    print('Startar test 6b/49')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})})}), 'Ã¤r')
    except:
        print(f'Fel i test 49: Exception')
        print_exception()

    print('Startar test 6b/50')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})})}), 'en')
    except:
        print(f'Fel i test 50: Exception')
        print_exception()

    print('Startar test 6b/51')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {})})}), 'effektiv')
    except:
        print(f'Fel i test 51: Exception')
        print_exception()

    print('Startar test 6b/52')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})})}), 'datastruktur')
    except:
        print(f'Fel i test 52: Exception')
        print_exception()

    print('Startar test 6b/53')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})})}), 'fÃ¶r')
    except:
        print(f'Fel i test 53: Exception')
        print_exception()

    print('Startar test 6b/54')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})})}), 'att')
    except:
        print(f'Fel i test 54: Exception')
        print_exception()

    print('Startar test 6b/55')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})})}), 'lagra')
    except:
        print(f'Fel i test 55: Exception')
        print_exception()

    print('Startar test 6b/56')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})})}), 'en')
    except:
        print(f'Fel i test 56: Exception')
        print_exception()

    print('Startar test 6b/57')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})})}), 'mÃ¤ngd')
    except:
        print(f'Fel i test 57: Exception')
        print_exception()

    print('Startar test 6b/58')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})})}), 'strÃ¤ngar')
    except:
        print(f'Fel i test 58: Exception')
        print_exception()

    print('Startar test 6b/59')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})})}), 'ha')
    except:
        print(f'Fel i test 59: Exception')
        print_exception()

    print('Startar test 6b/60')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})}), 'h': (False, {'a': (True, {})})}), 'ho')
    except:
        print(f'Fel i test 60: Exception')
        print_exception()

    print('Startar test 6b/61')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})}), 'h': (False, {'a': (True, {}), 'o': (True, {})})}), 'hu')
    except:
        print(f'Fel i test 61: Exception')
        print_exception()

    print('Startar test 6b/62')
    try:
        # (ReturnvÃ¤rdet Ã¤r irrelevant; funktionen anropas fÃ¶r sina sidoeffekter)
        add_word((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})}), 'h': (False, {'a': (True, {}), 'o': (True, {}), 'u': (True, {})})}), 'hÃ¥')
    except:
        print(f'Fel i test 62: Exception')
        print_exception()

    print('Startar test 6b/63')
    try:
        res = find_all_matches((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})}), 'h': (False, {'a': (True, {}), 'o': (True, {}), 'u': (True, {}), 'Ã¥': (True, {})})}), 'e')
        exp = {'effektiv', 'en'}
        if res != exp:
            print("Fel i test 6b/63: find_all_matches((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})}), 'h': (False, {'a': (True, {}), 'o': (True, {}), 'u': (True, {}), 'Ã¥': (True, {})})}), 'e')")
            print("Korrekt svar: {'effektiv', 'en'}")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 63: Exception')
        print_exception()

    print('Startar test 6b/64')
    try:
        res = find_all_matches((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})}), 'h': (False, {'a': (True, {}), 'o': (True, {}), 'u': (True, {}), 'Ã¥': (True, {})})}), 'a')
        exp = {'att'}
        if res != exp:
            print("Fel i test 6b/64: find_all_matches((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})}), 'h': (False, {'a': (True, {}), 'o': (True, {}), 'u': (True, {}), 'Ã¥': (True, {})})}), 'a')")
            print("Korrekt svar: {'att'}")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 64: Exception')
        print_exception()

    print('Startar test 6b/65')
    try:
        res = find_all_matches((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})}), 'h': (False, {'a': (True, {}), 'o': (True, {}), 'u': (True, {}), 'Ã¥': (True, {})})}), 'h')
        exp = {'hu', 'ha', 'ho', 'hÃ¥'}
        if res != exp:
            print("Fel i test 6b/65: find_all_matches((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})}), 'h': (False, {'a': (True, {}), 'o': (True, {}), 'u': (True, {}), 'Ã¥': (True, {})})}), 'h')")
            print("Korrekt svar: {'hu', 'ha', 'ho', 'hÃ¥'}")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 65: Exception')
        print_exception()

    print('Startar test 6b/66')
    try:
        res = find_all_matches((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})}), 'h': (False, {'a': (True, {}), 'o': (True, {}), 'u': (True, {}), 'Ã¥': (True, {})})}), 'q')
        exp = set()
        if res != exp:
            print("Fel i test 6b/66: find_all_matches((False, {'E': (False, {'n': (True, {})}), 'T': (False, {'r': (False, {'i': (False, {'e': (True, {})})})}), 'Ã¤': (False, {'r': (True, {})}), 'e': (False, {'n': (True, {}), 'f': (False, {'f': (False, {'e': (False, {'k': (False, {'t': (False, {'i': (False, {'v': (True, {})})})})})})})}), 'd': (False, {'a': (False, {'t': (False, {'a': (False, {'s': (False, {'t': (False, {'r': (False, {'u': (False, {'k': (False, {'t': (False, {'u': (False, {'r': (True, {})})})})})})})})})})})}), 'f': (False, {'Ã¶': (False, {'r': (True, {})})}), 'a': (False, {'t': (False, {'t': (True, {})})}), 'l': (False, {'a': (False, {'g': (False, {'r': (False, {'a': (True, {})})})})}), 'm': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'d': (True, {})})})})}), 's': (False, {'t': (False, {'r': (False, {'Ã¤': (False, {'n': (False, {'g': (False, {'a': (False, {'r': (True, {})})})})})})})}), 'h': (False, {'a': (True, {}), 'o': (True, {}), 'u': (True, {}), 'Ã¥': (True, {})})}), 'q')")
            print("Korrekt svar: set()")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 66: Exception')
        print_exception()


    print('Klar med tester fÃ¶r uppgift 6b')
    print()

if __name__ == '__main__':
    test_1()
    test_2()
    test_2()
    test_3()
    test_4a()
    test_4b()
    test_5a()
    test_5b()
    test_5c()
    test_6a()
    test_6b()
