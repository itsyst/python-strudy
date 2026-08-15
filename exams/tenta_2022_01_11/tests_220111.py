"""
HÃ¤r finns ett antal testfall fÃ¶r uppgifter i en tenta i TDDE24.

Testfallen Ã¤r skapade frÃ¥n anrop till ett egenutvecklat testramverk, som
ocksÃ¥ samlar ihop testresultat och kategoriserar olika problem som kan
uppstÃ¥.  De har alltsÃ¥ inte kÃ¶rts exakt sÃ¥ som de stÃ¥r hÃ¤r.

Som en hjÃ¤lp finns lÃ¶sningsfÃ¶rslagen med i filen.  ErsÃ¤tt dem med egna
lÃ¶sningar och kÃ¶r filen i Python 3.9 (python test.py) fÃ¶r att se om du har
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
Denna fil innehÃ¥ller ett antal lÃ¶sningsfÃ¶rslag fÃ¶r tentan i TDDE24 januari 2022.

Det finns alltid mÃ¥nga olika sÃ¤tt att lÃ¶sa en uppgift, och bara fÃ¶r att
lÃ¶sningsfÃ¶rslaget ser ut pÃ¥ ett visst sÃ¤tt betyder det inte att detta Ã¤r
det enda, eller ens det allra bÃ¤sta sÃ¤ttet att lÃ¶sa en uppgift.
"""


def gapful(n: int):
    digits = str(n)
    divisor = int(digits[0] + digits[-1])
    return n % divisor == 0


def reverse_pairs(seq: list):
    result = []

    for pos in range(0, len(seq), 2):
        if pos + 1 < len(seq):
            result.append(seq[pos + 1])
        result.append(seq[pos])

    return result


def reverse_pairs_r(seq: list):
    if not seq:
        return []
    elif len(seq) == 1:
        return seq
    else:
        return [seq[1], seq[0]] + reverse_pairs_r(seq[2:])


def doubled_odds(seq: list):
    result = []
    for element in seq:
        if isinstance(element, list):
            # Rekursera ner i listor fÃ¶r att behandla deras element
            result.append(doubled_odds(element))
        elif isinstance(element, int) and element % 2 == 1:
            # Specialbehandla udda heltal
            result.append(element * 2)
        else:
            # Allt annat Ã¤r bara godtyckliga element som "kopieras Ã¶ver"
            result.append(element)
    return result


def multiple_apply(fn, times: int):
    def retfun(x):
        for k in range(times):
            x = fn(x)
        return x

    return retfun


def pow2(n: int):
    return multiple_apply(lambda y: 2 * y, n)(1)


def pow2mult(n: int, c: int):
    multiplier = multiple_apply(lambda y: 2 * y, n)
    return multiplier(c)


def is_prime(n: int):
    if n < 2:
        return False
    for divisor in range(2, int(math.sqrt(n)) + 1):
        if n % divisor == 0:
            return False
    return True


def is_prime_2(n: int):
    return n >= 2 and all(n % divisor != 0 for divisor in range(2, int(math.sqrt(n)) + 1))


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


def all_splits(seq):
    if not seq:
        return [([], [])]

    ret = []
    for seq1, seq2 in all_splits(seq[1:]):
        ret.append((seq1 + [seq[0]], seq2))
        ret.append((seq1, seq2 + [seq[0]]))

    return ret


def minimize_differences(seq: list[int]):
    splits = all_splits(seq)
    best = splits[0]
    best_diff = abs(sum(best[0]) - sum(best[1]))

    for candidate in splits[1:]:
        candidate_diff = abs(sum(candidate[0]) - sum(candidate[1]))
        if candidate_diff < best_diff:
            best_diff = candidate_diff
            best = candidate

    return best


def minimize_differences_2(seq: list[int]):
    return min(all_splits(seq), key=lambda p: abs(sum(p[0]) - sum(p[1])))

# HÃ¤r lÃ¤gger du egna lÃ¶sningar!


# HÃ¤r finns extra funktioner som inte ingÃ¥r i lÃ¶sningarna, men som anvÃ¤nds
# av testfallen.
import math

def print_exception():
    import traceback
    import sys
    print(f"    {sys.exc_info()[0]}")

    for line in traceback.format_exc().split("\n"):
        print(f"    " + line)


def recursive(x):
    if x <= 1:
        return 1
    else:
        return recursive(x // 2) + recursive(x // 3)


def plus_one_point_five(x):
    return x + 1.5


def plus_one(x):
    return x + 1


def const_one(x):
    return 1


def minus_one(x):
    return x - 1


def times_two(x):
    return x * 2


def fib(x):
    n = [1, 1]
    while x > len(n):
        n.append(n[-1] + n[-2])
    return n[-1]



def test_1():
    print('PÃ¥bÃ¶rjar tester fÃ¶r uppgift 1')

    try:
        if not gapful(100):
            print('Fel i test 1/1: gapful(100)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 1/1: Exception')
        print_exception()

    try:
        if gapful(101):
            print('Fel i test 1/2: gapful(101)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/2: Exception')
        print_exception()

    try:
        if not gapful(105):
            print('Fel i test 1/3: gapful(105)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 1/3: Exception')
        print_exception()

    try:
        if gapful(106):
            print('Fel i test 1/4: gapful(106)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/4: Exception')
        print_exception()

    try:
        if not gapful(54288):
            print('Fel i test 1/5: gapful(54288)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 1/5: Exception')
        print_exception()

    try:
        if gapful(102):
            print('Fel i test 1/6: gapful(102)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/6: Exception')
        print_exception()

    try:
        if gapful(103):
            print('Fel i test 1/7: gapful(103)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/7: Exception')
        print_exception()

    try:
        if gapful(104):
            print('Fel i test 1/8: gapful(104)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/8: Exception')
        print_exception()

    try:
        if gapful(107):
            print('Fel i test 1/9: gapful(107)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/9: Exception')
        print_exception()

    try:
        if not gapful(108):
            print('Fel i test 1/10: gapful(108)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 1/10: Exception')
        print_exception()

    try:
        if gapful(109):
            print('Fel i test 1/11: gapful(109)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/11: Exception')
        print_exception()

    try:
        if not gapful(110):
            print('Fel i test 1/12: gapful(110)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 1/12: Exception')
        print_exception()

    try:
        if gapful(111):
            print('Fel i test 1/13: gapful(111)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/13: Exception')
        print_exception()

    try:
        if gapful(112):
            print('Fel i test 1/14: gapful(112)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/14: Exception')
        print_exception()

    try:
        if gapful(113):
            print('Fel i test 1/15: gapful(113)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/15: Exception')
        print_exception()

    try:
        if gapful(114):
            print('Fel i test 1/16: gapful(114)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/16: Exception')
        print_exception()

    try:
        if gapful(115):
            print('Fel i test 1/17: gapful(115)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/17: Exception')
        print_exception()

    try:
        if gapful(116):
            print('Fel i test 1/18: gapful(116)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/18: Exception')
        print_exception()

    try:
        if gapful(117):
            print('Fel i test 1/19: gapful(117)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/19: Exception')
        print_exception()

    try:
        if gapful(118):
            print('Fel i test 1/20: gapful(118)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/20: Exception')
        print_exception()

    try:
        if gapful(119):
            print('Fel i test 1/21: gapful(119)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/21: Exception')
        print_exception()

    try:
        if not gapful(120):
            print('Fel i test 1/22: gapful(120)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 1/22: Exception')
        print_exception()

    try:
        if not gapful(121):
            print('Fel i test 1/23: gapful(121)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 1/23: Exception')
        print_exception()

    try:
        if gapful(122):
            print('Fel i test 1/24: gapful(122)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/24: Exception')
        print_exception()

    try:
        if gapful(123):
            print('Fel i test 1/25: gapful(123)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/25: Exception')
        print_exception()

    try:
        if gapful(124):
            print('Fel i test 1/26: gapful(124)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/26: Exception')
        print_exception()

    try:
        if gapful(125):
            print('Fel i test 1/27: gapful(125)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/27: Exception')
        print_exception()

    try:
        if gapful(126):
            print('Fel i test 1/28: gapful(126)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/28: Exception')
        print_exception()

    try:
        if gapful(127):
            print('Fel i test 1/29: gapful(127)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/29: Exception')
        print_exception()

    try:
        if gapful(128):
            print('Fel i test 1/30: gapful(128)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/30: Exception')
        print_exception()

    try:
        if gapful(129):
            print('Fel i test 1/31: gapful(129)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/31: Exception')
        print_exception()

    try:
        if not gapful(130):
            print('Fel i test 1/32: gapful(130)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 1/32: Exception')
        print_exception()

    try:
        if gapful(131):
            print('Fel i test 1/33: gapful(131)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/33: Exception')
        print_exception()

    try:
        if not gapful(132):
            print('Fel i test 1/34: gapful(132)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 1/34: Exception')
        print_exception()

    try:
        if gapful(133):
            print('Fel i test 1/35: gapful(133)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/35: Exception')
        print_exception()

    try:
        if gapful(134):
            print('Fel i test 1/36: gapful(134)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/36: Exception')
        print_exception()

    try:
        if not gapful(135):
            print('Fel i test 1/37: gapful(135)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 1/37: Exception')
        print_exception()

    try:
        if gapful(136):
            print('Fel i test 1/38: gapful(136)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/38: Exception')
        print_exception()

    try:
        if gapful(137):
            print('Fel i test 1/39: gapful(137)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/39: Exception')
        print_exception()

    try:
        if gapful(138):
            print('Fel i test 1/40: gapful(138)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/40: Exception')
        print_exception()

    try:
        if gapful(139):
            print('Fel i test 1/41: gapful(139)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 1/41: Exception')
        print_exception()


    print('Klar med tester fÃ¶r uppgift 1')
    print()


def test_2a():
    print('PÃ¥bÃ¶rjar tester fÃ¶r uppgift 2a')

    try:
        res = reverse_pairs([])
        exp = []
        if res != exp:
            print("Fel i test 2a/1: reverse_pairs([])")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/1: Exception')
        print_exception()

    try:
        res = reverse_pairs([1, 2, 'x', 4])
        exp = [2, 1, 4, 'x']
        if res != exp:
            print("Fel i test 2a/2: reverse_pairs([1, 2, 'x', 4])")
            print("Korrekt svar: 2, 1, 4, 'x'")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/2: Exception')
        print_exception()

    try:
        res = reverse_pairs([1, 2, 3, 4, 5])
        exp = [2, 1, 4, 3, 5]
        if res != exp:
            print("Fel i test 2a/3: reverse_pairs([1, 2, 3, 4, 5])")
            print("Korrekt svar: 2, 1, 4, 3, 5")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/3: Exception')
        print_exception()

    try:
        res = reverse_pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
        exp = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 13]
        if res != exp:
            print("Fel i test 2a/4: reverse_pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])")
            print("Korrekt svar: 2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 13")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/4: Exception')
        print_exception()

    try:
        res = reverse_pairs([1])
        exp = [1]
        if res != exp:
            print("Fel i test 2a/5: reverse_pairs([1])")
            print("Korrekt svar: 1")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/5: Exception')
        print_exception()

    try:
        res = reverse_pairs(['a'])
        exp = ['a']
        if res != exp:
            print("Fel i test 2a/6: reverse_pairs(['a'])")
            print("Korrekt svar: 'a'")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/6: Exception')
        print_exception()

    try:
        res = reverse_pairs([False])
        exp = [False]
        if res != exp:
            print("Fel i test 2a/7: reverse_pairs([False])")
            print("Korrekt svar: False")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/7: Exception')
        print_exception()

    try:
        res = reverse_pairs([0.1])
        exp = [0.1]
        if res != exp:
            print("Fel i test 2a/8: reverse_pairs([0.1])")
            print("Korrekt svar: 0.1")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/8: Exception')
        print_exception()

    try:
        res = reverse_pairs([5, 467, 123, 4567, 879, 345, 89, 90, 78, 345])
        exp = [467, 5, 4567, 123, 345, 879, 90, 89, 345, 78]
        if res != exp:
            print("Fel i test 2a/9: reverse_pairs([5, 467, 123, 4567, 879, 345, 89, 90, 78, 345])")
            print("Korrekt svar: 467, 5, 4567, 123, 345, 879, 90, 89, 345, 78")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/9: Exception')
        print_exception()

    try:
        res = reverse_pairs([0])
        exp = [0]
        if res != exp:
            print("Fel i test 2a/10: reverse_pairs([0])")
            print("Korrekt svar: 0")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/10: Exception')
        print_exception()

    try:
        res = reverse_pairs([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        exp = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8]
        if res != exp:
            print("Fel i test 2a/11: reverse_pairs([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])")
            print("Korrekt svar: 1, 0, 3, 2, 5, 4, 7, 6, 9, 8")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/11: Exception')
        print_exception()

    try:
        res = reverse_pairs([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
        exp = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26, 29, 28, 31, 30, 33, 32, 35, 34, 37, 36, 39, 38, 41, 40, 43, 42, 45, 44, 47, 46, 49, 48, 51, 50, 53, 52, 55, 54, 57, 56, 59, 58, 61, 60, 63, 62, 65, 64, 67, 66, 69, 68, 71, 70, 73, 72, 75, 74, 77, 76, 79, 78, 81, 80, 83, 82, 85, 84, 87, 86, 89, 88, 91, 90, 93, 92, 95, 94, 97, 96, 99, 98]
        if res != exp:
            print("Fel i test 2a/12: reverse_pairs([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])")
            print("Korrekt svar: 1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26, 29, 28, 31, 30, 33, 32, 35, 34, 37, 36, 39, 38, 41, 40, 43, 42, 45, 44, 47, 46, 49, 48, 51, 50, 53, 52, 55, 54, 57, 56, 59, 58, 61, 60, 63, 62, 65, 64, 67, 66, 69, 68, 71, 70, 73, 72, 75, 74, 77, 76, 79, 78, 81, 80, 83, 82, 85, 84, 87, 86, 89, 88, 91, 90, 93, 92, 95, 94, 97, 96, 99, 98")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/12: Exception')
        print_exception()

    try:
        res = reverse_pairs([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9])
        exp = [9, 10, 7, 8, 5, 6, 3, 4, 1, 2, -1, 0, -3, -2, -5, -4, -7, -6, -9, -8]
        if res != exp:
            print("Fel i test 2a/13: reverse_pairs([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9])")
            print("Korrekt svar: 9, 10, 7, 8, 5, 6, 3, 4, 1, 2, -1, 0, -3, -2, -5, -4, -7, -6, -9, -8")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/13: Exception')
        print_exception()

    try:
        res = reverse_pairs([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
        exp = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        if res != exp:
            print("Fel i test 2a/14: reverse_pairs([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])")
            print("Korrekt svar: 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/14: Exception')
        print_exception()

    try:
        res = reverse_pairs([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
        exp = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        if res != exp:
            print("Fel i test 2a/15: reverse_pairs([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])")
            print("Korrekt svar: 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/15: Exception')
        print_exception()

    try:
        res = reverse_pairs([0, 11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220, 231, 242, 253, 264, 275, 286, 297, 308, 319, 330, 341, 352, 363, 374, 385, 396, 407, 418, 429, 440, 451, 462, 473, 484, 495, 506, 517, 528, 539, 550, 561, 572, 583, 594, 605, 616, 627, 638, 649, 660, 671, 682, 693, 704, 715, 726, 737, 748, 759, 770, 781, 792, 803, 814, 825, 836, 847, 858, 869, 880, 891, 902, 913, 924, 935, 946, 957, 968, 979, 990])
        exp = [11, 0, 33, 22, 55, 44, 77, 66, 99, 88, 121, 110, 143, 132, 165, 154, 187, 176, 209, 198, 231, 220, 253, 242, 275, 264, 297, 286, 319, 308, 341, 330, 363, 352, 385, 374, 407, 396, 429, 418, 451, 440, 473, 462, 495, 484, 517, 506, 539, 528, 561, 550, 583, 572, 605, 594, 627, 616, 649, 638, 671, 660, 693, 682, 715, 704, 737, 726, 759, 748, 781, 770, 803, 792, 825, 814, 847, 836, 869, 858, 891, 880, 913, 902, 935, 924, 957, 946, 979, 968, 990]
        if res != exp:
            print("Fel i test 2a/16: reverse_pairs([0, 11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220, 231, 242, 253, 264, 275, 286, 297, 308, 319, 330, 341, 352, 363, 374, 385, 396, 407, 418, 429, 440, 451, 462, 473, 484, 495, 506, 517, 528, 539, 550, 561, 572, 583, 594, 605, 616, 627, 638, 649, 660, 671, 682, 693, 704, 715, 726, 737, 748, 759, 770, 781, 792, 803, 814, 825, 836, 847, 858, 869, 880, 891, 902, 913, 924, 935, 946, 957, 968, 979, 990])")
            print("Korrekt svar: 11, 0, 33, 22, 55, 44, 77, 66, 99, 88, 121, 110, 143, 132, 165, 154, 187, 176, 209, 198, 231, 220, 253, 242, 275, 264, 297, 286, 319, 308, 341, 330, 363, 352, 385, 374, 407, 396, 429, 418, 451, 440, 473, 462, 495, 484, 517, 506, 539, 528, 561, 550, 583, 572, 605, 594, 627, 616, 649, 638, 671, 660, 693, 682, 715, 704, 737, 726, 759, 748, 781, 770, 803, 792, 825, 814, 847, 836, 869, 858, 891, 880, 913, 902, 935, 924, 957, 946, 979, 968, 990")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/16: Exception')
        print_exception()

    try:
        res = reverse_pairs(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
        exp = ['b', 'a', 'd', 'c', 'f', 'e', 'g']
        if res != exp:
            print("Fel i test 2a/17: reverse_pairs(['a', 'b', 'c', 'd', 'e', 'f', 'g'])")
            print("Korrekt svar: 'b', 'a', 'd', 'c', 'f', 'e', 'g'")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/17: Exception')
        print_exception()

    try:
        res = reverse_pairs(['Ã¥', 'Ã¤', 'Ã¶', 'Ã¢', 'Ã´', 'Ãª', 'Ã¡', 'Ã³', 'Ã©'])
        exp = ['Ã¤', 'Ã¥', 'Ã¢', 'Ã¶', 'Ãª', 'Ã´', 'Ã³', 'Ã¡', 'Ã©']
        if res != exp:
            print("Fel i test 2a/18: reverse_pairs(['Ã¥', 'Ã¤', 'Ã¶', 'Ã¢', 'Ã´', 'Ãª', 'Ã¡', 'Ã³', 'Ã©'])")
            print("Korrekt svar: 'Ã¤', 'Ã¥', 'Ã¢', 'Ã¶', 'Ãª', 'Ã´', 'Ã³', 'Ã¡', 'Ã©'")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/18: Exception')
        print_exception()

    try:
        res = reverse_pairs(['', '', '', ''])
        exp = ['', '', '', '']
        if res != exp:
            print("Fel i test 2a/19: reverse_pairs(['', '', '', ''])")
            print("Korrekt svar: '', '', '', ''")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/19: Exception')
        print_exception()

    try:
        res = reverse_pairs([' ', '', ' ', ''])
        exp = ['', ' ', '', ' ']
        if res != exp:
            print("Fel i test 2a/20: reverse_pairs([' ', '', ' ', ''])")
            print("Korrekt svar: '', ' ', '', ' '")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/20: Exception')
        print_exception()

    try:
        res = reverse_pairs(['nÃ¥gra', 'strÃ¤ngar', 'av', 'olika', 'lÃ¤ngd', 'i', 'hav', 'totalfÃ¶rstÃ¶rt', 'frÃ¥n', 'laxmassor'])
        exp = ['strÃ¤ngar', 'nÃ¥gra', 'olika', 'av', 'i', 'lÃ¤ngd', 'totalfÃ¶rstÃ¶rt', 'hav', 'laxmassor', 'frÃ¥n']
        if res != exp:
            print("Fel i test 2a/21: reverse_pairs(['nÃ¥gra', 'strÃ¤ngar', 'av', 'olika', 'lÃ¤ngd', 'i', 'hav', 'totalfÃ¶rstÃ¶rt', 'frÃ¥n', 'laxmassor'])")
            print("Korrekt svar: 'strÃ¤ngar', 'nÃ¥gra', 'olika', 'av', 'i', 'lÃ¤ngd', 'totalfÃ¶rstÃ¶rt', 'hav', 'laxmassor', 'frÃ¥n'")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/21: Exception')
        print_exception()

    try:
        res = reverse_pairs([' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', ''])
        exp = ['', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', '']
        if res != exp:
            print("Fel i test 2a/22: reverse_pairs([' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', ''])")
            print("Korrekt svar: '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ''")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/22: Exception')
        print_exception()

    try:
        res = reverse_pairs(['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '\x7f', '\x80', '\x81', '\x82', '\x83', '\x84', '\x85', '\x86', '\x87', '\x88', '\x89', '\x8a', '\x8b', '\x8c', '\x8d', '\x8e', '\x8f', '\x90', '\x91', '\x92', '\x93', '\x94', '\x95'])
        exp = ['\x01', '\x00', '\x03', '\x02', '\x05', '\x04', '\x07', '\x06', '\t', '\x08', '\x0b', '\n', '\r', '\x0c', '\x0f', '\x0e', '\x11', '\x10', '\x13', '\x12', '\x15', '\x14', '\x17', '\x16', '\x19', '\x18', '\x1b', '\x1a', '\x1d', '\x1c', '\x1f', '\x1e', '!', ' ', '#', '"', '%', '$', "'", '&', ')', '(', '+', '*', '-', ',', '/', '.', '1', '0', '3', '2', '5', '4', '7', '6', '9', '8', ';', ':', '=', '<', '?', '>', 'A', '@', 'C', 'B', 'E', 'D', 'G', 'F', 'I', 'H', 'K', 'J', 'M', 'L', 'O', 'N', 'Q', 'P', 'S', 'R', 'U', 'T', 'W', 'V', 'Y', 'X', '[', 'Z', ']', '\\', '_', '^', 'a', '`', 'c', 'b', 'e', 'd', 'g', 'f', 'i', 'h', 'k', 'j', 'm', 'l', 'o', 'n', 'q', 'p', 's', 'r', 'u', 't', 'w', 'v', 'y', 'x', '{', 'z', '}', '|', '\x7f', '~', '\x81', '\x80', '\x83', '\x82', '\x85', '\x84', '\x87', '\x86', '\x89', '\x88', '\x8b', '\x8a', '\x8d', '\x8c', '\x8f', '\x8e', '\x91', '\x90', '\x93', '\x92', '\x95', '\x94']
        if res != exp:
            print("Fel i test 2a/23: reverse_pairs([\'\\x00\', \'\\x01\', \'\\x02\', \'\\x03\', \'\\x04\', \'\\x05\', \'\\x06\', \'\\x07\', \'\\x08\', \'\\t\', \'\\n\', \'\\x0b\', \'\\x0c\', \'\\r\', \'\\x0e\', \'\\x0f\', \'\\x10\', \'\\x11\', \'\\x12\', \'\\x13\', \'\\x14\', \'\\x15\', \'\\x16\', \'\\x17\', \'\\x18\', \'\\x19\', \'\\x1a\', \'\\x1b\', \'\\x1c\', \'\\x1d\', \'\\x1e\', \'\\x1f\', \' \', \'!\', \'\"\', \'#\', \'$\', \'%\', \'&\', \"\'\", \'(\', \')\', \'*\', \'+\', \',\', \'-\', \'.\', \'/\', \'0\', \'1\', \'2\', \'3\', \'4\', \'5\', \'6\', \'7\', \'8\', \'9\', \':\', \';\', \'<\', \'=\', \'>\', \'?\', \'@\', \'A\', \'B\', \'C\', \'D\', \'E\', \'F\', \'G\', \'H\', \'I\', \'J\', \'K\', \'L\', \'M\', \'N\', \'O\', \'P\', \'Q\', \'R\', \'S\', \'T\', \'U\', \'V\', \'W\', \'X\', \'Y\', \'Z\', \'[\', \'\\\\\', \']\', \'^\', \'_\', \'`\', \'a\', \'b\', \'c\', \'d\', \'e\', \'f\', \'g\', \'h\', \'i\', \'j\', \'k\', \'l\', \'m\', \'n\', \'o\', \'p\', \'q\', \'r\', \'s\', \'t\', \'u\', \'v\', \'w\', \'x\', \'y\', \'z\', \'{\', \'|\', \'}\', \'~\', \'\\x7f\', \'\\x80\', \'\\x81\', \'\\x82\', \'\\x83\', \'\\x84\', \'\\x85\', \'\\x86\', \'\\x87\', \'\\x88\', \'\\x89\', \'\\x8a\', \'\\x8b\', \'\\x8c\', \'\\x8d\', \'\\x8e\', \'\\x8f\', \'\\x90\', \'\\x91\', \'\\x92\', \'\\x93\', \'\\x94\', \'\\x95\'])")
            print("Korrekt svar: '\x01', '\x00', '\x03', '\x02', '\x05', '\x04', '\x07', '\x06', '\t', '\x08', '\x0b', '\n', '\r', '\x0c', '\x0f', '\x0e', '\x11', '\x10', '\x13', '\x12', '\x15', '\x14', '\x17', '\x16', '\x19', '\x18', '\x1b', '\x1a', '\x1d', '\x1c', '\x1f', '\x1e', '!', ' ', '#', '\"', '%', '$', \"'\", '&', ')', '(', '+', '*', '-', ',', '/', '.', '1', '0', '3', '2', '5', '4', '7', '6', '9', '8', ';', ':', '=', '<', '?', '>', 'A', '@', 'C', 'B', 'E', 'D', 'G', 'F', 'I', 'H', 'K', 'J', 'M', 'L', 'O', 'N', 'Q', 'P', 'S', 'R', 'U', 'T', 'W', 'V', 'Y', 'X', '[', 'Z', ']', '\\', '_', '^', 'a', '`', 'c', 'b', 'e', 'd', 'g', 'f', 'i', 'h', 'k', 'j', 'm', 'l', 'o', 'n', 'q', 'p', 's', 'r', 'u', 't', 'w', 'v', 'y', 'x', '{', 'z', '}', '|', '\x7f', '~', '\x81', '\x80', '\x83', '\x82', '\x85', '\x84', '\x87', '\x86', '\x89', '\x88', '\x8b', '\x8a', '\x8d', '\x8c', '\x8f', '\x8e', '\x91', '\x90', '\x93', '\x92', '\x95', '\x94'")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/23: Exception')
        print_exception()

    try:
        res = reverse_pairs(['', '\x01', '\x02\x02', '\x03\x03\x03', '\x04\x04\x04\x04', '\x05\x05\x05\x05\x05', '\x06\x06\x06\x06\x06\x06', '\x07\x07\x07\x07\x07\x07\x07', '\x08\x08\x08\x08\x08\x08\x08\x08', '\t\t\t\t\t\t\t\t\t', '\n\n\n\n\n\n\n\n\n\n', '\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b', '\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c', '\r\r\r\r\r\r\r\r\r\r\r\r\r', '\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e', '\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f', '\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10', '\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11', '\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12', '\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13', '\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14', '\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15', '\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16', '\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17', '\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18', '\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19', '\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a', '\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b', '\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c', '\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d', '\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e', '\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f', '                                ', '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', '""""""""""""""""""""""""""""""""""', '###################################', '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$', '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%', '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&', "'''''''''''''''''''''''''''''''''''''''", '((((((((((((((((((((((((((((((((((((((((', ')))))))))))))))))))))))))))))))))))))))))', '******************************************', '+++++++++++++++++++++++++++++++++++++++++++', ',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,', '---------------------------------------------', '..............................................', '///////////////////////////////////////////////', '000000000000000000000000000000000000000000000000', '1111111111111111111111111111111111111111111111111', '22222222222222222222222222222222222222222222222222', '333333333333333333333333333333333333333333333333333', '4444444444444444444444444444444444444444444444444444', '55555555555555555555555555555555555555555555555555555', '666666666666666666666666666666666666666666666666666666', '7777777777777777777777777777777777777777777777777777777', '88888888888888888888888888888888888888888888888888888888', '999999999999999999999999999999999999999999999999999999999', '::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', ';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;', '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<', '=============================================================', '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', '???????????????????????????????????????????????????????????????', '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB', 'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC', 'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD', 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE', 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF', 'GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG', 'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH', 'IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII', 'JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ', 'KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK', 'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL', 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM', 'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN', 'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO', 'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP', 'QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ', 'RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR', 'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS', 'TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT', 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU', 'VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV', 'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY', 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ', '[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[', '\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\', ']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]', '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^', '_______________________________________________________________________________________________', '````````````````````````````````````````````````````````````````````````````````````````````````', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb', 'ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'])
        exp = ['\x01', '', '\x03\x03\x03', '\x02\x02', '\x05\x05\x05\x05\x05', '\x04\x04\x04\x04', '\x07\x07\x07\x07\x07\x07\x07', '\x06\x06\x06\x06\x06\x06', '\t\t\t\t\t\t\t\t\t', '\x08\x08\x08\x08\x08\x08\x08\x08', '\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b', '\n\n\n\n\n\n\n\n\n\n', '\r\r\r\r\r\r\r\r\r\r\r\r\r', '\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c', '\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f', '\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e', '\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11', '\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10', '\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13', '\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12', '\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15', '\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14', '\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17', '\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16', '\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19', '\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18', '\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b', '\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a', '\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d', '\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c', '\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f', '\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e', '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', '                                ', '###################################', '""""""""""""""""""""""""""""""""""', '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%', '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$', "'''''''''''''''''''''''''''''''''''''''", '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&', ')))))))))))))))))))))))))))))))))))))))))', '((((((((((((((((((((((((((((((((((((((((', '+++++++++++++++++++++++++++++++++++++++++++', '******************************************', '---------------------------------------------', ',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,', '///////////////////////////////////////////////', '..............................................', '1111111111111111111111111111111111111111111111111', '000000000000000000000000000000000000000000000000', '333333333333333333333333333333333333333333333333333', '22222222222222222222222222222222222222222222222222', '55555555555555555555555555555555555555555555555555555', '4444444444444444444444444444444444444444444444444444', '7777777777777777777777777777777777777777777777777777777', '666666666666666666666666666666666666666666666666666666', '999999999999999999999999999999999999999999999999999999999', '88888888888888888888888888888888888888888888888888888888', ';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;', '::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', '=============================================================', '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<', '???????????????????????????????????????????????????????????????', '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@', 'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC', 'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB', 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE', 'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD', 'GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG', 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF', 'IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII', 'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH', 'KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK', 'JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ', 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM', 'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL', 'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO', 'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN', 'QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ', 'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP', 'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS', 'RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR', 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU', 'TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT', 'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW', 'VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV', 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[', 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ', ']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]', '\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\', '_______________________________________________________________________________________________', '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', '````````````````````````````````````````````````````````````````````````````````````````````````', 'ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc', 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb']
        if res != exp:
            print("Fel i test 2a/24: reverse_pairs([\'\', \'\\x01\', \'\\x02\\x02\', \'\\x03\\x03\\x03\', \'\\x04\\x04\\x04\\x04\', \'\\x05\\x05\\x05\\x05\\x05\', \'\\x06\\x06\\x06\\x06\\x06\\x06\', \'\\x07\\x07\\x07\\x07\\x07\\x07\\x07\', \'\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\', \'\\t\\t\\t\\t\\t\\t\\t\\t\\t\', \'\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\', \'\\x0b\\x0b\\x0b\\x0b\\x0b\\x0b\\x0b\\x0b\\x0b\\x0b\\x0b\', \'\\x0c\\x0c\\x0c\\x0c\\x0c\\x0c\\x0c\\x0c\\x0c\\x0c\\x0c\\x0c\', \'\\r\\r\\r\\r\\r\\r\\r\\r\\r\\r\\r\\r\\r\', \'\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\', \'\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\', \'\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\', \'\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\', \'\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\', \'\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\', \'\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\', \'\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\', \'\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\', \'\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\', \'\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\', \'\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\', \'\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\', \'\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\', \'\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\', \'\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\', \'\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\', \'\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\', \'                                \', \'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\', \'\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\', \'###################################\', \'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\', \'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\', \'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\', \"\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\", \'((((((((((((((((((((((((((((((((((((((((\', \')))))))))))))))))))))))))))))))))))))))))\', \'******************************************\', \'+++++++++++++++++++++++++++++++++++++++++++\', \',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\', \'---------------------------------------------\', \'..............................................\', \'///////////////////////////////////////////////\', \'000000000000000000000000000000000000000000000000\', \'1111111111111111111111111111111111111111111111111\', \'22222222222222222222222222222222222222222222222222\', \'333333333333333333333333333333333333333333333333333\', \'4444444444444444444444444444444444444444444444444444\', \'55555555555555555555555555555555555555555555555555555\', \'666666666666666666666666666666666666666666666666666666\', \'7777777777777777777777777777777777777777777777777777777\', \'88888888888888888888888888888888888888888888888888888888\', \'999999999999999999999999999999999999999999999999999999999\', \'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\', \';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\', \'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\', \'=============================================================\', \'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\', \'???????????????????????????????????????????????????????????????\', \'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\', \'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\', \'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB\', \'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC\', \'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD\', \'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE\', \'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF\', \'GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG\', \'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\', \'IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII\', \'JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ\', \'KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK\', \'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL\', \'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\', \'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\', \'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\', \'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP\', \'QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ\', \'RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR\', \'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS\', \'TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT\', \'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU\', \'VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV\', \'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\', \'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\', \'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY\', \'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ\', \'[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[\', \'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\', \']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]\', \'^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\', \'_______________________________________________________________________________________________\', \'````````````````````````````````````````````````````````````````````````````````````````````````\', \'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\', \'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\', \'ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc\'])")
            print("Korrekt svar: '\x01', '', '\x03\x03\x03', '\x02\x02', '\x05\x05\x05\x05\x05', '\x04\x04\x04\x04', '\x07\x07\x07\x07\x07\x07\x07', '\x06\x06\x06\x06\x06\x06', '\t\t\t\t\t\t\t\t\t', '\x08\x08\x08\x08\x08\x08\x08\x08', '\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b', '\n\n\n\n\n\n\n\n\n\n', '\r\r\r\r\r\r\r\r\r\r\r\r\r', '\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c', '\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f', '\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e', '\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11', '\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10', '\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13', '\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12', '\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15', '\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14', '\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17', '\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16', '\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19', '\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18', '\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b', '\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a', '\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d', '\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c', '\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f', '\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e', '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', '                                ', '###################################', '\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"', '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%', '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$', \"'''''''''''''''''''''''''''''''''''''''\", '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&', ')))))))))))))))))))))))))))))))))))))))))', '((((((((((((((((((((((((((((((((((((((((', '+++++++++++++++++++++++++++++++++++++++++++', '******************************************', '---------------------------------------------', ',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,', '///////////////////////////////////////////////', '..............................................', '1111111111111111111111111111111111111111111111111', '000000000000000000000000000000000000000000000000', '333333333333333333333333333333333333333333333333333', '22222222222222222222222222222222222222222222222222', '55555555555555555555555555555555555555555555555555555', '4444444444444444444444444444444444444444444444444444', '7777777777777777777777777777777777777777777777777777777', '666666666666666666666666666666666666666666666666666666', '999999999999999999999999999999999999999999999999999999999', '88888888888888888888888888888888888888888888888888888888', ';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;', '::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', '=============================================================', '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<', '???????????????????????????????????????????????????????????????', '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@', 'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC', 'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB', 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE', 'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD', 'GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG', 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF', 'IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII', 'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH', 'KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK', 'JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ', 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM', 'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL', 'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO', 'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN', 'QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ', 'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP', 'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS', 'RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR', 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU', 'TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT', 'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW', 'VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV', 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[', 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ', ']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]', '\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\', '_______________________________________________________________________________________________', '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', '````````````````````````````````````````````````````````````````````````````````````````````````', 'ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc', 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/24: Exception')
        print_exception()

    try:
        res = reverse_pairs([True, False])
        exp = [False, True]
        if res != exp:
            print("Fel i test 2a/25: reverse_pairs([True, False])")
            print("Korrekt svar: False, True")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/25: Exception')
        print_exception()

    try:
        res = reverse_pairs([True, True, True, False, True])
        exp = [True, True, False, True, True]
        if res != exp:
            print("Fel i test 2a/26: reverse_pairs([True, True, True, False, True])")
            print("Korrekt svar: True, True, False, True, True")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/26: Exception')
        print_exception()

    try:
        res = reverse_pairs([True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True])
        exp = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
        if res != exp:
            print("Fel i test 2a/27: reverse_pairs([True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True])")
            print("Korrekt svar: True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/27: Exception')
        print_exception()

    try:
        res = reverse_pairs([True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False])
        exp = [False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True]
        if res != exp:
            print("Fel i test 2a/28: reverse_pairs([True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False])")
            print("Korrekt svar: False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/28: Exception')
        print_exception()

    try:
        res = reverse_pairs([False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False])
        exp = [True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, False]
        if res != exp:
            print("Fel i test 2a/29: reverse_pairs([False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False])")
            print("Korrekt svar: True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, False")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/29: Exception')
        print_exception()

    try:
        res = reverse_pairs([0.0, 1.0, 2.0])
        exp = [1.0, 0.0, 2.0]
        if res != exp:
            print("Fel i test 2a/30: reverse_pairs([0.0, 1.0, 2.0])")
            print("Korrekt svar: 1.0, 0.0, 2.0")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/30: Exception')
        print_exception()

    try:
        res = reverse_pairs([1e-06, 0.123456789, 0.111111111, 123.3])
        exp = [0.123456789, 1e-06, 123.3, 0.111111111]
        if res != exp:
            print("Fel i test 2a/31: reverse_pairs([1e-06, 0.123456789, 0.111111111, 123.3])")
            print("Korrekt svar: 0.123456789, 1e-06, 123.3, 0.111111111")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/31: Exception')
        print_exception()

    try:
        res = reverse_pairs([-25.0, -24.0, -23.0, -22.0, -21.0, -20.0, -19.0, -18.0, -17.0, -16.0, -15.0, -14.0, -13.0, -12.0, -11.0, -10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0])
        exp = [-24.0, -25.0, -22.0, -23.0, -20.0, -21.0, -18.0, -19.0, -16.0, -17.0, -14.0, -15.0, -12.0, -13.0, -10.0, -11.0, -8.0, -9.0, -6.0, -7.0, -4.0, -5.0, -2.0, -3.0, 0.0, -1.0, 2.0, 1.0, 4.0, 3.0, 6.0, 5.0, 8.0, 7.0, 10.0, 9.0, 12.0, 11.0, 14.0, 13.0, 16.0, 15.0, 18.0, 17.0, 20.0, 19.0, 22.0, 21.0, 24.0, 23.0]
        if res != exp:
            print("Fel i test 2a/32: reverse_pairs([-25.0, -24.0, -23.0, -22.0, -21.0, -20.0, -19.0, -18.0, -17.0, -16.0, -15.0, -14.0, -13.0, -12.0, -11.0, -10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0])")
            print("Korrekt svar: -24.0, -25.0, -22.0, -23.0, -20.0, -21.0, -18.0, -19.0, -16.0, -17.0, -14.0, -15.0, -12.0, -13.0, -10.0, -11.0, -8.0, -9.0, -6.0, -7.0, -4.0, -5.0, -2.0, -3.0, 0.0, -1.0, 2.0, 1.0, 4.0, 3.0, 6.0, 5.0, 8.0, 7.0, 10.0, 9.0, 12.0, 11.0, 14.0, 13.0, 16.0, 15.0, 18.0, 17.0, 20.0, 19.0, 22.0, 21.0, 24.0, 23.0")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/32: Exception')
        print_exception()

    try:
        res = reverse_pairs([-1.5e-06, -1.49e-06, -1.48e-06, -1.47e-06, -1.46e-06, -1.45e-06, -1.44e-06, -1.43e-06, -1.42e-06, -1.41e-06, -1.4e-06, -1.39e-06, -1.38e-06, -1.37e-06, -1.36e-06, -1.35e-06, -1.34e-06, -1.33e-06, -1.32e-06, -1.31e-06, -1.3e-06, -1.29e-06, -1.28e-06, -1.27e-06, -1.26e-06, -1.25e-06, -1.24e-06, -1.23e-06, -1.22e-06, -1.21e-06, -1.2e-06, -1.19e-06, -1.18e-06, -1.17e-06, -1.16e-06, -1.15e-06, -1.14e-06, -1.13e-06, -1.12e-06, -1.11e-06, -1.1e-06, -1.09e-06, -1.08e-06, -1.07e-06, -1.06e-06, -1.05e-06, -1.04e-06, -1.03e-06, -1.02e-06, -1.01e-06, -1e-06, -9.9e-07, -9.8e-07, -9.7e-07, -9.6e-07, -9.5e-07, -9.4e-07, -9.3e-07, -9.2e-07, -9.1e-07, -9e-07, -8.9e-07, -8.8e-07, -8.7e-07, -8.6e-07, -8.5e-07, -8.4e-07, -8.3e-07, -8.2e-07, -8.1e-07, -8e-07, -7.9e-07, -7.8e-07, -7.7e-07, -7.6e-07, -7.5e-07, -7.4e-07, -7.3e-07, -7.2e-07, -7.1e-07, -7e-07, -6.9e-07, -6.8e-07, -6.7e-07, -6.6e-07, -6.5e-07, -6.4e-07, -6.3e-07, -6.2e-07, -6.1e-07, -6e-07, -5.9e-07, -5.8e-07, -5.7e-07, -5.6e-07, -5.5e-07, -5.4e-07, -5.3e-07, -5.2e-07, -5.1e-07, -5e-07, -4.9e-07, -4.8e-07, -4.7e-07, -4.6e-07, -4.5e-07, -4.4e-07, -4.3e-07, -4.2e-07, -4.1e-07, -4e-07, -3.9e-07, -3.8e-07, -3.7e-07, -3.6e-07, -3.5e-07, -3.4e-07, -3.3e-07, -3.2e-07, -3.1e-07, -3e-07, -2.9e-07, -2.8e-07, -2.7e-07, -2.6e-07, -2.5e-07, -2.4e-07, -2.3e-07, -2.2e-07, -2.1e-07, -2e-07, -1.9e-07, -1.8e-07, -1.7e-07, -1.6e-07, -1.5e-07, -1.4e-07, -1.3e-07, -1.2e-07, -1.1e-07, -1e-07, -9e-08, -8e-08, -7e-08, -6e-08, -5e-08, -4e-08, -3e-08, -2e-08, -1e-08, 0.0, 1e-08, 2e-08, 3e-08, 4e-08, 5e-08, 6e-08, 7e-08, 8e-08, 9e-08, 1e-07, 1.1e-07, 1.2e-07, 1.3e-07, 1.4e-07, 1.5e-07, 1.6e-07, 1.7e-07, 1.8e-07, 1.9e-07, 2e-07, 2.1e-07, 2.2e-07, 2.3e-07, 2.4e-07, 2.5e-07, 2.6e-07, 2.7e-07, 2.8e-07, 2.9e-07, 3e-07, 3.1e-07, 3.2e-07, 3.3e-07, 3.4e-07, 3.5e-07, 3.6e-07, 3.7e-07, 3.8e-07, 3.9e-07, 4e-07, 4.1e-07, 4.2e-07, 4.3e-07, 4.4e-07, 4.5e-07, 4.6e-07, 4.7e-07, 4.8e-07, 4.9e-07, 5e-07, 5.1e-07, 5.2e-07, 5.3e-07, 5.4e-07, 5.5e-07, 5.6e-07, 5.7e-07, 5.8e-07, 5.9e-07, 6e-07, 6.1e-07, 6.2e-07, 6.3e-07, 6.4e-07, 6.5e-07, 6.6e-07, 6.7e-07, 6.8e-07, 6.9e-07, 7e-07, 7.1e-07, 7.2e-07, 7.3e-07, 7.4e-07, 7.5e-07, 7.6e-07, 7.7e-07, 7.8e-07, 7.9e-07, 8e-07, 8.1e-07, 8.2e-07, 8.3e-07, 8.4e-07, 8.5e-07, 8.6e-07, 8.7e-07, 8.8e-07, 8.9e-07, 9e-07, 9.1e-07, 9.2e-07, 9.3e-07, 9.4e-07, 9.5e-07, 9.6e-07, 9.7e-07, 9.8e-07, 9.9e-07, 1e-06, 1.01e-06, 1.02e-06, 1.03e-06, 1.04e-06, 1.05e-06, 1.06e-06, 1.07e-06, 1.08e-06, 1.09e-06, 1.1e-06, 1.11e-06, 1.12e-06, 1.13e-06, 1.14e-06, 1.15e-06, 1.16e-06, 1.17e-06, 1.18e-06, 1.19e-06, 1.2e-06, 1.21e-06, 1.22e-06, 1.23e-06, 1.24e-06, 1.25e-06, 1.26e-06, 1.27e-06, 1.28e-06, 1.29e-06, 1.3e-06, 1.31e-06, 1.32e-06, 1.33e-06, 1.34e-06, 1.35e-06, 1.36e-06, 1.37e-06, 1.38e-06, 1.39e-06, 1.4e-06, 1.41e-06, 1.42e-06, 1.43e-06, 1.44e-06, 1.45e-06, 1.46e-06, 1.47e-06, 1.48e-06, 1.49e-06])
        exp = [-1.49e-06, -1.5e-06, -1.47e-06, -1.48e-06, -1.45e-06, -1.46e-06, -1.43e-06, -1.44e-06, -1.41e-06, -1.42e-06, -1.39e-06, -1.4e-06, -1.37e-06, -1.38e-06, -1.35e-06, -1.36e-06, -1.33e-06, -1.34e-06, -1.31e-06, -1.32e-06, -1.29e-06, -1.3e-06, -1.27e-06, -1.28e-06, -1.25e-06, -1.26e-06, -1.23e-06, -1.24e-06, -1.21e-06, -1.22e-06, -1.19e-06, -1.2e-06, -1.17e-06, -1.18e-06, -1.15e-06, -1.16e-06, -1.13e-06, -1.14e-06, -1.11e-06, -1.12e-06, -1.09e-06, -1.1e-06, -1.07e-06, -1.08e-06, -1.05e-06, -1.06e-06, -1.03e-06, -1.04e-06, -1.01e-06, -1.02e-06, -9.9e-07, -1e-06, -9.7e-07, -9.8e-07, -9.5e-07, -9.6e-07, -9.3e-07, -9.4e-07, -9.1e-07, -9.2e-07, -8.9e-07, -9e-07, -8.7e-07, -8.8e-07, -8.5e-07, -8.6e-07, -8.3e-07, -8.4e-07, -8.1e-07, -8.2e-07, -7.9e-07, -8e-07, -7.7e-07, -7.8e-07, -7.5e-07, -7.6e-07, -7.3e-07, -7.4e-07, -7.1e-07, -7.2e-07, -6.9e-07, -7e-07, -6.7e-07, -6.8e-07, -6.5e-07, -6.6e-07, -6.3e-07, -6.4e-07, -6.1e-07, -6.2e-07, -5.9e-07, -6e-07, -5.7e-07, -5.8e-07, -5.5e-07, -5.6e-07, -5.3e-07, -5.4e-07, -5.1e-07, -5.2e-07, -4.9e-07, -5e-07, -4.7e-07, -4.8e-07, -4.5e-07, -4.6e-07, -4.3e-07, -4.4e-07, -4.1e-07, -4.2e-07, -3.9e-07, -4e-07, -3.7e-07, -3.8e-07, -3.5e-07, -3.6e-07, -3.3e-07, -3.4e-07, -3.1e-07, -3.2e-07, -2.9e-07, -3e-07, -2.7e-07, -2.8e-07, -2.5e-07, -2.6e-07, -2.3e-07, -2.4e-07, -2.1e-07, -2.2e-07, -1.9e-07, -2e-07, -1.7e-07, -1.8e-07, -1.5e-07, -1.6e-07, -1.3e-07, -1.4e-07, -1.1e-07, -1.2e-07, -9e-08, -1e-07, -7e-08, -8e-08, -5e-08, -6e-08, -3e-08, -4e-08, -1e-08, -2e-08, 1e-08, 0.0, 3e-08, 2e-08, 5e-08, 4e-08, 7e-08, 6e-08, 9e-08, 8e-08, 1.1e-07, 1e-07, 1.3e-07, 1.2e-07, 1.5e-07, 1.4e-07, 1.7e-07, 1.6e-07, 1.9e-07, 1.8e-07, 2.1e-07, 2e-07, 2.3e-07, 2.2e-07, 2.5e-07, 2.4e-07, 2.7e-07, 2.6e-07, 2.9e-07, 2.8e-07, 3.1e-07, 3e-07, 3.3e-07, 3.2e-07, 3.5e-07, 3.4e-07, 3.7e-07, 3.6e-07, 3.9e-07, 3.8e-07, 4.1e-07, 4e-07, 4.3e-07, 4.2e-07, 4.5e-07, 4.4e-07, 4.7e-07, 4.6e-07, 4.9e-07, 4.8e-07, 5.1e-07, 5e-07, 5.3e-07, 5.2e-07, 5.5e-07, 5.4e-07, 5.7e-07, 5.6e-07, 5.9e-07, 5.8e-07, 6.1e-07, 6e-07, 6.3e-07, 6.2e-07, 6.5e-07, 6.4e-07, 6.7e-07, 6.6e-07, 6.9e-07, 6.8e-07, 7.1e-07, 7e-07, 7.3e-07, 7.2e-07, 7.5e-07, 7.4e-07, 7.7e-07, 7.6e-07, 7.9e-07, 7.8e-07, 8.1e-07, 8e-07, 8.3e-07, 8.2e-07, 8.5e-07, 8.4e-07, 8.7e-07, 8.6e-07, 8.9e-07, 8.8e-07, 9.1e-07, 9e-07, 9.3e-07, 9.2e-07, 9.5e-07, 9.4e-07, 9.7e-07, 9.6e-07, 9.9e-07, 9.8e-07, 1.01e-06, 1e-06, 1.03e-06, 1.02e-06, 1.05e-06, 1.04e-06, 1.07e-06, 1.06e-06, 1.09e-06, 1.08e-06, 1.11e-06, 1.1e-06, 1.13e-06, 1.12e-06, 1.15e-06, 1.14e-06, 1.17e-06, 1.16e-06, 1.19e-06, 1.18e-06, 1.21e-06, 1.2e-06, 1.23e-06, 1.22e-06, 1.25e-06, 1.24e-06, 1.27e-06, 1.26e-06, 1.29e-06, 1.28e-06, 1.31e-06, 1.3e-06, 1.33e-06, 1.32e-06, 1.35e-06, 1.34e-06, 1.37e-06, 1.36e-06, 1.39e-06, 1.38e-06, 1.41e-06, 1.4e-06, 1.43e-06, 1.42e-06, 1.45e-06, 1.44e-06, 1.47e-06, 1.46e-06, 1.49e-06, 1.48e-06]
        if res != exp:
            print("Fel i test 2a/33: reverse_pairs([-1.5e-06, -1.49e-06, -1.48e-06, -1.47e-06, -1.46e-06, -1.45e-06, -1.44e-06, -1.43e-06, -1.42e-06, -1.41e-06, -1.4e-06, -1.39e-06, -1.38e-06, -1.37e-06, -1.36e-06, -1.35e-06, -1.34e-06, -1.33e-06, -1.32e-06, -1.31e-06, -1.3e-06, -1.29e-06, -1.28e-06, -1.27e-06, -1.26e-06, -1.25e-06, -1.24e-06, -1.23e-06, -1.22e-06, -1.21e-06, -1.2e-06, -1.19e-06, -1.18e-06, -1.17e-06, -1.16e-06, -1.15e-06, -1.14e-06, -1.13e-06, -1.12e-06, -1.11e-06, -1.1e-06, -1.09e-06, -1.08e-06, -1.07e-06, -1.06e-06, -1.05e-06, -1.04e-06, -1.03e-06, -1.02e-06, -1.01e-06, -1e-06, -9.9e-07, -9.8e-07, -9.7e-07, -9.6e-07, -9.5e-07, -9.4e-07, -9.3e-07, -9.2e-07, -9.1e-07, -9e-07, -8.9e-07, -8.8e-07, -8.7e-07, -8.6e-07, -8.5e-07, -8.4e-07, -8.3e-07, -8.2e-07, -8.1e-07, -8e-07, -7.9e-07, -7.8e-07, -7.7e-07, -7.6e-07, -7.5e-07, -7.4e-07, -7.3e-07, -7.2e-07, -7.1e-07, -7e-07, -6.9e-07, -6.8e-07, -6.7e-07, -6.6e-07, -6.5e-07, -6.4e-07, -6.3e-07, -6.2e-07, -6.1e-07, -6e-07, -5.9e-07, -5.8e-07, -5.7e-07, -5.6e-07, -5.5e-07, -5.4e-07, -5.3e-07, -5.2e-07, -5.1e-07, -5e-07, -4.9e-07, -4.8e-07, -4.7e-07, -4.6e-07, -4.5e-07, -4.4e-07, -4.3e-07, -4.2e-07, -4.1e-07, -4e-07, -3.9e-07, -3.8e-07, -3.7e-07, -3.6e-07, -3.5e-07, -3.4e-07, -3.3e-07, -3.2e-07, -3.1e-07, -3e-07, -2.9e-07, -2.8e-07, -2.7e-07, -2.6e-07, -2.5e-07, -2.4e-07, -2.3e-07, -2.2e-07, -2.1e-07, -2e-07, -1.9e-07, -1.8e-07, -1.7e-07, -1.6e-07, -1.5e-07, -1.4e-07, -1.3e-07, -1.2e-07, -1.1e-07, -1e-07, -9e-08, -8e-08, -7e-08, -6e-08, -5e-08, -4e-08, -3e-08, -2e-08, -1e-08, 0.0, 1e-08, 2e-08, 3e-08, 4e-08, 5e-08, 6e-08, 7e-08, 8e-08, 9e-08, 1e-07, 1.1e-07, 1.2e-07, 1.3e-07, 1.4e-07, 1.5e-07, 1.6e-07, 1.7e-07, 1.8e-07, 1.9e-07, 2e-07, 2.1e-07, 2.2e-07, 2.3e-07, 2.4e-07, 2.5e-07, 2.6e-07, 2.7e-07, 2.8e-07, 2.9e-07, 3e-07, 3.1e-07, 3.2e-07, 3.3e-07, 3.4e-07, 3.5e-07, 3.6e-07, 3.7e-07, 3.8e-07, 3.9e-07, 4e-07, 4.1e-07, 4.2e-07, 4.3e-07, 4.4e-07, 4.5e-07, 4.6e-07, 4.7e-07, 4.8e-07, 4.9e-07, 5e-07, 5.1e-07, 5.2e-07, 5.3e-07, 5.4e-07, 5.5e-07, 5.6e-07, 5.7e-07, 5.8e-07, 5.9e-07, 6e-07, 6.1e-07, 6.2e-07, 6.3e-07, 6.4e-07, 6.5e-07, 6.6e-07, 6.7e-07, 6.8e-07, 6.9e-07, 7e-07, 7.1e-07, 7.2e-07, 7.3e-07, 7.4e-07, 7.5e-07, 7.6e-07, 7.7e-07, 7.8e-07, 7.9e-07, 8e-07, 8.1e-07, 8.2e-07, 8.3e-07, 8.4e-07, 8.5e-07, 8.6e-07, 8.7e-07, 8.8e-07, 8.9e-07, 9e-07, 9.1e-07, 9.2e-07, 9.3e-07, 9.4e-07, 9.5e-07, 9.6e-07, 9.7e-07, 9.8e-07, 9.9e-07, 1e-06, 1.01e-06, 1.02e-06, 1.03e-06, 1.04e-06, 1.05e-06, 1.06e-06, 1.07e-06, 1.08e-06, 1.09e-06, 1.1e-06, 1.11e-06, 1.12e-06, 1.13e-06, 1.14e-06, 1.15e-06, 1.16e-06, 1.17e-06, 1.18e-06, 1.19e-06, 1.2e-06, 1.21e-06, 1.22e-06, 1.23e-06, 1.24e-06, 1.25e-06, 1.26e-06, 1.27e-06, 1.28e-06, 1.29e-06, 1.3e-06, 1.31e-06, 1.32e-06, 1.33e-06, 1.34e-06, 1.35e-06, 1.36e-06, 1.37e-06, 1.38e-06, 1.39e-06, 1.4e-06, 1.41e-06, 1.42e-06, 1.43e-06, 1.44e-06, 1.45e-06, 1.46e-06, 1.47e-06, 1.48e-06, 1.49e-06])")
            print("Korrekt svar: -1.49e-06, -1.5e-06, -1.47e-06, -1.48e-06, -1.45e-06, -1.46e-06, -1.43e-06, -1.44e-06, -1.41e-06, -1.42e-06, -1.39e-06, -1.4e-06, -1.37e-06, -1.38e-06, -1.35e-06, -1.36e-06, -1.33e-06, -1.34e-06, -1.31e-06, -1.32e-06, -1.29e-06, -1.3e-06, -1.27e-06, -1.28e-06, -1.25e-06, -1.26e-06, -1.23e-06, -1.24e-06, -1.21e-06, -1.22e-06, -1.19e-06, -1.2e-06, -1.17e-06, -1.18e-06, -1.15e-06, -1.16e-06, -1.13e-06, -1.14e-06, -1.11e-06, -1.12e-06, -1.09e-06, -1.1e-06, -1.07e-06, -1.08e-06, -1.05e-06, -1.06e-06, -1.03e-06, -1.04e-06, -1.01e-06, -1.02e-06, -9.9e-07, -1e-06, -9.7e-07, -9.8e-07, -9.5e-07, -9.6e-07, -9.3e-07, -9.4e-07, -9.1e-07, -9.2e-07, -8.9e-07, -9e-07, -8.7e-07, -8.8e-07, -8.5e-07, -8.6e-07, -8.3e-07, -8.4e-07, -8.1e-07, -8.2e-07, -7.9e-07, -8e-07, -7.7e-07, -7.8e-07, -7.5e-07, -7.6e-07, -7.3e-07, -7.4e-07, -7.1e-07, -7.2e-07, -6.9e-07, -7e-07, -6.7e-07, -6.8e-07, -6.5e-07, -6.6e-07, -6.3e-07, -6.4e-07, -6.1e-07, -6.2e-07, -5.9e-07, -6e-07, -5.7e-07, -5.8e-07, -5.5e-07, -5.6e-07, -5.3e-07, -5.4e-07, -5.1e-07, -5.2e-07, -4.9e-07, -5e-07, -4.7e-07, -4.8e-07, -4.5e-07, -4.6e-07, -4.3e-07, -4.4e-07, -4.1e-07, -4.2e-07, -3.9e-07, -4e-07, -3.7e-07, -3.8e-07, -3.5e-07, -3.6e-07, -3.3e-07, -3.4e-07, -3.1e-07, -3.2e-07, -2.9e-07, -3e-07, -2.7e-07, -2.8e-07, -2.5e-07, -2.6e-07, -2.3e-07, -2.4e-07, -2.1e-07, -2.2e-07, -1.9e-07, -2e-07, -1.7e-07, -1.8e-07, -1.5e-07, -1.6e-07, -1.3e-07, -1.4e-07, -1.1e-07, -1.2e-07, -9e-08, -1e-07, -7e-08, -8e-08, -5e-08, -6e-08, -3e-08, -4e-08, -1e-08, -2e-08, 1e-08, 0.0, 3e-08, 2e-08, 5e-08, 4e-08, 7e-08, 6e-08, 9e-08, 8e-08, 1.1e-07, 1e-07, 1.3e-07, 1.2e-07, 1.5e-07, 1.4e-07, 1.7e-07, 1.6e-07, 1.9e-07, 1.8e-07, 2.1e-07, 2e-07, 2.3e-07, 2.2e-07, 2.5e-07, 2.4e-07, 2.7e-07, 2.6e-07, 2.9e-07, 2.8e-07, 3.1e-07, 3e-07, 3.3e-07, 3.2e-07, 3.5e-07, 3.4e-07, 3.7e-07, 3.6e-07, 3.9e-07, 3.8e-07, 4.1e-07, 4e-07, 4.3e-07, 4.2e-07, 4.5e-07, 4.4e-07, 4.7e-07, 4.6e-07, 4.9e-07, 4.8e-07, 5.1e-07, 5e-07, 5.3e-07, 5.2e-07, 5.5e-07, 5.4e-07, 5.7e-07, 5.6e-07, 5.9e-07, 5.8e-07, 6.1e-07, 6e-07, 6.3e-07, 6.2e-07, 6.5e-07, 6.4e-07, 6.7e-07, 6.6e-07, 6.9e-07, 6.8e-07, 7.1e-07, 7e-07, 7.3e-07, 7.2e-07, 7.5e-07, 7.4e-07, 7.7e-07, 7.6e-07, 7.9e-07, 7.8e-07, 8.1e-07, 8e-07, 8.3e-07, 8.2e-07, 8.5e-07, 8.4e-07, 8.7e-07, 8.6e-07, 8.9e-07, 8.8e-07, 9.1e-07, 9e-07, 9.3e-07, 9.2e-07, 9.5e-07, 9.4e-07, 9.7e-07, 9.6e-07, 9.9e-07, 9.8e-07, 1.01e-06, 1e-06, 1.03e-06, 1.02e-06, 1.05e-06, 1.04e-06, 1.07e-06, 1.06e-06, 1.09e-06, 1.08e-06, 1.11e-06, 1.1e-06, 1.13e-06, 1.12e-06, 1.15e-06, 1.14e-06, 1.17e-06, 1.16e-06, 1.19e-06, 1.18e-06, 1.21e-06, 1.2e-06, 1.23e-06, 1.22e-06, 1.25e-06, 1.24e-06, 1.27e-06, 1.26e-06, 1.29e-06, 1.28e-06, 1.31e-06, 1.3e-06, 1.33e-06, 1.32e-06, 1.35e-06, 1.34e-06, 1.37e-06, 1.36e-06, 1.39e-06, 1.38e-06, 1.41e-06, 1.4e-06, 1.43e-06, 1.42e-06, 1.45e-06, 1.44e-06, 1.47e-06, 1.46e-06, 1.49e-06, 1.48e-06")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/33: Exception')
        print_exception()

    try:
        res = reverse_pairs([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0, 33.5, 34.0, 34.5, 35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0, 42.5, 43.0, 43.5, 44.0, 44.5, 45.0, 45.5, 46.0, 46.5, 47.0, 47.5, 48.0, 48.5, 49.0, 49.5, 50.0, 50.5, 51.0, 51.5, 52.0, 52.5, 53.0, 53.5, 54.0, 54.5, 55.0, 55.5, 56.0, 56.5, 57.0, 57.5, 58.0, 58.5, 59.0, 59.5, 60.0, 60.5, 61.0, 61.5, 62.0, 62.5, 63.0, 63.5, 64.0, 64.5, 65.0, 65.5, 66.0, 66.5, 67.0, 67.5, 68.0, 68.5, 69.0, 69.5, 70.0, 70.5, 71.0, 71.5, 72.0, 72.5, 73.0, 73.5, 74.0, 74.5])
        exp = [0.5, 0.0, 1.5, 1.0, 2.5, 2.0, 3.5, 3.0, 4.5, 4.0, 5.5, 5.0, 6.5, 6.0, 7.5, 7.0, 8.5, 8.0, 9.5, 9.0, 10.5, 10.0, 11.5, 11.0, 12.5, 12.0, 13.5, 13.0, 14.5, 14.0, 15.5, 15.0, 16.5, 16.0, 17.5, 17.0, 18.5, 18.0, 19.5, 19.0, 20.5, 20.0, 21.5, 21.0, 22.5, 22.0, 23.5, 23.0, 24.5, 24.0, 25.5, 25.0, 26.5, 26.0, 27.5, 27.0, 28.5, 28.0, 29.5, 29.0, 30.5, 30.0, 31.5, 31.0, 32.5, 32.0, 33.5, 33.0, 34.5, 34.0, 35.5, 35.0, 36.5, 36.0, 37.5, 37.0, 38.5, 38.0, 39.5, 39.0, 40.5, 40.0, 41.5, 41.0, 42.5, 42.0, 43.5, 43.0, 44.5, 44.0, 45.5, 45.0, 46.5, 46.0, 47.5, 47.0, 48.5, 48.0, 49.5, 49.0, 50.5, 50.0, 51.5, 51.0, 52.5, 52.0, 53.5, 53.0, 54.5, 54.0, 55.5, 55.0, 56.5, 56.0, 57.5, 57.0, 58.5, 58.0, 59.5, 59.0, 60.5, 60.0, 61.5, 61.0, 62.5, 62.0, 63.5, 63.0, 64.5, 64.0, 65.5, 65.0, 66.5, 66.0, 67.5, 67.0, 68.5, 68.0, 69.5, 69.0, 70.5, 70.0, 71.5, 71.0, 72.5, 72.0, 73.5, 73.0, 74.5, 74.0]
        if res != exp:
            print("Fel i test 2a/34: reverse_pairs([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0, 33.5, 34.0, 34.5, 35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0, 42.5, 43.0, 43.5, 44.0, 44.5, 45.0, 45.5, 46.0, 46.5, 47.0, 47.5, 48.0, 48.5, 49.0, 49.5, 50.0, 50.5, 51.0, 51.5, 52.0, 52.5, 53.0, 53.5, 54.0, 54.5, 55.0, 55.5, 56.0, 56.5, 57.0, 57.5, 58.0, 58.5, 59.0, 59.5, 60.0, 60.5, 61.0, 61.5, 62.0, 62.5, 63.0, 63.5, 64.0, 64.5, 65.0, 65.5, 66.0, 66.5, 67.0, 67.5, 68.0, 68.5, 69.0, 69.5, 70.0, 70.5, 71.0, 71.5, 72.0, 72.5, 73.0, 73.5, 74.0, 74.5])")
            print("Korrekt svar: 0.5, 0.0, 1.5, 1.0, 2.5, 2.0, 3.5, 3.0, 4.5, 4.0, 5.5, 5.0, 6.5, 6.0, 7.5, 7.0, 8.5, 8.0, 9.5, 9.0, 10.5, 10.0, 11.5, 11.0, 12.5, 12.0, 13.5, 13.0, 14.5, 14.0, 15.5, 15.0, 16.5, 16.0, 17.5, 17.0, 18.5, 18.0, 19.5, 19.0, 20.5, 20.0, 21.5, 21.0, 22.5, 22.0, 23.5, 23.0, 24.5, 24.0, 25.5, 25.0, 26.5, 26.0, 27.5, 27.0, 28.5, 28.0, 29.5, 29.0, 30.5, 30.0, 31.5, 31.0, 32.5, 32.0, 33.5, 33.0, 34.5, 34.0, 35.5, 35.0, 36.5, 36.0, 37.5, 37.0, 38.5, 38.0, 39.5, 39.0, 40.5, 40.0, 41.5, 41.0, 42.5, 42.0, 43.5, 43.0, 44.5, 44.0, 45.5, 45.0, 46.5, 46.0, 47.5, 47.0, 48.5, 48.0, 49.5, 49.0, 50.5, 50.0, 51.5, 51.0, 52.5, 52.0, 53.5, 53.0, 54.5, 54.0, 55.5, 55.0, 56.5, 56.0, 57.5, 57.0, 58.5, 58.0, 59.5, 59.0, 60.5, 60.0, 61.5, 61.0, 62.5, 62.0, 63.5, 63.0, 64.5, 64.0, 65.5, 65.0, 66.5, 66.0, 67.5, 67.0, 68.5, 68.0, 69.5, 69.0, 70.5, 70.0, 71.5, 71.0, 72.5, 72.0, 73.5, 73.0, 74.5, 74.0")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/34: Exception')
        print_exception()

    try:
        res = reverse_pairs(['kod', 123, False, 7.7])
        exp = [123, 'kod', 7.7, False]
        if res != exp:
            print("Fel i test 2a/35: reverse_pairs(['kod', 123, False, 7.7])")
            print("Korrekt svar: 123, 'kod', 7.7, False")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/35: Exception')
        print_exception()

    try:
        res = reverse_pairs([1, 1.0, 1, 1.0, 1, 1, 1.0])
        exp = [1.0, 1, 1.0, 1, 1, 1, 1.0]
        if res != exp:
            print("Fel i test 2a/36: reverse_pairs([1, 1.0, 1, 1.0, 1, 1, 1.0])")
            print("Korrekt svar: 1.0, 1, 1.0, 1, 1, 1, 1.0")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/36: Exception')
        print_exception()

    try:
        res = reverse_pairs(['123', 123, 97, 'a', False])
        exp = [123, '123', 'a', 97, False]
        if res != exp:
            print("Fel i test 2a/37: reverse_pairs(['123', 123, 97, 'a', False])")
            print("Korrekt svar: 123, '123', 'a', 97, False")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/37: Exception')
        print_exception()

    try:
        res = reverse_pairs(['0', 1.0, 2, '3', 4.0, 5, '6', 7.0, 8, '9', 10.0, 11, '12', 13.0, 14, '15', 16.0, 17, '18', 19.0, 20, '21', 22.0, 23, '24', 25.0, 26, '27', 28.0, 29, '30', 31.0, 32, '33', 34.0, 35, '36', 37.0, 38, '39', 40.0, 41, '42', 43.0, 44, '45', 46.0, 47, '48', 49.0, 50, '51', 52.0, 53, '54', 55.0, 56, '57', 58.0, 59, '60', 61.0, 62, '63', 64.0, 65, '66', 67.0, 68, '69', 70.0, 71, '72', 73.0, 74, '75', 76.0, 77, '78', 79.0, 80, '81', 82.0, 83, '84', 85.0, 86, '87', 88.0, 89, '90', 91.0, 92, '93', 94.0, 95, '96', 97.0, 98, '99', 100.0, 101, '102', 103.0, 104, '105', 106.0, 107, '108', 109.0, 110, '111', 112.0, 113, '114', 115.0, 116, '117', 118.0, 119, '120', 121.0, 122, '123', 124.0, 125, '126', 127.0, 128, '129', 130.0, 131, '132', 133.0, 134, '135', 136.0, 137, '138', 139.0, 140, '141', 142.0, 143, '144', 145.0, 146, '147', 148.0, 149])
        exp = [1.0, '0', '3', 2, 5, 4.0, 7.0, '6', '9', 8, 11, 10.0, 13.0, '12', '15', 14, 17, 16.0, 19.0, '18', '21', 20, 23, 22.0, 25.0, '24', '27', 26, 29, 28.0, 31.0, '30', '33', 32, 35, 34.0, 37.0, '36', '39', 38, 41, 40.0, 43.0, '42', '45', 44, 47, 46.0, 49.0, '48', '51', 50, 53, 52.0, 55.0, '54', '57', 56, 59, 58.0, 61.0, '60', '63', 62, 65, 64.0, 67.0, '66', '69', 68, 71, 70.0, 73.0, '72', '75', 74, 77, 76.0, 79.0, '78', '81', 80, 83, 82.0, 85.0, '84', '87', 86, 89, 88.0, 91.0, '90', '93', 92, 95, 94.0, 97.0, '96', '99', 98, 101, 100.0, 103.0, '102', '105', 104, 107, 106.0, 109.0, '108', '111', 110, 113, 112.0, 115.0, '114', '117', 116, 119, 118.0, 121.0, '120', '123', 122, 125, 124.0, 127.0, '126', '129', 128, 131, 130.0, 133.0, '132', '135', 134, 137, 136.0, 139.0, '138', '141', 140, 143, 142.0, 145.0, '144', '147', 146, 149, 148.0]
        if res != exp:
            print("Fel i test 2a/38: reverse_pairs(['0', 1.0, 2, '3', 4.0, 5, '6', 7.0, 8, '9', 10.0, 11, '12', 13.0, 14, '15', 16.0, 17, '18', 19.0, 20, '21', 22.0, 23, '24', 25.0, 26, '27', 28.0, 29, '30', 31.0, 32, '33', 34.0, 35, '36', 37.0, 38, '39', 40.0, 41, '42', 43.0, 44, '45', 46.0, 47, '48', 49.0, 50, '51', 52.0, 53, '54', 55.0, 56, '57', 58.0, 59, '60', 61.0, 62, '63', 64.0, 65, '66', 67.0, 68, '69', 70.0, 71, '72', 73.0, 74, '75', 76.0, 77, '78', 79.0, 80, '81', 82.0, 83, '84', 85.0, 86, '87', 88.0, 89, '90', 91.0, 92, '93', 94.0, 95, '96', 97.0, 98, '99', 100.0, 101, '102', 103.0, 104, '105', 106.0, 107, '108', 109.0, 110, '111', 112.0, 113, '114', 115.0, 116, '117', 118.0, 119, '120', 121.0, 122, '123', 124.0, 125, '126', 127.0, 128, '129', 130.0, 131, '132', 133.0, 134, '135', 136.0, 137, '138', 139.0, 140, '141', 142.0, 143, '144', 145.0, 146, '147', 148.0, 149])")
            print("Korrekt svar: 1.0, '0', '3', 2, 5, 4.0, 7.0, '6', '9', 8, 11, 10.0, 13.0, '12', '15', 14, 17, 16.0, 19.0, '18', '21', 20, 23, 22.0, 25.0, '24', '27', 26, 29, 28.0, 31.0, '30', '33', 32, 35, 34.0, 37.0, '36', '39', 38, 41, 40.0, 43.0, '42', '45', 44, 47, 46.0, 49.0, '48', '51', 50, 53, 52.0, 55.0, '54', '57', 56, 59, 58.0, 61.0, '60', '63', 62, 65, 64.0, 67.0, '66', '69', 68, 71, 70.0, 73.0, '72', '75', 74, 77, 76.0, 79.0, '78', '81', 80, 83, 82.0, 85.0, '84', '87', 86, 89, 88.0, 91.0, '90', '93', 92, 95, 94.0, 97.0, '96', '99', 98, 101, 100.0, 103.0, '102', '105', 104, 107, 106.0, 109.0, '108', '111', 110, 113, 112.0, 115.0, '114', '117', 116, 119, 118.0, 121.0, '120', '123', 122, 125, 124.0, 127.0, '126', '129', 128, 131, 130.0, 133.0, '132', '135', 134, 137, 136.0, 139.0, '138', '141', 140, 143, 142.0, 145.0, '144', '147', 146, 149, 148.0")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/38: Exception')
        print_exception()

    try:
        res = reverse_pairs(['1', 1, 2, '2', '3', '3', 4, 4])
        exp = [1, '1', '2', 2, '3', '3', 4, 4]
        if res != exp:
            print("Fel i test 2a/39: reverse_pairs(['1', 1, 2, '2', '3', '3', 4, 4])")
            print("Korrekt svar: 1, '1', '2', 2, '3', '3', 4, 4")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/39: Exception')
        print_exception()

    try:
        res = reverse_pairs([[]])
        exp = [[]]
        if res != exp:
            print("Fel i test 2a/40: reverse_pairs([[]])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/40: Exception')
        print_exception()

    try:
        res = reverse_pairs([[], [[]]])
        exp = [[[]], []]
        if res != exp:
            print("Fel i test 2a/41: reverse_pairs([[], [[]]])")
            print("Korrekt svar: [[]], []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/41: Exception')
        print_exception()

    try:
        res = reverse_pairs([[[[[]]]], [], [[]]])
        exp = [[], [[[[]]]], [[]]]
        if res != exp:
            print("Fel i test 2a/42: reverse_pairs([[[[[]]]], [], [[]]])")
            print("Korrekt svar: [], [[[[]]]], [[]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/42: Exception')
        print_exception()

    try:
        res = reverse_pairs([[]])
        exp = [[]]
        if res != exp:
            print("Fel i test 2a/43: reverse_pairs([[]])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/43: Exception')
        print_exception()

    try:
        res = reverse_pairs([[[[[[[[[[[]]]]]]]]]]])
        exp = [[[[[[[[[[[]]]]]]]]]]]
        if res != exp:
            print("Fel i test 2a/44: reverse_pairs([[[[[[[[[[[]]]]]]]]]]])")
            print("Korrekt svar: [[[[[[[[[[]]]]]]]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/44: Exception')
        print_exception()

    try:
        res = reverse_pairs([[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]])
        exp = [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
        if res != exp:
            print("Fel i test 2a/45: reverse_pairs([[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]])")
            print("Korrekt svar: [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/45: Exception')
        print_exception()

    try:
        res = reverse_pairs([[1], [2]])
        exp = [[2], [1]]
        if res != exp:
            print("Fel i test 2a/46: reverse_pairs([[1], [2]])")
            print("Korrekt svar: [2], [1]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/46: Exception')
        print_exception()

    try:
        res = reverse_pairs([[1], [[2]], [[[3]]], [[[[4]]]]])
        exp = [[[2]], [1], [[[[4]]]], [[[3]]]]
        if res != exp:
            print("Fel i test 2a/47: reverse_pairs([[1], [[2]], [[[3]]], [[[[4]]]]])")
            print("Korrekt svar: [[2]], [1], [[[[4]]]], [[[3]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/47: Exception')
        print_exception()

    try:
        res = reverse_pairs([[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12], [0, 4, 8, 12, 16]], [[0, 0, 0, 0, 0], [0, 2, 4, 6, 8], [0, 4, 8, 12, 16], [0, 6, 12, 18, 24], [0, 8, 16, 24, 32]], [[0, 0, 0, 0, 0], [0, 3, 6, 9, 12], [0, 6, 12, 18, 24], [0, 9, 18, 27, 36], [0, 12, 24, 36, 48]], [[0, 0, 0, 0, 0], [0, 4, 8, 12, 16], [0, 8, 16, 24, 32], [0, 12, 24, 36, 48], [0, 16, 32, 48, 64]]])
        exp = [[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12], [0, 4, 8, 12, 16]], [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 3, 6, 9, 12], [0, 6, 12, 18, 24], [0, 9, 18, 27, 36], [0, 12, 24, 36, 48]], [[0, 0, 0, 0, 0], [0, 2, 4, 6, 8], [0, 4, 8, 12, 16], [0, 6, 12, 18, 24], [0, 8, 16, 24, 32]], [[0, 0, 0, 0, 0], [0, 4, 8, 12, 16], [0, 8, 16, 24, 32], [0, 12, 24, 36, 48], [0, 16, 32, 48, 64]]]
        if res != exp:
            print("Fel i test 2a/48: reverse_pairs([[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12], [0, 4, 8, 12, 16]], [[0, 0, 0, 0, 0], [0, 2, 4, 6, 8], [0, 4, 8, 12, 16], [0, 6, 12, 18, 24], [0, 8, 16, 24, 32]], [[0, 0, 0, 0, 0], [0, 3, 6, 9, 12], [0, 6, 12, 18, 24], [0, 9, 18, 27, 36], [0, 12, 24, 36, 48]], [[0, 0, 0, 0, 0], [0, 4, 8, 12, 16], [0, 8, 16, 24, 32], [0, 12, 24, 36, 48], [0, 16, 32, 48, 64]]])")
            print("Korrekt svar: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12], [0, 4, 8, 12, 16]], [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 3, 6, 9, 12], [0, 6, 12, 18, 24], [0, 9, 18, 27, 36], [0, 12, 24, 36, 48]], [[0, 0, 0, 0, 0], [0, 2, 4, 6, 8], [0, 4, 8, 12, 16], [0, 6, 12, 18, 24], [0, 8, 16, 24, 32]], [[0, 0, 0, 0, 0], [0, 4, 8, 12, 16], [0, 8, 16, 24, 32], [0, 12, 24, 36, 48], [0, 16, 32, 48, 64]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/48: Exception')
        print_exception()

    try:
        res = reverse_pairs([(), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ()])
        exp = [(), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ()]
        if res != exp:
            print("Fel i test 2a/49: reverse_pairs([(), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ()])")
            print("Korrekt svar: (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ()")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/49: Exception')
        print_exception()

    try:
        res = reverse_pairs([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])
        exp = [(0, 1), (0, 0), (1, 0), (0, 2), (1, 2), (1, 1), (2, 1), (2, 0), (2, 2)]
        if res != exp:
            print("Fel i test 2a/50: reverse_pairs([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])")
            print("Korrekt svar: (0, 1), (0, 0), (1, 0), (0, 2), (1, 2), (1, 1), (2, 1), (2, 0), (2, 2)")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/50: Exception')
        print_exception()

    try:
        res = reverse_pairs([{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}])
        exp = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
        if res != exp:
            print("Fel i test 2a/51: reverse_pairs([{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}])")
            print("Korrekt svar: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/51: Exception')
        print_exception()

    try:
        res = reverse_pairs([{0: 0}, {1: 1}, {2: 2}, {3: 3}, {4: 4}, {5: 5}, {6: 6}, {7: 7}, {8: 8}, {9: 9}, {10: 10}, {11: 11}, {12: 12}, {13: 13}, {14: 14}, {15: 15}, {16: 16}, {17: 17}, {18: 18}, {19: 19}, {20: 20}, {21: 21}, {22: 22}, {23: 23}, {24: 24}, {25: 25}, {26: 26}, {27: 27}, {28: 28}, {29: 29}, {30: 30}, {31: 31}, {32: 32}, {33: 33}, {34: 34}, {35: 35}, {36: 36}, {37: 37}, {38: 38}, {39: 39}, {40: 40}, {41: 41}, {42: 42}, {43: 43}, {44: 44}, {45: 45}, {46: 46}, {47: 47}, {48: 48}, {49: 49}, {50: 50}, {51: 51}, {52: 52}, {53: 53}, {54: 54}, {55: 55}, {56: 56}, {57: 57}, {58: 58}, {59: 59}, {60: 60}, {61: 61}, {62: 62}, {63: 63}, {64: 64}, {65: 65}, {66: 66}, {67: 67}, {68: 68}, {69: 69}, {70: 70}, {71: 71}, {72: 72}, {73: 73}, {74: 74}, {75: 75}, {76: 76}, {77: 77}, {78: 78}, {79: 79}, {80: 80}, {81: 81}, {82: 82}, {83: 83}, {84: 84}, {85: 85}, {86: 86}, {87: 87}, {88: 88}, {89: 89}, {90: 90}, {91: 91}, {92: 92}, {93: 93}, {94: 94}, {95: 95}, {96: 96}, {97: 97}, {98: 98}, {99: 99}])
        exp = [{1: 1}, {0: 0}, {3: 3}, {2: 2}, {5: 5}, {4: 4}, {7: 7}, {6: 6}, {9: 9}, {8: 8}, {11: 11}, {10: 10}, {13: 13}, {12: 12}, {15: 15}, {14: 14}, {17: 17}, {16: 16}, {19: 19}, {18: 18}, {21: 21}, {20: 20}, {23: 23}, {22: 22}, {25: 25}, {24: 24}, {27: 27}, {26: 26}, {29: 29}, {28: 28}, {31: 31}, {30: 30}, {33: 33}, {32: 32}, {35: 35}, {34: 34}, {37: 37}, {36: 36}, {39: 39}, {38: 38}, {41: 41}, {40: 40}, {43: 43}, {42: 42}, {45: 45}, {44: 44}, {47: 47}, {46: 46}, {49: 49}, {48: 48}, {51: 51}, {50: 50}, {53: 53}, {52: 52}, {55: 55}, {54: 54}, {57: 57}, {56: 56}, {59: 59}, {58: 58}, {61: 61}, {60: 60}, {63: 63}, {62: 62}, {65: 65}, {64: 64}, {67: 67}, {66: 66}, {69: 69}, {68: 68}, {71: 71}, {70: 70}, {73: 73}, {72: 72}, {75: 75}, {74: 74}, {77: 77}, {76: 76}, {79: 79}, {78: 78}, {81: 81}, {80: 80}, {83: 83}, {82: 82}, {85: 85}, {84: 84}, {87: 87}, {86: 86}, {89: 89}, {88: 88}, {91: 91}, {90: 90}, {93: 93}, {92: 92}, {95: 95}, {94: 94}, {97: 97}, {96: 96}, {99: 99}, {98: 98}]
        if res != exp:
            print("Fel i test 2a/52: reverse_pairs([{0: 0}, {1: 1}, {2: 2}, {3: 3}, {4: 4}, {5: 5}, {6: 6}, {7: 7}, {8: 8}, {9: 9}, {10: 10}, {11: 11}, {12: 12}, {13: 13}, {14: 14}, {15: 15}, {16: 16}, {17: 17}, {18: 18}, {19: 19}, {20: 20}, {21: 21}, {22: 22}, {23: 23}, {24: 24}, {25: 25}, {26: 26}, {27: 27}, {28: 28}, {29: 29}, {30: 30}, {31: 31}, {32: 32}, {33: 33}, {34: 34}, {35: 35}, {36: 36}, {37: 37}, {38: 38}, {39: 39}, {40: 40}, {41: 41}, {42: 42}, {43: 43}, {44: 44}, {45: 45}, {46: 46}, {47: 47}, {48: 48}, {49: 49}, {50: 50}, {51: 51}, {52: 52}, {53: 53}, {54: 54}, {55: 55}, {56: 56}, {57: 57}, {58: 58}, {59: 59}, {60: 60}, {61: 61}, {62: 62}, {63: 63}, {64: 64}, {65: 65}, {66: 66}, {67: 67}, {68: 68}, {69: 69}, {70: 70}, {71: 71}, {72: 72}, {73: 73}, {74: 74}, {75: 75}, {76: 76}, {77: 77}, {78: 78}, {79: 79}, {80: 80}, {81: 81}, {82: 82}, {83: 83}, {84: 84}, {85: 85}, {86: 86}, {87: 87}, {88: 88}, {89: 89}, {90: 90}, {91: 91}, {92: 92}, {93: 93}, {94: 94}, {95: 95}, {96: 96}, {97: 97}, {98: 98}, {99: 99}])")
            print("Korrekt svar: {1: 1}, {0: 0}, {3: 3}, {2: 2}, {5: 5}, {4: 4}, {7: 7}, {6: 6}, {9: 9}, {8: 8}, {11: 11}, {10: 10}, {13: 13}, {12: 12}, {15: 15}, {14: 14}, {17: 17}, {16: 16}, {19: 19}, {18: 18}, {21: 21}, {20: 20}, {23: 23}, {22: 22}, {25: 25}, {24: 24}, {27: 27}, {26: 26}, {29: 29}, {28: 28}, {31: 31}, {30: 30}, {33: 33}, {32: 32}, {35: 35}, {34: 34}, {37: 37}, {36: 36}, {39: 39}, {38: 38}, {41: 41}, {40: 40}, {43: 43}, {42: 42}, {45: 45}, {44: 44}, {47: 47}, {46: 46}, {49: 49}, {48: 48}, {51: 51}, {50: 50}, {53: 53}, {52: 52}, {55: 55}, {54: 54}, {57: 57}, {56: 56}, {59: 59}, {58: 58}, {61: 61}, {60: 60}, {63: 63}, {62: 62}, {65: 65}, {64: 64}, {67: 67}, {66: 66}, {69: 69}, {68: 68}, {71: 71}, {70: 70}, {73: 73}, {72: 72}, {75: 75}, {74: 74}, {77: 77}, {76: 76}, {79: 79}, {78: 78}, {81: 81}, {80: 80}, {83: 83}, {82: 82}, {85: 85}, {84: 84}, {87: 87}, {86: 86}, {89: 89}, {88: 88}, {91: 91}, {90: 90}, {93: 93}, {92: 92}, {95: 95}, {94: 94}, {97: 97}, {96: 96}, {99: 99}, {98: 98}")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/52: Exception')
        print_exception()

    try:
        res = reverse_pairs([set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()])
        exp = [set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()]
        if res != exp:
            print("Fel i test 2a/53: reverse_pairs([set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()])")
            print("Korrekt svar: set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/53: Exception')
        print_exception()

    try:
        res = reverse_pairs([{-100}, {-99}, {-98}, {-97}, {-96}, {-95}, {-94}, {-93}, {-92}, {-91}, {-90}, {-89}, {-88}, {-87}, {-86}, {-85}, {-84}, {-83}, {-82}, {-81}, {-80}, {-79}, {-78}, {-77}, {-76}, {-75}, {-74}, {-73}, {-72}, {-71}, {-70}, {-69}, {-68}, {-67}, {-66}, {-65}, {-64}, {-63}, {-62}, {-61}, {-60}, {-59}, {-58}, {-57}, {-56}, {-55}, {-54}, {-53}, {-52}, {-51}, {-50}, {-49}, {-48}, {-47}, {-46}, {-45}, {-44}, {-43}, {-42}, {-41}, {-40}, {-39}, {-38}, {-37}, {-36}, {-35}, {-34}, {-33}, {-32}, {-31}, {-30}, {-29}, {-28}, {-27}, {-26}, {-25}, {-24}, {-23}, {-22}, {-21}, {-20}, {-19}, {-18}, {-17}, {-16}, {-15}, {-14}, {-13}, {-12}, {-11}, {-10}, {-9}, {-8}, {-7}, {-6}, {-5}, {-4}, {-3}, {-2}, {-1}, {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}, {24}, {25}, {26}, {27}, {28}, {29}, {30}, {31}, {32}, {33}, {34}, {35}, {36}, {37}, {38}, {39}, {40}, {41}, {42}, {43}, {44}, {45}, {46}, {47}, {48}, {49}, {50}, {51}, {52}, {53}, {54}, {55}, {56}, {57}, {58}, {59}, {60}, {61}, {62}, {63}, {64}, {65}, {66}, {67}, {68}, {69}, {70}, {71}, {72}, {73}, {74}, {75}, {76}, {77}, {78}, {79}, {80}, {81}, {82}, {83}, {84}, {85}, {86}, {87}, {88}, {89}, {90}, {91}, {92}, {93}, {94}, {95}, {96}, {97}, {98}, {99}])
        exp = [{-99}, {-100}, {-97}, {-98}, {-95}, {-96}, {-93}, {-94}, {-91}, {-92}, {-89}, {-90}, {-87}, {-88}, {-85}, {-86}, {-83}, {-84}, {-81}, {-82}, {-79}, {-80}, {-77}, {-78}, {-75}, {-76}, {-73}, {-74}, {-71}, {-72}, {-69}, {-70}, {-67}, {-68}, {-65}, {-66}, {-63}, {-64}, {-61}, {-62}, {-59}, {-60}, {-57}, {-58}, {-55}, {-56}, {-53}, {-54}, {-51}, {-52}, {-49}, {-50}, {-47}, {-48}, {-45}, {-46}, {-43}, {-44}, {-41}, {-42}, {-39}, {-40}, {-37}, {-38}, {-35}, {-36}, {-33}, {-34}, {-31}, {-32}, {-29}, {-30}, {-27}, {-28}, {-25}, {-26}, {-23}, {-24}, {-21}, {-22}, {-19}, {-20}, {-17}, {-18}, {-15}, {-16}, {-13}, {-14}, {-11}, {-12}, {-9}, {-10}, {-7}, {-8}, {-5}, {-6}, {-3}, {-4}, {-1}, {-2}, {1}, {0}, {3}, {2}, {5}, {4}, {7}, {6}, {9}, {8}, {11}, {10}, {13}, {12}, {15}, {14}, {17}, {16}, {19}, {18}, {21}, {20}, {23}, {22}, {25}, {24}, {27}, {26}, {29}, {28}, {31}, {30}, {33}, {32}, {35}, {34}, {37}, {36}, {39}, {38}, {41}, {40}, {43}, {42}, {45}, {44}, {47}, {46}, {49}, {48}, {51}, {50}, {53}, {52}, {55}, {54}, {57}, {56}, {59}, {58}, {61}, {60}, {63}, {62}, {65}, {64}, {67}, {66}, {69}, {68}, {71}, {70}, {73}, {72}, {75}, {74}, {77}, {76}, {79}, {78}, {81}, {80}, {83}, {82}, {85}, {84}, {87}, {86}, {89}, {88}, {91}, {90}, {93}, {92}, {95}, {94}, {97}, {96}, {99}, {98}]
        if res != exp:
            print("Fel i test 2a/54: reverse_pairs([{-100}, {-99}, {-98}, {-97}, {-96}, {-95}, {-94}, {-93}, {-92}, {-91}, {-90}, {-89}, {-88}, {-87}, {-86}, {-85}, {-84}, {-83}, {-82}, {-81}, {-80}, {-79}, {-78}, {-77}, {-76}, {-75}, {-74}, {-73}, {-72}, {-71}, {-70}, {-69}, {-68}, {-67}, {-66}, {-65}, {-64}, {-63}, {-62}, {-61}, {-60}, {-59}, {-58}, {-57}, {-56}, {-55}, {-54}, {-53}, {-52}, {-51}, {-50}, {-49}, {-48}, {-47}, {-46}, {-45}, {-44}, {-43}, {-42}, {-41}, {-40}, {-39}, {-38}, {-37}, {-36}, {-35}, {-34}, {-33}, {-32}, {-31}, {-30}, {-29}, {-28}, {-27}, {-26}, {-25}, {-24}, {-23}, {-22}, {-21}, {-20}, {-19}, {-18}, {-17}, {-16}, {-15}, {-14}, {-13}, {-12}, {-11}, {-10}, {-9}, {-8}, {-7}, {-6}, {-5}, {-4}, {-3}, {-2}, {-1}, {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}, {24}, {25}, {26}, {27}, {28}, {29}, {30}, {31}, {32}, {33}, {34}, {35}, {36}, {37}, {38}, {39}, {40}, {41}, {42}, {43}, {44}, {45}, {46}, {47}, {48}, {49}, {50}, {51}, {52}, {53}, {54}, {55}, {56}, {57}, {58}, {59}, {60}, {61}, {62}, {63}, {64}, {65}, {66}, {67}, {68}, {69}, {70}, {71}, {72}, {73}, {74}, {75}, {76}, {77}, {78}, {79}, {80}, {81}, {82}, {83}, {84}, {85}, {86}, {87}, {88}, {89}, {90}, {91}, {92}, {93}, {94}, {95}, {96}, {97}, {98}, {99}])")
            print("Korrekt svar: {-99}, {-100}, {-97}, {-98}, {-95}, {-96}, {-93}, {-94}, {-91}, {-92}, {-89}, {-90}, {-87}, {-88}, {-85}, {-86}, {-83}, {-84}, {-81}, {-82}, {-79}, {-80}, {-77}, {-78}, {-75}, {-76}, {-73}, {-74}, {-71}, {-72}, {-69}, {-70}, {-67}, {-68}, {-65}, {-66}, {-63}, {-64}, {-61}, {-62}, {-59}, {-60}, {-57}, {-58}, {-55}, {-56}, {-53}, {-54}, {-51}, {-52}, {-49}, {-50}, {-47}, {-48}, {-45}, {-46}, {-43}, {-44}, {-41}, {-42}, {-39}, {-40}, {-37}, {-38}, {-35}, {-36}, {-33}, {-34}, {-31}, {-32}, {-29}, {-30}, {-27}, {-28}, {-25}, {-26}, {-23}, {-24}, {-21}, {-22}, {-19}, {-20}, {-17}, {-18}, {-15}, {-16}, {-13}, {-14}, {-11}, {-12}, {-9}, {-10}, {-7}, {-8}, {-5}, {-6}, {-3}, {-4}, {-1}, {-2}, {1}, {0}, {3}, {2}, {5}, {4}, {7}, {6}, {9}, {8}, {11}, {10}, {13}, {12}, {15}, {14}, {17}, {16}, {19}, {18}, {21}, {20}, {23}, {22}, {25}, {24}, {27}, {26}, {29}, {28}, {31}, {30}, {33}, {32}, {35}, {34}, {37}, {36}, {39}, {38}, {41}, {40}, {43}, {42}, {45}, {44}, {47}, {46}, {49}, {48}, {51}, {50}, {53}, {52}, {55}, {54}, {57}, {56}, {59}, {58}, {61}, {60}, {63}, {62}, {65}, {64}, {67}, {66}, {69}, {68}, {71}, {70}, {73}, {72}, {75}, {74}, {77}, {76}, {79}, {78}, {81}, {80}, {83}, {82}, {85}, {84}, {87}, {86}, {89}, {88}, {91}, {90}, {93}, {92}, {95}, {94}, {97}, {96}, {99}, {98}")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/54: Exception')
        print_exception()

    try:
        res = reverse_pairs([{}, set(), (), []])
        exp = [set(), {}, [], ()]
        if res != exp:
            print("Fel i test 2a/55: reverse_pairs([{}, set(), (), []])")
            print("Korrekt svar: set(), {}, [], ()")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/55: Exception')
        print_exception()

    try:
        res = reverse_pairs([{1, 2, '3'}, [1, '2', 3], {'1': 1, 2: '2', 3: '3'}, ('1', 2, '3')])
        exp = [[1, '2', 3], {1, 2, '3'}, ('1', 2, '3'), {'1': 1, 2: '2', 3: '3'}]
        if res != exp:
            print("Fel i test 2a/56: reverse_pairs([{1, 2, '3'}, [1, '2', 3], {'1': 1, 2: '2', 3: '3'}, ('1', 2, '3')])")
            print("Korrekt svar: [1, '2', 3], {1, 2, '3'}, ('1', 2, '3'), {'1': 1, 2: '2', 3: '3'}")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/56: Exception')
        print_exception()

    try:
        res = reverse_pairs([[set(), (2, 'a'), {1: 'a'}], {2, 3, (1, 'a', False)}, {'1': [1, 2, 3], '2': {}}, (set(), [2], {1: '1'})])
        exp = [{2, 3, (1, 'a', False)}, [set(), (2, 'a'), {1: 'a'}], (set(), [2], {1: '1'}), {'1': [1, 2, 3], '2': {}}]
        if res != exp:
            print("Fel i test 2a/57: reverse_pairs([[set(), (2, 'a'), {1: 'a'}], {2, 3, (1, 'a', False)}, {'1': [1, 2, 3], '2': {}}, (set(), [2], {1: '1'})])")
            print("Korrekt svar: {2, 3, (1, 'a', False)}, [set(), (2, 'a'), {1: 'a'}], (set(), [2], {1: '1'}), {'1': [1, 2, 3], '2': {}}")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/57: Exception')
        print_exception()



    try:
        res = reverse_pairs([int])
        exp = [int]
        if res != exp:
            print("Fel i test 2a/60: reverse_pairs([int])")
            print("Korrekt svar: <class '__main__.int'>")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/60: Exception')
        print_exception()

    try:
        res = reverse_pairs([int, list])
        exp = [list, int]
        if res != exp:
            print("Fel i test 2a/61: reverse_pairs([int, list])")
            print("Korrekt svar: <class '__main__.list'>, <class '__main__.int'>")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/61: Exception')
        print_exception()

    try:
        res = reverse_pairs([1, {'a': 2}, 3])
        exp = [{'a': 2}, 1, 3]
        if res != exp:
            print("Fel i test 2a/62: reverse_pairs([1, {'a': 2}, 3])")
            print("Korrekt svar: {'a': 2}, 1, 3")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/62: Exception')
        print_exception()

    try:
        res = reverse_pairs([[1, 2, 3], '123'])
        exp = ['123', [1, 2, 3]]
        if res != exp:
            print("Fel i test 2a/63: reverse_pairs([[1, 2, 3], '123'])")
            print("Korrekt svar: '123', [1, 2, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/63: Exception')
        print_exception()


    try:
        res = reverse_pairs([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        exp = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if res != exp:
            print("Fel i test 2a/65: reverse_pairs([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])")
            print("Korrekt svar: 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/65: Exception')
        print_exception()

    try:
        res = reverse_pairs([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999])
        exp = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26, 29, 28, 31, 30, 33, 32, 35, 34, 37, 36, 39, 38, 41, 40, 43, 42, 45, 44, 47, 46, 49, 48, 51, 50, 53, 52, 55, 54, 57, 56, 59, 58, 61, 60, 63, 62, 65, 64, 67, 66, 69, 68, 71, 70, 73, 72, 75, 74, 77, 76, 79, 78, 81, 80, 83, 82, 85, 84, 87, 86, 89, 88, 91, 90, 93, 92, 95, 94, 97, 96, 99, 98, 101, 100, 103, 102, 105, 104, 107, 106, 109, 108, 111, 110, 113, 112, 115, 114, 117, 116, 119, 118, 121, 120, 123, 122, 125, 124, 127, 126, 129, 128, 131, 130, 133, 132, 135, 134, 137, 136, 139, 138, 141, 140, 143, 142, 145, 144, 147, 146, 149, 148, 151, 150, 153, 152, 155, 154, 157, 156, 159, 158, 161, 160, 163, 162, 165, 164, 167, 166, 169, 168, 171, 170, 173, 172, 175, 174, 177, 176, 179, 178, 181, 180, 183, 182, 185, 184, 187, 186, 189, 188, 191, 190, 193, 192, 195, 194, 197, 196, 199, 198, 201, 200, 203, 202, 205, 204, 207, 206, 209, 208, 211, 210, 213, 212, 215, 214, 217, 216, 219, 218, 221, 220, 223, 222, 225, 224, 227, 226, 229, 228, 231, 230, 233, 232, 235, 234, 237, 236, 239, 238, 241, 240, 243, 242, 245, 244, 247, 246, 249, 248, 251, 250, 253, 252, 255, 254, 257, 256, 259, 258, 261, 260, 263, 262, 265, 264, 267, 266, 269, 268, 271, 270, 273, 272, 275, 274, 277, 276, 279, 278, 281, 280, 283, 282, 285, 284, 287, 286, 289, 288, 291, 290, 293, 292, 295, 294, 297, 296, 299, 298, 301, 300, 303, 302, 305, 304, 307, 306, 309, 308, 311, 310, 313, 312, 315, 314, 317, 316, 319, 318, 321, 320, 323, 322, 325, 324, 327, 326, 329, 328, 331, 330, 333, 332, 335, 334, 337, 336, 339, 338, 341, 340, 343, 342, 345, 344, 347, 346, 349, 348, 351, 350, 353, 352, 355, 354, 357, 356, 359, 358, 361, 360, 363, 362, 365, 364, 367, 366, 369, 368, 371, 370, 373, 372, 375, 374, 377, 376, 379, 378, 381, 380, 383, 382, 385, 384, 387, 386, 389, 388, 391, 390, 393, 392, 395, 394, 397, 396, 399, 398, 401, 400, 403, 402, 405, 404, 407, 406, 409, 408, 411, 410, 413, 412, 415, 414, 417, 416, 419, 418, 421, 420, 423, 422, 425, 424, 427, 426, 429, 428, 431, 430, 433, 432, 435, 434, 437, 436, 439, 438, 441, 440, 443, 442, 445, 444, 447, 446, 449, 448, 451, 450, 453, 452, 455, 454, 457, 456, 459, 458, 461, 460, 463, 462, 465, 464, 467, 466, 469, 468, 471, 470, 473, 472, 475, 474, 477, 476, 479, 478, 481, 480, 483, 482, 485, 484, 487, 486, 489, 488, 491, 490, 493, 492, 495, 494, 497, 496, 499, 498, 501, 500, 503, 502, 505, 504, 507, 506, 509, 508, 511, 510, 513, 512, 515, 514, 517, 516, 519, 518, 521, 520, 523, 522, 525, 524, 527, 526, 529, 528, 531, 530, 533, 532, 535, 534, 537, 536, 539, 538, 541, 540, 543, 542, 545, 544, 547, 546, 549, 548, 551, 550, 553, 552, 555, 554, 557, 556, 559, 558, 561, 560, 563, 562, 565, 564, 567, 566, 569, 568, 571, 570, 573, 572, 575, 574, 577, 576, 579, 578, 581, 580, 583, 582, 585, 584, 587, 586, 589, 588, 591, 590, 593, 592, 595, 594, 597, 596, 599, 598, 601, 600, 603, 602, 605, 604, 607, 606, 609, 608, 611, 610, 613, 612, 615, 614, 617, 616, 619, 618, 621, 620, 623, 622, 625, 624, 627, 626, 629, 628, 631, 630, 633, 632, 635, 634, 637, 636, 639, 638, 641, 640, 643, 642, 645, 644, 647, 646, 649, 648, 651, 650, 653, 652, 655, 654, 657, 656, 659, 658, 661, 660, 663, 662, 665, 664, 667, 666, 669, 668, 671, 670, 673, 672, 675, 674, 677, 676, 679, 678, 681, 680, 683, 682, 685, 684, 687, 686, 689, 688, 691, 690, 693, 692, 695, 694, 697, 696, 699, 698, 701, 700, 703, 702, 705, 704, 707, 706, 709, 708, 711, 710, 713, 712, 715, 714, 717, 716, 719, 718, 721, 720, 723, 722, 725, 724, 727, 726, 729, 728, 731, 730, 733, 732, 735, 734, 737, 736, 739, 738, 741, 740, 743, 742, 745, 744, 747, 746, 749, 748, 751, 750, 753, 752, 755, 754, 757, 756, 759, 758, 761, 760, 763, 762, 765, 764, 767, 766, 769, 768, 771, 770, 773, 772, 775, 774, 777, 776, 779, 778, 781, 780, 783, 782, 785, 784, 787, 786, 789, 788, 791, 790, 793, 792, 795, 794, 797, 796, 799, 798, 801, 800, 803, 802, 805, 804, 807, 806, 809, 808, 811, 810, 813, 812, 815, 814, 817, 816, 819, 818, 821, 820, 823, 822, 825, 824, 827, 826, 829, 828, 831, 830, 833, 832, 835, 834, 837, 836, 839, 838, 841, 840, 843, 842, 845, 844, 847, 846, 849, 848, 851, 850, 853, 852, 855, 854, 857, 856, 859, 858, 861, 860, 863, 862, 865, 864, 867, 866, 869, 868, 871, 870, 873, 872, 875, 874, 877, 876, 879, 878, 881, 880, 883, 882, 885, 884, 887, 886, 889, 888, 891, 890, 893, 892, 895, 894, 897, 896, 899, 898, 901, 900, 903, 902, 905, 904, 907, 906, 909, 908, 911, 910, 913, 912, 915, 914, 917, 916, 919, 918, 921, 920, 923, 922, 925, 924, 927, 926, 929, 928, 931, 930, 933, 932, 935, 934, 937, 936, 939, 938, 941, 940, 943, 942, 945, 944, 947, 946, 949, 948, 951, 950, 953, 952, 955, 954, 957, 956, 959, 958, 961, 960, 963, 962, 965, 964, 967, 966, 969, 968, 971, 970, 973, 972, 975, 974, 977, 976, 979, 978, 981, 980, 983, 982, 985, 984, 987, 986, 989, 988, 991, 990, 993, 992, 995, 994, 997, 996, 999, 998]
        if res != exp:
            print("Fel i test 2a/66: reverse_pairs([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999])")
            print("Korrekt svar: 1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26, 29, 28, 31, 30, 33, 32, 35, 34, 37, 36, 39, 38, 41, 40, 43, 42, 45, 44, 47, 46, 49, 48, 51, 50, 53, 52, 55, 54, 57, 56, 59, 58, 61, 60, 63, 62, 65, 64, 67, 66, 69, 68, 71, 70, 73, 72, 75, 74, 77, 76, 79, 78, 81, 80, 83, 82, 85, 84, 87, 86, 89, 88, 91, 90, 93, 92, 95, 94, 97, 96, 99, 98, 101, 100, 103, 102, 105, 104, 107, 106, 109, 108, 111, 110, 113, 112, 115, 114, 117, 116, 119, 118, 121, 120, 123, 122, 125, 124, 127, 126, 129, 128, 131, 130, 133, 132, 135, 134, 137, 136, 139, 138, 141, 140, 143, 142, 145, 144, 147, 146, 149, 148, 151, 150, 153, 152, 155, 154, 157, 156, 159, 158, 161, 160, 163, 162, 165, 164, 167, 166, 169, 168, 171, 170, 173, 172, 175, 174, 177, 176, 179, 178, 181, 180, 183, 182, 185, 184, 187, 186, 189, 188, 191, 190, 193, 192, 195, 194, 197, 196, 199, 198, 201, 200, 203, 202, 205, 204, 207, 206, 209, 208, 211, 210, 213, 212, 215, 214, 217, 216, 219, 218, 221, 220, 223, 222, 225, 224, 227, 226, 229, 228, 231, 230, 233, 232, 235, 234, 237, 236, 239, 238, 241, 240, 243, 242, 245, 244, 247, 246, 249, 248, 251, 250, 253, 252, 255, 254, 257, 256, 259, 258, 261, 260, 263, 262, 265, 264, 267, 266, 269, 268, 271, 270, 273, 272, 275, 274, 277, 276, 279, 278, 281, 280, 283, 282, 285, 284, 287, 286, 289, 288, 291, 290, 293, 292, 295, 294, 297, 296, 299, 298, 301, 300, 303, 302, 305, 304, 307, 306, 309, 308, 311, 310, 313, 312, 315, 314, 317, 316, 319, 318, 321, 320, 323, 322, 325, 324, 327, 326, 329, 328, 331, 330, 333, 332, 335, 334, 337, 336, 339, 338, 341, 340, 343, 342, 345, 344, 347, 346, 349, 348, 351, 350, 353, 352, 355, 354, 357, 356, 359, 358, 361, 360, 363, 362, 365, 364, 367, 366, 369, 368, 371, 370, 373, 372, 375, 374, 377, 376, 379, 378, 381, 380, 383, 382, 385, 384, 387, 386, 389, 388, 391, 390, 393, 392, 395, 394, 397, 396, 399, 398, 401, 400, 403, 402, 405, 404, 407, 406, 409, 408, 411, 410, 413, 412, 415, 414, 417, 416, 419, 418, 421, 420, 423, 422, 425, 424, 427, 426, 429, 428, 431, 430, 433, 432, 435, 434, 437, 436, 439, 438, 441, 440, 443, 442, 445, 444, 447, 446, 449, 448, 451, 450, 453, 452, 455, 454, 457, 456, 459, 458, 461, 460, 463, 462, 465, 464, 467, 466, 469, 468, 471, 470, 473, 472, 475, 474, 477, 476, 479, 478, 481, 480, 483, 482, 485, 484, 487, 486, 489, 488, 491, 490, 493, 492, 495, 494, 497, 496, 499, 498, 501, 500, 503, 502, 505, 504, 507, 506, 509, 508, 511, 510, 513, 512, 515, 514, 517, 516, 519, 518, 521, 520, 523, 522, 525, 524, 527, 526, 529, 528, 531, 530, 533, 532, 535, 534, 537, 536, 539, 538, 541, 540, 543, 542, 545, 544, 547, 546, 549, 548, 551, 550, 553, 552, 555, 554, 557, 556, 559, 558, 561, 560, 563, 562, 565, 564, 567, 566, 569, 568, 571, 570, 573, 572, 575, 574, 577, 576, 579, 578, 581, 580, 583, 582, 585, 584, 587, 586, 589, 588, 591, 590, 593, 592, 595, 594, 597, 596, 599, 598, 601, 600, 603, 602, 605, 604, 607, 606, 609, 608, 611, 610, 613, 612, 615, 614, 617, 616, 619, 618, 621, 620, 623, 622, 625, 624, 627, 626, 629, 628, 631, 630, 633, 632, 635, 634, 637, 636, 639, 638, 641, 640, 643, 642, 645, 644, 647, 646, 649, 648, 651, 650, 653, 652, 655, 654, 657, 656, 659, 658, 661, 660, 663, 662, 665, 664, 667, 666, 669, 668, 671, 670, 673, 672, 675, 674, 677, 676, 679, 678, 681, 680, 683, 682, 685, 684, 687, 686, 689, 688, 691, 690, 693, 692, 695, 694, 697, 696, 699, 698, 701, 700, 703, 702, 705, 704, 707, 706, 709, 708, 711, 710, 713, 712, 715, 714, 717, 716, 719, 718, 721, 720, 723, 722, 725, 724, 727, 726, 729, 728, 731, 730, 733, 732, 735, 734, 737, 736, 739, 738, 741, 740, 743, 742, 745, 744, 747, 746, 749, 748, 751, 750, 753, 752, 755, 754, 757, 756, 759, 758, 761, 760, 763, 762, 765, 764, 767, 766, 769, 768, 771, 770, 773, 772, 775, 774, 777, 776, 779, 778, 781, 780, 783, 782, 785, 784, 787, 786, 789, 788, 791, 790, 793, 792, 795, 794, 797, 796, 799, 798, 801, 800, 803, 802, 805, 804, 807, 806, 809, 808, 811, 810, 813, 812, 815, 814, 817, 816, 819, 818, 821, 820, 823, 822, 825, 824, 827, 826, 829, 828, 831, 830, 833, 832, 835, 834, 837, 836, 839, 838, 841, 840, 843, 842, 845, 844, 847, 846, 849, 848, 851, 850, 853, 852, 855, 854, 857, 856, 859, 858, 861, 860, 863, 862, 865, 864, 867, 866, 869, 868, 871, 870, 873, 872, 875, 874, 877, 876, 879, 878, 881, 880, 883, 882, 885, 884, 887, 886, 889, 888, 891, 890, 893, 892, 895, 894, 897, 896, 899, 898, 901, 900, 903, 902, 905, 904, 907, 906, 909, 908, 911, 910, 913, 912, 915, 914, 917, 916, 919, 918, 921, 920, 923, 922, 925, 924, 927, 926, 929, 928, 931, 930, 933, 932, 935, 934, 937, 936, 939, 938, 941, 940, 943, 942, 945, 944, 947, 946, 949, 948, 951, 950, 953, 952, 955, 954, 957, 956, 959, 958, 961, 960, 963, 962, 965, 964, 967, 966, 969, 968, 971, 970, 973, 972, 975, 974, 977, 976, 979, 978, 981, 980, 983, 982, 985, 984, 987, 986, 989, 988, 991, 990, 993, 992, 995, 994, 997, 996, 999, 998")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/66: Exception')
        print_exception()

    try:
        res = reverse_pairs(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176', '177', '178', '179', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191', '192', '193', '194', '195', '196', '197', '198', '199', '200', '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '211', '212', '213', '214', '215', '216', '217', '218', '219', '220', '221', '222', '223', '224', '225', '226', '227', '228', '229', '230', '231', '232', '233', '234', '235', '236', '237', '238', '239', '240', '241', '242', '243', '244', '245', '246', '247', '248', '249', '250', '251', '252', '253', '254', '255', '256', '257', '258', '259', '260', '261', '262', '263', '264', '265', '266', '267', '268', '269', '270', '271', '272', '273', '274', '275', '276', '277', '278', '279', '280', '281', '282', '283', '284', '285', '286', '287', '288', '289', '290', '291', '292', '293', '294', '295', '296', '297', '298', '299', '300', '301', '302', '303', '304', '305', '306', '307', '308', '309', '310', '311', '312', '313', '314', '315', '316', '317', '318', '319', '320', '321', '322', '323', '324', '325', '326', '327', '328', '329', '330', '331', '332', '333', '334', '335', '336', '337', '338', '339', '340', '341', '342', '343', '344', '345', '346', '347', '348', '349', '350', '351', '352', '353', '354', '355', '356', '357', '358', '359', '360', '361', '362', '363', '364', '365', '366', '367', '368', '369', '370', '371', '372', '373', '374', '375', '376', '377', '378', '379', '380', '381', '382', '383', '384', '385', '386', '387', '388', '389', '390', '391', '392', '393', '394', '395', '396', '397', '398', '399', '400', '401', '402', '403', '404', '405', '406', '407', '408', '409', '410', '411', '412', '413', '414', '415', '416', '417', '418', '419', '420', '421', '422', '423', '424', '425', '426', '427', '428', '429', '430', '431', '432', '433', '434', '435', '436', '437', '438', '439', '440', '441', '442', '443', '444', '445', '446', '447', '448', '449', '450', '451', '452', '453', '454', '455', '456', '457', '458', '459', '460', '461', '462', '463', '464', '465', '466', '467', '468', '469', '470', '471', '472', '473', '474', '475', '476', '477', '478', '479', '480', '481', '482', '483', '484', '485', '486', '487', '488', '489', '490', '491', '492', '493', '494', '495', '496', '497', '498', '499', '500', '501', '502', '503', '504', '505', '506', '507', '508', '509', '510', '511', '512', '513', '514', '515', '516', '517', '518', '519', '520', '521', '522', '523', '524', '525', '526', '527', '528', '529', '530', '531', '532', '533', '534', '535', '536', '537', '538', '539', '540', '541', '542', '543', '544', '545', '546', '547', '548', '549', '550', '551', '552', '553', '554', '555', '556', '557', '558', '559', '560', '561', '562', '563', '564', '565', '566', '567', '568', '569', '570', '571', '572', '573', '574', '575', '576', '577', '578', '579', '580', '581', '582', '583', '584', '585', '586', '587', '588', '589', '590', '591', '592', '593', '594', '595', '596', '597', '598', '599', '600', '601', '602', '603', '604', '605', '606', '607', '608', '609', '610', '611', '612', '613', '614', '615', '616', '617', '618', '619', '620', '621', '622', '623', '624', '625', '626', '627', '628', '629', '630', '631', '632', '633', '634', '635', '636', '637', '638', '639', '640', '641', '642', '643', '644', '645', '646', '647', '648', '649', '650', '651', '652', '653', '654', '655', '656', '657', '658', '659', '660', '661', '662', '663', '664', '665', '666', '667', '668', '669', '670', '671', '672', '673', '674', '675', '676', '677', '678', '679', '680', '681', '682', '683', '684', '685', '686', '687', '688', '689', '690', '691', '692', '693', '694', '695', '696', '697', '698', '699', '700', '701', '702', '703', '704', '705', '706', '707', '708', '709', '710', '711', '712', '713', '714', '715', '716', '717', '718', '719', '720', '721', '722', '723', '724', '725', '726', '727', '728', '729', '730', '731', '732', '733', '734', '735', '736', '737', '738', '739', '740', '741', '742', '743', '744', '745', '746', '747', '748', '749', '750', '751', '752', '753', '754', '755', '756', '757', '758', '759', '760', '761', '762', '763', '764', '765', '766', '767', '768', '769', '770', '771', '772', '773', '774', '775', '776', '777', '778', '779', '780', '781', '782', '783', '784', '785', '786', '787', '788', '789', '790', '791', '792', '793', '794', '795', '796', '797', '798', '799', '800', '801', '802', '803', '804', '805', '806', '807', '808', '809', '810', '811', '812', '813', '814', '815', '816', '817', '818', '819', '820', '821', '822', '823', '824', '825', '826', '827', '828', '829', '830', '831', '832', '833', '834', '835', '836', '837', '838', '839', '840', '841', '842', '843', '844', '845', '846', '847', '848', '849', '850', '851', '852', '853', '854', '855', '856', '857', '858', '859', '860', '861', '862', '863', '864', '865', '866', '867', '868', '869', '870', '871', '872', '873', '874', '875', '876', '877', '878', '879', '880', '881', '882', '883', '884', '885', '886', '887', '888', '889', '890', '891', '892', '893', '894', '895', '896', '897', '898', '899', '900', '901', '902', '903', '904', '905', '906', '907', '908', '909', '910', '911', '912', '913', '914', '915', '916', '917', '918', '919', '920', '921', '922', '923', '924', '925', '926', '927', '928', '929', '930', '931', '932', '933', '934', '935', '936', '937', '938', '939', '940', '941', '942', '943', '944', '945', '946', '947', '948', '949', '950', '951', '952', '953', '954', '955', '956', '957', '958', '959', '960', '961', '962', '963', '964', '965', '966', '967', '968', '969', '970', '971', '972', '973', '974', '975', '976', '977', '978', '979', '980', '981', '982', '983', '984', '985', '986', '987', '988', '989', '990', '991', '992', '993', '994', '995', '996', '997', '998', '999'])
        exp = ['1', '0', '3', '2', '5', '4', '7', '6', '9', '8', '11', '10', '13', '12', '15', '14', '17', '16', '19', '18', '21', '20', '23', '22', '25', '24', '27', '26', '29', '28', '31', '30', '33', '32', '35', '34', '37', '36', '39', '38', '41', '40', '43', '42', '45', '44', '47', '46', '49', '48', '51', '50', '53', '52', '55', '54', '57', '56', '59', '58', '61', '60', '63', '62', '65', '64', '67', '66', '69', '68', '71', '70', '73', '72', '75', '74', '77', '76', '79', '78', '81', '80', '83', '82', '85', '84', '87', '86', '89', '88', '91', '90', '93', '92', '95', '94', '97', '96', '99', '98', '101', '100', '103', '102', '105', '104', '107', '106', '109', '108', '111', '110', '113', '112', '115', '114', '117', '116', '119', '118', '121', '120', '123', '122', '125', '124', '127', '126', '129', '128', '131', '130', '133', '132', '135', '134', '137', '136', '139', '138', '141', '140', '143', '142', '145', '144', '147', '146', '149', '148', '151', '150', '153', '152', '155', '154', '157', '156', '159', '158', '161', '160', '163', '162', '165', '164', '167', '166', '169', '168', '171', '170', '173', '172', '175', '174', '177', '176', '179', '178', '181', '180', '183', '182', '185', '184', '187', '186', '189', '188', '191', '190', '193', '192', '195', '194', '197', '196', '199', '198', '201', '200', '203', '202', '205', '204', '207', '206', '209', '208', '211', '210', '213', '212', '215', '214', '217', '216', '219', '218', '221', '220', '223', '222', '225', '224', '227', '226', '229', '228', '231', '230', '233', '232', '235', '234', '237', '236', '239', '238', '241', '240', '243', '242', '245', '244', '247', '246', '249', '248', '251', '250', '253', '252', '255', '254', '257', '256', '259', '258', '261', '260', '263', '262', '265', '264', '267', '266', '269', '268', '271', '270', '273', '272', '275', '274', '277', '276', '279', '278', '281', '280', '283', '282', '285', '284', '287', '286', '289', '288', '291', '290', '293', '292', '295', '294', '297', '296', '299', '298', '301', '300', '303', '302', '305', '304', '307', '306', '309', '308', '311', '310', '313', '312', '315', '314', '317', '316', '319', '318', '321', '320', '323', '322', '325', '324', '327', '326', '329', '328', '331', '330', '333', '332', '335', '334', '337', '336', '339', '338', '341', '340', '343', '342', '345', '344', '347', '346', '349', '348', '351', '350', '353', '352', '355', '354', '357', '356', '359', '358', '361', '360', '363', '362', '365', '364', '367', '366', '369', '368', '371', '370', '373', '372', '375', '374', '377', '376', '379', '378', '381', '380', '383', '382', '385', '384', '387', '386', '389', '388', '391', '390', '393', '392', '395', '394', '397', '396', '399', '398', '401', '400', '403', '402', '405', '404', '407', '406', '409', '408', '411', '410', '413', '412', '415', '414', '417', '416', '419', '418', '421', '420', '423', '422', '425', '424', '427', '426', '429', '428', '431', '430', '433', '432', '435', '434', '437', '436', '439', '438', '441', '440', '443', '442', '445', '444', '447', '446', '449', '448', '451', '450', '453', '452', '455', '454', '457', '456', '459', '458', '461', '460', '463', '462', '465', '464', '467', '466', '469', '468', '471', '470', '473', '472', '475', '474', '477', '476', '479', '478', '481', '480', '483', '482', '485', '484', '487', '486', '489', '488', '491', '490', '493', '492', '495', '494', '497', '496', '499', '498', '501', '500', '503', '502', '505', '504', '507', '506', '509', '508', '511', '510', '513', '512', '515', '514', '517', '516', '519', '518', '521', '520', '523', '522', '525', '524', '527', '526', '529', '528', '531', '530', '533', '532', '535', '534', '537', '536', '539', '538', '541', '540', '543', '542', '545', '544', '547', '546', '549', '548', '551', '550', '553', '552', '555', '554', '557', '556', '559', '558', '561', '560', '563', '562', '565', '564', '567', '566', '569', '568', '571', '570', '573', '572', '575', '574', '577', '576', '579', '578', '581', '580', '583', '582', '585', '584', '587', '586', '589', '588', '591', '590', '593', '592', '595', '594', '597', '596', '599', '598', '601', '600', '603', '602', '605', '604', '607', '606', '609', '608', '611', '610', '613', '612', '615', '614', '617', '616', '619', '618', '621', '620', '623', '622', '625', '624', '627', '626', '629', '628', '631', '630', '633', '632', '635', '634', '637', '636', '639', '638', '641', '640', '643', '642', '645', '644', '647', '646', '649', '648', '651', '650', '653', '652', '655', '654', '657', '656', '659', '658', '661', '660', '663', '662', '665', '664', '667', '666', '669', '668', '671', '670', '673', '672', '675', '674', '677', '676', '679', '678', '681', '680', '683', '682', '685', '684', '687', '686', '689', '688', '691', '690', '693', '692', '695', '694', '697', '696', '699', '698', '701', '700', '703', '702', '705', '704', '707', '706', '709', '708', '711', '710', '713', '712', '715', '714', '717', '716', '719', '718', '721', '720', '723', '722', '725', '724', '727', '726', '729', '728', '731', '730', '733', '732', '735', '734', '737', '736', '739', '738', '741', '740', '743', '742', '745', '744', '747', '746', '749', '748', '751', '750', '753', '752', '755', '754', '757', '756', '759', '758', '761', '760', '763', '762', '765', '764', '767', '766', '769', '768', '771', '770', '773', '772', '775', '774', '777', '776', '779', '778', '781', '780', '783', '782', '785', '784', '787', '786', '789', '788', '791', '790', '793', '792', '795', '794', '797', '796', '799', '798', '801', '800', '803', '802', '805', '804', '807', '806', '809', '808', '811', '810', '813', '812', '815', '814', '817', '816', '819', '818', '821', '820', '823', '822', '825', '824', '827', '826', '829', '828', '831', '830', '833', '832', '835', '834', '837', '836', '839', '838', '841', '840', '843', '842', '845', '844', '847', '846', '849', '848', '851', '850', '853', '852', '855', '854', '857', '856', '859', '858', '861', '860', '863', '862', '865', '864', '867', '866', '869', '868', '871', '870', '873', '872', '875', '874', '877', '876', '879', '878', '881', '880', '883', '882', '885', '884', '887', '886', '889', '888', '891', '890', '893', '892', '895', '894', '897', '896', '899', '898', '901', '900', '903', '902', '905', '904', '907', '906', '909', '908', '911', '910', '913', '912', '915', '914', '917', '916', '919', '918', '921', '920', '923', '922', '925', '924', '927', '926', '929', '928', '931', '930', '933', '932', '935', '934', '937', '936', '939', '938', '941', '940', '943', '942', '945', '944', '947', '946', '949', '948', '951', '950', '953', '952', '955', '954', '957', '956', '959', '958', '961', '960', '963', '962', '965', '964', '967', '966', '969', '968', '971', '970', '973', '972', '975', '974', '977', '976', '979', '978', '981', '980', '983', '982', '985', '984', '987', '986', '989', '988', '991', '990', '993', '992', '995', '994', '997', '996', '999', '998']
        if res != exp:
            print("Fel i test 2a/67: reverse_pairs(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176', '177', '178', '179', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191', '192', '193', '194', '195', '196', '197', '198', '199', '200', '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '211', '212', '213', '214', '215', '216', '217', '218', '219', '220', '221', '222', '223', '224', '225', '226', '227', '228', '229', '230', '231', '232', '233', '234', '235', '236', '237', '238', '239', '240', '241', '242', '243', '244', '245', '246', '247', '248', '249', '250', '251', '252', '253', '254', '255', '256', '257', '258', '259', '260', '261', '262', '263', '264', '265', '266', '267', '268', '269', '270', '271', '272', '273', '274', '275', '276', '277', '278', '279', '280', '281', '282', '283', '284', '285', '286', '287', '288', '289', '290', '291', '292', '293', '294', '295', '296', '297', '298', '299', '300', '301', '302', '303', '304', '305', '306', '307', '308', '309', '310', '311', '312', '313', '314', '315', '316', '317', '318', '319', '320', '321', '322', '323', '324', '325', '326', '327', '328', '329', '330', '331', '332', '333', '334', '335', '336', '337', '338', '339', '340', '341', '342', '343', '344', '345', '346', '347', '348', '349', '350', '351', '352', '353', '354', '355', '356', '357', '358', '359', '360', '361', '362', '363', '364', '365', '366', '367', '368', '369', '370', '371', '372', '373', '374', '375', '376', '377', '378', '379', '380', '381', '382', '383', '384', '385', '386', '387', '388', '389', '390', '391', '392', '393', '394', '395', '396', '397', '398', '399', '400', '401', '402', '403', '404', '405', '406', '407', '408', '409', '410', '411', '412', '413', '414', '415', '416', '417', '418', '419', '420', '421', '422', '423', '424', '425', '426', '427', '428', '429', '430', '431', '432', '433', '434', '435', '436', '437', '438', '439', '440', '441', '442', '443', '444', '445', '446', '447', '448', '449', '450', '451', '452', '453', '454', '455', '456', '457', '458', '459', '460', '461', '462', '463', '464', '465', '466', '467', '468', '469', '470', '471', '472', '473', '474', '475', '476', '477', '478', '479', '480', '481', '482', '483', '484', '485', '486', '487', '488', '489', '490', '491', '492', '493', '494', '495', '496', '497', '498', '499', '500', '501', '502', '503', '504', '505', '506', '507', '508', '509', '510', '511', '512', '513', '514', '515', '516', '517', '518', '519', '520', '521', '522', '523', '524', '525', '526', '527', '528', '529', '530', '531', '532', '533', '534', '535', '536', '537', '538', '539', '540', '541', '542', '543', '544', '545', '546', '547', '548', '549', '550', '551', '552', '553', '554', '555', '556', '557', '558', '559', '560', '561', '562', '563', '564', '565', '566', '567', '568', '569', '570', '571', '572', '573', '574', '575', '576', '577', '578', '579', '580', '581', '582', '583', '584', '585', '586', '587', '588', '589', '590', '591', '592', '593', '594', '595', '596', '597', '598', '599', '600', '601', '602', '603', '604', '605', '606', '607', '608', '609', '610', '611', '612', '613', '614', '615', '616', '617', '618', '619', '620', '621', '622', '623', '624', '625', '626', '627', '628', '629', '630', '631', '632', '633', '634', '635', '636', '637', '638', '639', '640', '641', '642', '643', '644', '645', '646', '647', '648', '649', '650', '651', '652', '653', '654', '655', '656', '657', '658', '659', '660', '661', '662', '663', '664', '665', '666', '667', '668', '669', '670', '671', '672', '673', '674', '675', '676', '677', '678', '679', '680', '681', '682', '683', '684', '685', '686', '687', '688', '689', '690', '691', '692', '693', '694', '695', '696', '697', '698', '699', '700', '701', '702', '703', '704', '705', '706', '707', '708', '709', '710', '711', '712', '713', '714', '715', '716', '717', '718', '719', '720', '721', '722', '723', '724', '725', '726', '727', '728', '729', '730', '731', '732', '733', '734', '735', '736', '737', '738', '739', '740', '741', '742', '743', '744', '745', '746', '747', '748', '749', '750', '751', '752', '753', '754', '755', '756', '757', '758', '759', '760', '761', '762', '763', '764', '765', '766', '767', '768', '769', '770', '771', '772', '773', '774', '775', '776', '777', '778', '779', '780', '781', '782', '783', '784', '785', '786', '787', '788', '789', '790', '791', '792', '793', '794', '795', '796', '797', '798', '799', '800', '801', '802', '803', '804', '805', '806', '807', '808', '809', '810', '811', '812', '813', '814', '815', '816', '817', '818', '819', '820', '821', '822', '823', '824', '825', '826', '827', '828', '829', '830', '831', '832', '833', '834', '835', '836', '837', '838', '839', '840', '841', '842', '843', '844', '845', '846', '847', '848', '849', '850', '851', '852', '853', '854', '855', '856', '857', '858', '859', '860', '861', '862', '863', '864', '865', '866', '867', '868', '869', '870', '871', '872', '873', '874', '875', '876', '877', '878', '879', '880', '881', '882', '883', '884', '885', '886', '887', '888', '889', '890', '891', '892', '893', '894', '895', '896', '897', '898', '899', '900', '901', '902', '903', '904', '905', '906', '907', '908', '909', '910', '911', '912', '913', '914', '915', '916', '917', '918', '919', '920', '921', '922', '923', '924', '925', '926', '927', '928', '929', '930', '931', '932', '933', '934', '935', '936', '937', '938', '939', '940', '941', '942', '943', '944', '945', '946', '947', '948', '949', '950', '951', '952', '953', '954', '955', '956', '957', '958', '959', '960', '961', '962', '963', '964', '965', '966', '967', '968', '969', '970', '971', '972', '973', '974', '975', '976', '977', '978', '979', '980', '981', '982', '983', '984', '985', '986', '987', '988', '989', '990', '991', '992', '993', '994', '995', '996', '997', '998', '999'])")
            print("Korrekt svar: '1', '0', '3', '2', '5', '4', '7', '6', '9', '8', '11', '10', '13', '12', '15', '14', '17', '16', '19', '18', '21', '20', '23', '22', '25', '24', '27', '26', '29', '28', '31', '30', '33', '32', '35', '34', '37', '36', '39', '38', '41', '40', '43', '42', '45', '44', '47', '46', '49', '48', '51', '50', '53', '52', '55', '54', '57', '56', '59', '58', '61', '60', '63', '62', '65', '64', '67', '66', '69', '68', '71', '70', '73', '72', '75', '74', '77', '76', '79', '78', '81', '80', '83', '82', '85', '84', '87', '86', '89', '88', '91', '90', '93', '92', '95', '94', '97', '96', '99', '98', '101', '100', '103', '102', '105', '104', '107', '106', '109', '108', '111', '110', '113', '112', '115', '114', '117', '116', '119', '118', '121', '120', '123', '122', '125', '124', '127', '126', '129', '128', '131', '130', '133', '132', '135', '134', '137', '136', '139', '138', '141', '140', '143', '142', '145', '144', '147', '146', '149', '148', '151', '150', '153', '152', '155', '154', '157', '156', '159', '158', '161', '160', '163', '162', '165', '164', '167', '166', '169', '168', '171', '170', '173', '172', '175', '174', '177', '176', '179', '178', '181', '180', '183', '182', '185', '184', '187', '186', '189', '188', '191', '190', '193', '192', '195', '194', '197', '196', '199', '198', '201', '200', '203', '202', '205', '204', '207', '206', '209', '208', '211', '210', '213', '212', '215', '214', '217', '216', '219', '218', '221', '220', '223', '222', '225', '224', '227', '226', '229', '228', '231', '230', '233', '232', '235', '234', '237', '236', '239', '238', '241', '240', '243', '242', '245', '244', '247', '246', '249', '248', '251', '250', '253', '252', '255', '254', '257', '256', '259', '258', '261', '260', '263', '262', '265', '264', '267', '266', '269', '268', '271', '270', '273', '272', '275', '274', '277', '276', '279', '278', '281', '280', '283', '282', '285', '284', '287', '286', '289', '288', '291', '290', '293', '292', '295', '294', '297', '296', '299', '298', '301', '300', '303', '302', '305', '304', '307', '306', '309', '308', '311', '310', '313', '312', '315', '314', '317', '316', '319', '318', '321', '320', '323', '322', '325', '324', '327', '326', '329', '328', '331', '330', '333', '332', '335', '334', '337', '336', '339', '338', '341', '340', '343', '342', '345', '344', '347', '346', '349', '348', '351', '350', '353', '352', '355', '354', '357', '356', '359', '358', '361', '360', '363', '362', '365', '364', '367', '366', '369', '368', '371', '370', '373', '372', '375', '374', '377', '376', '379', '378', '381', '380', '383', '382', '385', '384', '387', '386', '389', '388', '391', '390', '393', '392', '395', '394', '397', '396', '399', '398', '401', '400', '403', '402', '405', '404', '407', '406', '409', '408', '411', '410', '413', '412', '415', '414', '417', '416', '419', '418', '421', '420', '423', '422', '425', '424', '427', '426', '429', '428', '431', '430', '433', '432', '435', '434', '437', '436', '439', '438', '441', '440', '443', '442', '445', '444', '447', '446', '449', '448', '451', '450', '453', '452', '455', '454', '457', '456', '459', '458', '461', '460', '463', '462', '465', '464', '467', '466', '469', '468', '471', '470', '473', '472', '475', '474', '477', '476', '479', '478', '481', '480', '483', '482', '485', '484', '487', '486', '489', '488', '491', '490', '493', '492', '495', '494', '497', '496', '499', '498', '501', '500', '503', '502', '505', '504', '507', '506', '509', '508', '511', '510', '513', '512', '515', '514', '517', '516', '519', '518', '521', '520', '523', '522', '525', '524', '527', '526', '529', '528', '531', '530', '533', '532', '535', '534', '537', '536', '539', '538', '541', '540', '543', '542', '545', '544', '547', '546', '549', '548', '551', '550', '553', '552', '555', '554', '557', '556', '559', '558', '561', '560', '563', '562', '565', '564', '567', '566', '569', '568', '571', '570', '573', '572', '575', '574', '577', '576', '579', '578', '581', '580', '583', '582', '585', '584', '587', '586', '589', '588', '591', '590', '593', '592', '595', '594', '597', '596', '599', '598', '601', '600', '603', '602', '605', '604', '607', '606', '609', '608', '611', '610', '613', '612', '615', '614', '617', '616', '619', '618', '621', '620', '623', '622', '625', '624', '627', '626', '629', '628', '631', '630', '633', '632', '635', '634', '637', '636', '639', '638', '641', '640', '643', '642', '645', '644', '647', '646', '649', '648', '651', '650', '653', '652', '655', '654', '657', '656', '659', '658', '661', '660', '663', '662', '665', '664', '667', '666', '669', '668', '671', '670', '673', '672', '675', '674', '677', '676', '679', '678', '681', '680', '683', '682', '685', '684', '687', '686', '689', '688', '691', '690', '693', '692', '695', '694', '697', '696', '699', '698', '701', '700', '703', '702', '705', '704', '707', '706', '709', '708', '711', '710', '713', '712', '715', '714', '717', '716', '719', '718', '721', '720', '723', '722', '725', '724', '727', '726', '729', '728', '731', '730', '733', '732', '735', '734', '737', '736', '739', '738', '741', '740', '743', '742', '745', '744', '747', '746', '749', '748', '751', '750', '753', '752', '755', '754', '757', '756', '759', '758', '761', '760', '763', '762', '765', '764', '767', '766', '769', '768', '771', '770', '773', '772', '775', '774', '777', '776', '779', '778', '781', '780', '783', '782', '785', '784', '787', '786', '789', '788', '791', '790', '793', '792', '795', '794', '797', '796', '799', '798', '801', '800', '803', '802', '805', '804', '807', '806', '809', '808', '811', '810', '813', '812', '815', '814', '817', '816', '819', '818', '821', '820', '823', '822', '825', '824', '827', '826', '829', '828', '831', '830', '833', '832', '835', '834', '837', '836', '839', '838', '841', '840', '843', '842', '845', '844', '847', '846', '849', '848', '851', '850', '853', '852', '855', '854', '857', '856', '859', '858', '861', '860', '863', '862', '865', '864', '867', '866', '869', '868', '871', '870', '873', '872', '875', '874', '877', '876', '879', '878', '881', '880', '883', '882', '885', '884', '887', '886', '889', '888', '891', '890', '893', '892', '895', '894', '897', '896', '899', '898', '901', '900', '903', '902', '905', '904', '907', '906', '909', '908', '911', '910', '913', '912', '915', '914', '917', '916', '919', '918', '921', '920', '923', '922', '925', '924', '927', '926', '929', '928', '931', '930', '933', '932', '935', '934', '937', '936', '939', '938', '941', '940', '943', '942', '945', '944', '947', '946', '949', '948', '951', '950', '953', '952', '955', '954', '957', '956', '959', '958', '961', '960', '963', '962', '965', '964', '967', '966', '969', '968', '971', '970', '973', '972', '975', '974', '977', '976', '979', '978', '981', '980', '983', '982', '985', '984', '987', '986', '989', '988', '991', '990', '993', '992', '995', '994', '997', '996', '999', '998'")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/67: Exception')
        print_exception()

    try:
        res = reverse_pairs([[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []])
        exp = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        if res != exp:
            print("Fel i test 2a/68: reverse_pairs([[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []])")
            print("Korrekt svar: [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/68: Exception')
        print_exception()

    try:
        res = reverse_pairs(['', '', '', '', '', '', '', '', ''])
        exp = ['', '', '', '', '', '', '', '', '']
        if res != exp:
            print("Fel i test 2a/69: reverse_pairs(['', '', '', '', '', '', '', '', ''])")
            print("Korrekt svar: '', '', '', '', '', '', '', '', ''")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/69: Exception')
        print_exception()

    try:
        res = reverse_pairs(['', '', '', '', '', '', '', '', '', ''])
        exp = ['', '', '', '', '', '', '', '', '', '']
        if res != exp:
            print("Fel i test 2a/70: reverse_pairs(['', '', '', '', '', '', '', '', '', ''])")
            print("Korrekt svar: '', '', '', '', '', '', '', '', '', ''")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/70: Exception')
        print_exception()

    try:
        res = reverse_pairs([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
        exp = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        if res != exp:
            print("Fel i test 2a/71: reverse_pairs([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])")
            print("Korrekt svar: ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/71: Exception')
        print_exception()

    try:
        res = reverse_pairs([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
        exp = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        if res != exp:
            print("Fel i test 2a/72: reverse_pairs([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])")
            print("Korrekt svar: ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/72: Exception')
        print_exception()

    try:
        res = reverse_pairs([1, 1, 1, 1, 1, 1, 1, 1, 1])
        exp = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        if res != exp:
            print("Fel i test 2a/73: reverse_pairs([1, 1, 1, 1, 1, 1, 1, 1, 1])")
            print("Korrekt svar: 1, 1, 1, 1, 1, 1, 1, 1, 1")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/73: Exception')
        print_exception()

    try:
        res = reverse_pairs([2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
        exp = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        if res != exp:
            print("Fel i test 2a/74: reverse_pairs([2, 2, 2, 2, 2, 2, 2, 2, 2, 2])")
            print("Korrekt svar: 2, 2, 2, 2, 2, 2, 2, 2, 2, 2")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2a/74: Exception')
        print_exception()


    print('Klar med tester fÃ¶r uppgift 2a')
    print()


def test_2b():
    print('PÃ¥bÃ¶rjar tester fÃ¶r uppgift 2b')

    try:
        res = reverse_pairs_r([])
        exp = []
        if res != exp:
            print("Fel i test 2b/1: reverse_pairs_r([])")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/1: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([1, 2, 'x', 4])
        exp = [2, 1, 4, 'x']
        if res != exp:
            print("Fel i test 2b/2: reverse_pairs_r([1, 2, 'x', 4])")
            print("Korrekt svar: 2, 1, 4, 'x'")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/2: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([1, 2, 3, 4, 5])
        exp = [2, 1, 4, 3, 5]
        if res != exp:
            print("Fel i test 2b/3: reverse_pairs_r([1, 2, 3, 4, 5])")
            print("Korrekt svar: 2, 1, 4, 3, 5")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/3: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
        exp = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 13]
        if res != exp:
            print("Fel i test 2b/4: reverse_pairs_r([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])")
            print("Korrekt svar: 2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 13")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/4: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([1])
        exp = [1]
        if res != exp:
            print("Fel i test 2b/5: reverse_pairs_r([1])")
            print("Korrekt svar: 1")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/5: Exception')
        print_exception()

    try:
        res = reverse_pairs_r(['a'])
        exp = ['a']
        if res != exp:
            print("Fel i test 2b/6: reverse_pairs_r(['a'])")
            print("Korrekt svar: 'a'")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/6: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([False])
        exp = [False]
        if res != exp:
            print("Fel i test 2b/7: reverse_pairs_r([False])")
            print("Korrekt svar: False")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/7: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([0.1])
        exp = [0.1]
        if res != exp:
            print("Fel i test 2b/8: reverse_pairs_r([0.1])")
            print("Korrekt svar: 0.1")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/8: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([5, 467, 123, 4567, 879, 345, 89, 90, 78, 345])
        exp = [467, 5, 4567, 123, 345, 879, 90, 89, 345, 78]
        if res != exp:
            print("Fel i test 2b/9: reverse_pairs_r([5, 467, 123, 4567, 879, 345, 89, 90, 78, 345])")
            print("Korrekt svar: 467, 5, 4567, 123, 345, 879, 90, 89, 345, 78")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/9: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([0])
        exp = [0]
        if res != exp:
            print("Fel i test 2b/10: reverse_pairs_r([0])")
            print("Korrekt svar: 0")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/10: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        exp = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8]
        if res != exp:
            print("Fel i test 2b/11: reverse_pairs_r([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])")
            print("Korrekt svar: 1, 0, 3, 2, 5, 4, 7, 6, 9, 8")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/11: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
        exp = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26, 29, 28, 31, 30, 33, 32, 35, 34, 37, 36, 39, 38, 41, 40, 43, 42, 45, 44, 47, 46, 49, 48, 51, 50, 53, 52, 55, 54, 57, 56, 59, 58, 61, 60, 63, 62, 65, 64, 67, 66, 69, 68, 71, 70, 73, 72, 75, 74, 77, 76, 79, 78, 81, 80, 83, 82, 85, 84, 87, 86, 89, 88, 91, 90, 93, 92, 95, 94, 97, 96, 99, 98]
        if res != exp:
            print("Fel i test 2b/12: reverse_pairs_r([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])")
            print("Korrekt svar: 1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26, 29, 28, 31, 30, 33, 32, 35, 34, 37, 36, 39, 38, 41, 40, 43, 42, 45, 44, 47, 46, 49, 48, 51, 50, 53, 52, 55, 54, 57, 56, 59, 58, 61, 60, 63, 62, 65, 64, 67, 66, 69, 68, 71, 70, 73, 72, 75, 74, 77, 76, 79, 78, 81, 80, 83, 82, 85, 84, 87, 86, 89, 88, 91, 90, 93, 92, 95, 94, 97, 96, 99, 98")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/12: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9])
        exp = [9, 10, 7, 8, 5, 6, 3, 4, 1, 2, -1, 0, -3, -2, -5, -4, -7, -6, -9, -8]
        if res != exp:
            print("Fel i test 2b/13: reverse_pairs_r([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9])")
            print("Korrekt svar: 9, 10, 7, 8, 5, 6, 3, 4, 1, 2, -1, 0, -3, -2, -5, -4, -7, -6, -9, -8")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/13: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
        exp = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        if res != exp:
            print("Fel i test 2b/14: reverse_pairs_r([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])")
            print("Korrekt svar: 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/14: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
        exp = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        if res != exp:
            print("Fel i test 2b/15: reverse_pairs_r([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])")
            print("Korrekt svar: 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/15: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([0, 11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220, 231, 242, 253, 264, 275, 286, 297, 308, 319, 330, 341, 352, 363, 374, 385, 396, 407, 418, 429, 440, 451, 462, 473, 484, 495, 506, 517, 528, 539, 550, 561, 572, 583, 594, 605, 616, 627, 638, 649, 660, 671, 682, 693, 704, 715, 726, 737, 748, 759, 770, 781, 792, 803, 814, 825, 836, 847, 858, 869, 880, 891, 902, 913, 924, 935, 946, 957, 968, 979, 990])
        exp = [11, 0, 33, 22, 55, 44, 77, 66, 99, 88, 121, 110, 143, 132, 165, 154, 187, 176, 209, 198, 231, 220, 253, 242, 275, 264, 297, 286, 319, 308, 341, 330, 363, 352, 385, 374, 407, 396, 429, 418, 451, 440, 473, 462, 495, 484, 517, 506, 539, 528, 561, 550, 583, 572, 605, 594, 627, 616, 649, 638, 671, 660, 693, 682, 715, 704, 737, 726, 759, 748, 781, 770, 803, 792, 825, 814, 847, 836, 869, 858, 891, 880, 913, 902, 935, 924, 957, 946, 979, 968, 990]
        if res != exp:
            print("Fel i test 2b/16: reverse_pairs_r([0, 11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220, 231, 242, 253, 264, 275, 286, 297, 308, 319, 330, 341, 352, 363, 374, 385, 396, 407, 418, 429, 440, 451, 462, 473, 484, 495, 506, 517, 528, 539, 550, 561, 572, 583, 594, 605, 616, 627, 638, 649, 660, 671, 682, 693, 704, 715, 726, 737, 748, 759, 770, 781, 792, 803, 814, 825, 836, 847, 858, 869, 880, 891, 902, 913, 924, 935, 946, 957, 968, 979, 990])")
            print("Korrekt svar: 11, 0, 33, 22, 55, 44, 77, 66, 99, 88, 121, 110, 143, 132, 165, 154, 187, 176, 209, 198, 231, 220, 253, 242, 275, 264, 297, 286, 319, 308, 341, 330, 363, 352, 385, 374, 407, 396, 429, 418, 451, 440, 473, 462, 495, 484, 517, 506, 539, 528, 561, 550, 583, 572, 605, 594, 627, 616, 649, 638, 671, 660, 693, 682, 715, 704, 737, 726, 759, 748, 781, 770, 803, 792, 825, 814, 847, 836, 869, 858, 891, 880, 913, 902, 935, 924, 957, 946, 979, 968, 990")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/16: Exception')
        print_exception()

    try:
        res = reverse_pairs_r(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
        exp = ['b', 'a', 'd', 'c', 'f', 'e', 'g']
        if res != exp:
            print("Fel i test 2b/17: reverse_pairs_r(['a', 'b', 'c', 'd', 'e', 'f', 'g'])")
            print("Korrekt svar: 'b', 'a', 'd', 'c', 'f', 'e', 'g'")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/17: Exception')
        print_exception()

    try:
        res = reverse_pairs_r(['Ã¥', 'Ã¤', 'Ã¶', 'Ã¢', 'Ã´', 'Ãª', 'Ã¡', 'Ã³', 'Ã©'])
        exp = ['Ã¤', 'Ã¥', 'Ã¢', 'Ã¶', 'Ãª', 'Ã´', 'Ã³', 'Ã¡', 'Ã©']
        if res != exp:
            print("Fel i test 2b/18: reverse_pairs_r(['Ã¥', 'Ã¤', 'Ã¶', 'Ã¢', 'Ã´', 'Ãª', 'Ã¡', 'Ã³', 'Ã©'])")
            print("Korrekt svar: 'Ã¤', 'Ã¥', 'Ã¢', 'Ã¶', 'Ãª', 'Ã´', 'Ã³', 'Ã¡', 'Ã©'")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/18: Exception')
        print_exception()

    try:
        res = reverse_pairs_r(['', '', '', ''])
        exp = ['', '', '', '']
        if res != exp:
            print("Fel i test 2b/19: reverse_pairs_r(['', '', '', ''])")
            print("Korrekt svar: '', '', '', ''")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/19: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([' ', '', ' ', ''])
        exp = ['', ' ', '', ' ']
        if res != exp:
            print("Fel i test 2b/20: reverse_pairs_r([' ', '', ' ', ''])")
            print("Korrekt svar: '', ' ', '', ' '")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/20: Exception')
        print_exception()

    try:
        res = reverse_pairs_r(['nÃ¥gra', 'strÃ¤ngar', 'av', 'olika', 'lÃ¤ngd', 'i', 'hav', 'totalfÃ¶rstÃ¶rt', 'frÃ¥n', 'laxmassor'])
        exp = ['strÃ¤ngar', 'nÃ¥gra', 'olika', 'av', 'i', 'lÃ¤ngd', 'totalfÃ¶rstÃ¶rt', 'hav', 'laxmassor', 'frÃ¥n']
        if res != exp:
            print("Fel i test 2b/21: reverse_pairs_r(['nÃ¥gra', 'strÃ¤ngar', 'av', 'olika', 'lÃ¤ngd', 'i', 'hav', 'totalfÃ¶rstÃ¶rt', 'frÃ¥n', 'laxmassor'])")
            print("Korrekt svar: 'strÃ¤ngar', 'nÃ¥gra', 'olika', 'av', 'i', 'lÃ¤ngd', 'totalfÃ¶rstÃ¶rt', 'hav', 'laxmassor', 'frÃ¥n'")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/21: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', ''])
        exp = ['', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', '']
        if res != exp:
            print("Fel i test 2b/22: reverse_pairs_r([' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', ''])")
            print("Korrekt svar: '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ' ', '', '', '', '', ' ', ''")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/22: Exception')
        print_exception()

    try:
        res = reverse_pairs_r(['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '\x7f', '\x80', '\x81', '\x82', '\x83', '\x84', '\x85', '\x86', '\x87', '\x88', '\x89', '\x8a', '\x8b', '\x8c', '\x8d', '\x8e', '\x8f', '\x90', '\x91', '\x92', '\x93', '\x94', '\x95'])
        exp = ['\x01', '\x00', '\x03', '\x02', '\x05', '\x04', '\x07', '\x06', '\t', '\x08', '\x0b', '\n', '\r', '\x0c', '\x0f', '\x0e', '\x11', '\x10', '\x13', '\x12', '\x15', '\x14', '\x17', '\x16', '\x19', '\x18', '\x1b', '\x1a', '\x1d', '\x1c', '\x1f', '\x1e', '!', ' ', '#', '"', '%', '$', "'", '&', ')', '(', '+', '*', '-', ',', '/', '.', '1', '0', '3', '2', '5', '4', '7', '6', '9', '8', ';', ':', '=', '<', '?', '>', 'A', '@', 'C', 'B', 'E', 'D', 'G', 'F', 'I', 'H', 'K', 'J', 'M', 'L', 'O', 'N', 'Q', 'P', 'S', 'R', 'U', 'T', 'W', 'V', 'Y', 'X', '[', 'Z', ']', '\\', '_', '^', 'a', '`', 'c', 'b', 'e', 'd', 'g', 'f', 'i', 'h', 'k', 'j', 'm', 'l', 'o', 'n', 'q', 'p', 's', 'r', 'u', 't', 'w', 'v', 'y', 'x', '{', 'z', '}', '|', '\x7f', '~', '\x81', '\x80', '\x83', '\x82', '\x85', '\x84', '\x87', '\x86', '\x89', '\x88', '\x8b', '\x8a', '\x8d', '\x8c', '\x8f', '\x8e', '\x91', '\x90', '\x93', '\x92', '\x95', '\x94']
        if res != exp:
            print("Fel i test 2b/23: reverse_pairs_r([\'\\x00\', \'\\x01\', \'\\x02\', \'\\x03\', \'\\x04\', \'\\x05\', \'\\x06\', \'\\x07\', \'\\x08\', \'\\t\', \'\\n\', \'\\x0b\', \'\\x0c\', \'\\r\', \'\\x0e\', \'\\x0f\', \'\\x10\', \'\\x11\', \'\\x12\', \'\\x13\', \'\\x14\', \'\\x15\', \'\\x16\', \'\\x17\', \'\\x18\', \'\\x19\', \'\\x1a\', \'\\x1b\', \'\\x1c\', \'\\x1d\', \'\\x1e\', \'\\x1f\', \' \', \'!\', \'\"\', \'#\', \'$\', \'%\', \'&\', \"\'\", \'(\', \')\', \'*\', \'+\', \',\', \'-\', \'.\', \'/\', \'0\', \'1\', \'2\', \'3\', \'4\', \'5\', \'6\', \'7\', \'8\', \'9\', \':\', \';\', \'<\', \'=\', \'>\', \'?\', \'@\', \'A\', \'B\', \'C\', \'D\', \'E\', \'F\', \'G\', \'H\', \'I\', \'J\', \'K\', \'L\', \'M\', \'N\', \'O\', \'P\', \'Q\', \'R\', \'S\', \'T\', \'U\', \'V\', \'W\', \'X\', \'Y\', \'Z\', \'[\', \'\\\\\', \']\', \'^\', \'_\', \'`\', \'a\', \'b\', \'c\', \'d\', \'e\', \'f\', \'g\', \'h\', \'i\', \'j\', \'k\', \'l\', \'m\', \'n\', \'o\', \'p\', \'q\', \'r\', \'s\', \'t\', \'u\', \'v\', \'w\', \'x\', \'y\', \'z\', \'{\', \'|\', \'}\', \'~\', \'\\x7f\', \'\\x80\', \'\\x81\', \'\\x82\', \'\\x83\', \'\\x84\', \'\\x85\', \'\\x86\', \'\\x87\', \'\\x88\', \'\\x89\', \'\\x8a\', \'\\x8b\', \'\\x8c\', \'\\x8d\', \'\\x8e\', \'\\x8f\', \'\\x90\', \'\\x91\', \'\\x92\', \'\\x93\', \'\\x94\', \'\\x95\'])")
            print("Korrekt svar: '\x01', '\x00', '\x03', '\x02', '\x05', '\x04', '\x07', '\x06', '\t', '\x08', '\x0b', '\n', '\r', '\x0c', '\x0f', '\x0e', '\x11', '\x10', '\x13', '\x12', '\x15', '\x14', '\x17', '\x16', '\x19', '\x18', '\x1b', '\x1a', '\x1d', '\x1c', '\x1f', '\x1e', '!', ' ', '#', '\"', '%', '$', \"'\", '&', ')', '(', '+', '*', '-', ',', '/', '.', '1', '0', '3', '2', '5', '4', '7', '6', '9', '8', ';', ':', '=', '<', '?', '>', 'A', '@', 'C', 'B', 'E', 'D', 'G', 'F', 'I', 'H', 'K', 'J', 'M', 'L', 'O', 'N', 'Q', 'P', 'S', 'R', 'U', 'T', 'W', 'V', 'Y', 'X', '[', 'Z', ']', '\\', '_', '^', 'a', '`', 'c', 'b', 'e', 'd', 'g', 'f', 'i', 'h', 'k', 'j', 'm', 'l', 'o', 'n', 'q', 'p', 's', 'r', 'u', 't', 'w', 'v', 'y', 'x', '{', 'z', '}', '|', '\x7f', '~', '\x81', '\x80', '\x83', '\x82', '\x85', '\x84', '\x87', '\x86', '\x89', '\x88', '\x8b', '\x8a', '\x8d', '\x8c', '\x8f', '\x8e', '\x91', '\x90', '\x93', '\x92', '\x95', '\x94'")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/23: Exception')
        print_exception()

    try:
        res = reverse_pairs_r(['', '\x01', '\x02\x02', '\x03\x03\x03', '\x04\x04\x04\x04', '\x05\x05\x05\x05\x05', '\x06\x06\x06\x06\x06\x06', '\x07\x07\x07\x07\x07\x07\x07', '\x08\x08\x08\x08\x08\x08\x08\x08', '\t\t\t\t\t\t\t\t\t', '\n\n\n\n\n\n\n\n\n\n', '\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b', '\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c', '\r\r\r\r\r\r\r\r\r\r\r\r\r', '\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e', '\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f', '\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10', '\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11', '\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12', '\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13', '\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14', '\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15', '\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16', '\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17', '\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18', '\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19', '\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a', '\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b', '\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c', '\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d', '\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e', '\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f', '                                ', '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', '""""""""""""""""""""""""""""""""""', '###################################', '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$', '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%', '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&', "'''''''''''''''''''''''''''''''''''''''", '((((((((((((((((((((((((((((((((((((((((', ')))))))))))))))))))))))))))))))))))))))))', '******************************************', '+++++++++++++++++++++++++++++++++++++++++++', ',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,', '---------------------------------------------', '..............................................', '///////////////////////////////////////////////', '000000000000000000000000000000000000000000000000', '1111111111111111111111111111111111111111111111111', '22222222222222222222222222222222222222222222222222', '333333333333333333333333333333333333333333333333333', '4444444444444444444444444444444444444444444444444444', '55555555555555555555555555555555555555555555555555555', '666666666666666666666666666666666666666666666666666666', '7777777777777777777777777777777777777777777777777777777', '88888888888888888888888888888888888888888888888888888888', '999999999999999999999999999999999999999999999999999999999', '::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', ';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;', '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<', '=============================================================', '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', '???????????????????????????????????????????????????????????????', '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB', 'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC', 'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD', 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE', 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF', 'GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG', 'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH', 'IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII', 'JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ', 'KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK', 'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL', 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM', 'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN', 'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO', 'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP', 'QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ', 'RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR', 'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS', 'TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT', 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU', 'VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV', 'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY', 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ', '[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[', '\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\', ']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]', '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^', '_______________________________________________________________________________________________', '````````````````````````````````````````````````````````````````````````````````````````````````', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb', 'ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'])
        exp = ['\x01', '', '\x03\x03\x03', '\x02\x02', '\x05\x05\x05\x05\x05', '\x04\x04\x04\x04', '\x07\x07\x07\x07\x07\x07\x07', '\x06\x06\x06\x06\x06\x06', '\t\t\t\t\t\t\t\t\t', '\x08\x08\x08\x08\x08\x08\x08\x08', '\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b', '\n\n\n\n\n\n\n\n\n\n', '\r\r\r\r\r\r\r\r\r\r\r\r\r', '\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c', '\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f', '\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e', '\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11', '\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10', '\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13', '\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12', '\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15', '\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14', '\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17', '\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16', '\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19', '\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18', '\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b', '\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a', '\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d', '\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c', '\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f', '\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e', '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', '                                ', '###################################', '""""""""""""""""""""""""""""""""""', '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%', '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$', "'''''''''''''''''''''''''''''''''''''''", '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&', ')))))))))))))))))))))))))))))))))))))))))', '((((((((((((((((((((((((((((((((((((((((', '+++++++++++++++++++++++++++++++++++++++++++', '******************************************', '---------------------------------------------', ',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,', '///////////////////////////////////////////////', '..............................................', '1111111111111111111111111111111111111111111111111', '000000000000000000000000000000000000000000000000', '333333333333333333333333333333333333333333333333333', '22222222222222222222222222222222222222222222222222', '55555555555555555555555555555555555555555555555555555', '4444444444444444444444444444444444444444444444444444', '7777777777777777777777777777777777777777777777777777777', '666666666666666666666666666666666666666666666666666666', '999999999999999999999999999999999999999999999999999999999', '88888888888888888888888888888888888888888888888888888888', ';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;', '::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', '=============================================================', '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<', '???????????????????????????????????????????????????????????????', '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@', 'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC', 'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB', 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE', 'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD', 'GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG', 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF', 'IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII', 'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH', 'KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK', 'JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ', 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM', 'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL', 'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO', 'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN', 'QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ', 'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP', 'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS', 'RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR', 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU', 'TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT', 'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW', 'VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV', 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[', 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ', ']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]', '\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\', '_______________________________________________________________________________________________', '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', '````````````````````````````````````````````````````````````````````````````````````````````````', 'ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc', 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb']
        if res != exp:
            print("Fel i test 2b/24: reverse_pairs_r([\'\', \'\\x01\', \'\\x02\\x02\', \'\\x03\\x03\\x03\', \'\\x04\\x04\\x04\\x04\', \'\\x05\\x05\\x05\\x05\\x05\', \'\\x06\\x06\\x06\\x06\\x06\\x06\', \'\\x07\\x07\\x07\\x07\\x07\\x07\\x07\', \'\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\', \'\\t\\t\\t\\t\\t\\t\\t\\t\\t\', \'\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\', \'\\x0b\\x0b\\x0b\\x0b\\x0b\\x0b\\x0b\\x0b\\x0b\\x0b\\x0b\', \'\\x0c\\x0c\\x0c\\x0c\\x0c\\x0c\\x0c\\x0c\\x0c\\x0c\\x0c\\x0c\', \'\\r\\r\\r\\r\\r\\r\\r\\r\\r\\r\\r\\r\\r\', \'\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\', \'\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\', \'\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\', \'\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\', \'\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\', \'\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\', \'\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\', \'\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\', \'\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\', \'\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\', \'\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\', \'\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\', \'\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\', \'\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\', \'\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\', \'\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\', \'\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\', \'\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\', \'                                \', \'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\', \'\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\', \'###################################\', \'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\', \'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\', \'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\', \"\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\", \'((((((((((((((((((((((((((((((((((((((((\', \')))))))))))))))))))))))))))))))))))))))))\', \'******************************************\', \'+++++++++++++++++++++++++++++++++++++++++++\', \',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\', \'---------------------------------------------\', \'..............................................\', \'///////////////////////////////////////////////\', \'000000000000000000000000000000000000000000000000\', \'1111111111111111111111111111111111111111111111111\', \'22222222222222222222222222222222222222222222222222\', \'333333333333333333333333333333333333333333333333333\', \'4444444444444444444444444444444444444444444444444444\', \'55555555555555555555555555555555555555555555555555555\', \'666666666666666666666666666666666666666666666666666666\', \'7777777777777777777777777777777777777777777777777777777\', \'88888888888888888888888888888888888888888888888888888888\', \'999999999999999999999999999999999999999999999999999999999\', \'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\', \';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\', \'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\', \'=============================================================\', \'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\', \'???????????????????????????????????????????????????????????????\', \'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\', \'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\', \'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB\', \'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC\', \'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD\', \'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE\', \'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF\', \'GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG\', \'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\', \'IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII\', \'JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ\', \'KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK\', \'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL\', \'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\', \'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\', \'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\', \'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP\', \'QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ\', \'RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR\', \'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS\', \'TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT\', \'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU\', \'VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV\', \'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\', \'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\', \'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY\', \'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ\', \'[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[\', \'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\', \']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]\', \'^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\', \'_______________________________________________________________________________________________\', \'````````````````````````````````````````````````````````````````````````````````````````````````\', \'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\', \'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\', \'ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc\'])")
            print("Korrekt svar: '\x01', '', '\x03\x03\x03', '\x02\x02', '\x05\x05\x05\x05\x05', '\x04\x04\x04\x04', '\x07\x07\x07\x07\x07\x07\x07', '\x06\x06\x06\x06\x06\x06', '\t\t\t\t\t\t\t\t\t', '\x08\x08\x08\x08\x08\x08\x08\x08', '\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b', '\n\n\n\n\n\n\n\n\n\n', '\r\r\r\r\r\r\r\r\r\r\r\r\r', '\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c', '\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f', '\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e', '\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11', '\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10', '\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13', '\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12', '\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15', '\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14', '\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17', '\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16', '\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19', '\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18', '\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b', '\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a', '\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d', '\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c', '\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f', '\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e', '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', '                                ', '###################################', '\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"', '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%', '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$', \"'''''''''''''''''''''''''''''''''''''''\", '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&', ')))))))))))))))))))))))))))))))))))))))))', '((((((((((((((((((((((((((((((((((((((((', '+++++++++++++++++++++++++++++++++++++++++++', '******************************************', '---------------------------------------------', ',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,', '///////////////////////////////////////////////', '..............................................', '1111111111111111111111111111111111111111111111111', '000000000000000000000000000000000000000000000000', '333333333333333333333333333333333333333333333333333', '22222222222222222222222222222222222222222222222222', '55555555555555555555555555555555555555555555555555555', '4444444444444444444444444444444444444444444444444444', '7777777777777777777777777777777777777777777777777777777', '666666666666666666666666666666666666666666666666666666', '999999999999999999999999999999999999999999999999999999999', '88888888888888888888888888888888888888888888888888888888', ';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;', '::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', '=============================================================', '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<', '???????????????????????????????????????????????????????????????', '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@', 'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC', 'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB', 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE', 'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD', 'GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG', 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF', 'IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII', 'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH', 'KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK', 'JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ', 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM', 'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL', 'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO', 'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN', 'QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ', 'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP', 'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS', 'RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR', 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU', 'TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT', 'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW', 'VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV', 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', '[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[', 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ', ']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]', '\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\', '_______________________________________________________________________________________________', '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', '````````````````````````````````````````````````````````````````````````````````````````````````', 'ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc', 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/24: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([True, False])
        exp = [False, True]
        if res != exp:
            print("Fel i test 2b/25: reverse_pairs_r([True, False])")
            print("Korrekt svar: False, True")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/25: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([True, True, True, False, True])
        exp = [True, True, False, True, True]
        if res != exp:
            print("Fel i test 2b/26: reverse_pairs_r([True, True, True, False, True])")
            print("Korrekt svar: True, True, False, True, True")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/26: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True])
        exp = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
        if res != exp:
            print("Fel i test 2b/27: reverse_pairs_r([True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True])")
            print("Korrekt svar: True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/27: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False])
        exp = [False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True]
        if res != exp:
            print("Fel i test 2b/28: reverse_pairs_r([True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False])")
            print("Korrekt svar: False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/28: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False])
        exp = [True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, False]
        if res != exp:
            print("Fel i test 2b/29: reverse_pairs_r([False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False])")
            print("Korrekt svar: True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, False")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/29: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([0.0, 1.0, 2.0])
        exp = [1.0, 0.0, 2.0]
        if res != exp:
            print("Fel i test 2b/30: reverse_pairs_r([0.0, 1.0, 2.0])")
            print("Korrekt svar: 1.0, 0.0, 2.0")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/30: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([1e-06, 0.123456789, 0.111111111, 123.3])
        exp = [0.123456789, 1e-06, 123.3, 0.111111111]
        if res != exp:
            print("Fel i test 2b/31: reverse_pairs_r([1e-06, 0.123456789, 0.111111111, 123.3])")
            print("Korrekt svar: 0.123456789, 1e-06, 123.3, 0.111111111")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/31: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([-25.0, -24.0, -23.0, -22.0, -21.0, -20.0, -19.0, -18.0, -17.0, -16.0, -15.0, -14.0, -13.0, -12.0, -11.0, -10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0])
        exp = [-24.0, -25.0, -22.0, -23.0, -20.0, -21.0, -18.0, -19.0, -16.0, -17.0, -14.0, -15.0, -12.0, -13.0, -10.0, -11.0, -8.0, -9.0, -6.0, -7.0, -4.0, -5.0, -2.0, -3.0, 0.0, -1.0, 2.0, 1.0, 4.0, 3.0, 6.0, 5.0, 8.0, 7.0, 10.0, 9.0, 12.0, 11.0, 14.0, 13.0, 16.0, 15.0, 18.0, 17.0, 20.0, 19.0, 22.0, 21.0, 24.0, 23.0]
        if res != exp:
            print("Fel i test 2b/32: reverse_pairs_r([-25.0, -24.0, -23.0, -22.0, -21.0, -20.0, -19.0, -18.0, -17.0, -16.0, -15.0, -14.0, -13.0, -12.0, -11.0, -10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0])")
            print("Korrekt svar: -24.0, -25.0, -22.0, -23.0, -20.0, -21.0, -18.0, -19.0, -16.0, -17.0, -14.0, -15.0, -12.0, -13.0, -10.0, -11.0, -8.0, -9.0, -6.0, -7.0, -4.0, -5.0, -2.0, -3.0, 0.0, -1.0, 2.0, 1.0, 4.0, 3.0, 6.0, 5.0, 8.0, 7.0, 10.0, 9.0, 12.0, 11.0, 14.0, 13.0, 16.0, 15.0, 18.0, 17.0, 20.0, 19.0, 22.0, 21.0, 24.0, 23.0")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/32: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([-1.5e-06, -1.49e-06, -1.48e-06, -1.47e-06, -1.46e-06, -1.45e-06, -1.44e-06, -1.43e-06, -1.42e-06, -1.41e-06, -1.4e-06, -1.39e-06, -1.38e-06, -1.37e-06, -1.36e-06, -1.35e-06, -1.34e-06, -1.33e-06, -1.32e-06, -1.31e-06, -1.3e-06, -1.29e-06, -1.28e-06, -1.27e-06, -1.26e-06, -1.25e-06, -1.24e-06, -1.23e-06, -1.22e-06, -1.21e-06, -1.2e-06, -1.19e-06, -1.18e-06, -1.17e-06, -1.16e-06, -1.15e-06, -1.14e-06, -1.13e-06, -1.12e-06, -1.11e-06, -1.1e-06, -1.09e-06, -1.08e-06, -1.07e-06, -1.06e-06, -1.05e-06, -1.04e-06, -1.03e-06, -1.02e-06, -1.01e-06, -1e-06, -9.9e-07, -9.8e-07, -9.7e-07, -9.6e-07, -9.5e-07, -9.4e-07, -9.3e-07, -9.2e-07, -9.1e-07, -9e-07, -8.9e-07, -8.8e-07, -8.7e-07, -8.6e-07, -8.5e-07, -8.4e-07, -8.3e-07, -8.2e-07, -8.1e-07, -8e-07, -7.9e-07, -7.8e-07, -7.7e-07, -7.6e-07, -7.5e-07, -7.4e-07, -7.3e-07, -7.2e-07, -7.1e-07, -7e-07, -6.9e-07, -6.8e-07, -6.7e-07, -6.6e-07, -6.5e-07, -6.4e-07, -6.3e-07, -6.2e-07, -6.1e-07, -6e-07, -5.9e-07, -5.8e-07, -5.7e-07, -5.6e-07, -5.5e-07, -5.4e-07, -5.3e-07, -5.2e-07, -5.1e-07, -5e-07, -4.9e-07, -4.8e-07, -4.7e-07, -4.6e-07, -4.5e-07, -4.4e-07, -4.3e-07, -4.2e-07, -4.1e-07, -4e-07, -3.9e-07, -3.8e-07, -3.7e-07, -3.6e-07, -3.5e-07, -3.4e-07, -3.3e-07, -3.2e-07, -3.1e-07, -3e-07, -2.9e-07, -2.8e-07, -2.7e-07, -2.6e-07, -2.5e-07, -2.4e-07, -2.3e-07, -2.2e-07, -2.1e-07, -2e-07, -1.9e-07, -1.8e-07, -1.7e-07, -1.6e-07, -1.5e-07, -1.4e-07, -1.3e-07, -1.2e-07, -1.1e-07, -1e-07, -9e-08, -8e-08, -7e-08, -6e-08, -5e-08, -4e-08, -3e-08, -2e-08, -1e-08, 0.0, 1e-08, 2e-08, 3e-08, 4e-08, 5e-08, 6e-08, 7e-08, 8e-08, 9e-08, 1e-07, 1.1e-07, 1.2e-07, 1.3e-07, 1.4e-07, 1.5e-07, 1.6e-07, 1.7e-07, 1.8e-07, 1.9e-07, 2e-07, 2.1e-07, 2.2e-07, 2.3e-07, 2.4e-07, 2.5e-07, 2.6e-07, 2.7e-07, 2.8e-07, 2.9e-07, 3e-07, 3.1e-07, 3.2e-07, 3.3e-07, 3.4e-07, 3.5e-07, 3.6e-07, 3.7e-07, 3.8e-07, 3.9e-07, 4e-07, 4.1e-07, 4.2e-07, 4.3e-07, 4.4e-07, 4.5e-07, 4.6e-07, 4.7e-07, 4.8e-07, 4.9e-07, 5e-07, 5.1e-07, 5.2e-07, 5.3e-07, 5.4e-07, 5.5e-07, 5.6e-07, 5.7e-07, 5.8e-07, 5.9e-07, 6e-07, 6.1e-07, 6.2e-07, 6.3e-07, 6.4e-07, 6.5e-07, 6.6e-07, 6.7e-07, 6.8e-07, 6.9e-07, 7e-07, 7.1e-07, 7.2e-07, 7.3e-07, 7.4e-07, 7.5e-07, 7.6e-07, 7.7e-07, 7.8e-07, 7.9e-07, 8e-07, 8.1e-07, 8.2e-07, 8.3e-07, 8.4e-07, 8.5e-07, 8.6e-07, 8.7e-07, 8.8e-07, 8.9e-07, 9e-07, 9.1e-07, 9.2e-07, 9.3e-07, 9.4e-07, 9.5e-07, 9.6e-07, 9.7e-07, 9.8e-07, 9.9e-07, 1e-06, 1.01e-06, 1.02e-06, 1.03e-06, 1.04e-06, 1.05e-06, 1.06e-06, 1.07e-06, 1.08e-06, 1.09e-06, 1.1e-06, 1.11e-06, 1.12e-06, 1.13e-06, 1.14e-06, 1.15e-06, 1.16e-06, 1.17e-06, 1.18e-06, 1.19e-06, 1.2e-06, 1.21e-06, 1.22e-06, 1.23e-06, 1.24e-06, 1.25e-06, 1.26e-06, 1.27e-06, 1.28e-06, 1.29e-06, 1.3e-06, 1.31e-06, 1.32e-06, 1.33e-06, 1.34e-06, 1.35e-06, 1.36e-06, 1.37e-06, 1.38e-06, 1.39e-06, 1.4e-06, 1.41e-06, 1.42e-06, 1.43e-06, 1.44e-06, 1.45e-06, 1.46e-06, 1.47e-06, 1.48e-06, 1.49e-06])
        exp = [-1.49e-06, -1.5e-06, -1.47e-06, -1.48e-06, -1.45e-06, -1.46e-06, -1.43e-06, -1.44e-06, -1.41e-06, -1.42e-06, -1.39e-06, -1.4e-06, -1.37e-06, -1.38e-06, -1.35e-06, -1.36e-06, -1.33e-06, -1.34e-06, -1.31e-06, -1.32e-06, -1.29e-06, -1.3e-06, -1.27e-06, -1.28e-06, -1.25e-06, -1.26e-06, -1.23e-06, -1.24e-06, -1.21e-06, -1.22e-06, -1.19e-06, -1.2e-06, -1.17e-06, -1.18e-06, -1.15e-06, -1.16e-06, -1.13e-06, -1.14e-06, -1.11e-06, -1.12e-06, -1.09e-06, -1.1e-06, -1.07e-06, -1.08e-06, -1.05e-06, -1.06e-06, -1.03e-06, -1.04e-06, -1.01e-06, -1.02e-06, -9.9e-07, -1e-06, -9.7e-07, -9.8e-07, -9.5e-07, -9.6e-07, -9.3e-07, -9.4e-07, -9.1e-07, -9.2e-07, -8.9e-07, -9e-07, -8.7e-07, -8.8e-07, -8.5e-07, -8.6e-07, -8.3e-07, -8.4e-07, -8.1e-07, -8.2e-07, -7.9e-07, -8e-07, -7.7e-07, -7.8e-07, -7.5e-07, -7.6e-07, -7.3e-07, -7.4e-07, -7.1e-07, -7.2e-07, -6.9e-07, -7e-07, -6.7e-07, -6.8e-07, -6.5e-07, -6.6e-07, -6.3e-07, -6.4e-07, -6.1e-07, -6.2e-07, -5.9e-07, -6e-07, -5.7e-07, -5.8e-07, -5.5e-07, -5.6e-07, -5.3e-07, -5.4e-07, -5.1e-07, -5.2e-07, -4.9e-07, -5e-07, -4.7e-07, -4.8e-07, -4.5e-07, -4.6e-07, -4.3e-07, -4.4e-07, -4.1e-07, -4.2e-07, -3.9e-07, -4e-07, -3.7e-07, -3.8e-07, -3.5e-07, -3.6e-07, -3.3e-07, -3.4e-07, -3.1e-07, -3.2e-07, -2.9e-07, -3e-07, -2.7e-07, -2.8e-07, -2.5e-07, -2.6e-07, -2.3e-07, -2.4e-07, -2.1e-07, -2.2e-07, -1.9e-07, -2e-07, -1.7e-07, -1.8e-07, -1.5e-07, -1.6e-07, -1.3e-07, -1.4e-07, -1.1e-07, -1.2e-07, -9e-08, -1e-07, -7e-08, -8e-08, -5e-08, -6e-08, -3e-08, -4e-08, -1e-08, -2e-08, 1e-08, 0.0, 3e-08, 2e-08, 5e-08, 4e-08, 7e-08, 6e-08, 9e-08, 8e-08, 1.1e-07, 1e-07, 1.3e-07, 1.2e-07, 1.5e-07, 1.4e-07, 1.7e-07, 1.6e-07, 1.9e-07, 1.8e-07, 2.1e-07, 2e-07, 2.3e-07, 2.2e-07, 2.5e-07, 2.4e-07, 2.7e-07, 2.6e-07, 2.9e-07, 2.8e-07, 3.1e-07, 3e-07, 3.3e-07, 3.2e-07, 3.5e-07, 3.4e-07, 3.7e-07, 3.6e-07, 3.9e-07, 3.8e-07, 4.1e-07, 4e-07, 4.3e-07, 4.2e-07, 4.5e-07, 4.4e-07, 4.7e-07, 4.6e-07, 4.9e-07, 4.8e-07, 5.1e-07, 5e-07, 5.3e-07, 5.2e-07, 5.5e-07, 5.4e-07, 5.7e-07, 5.6e-07, 5.9e-07, 5.8e-07, 6.1e-07, 6e-07, 6.3e-07, 6.2e-07, 6.5e-07, 6.4e-07, 6.7e-07, 6.6e-07, 6.9e-07, 6.8e-07, 7.1e-07, 7e-07, 7.3e-07, 7.2e-07, 7.5e-07, 7.4e-07, 7.7e-07, 7.6e-07, 7.9e-07, 7.8e-07, 8.1e-07, 8e-07, 8.3e-07, 8.2e-07, 8.5e-07, 8.4e-07, 8.7e-07, 8.6e-07, 8.9e-07, 8.8e-07, 9.1e-07, 9e-07, 9.3e-07, 9.2e-07, 9.5e-07, 9.4e-07, 9.7e-07, 9.6e-07, 9.9e-07, 9.8e-07, 1.01e-06, 1e-06, 1.03e-06, 1.02e-06, 1.05e-06, 1.04e-06, 1.07e-06, 1.06e-06, 1.09e-06, 1.08e-06, 1.11e-06, 1.1e-06, 1.13e-06, 1.12e-06, 1.15e-06, 1.14e-06, 1.17e-06, 1.16e-06, 1.19e-06, 1.18e-06, 1.21e-06, 1.2e-06, 1.23e-06, 1.22e-06, 1.25e-06, 1.24e-06, 1.27e-06, 1.26e-06, 1.29e-06, 1.28e-06, 1.31e-06, 1.3e-06, 1.33e-06, 1.32e-06, 1.35e-06, 1.34e-06, 1.37e-06, 1.36e-06, 1.39e-06, 1.38e-06, 1.41e-06, 1.4e-06, 1.43e-06, 1.42e-06, 1.45e-06, 1.44e-06, 1.47e-06, 1.46e-06, 1.49e-06, 1.48e-06]
        if res != exp:
            print("Fel i test 2b/33: reverse_pairs_r([-1.5e-06, -1.49e-06, -1.48e-06, -1.47e-06, -1.46e-06, -1.45e-06, -1.44e-06, -1.43e-06, -1.42e-06, -1.41e-06, -1.4e-06, -1.39e-06, -1.38e-06, -1.37e-06, -1.36e-06, -1.35e-06, -1.34e-06, -1.33e-06, -1.32e-06, -1.31e-06, -1.3e-06, -1.29e-06, -1.28e-06, -1.27e-06, -1.26e-06, -1.25e-06, -1.24e-06, -1.23e-06, -1.22e-06, -1.21e-06, -1.2e-06, -1.19e-06, -1.18e-06, -1.17e-06, -1.16e-06, -1.15e-06, -1.14e-06, -1.13e-06, -1.12e-06, -1.11e-06, -1.1e-06, -1.09e-06, -1.08e-06, -1.07e-06, -1.06e-06, -1.05e-06, -1.04e-06, -1.03e-06, -1.02e-06, -1.01e-06, -1e-06, -9.9e-07, -9.8e-07, -9.7e-07, -9.6e-07, -9.5e-07, -9.4e-07, -9.3e-07, -9.2e-07, -9.1e-07, -9e-07, -8.9e-07, -8.8e-07, -8.7e-07, -8.6e-07, -8.5e-07, -8.4e-07, -8.3e-07, -8.2e-07, -8.1e-07, -8e-07, -7.9e-07, -7.8e-07, -7.7e-07, -7.6e-07, -7.5e-07, -7.4e-07, -7.3e-07, -7.2e-07, -7.1e-07, -7e-07, -6.9e-07, -6.8e-07, -6.7e-07, -6.6e-07, -6.5e-07, -6.4e-07, -6.3e-07, -6.2e-07, -6.1e-07, -6e-07, -5.9e-07, -5.8e-07, -5.7e-07, -5.6e-07, -5.5e-07, -5.4e-07, -5.3e-07, -5.2e-07, -5.1e-07, -5e-07, -4.9e-07, -4.8e-07, -4.7e-07, -4.6e-07, -4.5e-07, -4.4e-07, -4.3e-07, -4.2e-07, -4.1e-07, -4e-07, -3.9e-07, -3.8e-07, -3.7e-07, -3.6e-07, -3.5e-07, -3.4e-07, -3.3e-07, -3.2e-07, -3.1e-07, -3e-07, -2.9e-07, -2.8e-07, -2.7e-07, -2.6e-07, -2.5e-07, -2.4e-07, -2.3e-07, -2.2e-07, -2.1e-07, -2e-07, -1.9e-07, -1.8e-07, -1.7e-07, -1.6e-07, -1.5e-07, -1.4e-07, -1.3e-07, -1.2e-07, -1.1e-07, -1e-07, -9e-08, -8e-08, -7e-08, -6e-08, -5e-08, -4e-08, -3e-08, -2e-08, -1e-08, 0.0, 1e-08, 2e-08, 3e-08, 4e-08, 5e-08, 6e-08, 7e-08, 8e-08, 9e-08, 1e-07, 1.1e-07, 1.2e-07, 1.3e-07, 1.4e-07, 1.5e-07, 1.6e-07, 1.7e-07, 1.8e-07, 1.9e-07, 2e-07, 2.1e-07, 2.2e-07, 2.3e-07, 2.4e-07, 2.5e-07, 2.6e-07, 2.7e-07, 2.8e-07, 2.9e-07, 3e-07, 3.1e-07, 3.2e-07, 3.3e-07, 3.4e-07, 3.5e-07, 3.6e-07, 3.7e-07, 3.8e-07, 3.9e-07, 4e-07, 4.1e-07, 4.2e-07, 4.3e-07, 4.4e-07, 4.5e-07, 4.6e-07, 4.7e-07, 4.8e-07, 4.9e-07, 5e-07, 5.1e-07, 5.2e-07, 5.3e-07, 5.4e-07, 5.5e-07, 5.6e-07, 5.7e-07, 5.8e-07, 5.9e-07, 6e-07, 6.1e-07, 6.2e-07, 6.3e-07, 6.4e-07, 6.5e-07, 6.6e-07, 6.7e-07, 6.8e-07, 6.9e-07, 7e-07, 7.1e-07, 7.2e-07, 7.3e-07, 7.4e-07, 7.5e-07, 7.6e-07, 7.7e-07, 7.8e-07, 7.9e-07, 8e-07, 8.1e-07, 8.2e-07, 8.3e-07, 8.4e-07, 8.5e-07, 8.6e-07, 8.7e-07, 8.8e-07, 8.9e-07, 9e-07, 9.1e-07, 9.2e-07, 9.3e-07, 9.4e-07, 9.5e-07, 9.6e-07, 9.7e-07, 9.8e-07, 9.9e-07, 1e-06, 1.01e-06, 1.02e-06, 1.03e-06, 1.04e-06, 1.05e-06, 1.06e-06, 1.07e-06, 1.08e-06, 1.09e-06, 1.1e-06, 1.11e-06, 1.12e-06, 1.13e-06, 1.14e-06, 1.15e-06, 1.16e-06, 1.17e-06, 1.18e-06, 1.19e-06, 1.2e-06, 1.21e-06, 1.22e-06, 1.23e-06, 1.24e-06, 1.25e-06, 1.26e-06, 1.27e-06, 1.28e-06, 1.29e-06, 1.3e-06, 1.31e-06, 1.32e-06, 1.33e-06, 1.34e-06, 1.35e-06, 1.36e-06, 1.37e-06, 1.38e-06, 1.39e-06, 1.4e-06, 1.41e-06, 1.42e-06, 1.43e-06, 1.44e-06, 1.45e-06, 1.46e-06, 1.47e-06, 1.48e-06, 1.49e-06])")
            print("Korrekt svar: -1.49e-06, -1.5e-06, -1.47e-06, -1.48e-06, -1.45e-06, -1.46e-06, -1.43e-06, -1.44e-06, -1.41e-06, -1.42e-06, -1.39e-06, -1.4e-06, -1.37e-06, -1.38e-06, -1.35e-06, -1.36e-06, -1.33e-06, -1.34e-06, -1.31e-06, -1.32e-06, -1.29e-06, -1.3e-06, -1.27e-06, -1.28e-06, -1.25e-06, -1.26e-06, -1.23e-06, -1.24e-06, -1.21e-06, -1.22e-06, -1.19e-06, -1.2e-06, -1.17e-06, -1.18e-06, -1.15e-06, -1.16e-06, -1.13e-06, -1.14e-06, -1.11e-06, -1.12e-06, -1.09e-06, -1.1e-06, -1.07e-06, -1.08e-06, -1.05e-06, -1.06e-06, -1.03e-06, -1.04e-06, -1.01e-06, -1.02e-06, -9.9e-07, -1e-06, -9.7e-07, -9.8e-07, -9.5e-07, -9.6e-07, -9.3e-07, -9.4e-07, -9.1e-07, -9.2e-07, -8.9e-07, -9e-07, -8.7e-07, -8.8e-07, -8.5e-07, -8.6e-07, -8.3e-07, -8.4e-07, -8.1e-07, -8.2e-07, -7.9e-07, -8e-07, -7.7e-07, -7.8e-07, -7.5e-07, -7.6e-07, -7.3e-07, -7.4e-07, -7.1e-07, -7.2e-07, -6.9e-07, -7e-07, -6.7e-07, -6.8e-07, -6.5e-07, -6.6e-07, -6.3e-07, -6.4e-07, -6.1e-07, -6.2e-07, -5.9e-07, -6e-07, -5.7e-07, -5.8e-07, -5.5e-07, -5.6e-07, -5.3e-07, -5.4e-07, -5.1e-07, -5.2e-07, -4.9e-07, -5e-07, -4.7e-07, -4.8e-07, -4.5e-07, -4.6e-07, -4.3e-07, -4.4e-07, -4.1e-07, -4.2e-07, -3.9e-07, -4e-07, -3.7e-07, -3.8e-07, -3.5e-07, -3.6e-07, -3.3e-07, -3.4e-07, -3.1e-07, -3.2e-07, -2.9e-07, -3e-07, -2.7e-07, -2.8e-07, -2.5e-07, -2.6e-07, -2.3e-07, -2.4e-07, -2.1e-07, -2.2e-07, -1.9e-07, -2e-07, -1.7e-07, -1.8e-07, -1.5e-07, -1.6e-07, -1.3e-07, -1.4e-07, -1.1e-07, -1.2e-07, -9e-08, -1e-07, -7e-08, -8e-08, -5e-08, -6e-08, -3e-08, -4e-08, -1e-08, -2e-08, 1e-08, 0.0, 3e-08, 2e-08, 5e-08, 4e-08, 7e-08, 6e-08, 9e-08, 8e-08, 1.1e-07, 1e-07, 1.3e-07, 1.2e-07, 1.5e-07, 1.4e-07, 1.7e-07, 1.6e-07, 1.9e-07, 1.8e-07, 2.1e-07, 2e-07, 2.3e-07, 2.2e-07, 2.5e-07, 2.4e-07, 2.7e-07, 2.6e-07, 2.9e-07, 2.8e-07, 3.1e-07, 3e-07, 3.3e-07, 3.2e-07, 3.5e-07, 3.4e-07, 3.7e-07, 3.6e-07, 3.9e-07, 3.8e-07, 4.1e-07, 4e-07, 4.3e-07, 4.2e-07, 4.5e-07, 4.4e-07, 4.7e-07, 4.6e-07, 4.9e-07, 4.8e-07, 5.1e-07, 5e-07, 5.3e-07, 5.2e-07, 5.5e-07, 5.4e-07, 5.7e-07, 5.6e-07, 5.9e-07, 5.8e-07, 6.1e-07, 6e-07, 6.3e-07, 6.2e-07, 6.5e-07, 6.4e-07, 6.7e-07, 6.6e-07, 6.9e-07, 6.8e-07, 7.1e-07, 7e-07, 7.3e-07, 7.2e-07, 7.5e-07, 7.4e-07, 7.7e-07, 7.6e-07, 7.9e-07, 7.8e-07, 8.1e-07, 8e-07, 8.3e-07, 8.2e-07, 8.5e-07, 8.4e-07, 8.7e-07, 8.6e-07, 8.9e-07, 8.8e-07, 9.1e-07, 9e-07, 9.3e-07, 9.2e-07, 9.5e-07, 9.4e-07, 9.7e-07, 9.6e-07, 9.9e-07, 9.8e-07, 1.01e-06, 1e-06, 1.03e-06, 1.02e-06, 1.05e-06, 1.04e-06, 1.07e-06, 1.06e-06, 1.09e-06, 1.08e-06, 1.11e-06, 1.1e-06, 1.13e-06, 1.12e-06, 1.15e-06, 1.14e-06, 1.17e-06, 1.16e-06, 1.19e-06, 1.18e-06, 1.21e-06, 1.2e-06, 1.23e-06, 1.22e-06, 1.25e-06, 1.24e-06, 1.27e-06, 1.26e-06, 1.29e-06, 1.28e-06, 1.31e-06, 1.3e-06, 1.33e-06, 1.32e-06, 1.35e-06, 1.34e-06, 1.37e-06, 1.36e-06, 1.39e-06, 1.38e-06, 1.41e-06, 1.4e-06, 1.43e-06, 1.42e-06, 1.45e-06, 1.44e-06, 1.47e-06, 1.46e-06, 1.49e-06, 1.48e-06")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/33: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0, 33.5, 34.0, 34.5, 35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0, 42.5, 43.0, 43.5, 44.0, 44.5, 45.0, 45.5, 46.0, 46.5, 47.0, 47.5, 48.0, 48.5, 49.0, 49.5, 50.0, 50.5, 51.0, 51.5, 52.0, 52.5, 53.0, 53.5, 54.0, 54.5, 55.0, 55.5, 56.0, 56.5, 57.0, 57.5, 58.0, 58.5, 59.0, 59.5, 60.0, 60.5, 61.0, 61.5, 62.0, 62.5, 63.0, 63.5, 64.0, 64.5, 65.0, 65.5, 66.0, 66.5, 67.0, 67.5, 68.0, 68.5, 69.0, 69.5, 70.0, 70.5, 71.0, 71.5, 72.0, 72.5, 73.0, 73.5, 74.0, 74.5])
        exp = [0.5, 0.0, 1.5, 1.0, 2.5, 2.0, 3.5, 3.0, 4.5, 4.0, 5.5, 5.0, 6.5, 6.0, 7.5, 7.0, 8.5, 8.0, 9.5, 9.0, 10.5, 10.0, 11.5, 11.0, 12.5, 12.0, 13.5, 13.0, 14.5, 14.0, 15.5, 15.0, 16.5, 16.0, 17.5, 17.0, 18.5, 18.0, 19.5, 19.0, 20.5, 20.0, 21.5, 21.0, 22.5, 22.0, 23.5, 23.0, 24.5, 24.0, 25.5, 25.0, 26.5, 26.0, 27.5, 27.0, 28.5, 28.0, 29.5, 29.0, 30.5, 30.0, 31.5, 31.0, 32.5, 32.0, 33.5, 33.0, 34.5, 34.0, 35.5, 35.0, 36.5, 36.0, 37.5, 37.0, 38.5, 38.0, 39.5, 39.0, 40.5, 40.0, 41.5, 41.0, 42.5, 42.0, 43.5, 43.0, 44.5, 44.0, 45.5, 45.0, 46.5, 46.0, 47.5, 47.0, 48.5, 48.0, 49.5, 49.0, 50.5, 50.0, 51.5, 51.0, 52.5, 52.0, 53.5, 53.0, 54.5, 54.0, 55.5, 55.0, 56.5, 56.0, 57.5, 57.0, 58.5, 58.0, 59.5, 59.0, 60.5, 60.0, 61.5, 61.0, 62.5, 62.0, 63.5, 63.0, 64.5, 64.0, 65.5, 65.0, 66.5, 66.0, 67.5, 67.0, 68.5, 68.0, 69.5, 69.0, 70.5, 70.0, 71.5, 71.0, 72.5, 72.0, 73.5, 73.0, 74.5, 74.0]
        if res != exp:
            print("Fel i test 2b/34: reverse_pairs_r([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0, 33.5, 34.0, 34.5, 35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0, 42.5, 43.0, 43.5, 44.0, 44.5, 45.0, 45.5, 46.0, 46.5, 47.0, 47.5, 48.0, 48.5, 49.0, 49.5, 50.0, 50.5, 51.0, 51.5, 52.0, 52.5, 53.0, 53.5, 54.0, 54.5, 55.0, 55.5, 56.0, 56.5, 57.0, 57.5, 58.0, 58.5, 59.0, 59.5, 60.0, 60.5, 61.0, 61.5, 62.0, 62.5, 63.0, 63.5, 64.0, 64.5, 65.0, 65.5, 66.0, 66.5, 67.0, 67.5, 68.0, 68.5, 69.0, 69.5, 70.0, 70.5, 71.0, 71.5, 72.0, 72.5, 73.0, 73.5, 74.0, 74.5])")
            print("Korrekt svar: 0.5, 0.0, 1.5, 1.0, 2.5, 2.0, 3.5, 3.0, 4.5, 4.0, 5.5, 5.0, 6.5, 6.0, 7.5, 7.0, 8.5, 8.0, 9.5, 9.0, 10.5, 10.0, 11.5, 11.0, 12.5, 12.0, 13.5, 13.0, 14.5, 14.0, 15.5, 15.0, 16.5, 16.0, 17.5, 17.0, 18.5, 18.0, 19.5, 19.0, 20.5, 20.0, 21.5, 21.0, 22.5, 22.0, 23.5, 23.0, 24.5, 24.0, 25.5, 25.0, 26.5, 26.0, 27.5, 27.0, 28.5, 28.0, 29.5, 29.0, 30.5, 30.0, 31.5, 31.0, 32.5, 32.0, 33.5, 33.0, 34.5, 34.0, 35.5, 35.0, 36.5, 36.0, 37.5, 37.0, 38.5, 38.0, 39.5, 39.0, 40.5, 40.0, 41.5, 41.0, 42.5, 42.0, 43.5, 43.0, 44.5, 44.0, 45.5, 45.0, 46.5, 46.0, 47.5, 47.0, 48.5, 48.0, 49.5, 49.0, 50.5, 50.0, 51.5, 51.0, 52.5, 52.0, 53.5, 53.0, 54.5, 54.0, 55.5, 55.0, 56.5, 56.0, 57.5, 57.0, 58.5, 58.0, 59.5, 59.0, 60.5, 60.0, 61.5, 61.0, 62.5, 62.0, 63.5, 63.0, 64.5, 64.0, 65.5, 65.0, 66.5, 66.0, 67.5, 67.0, 68.5, 68.0, 69.5, 69.0, 70.5, 70.0, 71.5, 71.0, 72.5, 72.0, 73.5, 73.0, 74.5, 74.0")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/34: Exception')
        print_exception()

    try:
        res = reverse_pairs_r(['kod', 123, False, 7.7])
        exp = [123, 'kod', 7.7, False]
        if res != exp:
            print("Fel i test 2b/35: reverse_pairs_r(['kod', 123, False, 7.7])")
            print("Korrekt svar: 123, 'kod', 7.7, False")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/35: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([1, 1.0, 1, 1.0, 1, 1, 1.0])
        exp = [1.0, 1, 1.0, 1, 1, 1, 1.0]
        if res != exp:
            print("Fel i test 2b/36: reverse_pairs_r([1, 1.0, 1, 1.0, 1, 1, 1.0])")
            print("Korrekt svar: 1.0, 1, 1.0, 1, 1, 1, 1.0")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/36: Exception')
        print_exception()

    try:
        res = reverse_pairs_r(['123', 123, 97, 'a', False])
        exp = [123, '123', 'a', 97, False]
        if res != exp:
            print("Fel i test 2b/37: reverse_pairs_r(['123', 123, 97, 'a', False])")
            print("Korrekt svar: 123, '123', 'a', 97, False")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/37: Exception')
        print_exception()

    try:
        res = reverse_pairs_r(['0', 1.0, 2, '3', 4.0, 5, '6', 7.0, 8, '9', 10.0, 11, '12', 13.0, 14, '15', 16.0, 17, '18', 19.0, 20, '21', 22.0, 23, '24', 25.0, 26, '27', 28.0, 29, '30', 31.0, 32, '33', 34.0, 35, '36', 37.0, 38, '39', 40.0, 41, '42', 43.0, 44, '45', 46.0, 47, '48', 49.0, 50, '51', 52.0, 53, '54', 55.0, 56, '57', 58.0, 59, '60', 61.0, 62, '63', 64.0, 65, '66', 67.0, 68, '69', 70.0, 71, '72', 73.0, 74, '75', 76.0, 77, '78', 79.0, 80, '81', 82.0, 83, '84', 85.0, 86, '87', 88.0, 89, '90', 91.0, 92, '93', 94.0, 95, '96', 97.0, 98, '99', 100.0, 101, '102', 103.0, 104, '105', 106.0, 107, '108', 109.0, 110, '111', 112.0, 113, '114', 115.0, 116, '117', 118.0, 119, '120', 121.0, 122, '123', 124.0, 125, '126', 127.0, 128, '129', 130.0, 131, '132', 133.0, 134, '135', 136.0, 137, '138', 139.0, 140, '141', 142.0, 143, '144', 145.0, 146, '147', 148.0, 149])
        exp = [1.0, '0', '3', 2, 5, 4.0, 7.0, '6', '9', 8, 11, 10.0, 13.0, '12', '15', 14, 17, 16.0, 19.0, '18', '21', 20, 23, 22.0, 25.0, '24', '27', 26, 29, 28.0, 31.0, '30', '33', 32, 35, 34.0, 37.0, '36', '39', 38, 41, 40.0, 43.0, '42', '45', 44, 47, 46.0, 49.0, '48', '51', 50, 53, 52.0, 55.0, '54', '57', 56, 59, 58.0, 61.0, '60', '63', 62, 65, 64.0, 67.0, '66', '69', 68, 71, 70.0, 73.0, '72', '75', 74, 77, 76.0, 79.0, '78', '81', 80, 83, 82.0, 85.0, '84', '87', 86, 89, 88.0, 91.0, '90', '93', 92, 95, 94.0, 97.0, '96', '99', 98, 101, 100.0, 103.0, '102', '105', 104, 107, 106.0, 109.0, '108', '111', 110, 113, 112.0, 115.0, '114', '117', 116, 119, 118.0, 121.0, '120', '123', 122, 125, 124.0, 127.0, '126', '129', 128, 131, 130.0, 133.0, '132', '135', 134, 137, 136.0, 139.0, '138', '141', 140, 143, 142.0, 145.0, '144', '147', 146, 149, 148.0]
        if res != exp:
            print("Fel i test 2b/38: reverse_pairs_r(['0', 1.0, 2, '3', 4.0, 5, '6', 7.0, 8, '9', 10.0, 11, '12', 13.0, 14, '15', 16.0, 17, '18', 19.0, 20, '21', 22.0, 23, '24', 25.0, 26, '27', 28.0, 29, '30', 31.0, 32, '33', 34.0, 35, '36', 37.0, 38, '39', 40.0, 41, '42', 43.0, 44, '45', 46.0, 47, '48', 49.0, 50, '51', 52.0, 53, '54', 55.0, 56, '57', 58.0, 59, '60', 61.0, 62, '63', 64.0, 65, '66', 67.0, 68, '69', 70.0, 71, '72', 73.0, 74, '75', 76.0, 77, '78', 79.0, 80, '81', 82.0, 83, '84', 85.0, 86, '87', 88.0, 89, '90', 91.0, 92, '93', 94.0, 95, '96', 97.0, 98, '99', 100.0, 101, '102', 103.0, 104, '105', 106.0, 107, '108', 109.0, 110, '111', 112.0, 113, '114', 115.0, 116, '117', 118.0, 119, '120', 121.0, 122, '123', 124.0, 125, '126', 127.0, 128, '129', 130.0, 131, '132', 133.0, 134, '135', 136.0, 137, '138', 139.0, 140, '141', 142.0, 143, '144', 145.0, 146, '147', 148.0, 149])")
            print("Korrekt svar: 1.0, '0', '3', 2, 5, 4.0, 7.0, '6', '9', 8, 11, 10.0, 13.0, '12', '15', 14, 17, 16.0, 19.0, '18', '21', 20, 23, 22.0, 25.0, '24', '27', 26, 29, 28.0, 31.0, '30', '33', 32, 35, 34.0, 37.0, '36', '39', 38, 41, 40.0, 43.0, '42', '45', 44, 47, 46.0, 49.0, '48', '51', 50, 53, 52.0, 55.0, '54', '57', 56, 59, 58.0, 61.0, '60', '63', 62, 65, 64.0, 67.0, '66', '69', 68, 71, 70.0, 73.0, '72', '75', 74, 77, 76.0, 79.0, '78', '81', 80, 83, 82.0, 85.0, '84', '87', 86, 89, 88.0, 91.0, '90', '93', 92, 95, 94.0, 97.0, '96', '99', 98, 101, 100.0, 103.0, '102', '105', 104, 107, 106.0, 109.0, '108', '111', 110, 113, 112.0, 115.0, '114', '117', 116, 119, 118.0, 121.0, '120', '123', 122, 125, 124.0, 127.0, '126', '129', 128, 131, 130.0, 133.0, '132', '135', 134, 137, 136.0, 139.0, '138', '141', 140, 143, 142.0, 145.0, '144', '147', 146, 149, 148.0")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/38: Exception')
        print_exception()

    try:
        res = reverse_pairs_r(['1', 1, 2, '2', '3', '3', 4, 4])
        exp = [1, '1', '2', 2, '3', '3', 4, 4]
        if res != exp:
            print("Fel i test 2b/39: reverse_pairs_r(['1', 1, 2, '2', '3', '3', 4, 4])")
            print("Korrekt svar: 1, '1', '2', 2, '3', '3', 4, 4")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/39: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([[]])
        exp = [[]]
        if res != exp:
            print("Fel i test 2b/40: reverse_pairs_r([[]])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/40: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([[], [[]]])
        exp = [[[]], []]
        if res != exp:
            print("Fel i test 2b/41: reverse_pairs_r([[], [[]]])")
            print("Korrekt svar: [[]], []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/41: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([[[[[]]]], [], [[]]])
        exp = [[], [[[[]]]], [[]]]
        if res != exp:
            print("Fel i test 2b/42: reverse_pairs_r([[[[[]]]], [], [[]]])")
            print("Korrekt svar: [], [[[[]]]], [[]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/42: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([[]])
        exp = [[]]
        if res != exp:
            print("Fel i test 2b/43: reverse_pairs_r([[]])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/43: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([[[[[[[[[[[]]]]]]]]]]])
        exp = [[[[[[[[[[[]]]]]]]]]]]
        if res != exp:
            print("Fel i test 2b/44: reverse_pairs_r([[[[[[[[[[[]]]]]]]]]]])")
            print("Korrekt svar: [[[[[[[[[[]]]]]]]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/44: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]])
        exp = [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
        if res != exp:
            print("Fel i test 2b/45: reverse_pairs_r([[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]])")
            print("Korrekt svar: [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/45: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([[1], [2]])
        exp = [[2], [1]]
        if res != exp:
            print("Fel i test 2b/46: reverse_pairs_r([[1], [2]])")
            print("Korrekt svar: [2], [1]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/46: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([[1], [[2]], [[[3]]], [[[[4]]]]])
        exp = [[[2]], [1], [[[[4]]]], [[[3]]]]
        if res != exp:
            print("Fel i test 2b/47: reverse_pairs_r([[1], [[2]], [[[3]]], [[[[4]]]]])")
            print("Korrekt svar: [[2]], [1], [[[[4]]]], [[[3]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/47: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12], [0, 4, 8, 12, 16]], [[0, 0, 0, 0, 0], [0, 2, 4, 6, 8], [0, 4, 8, 12, 16], [0, 6, 12, 18, 24], [0, 8, 16, 24, 32]], [[0, 0, 0, 0, 0], [0, 3, 6, 9, 12], [0, 6, 12, 18, 24], [0, 9, 18, 27, 36], [0, 12, 24, 36, 48]], [[0, 0, 0, 0, 0], [0, 4, 8, 12, 16], [0, 8, 16, 24, 32], [0, 12, 24, 36, 48], [0, 16, 32, 48, 64]]])
        exp = [[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12], [0, 4, 8, 12, 16]], [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 3, 6, 9, 12], [0, 6, 12, 18, 24], [0, 9, 18, 27, 36], [0, 12, 24, 36, 48]], [[0, 0, 0, 0, 0], [0, 2, 4, 6, 8], [0, 4, 8, 12, 16], [0, 6, 12, 18, 24], [0, 8, 16, 24, 32]], [[0, 0, 0, 0, 0], [0, 4, 8, 12, 16], [0, 8, 16, 24, 32], [0, 12, 24, 36, 48], [0, 16, 32, 48, 64]]]
        if res != exp:
            print("Fel i test 2b/48: reverse_pairs_r([[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12], [0, 4, 8, 12, 16]], [[0, 0, 0, 0, 0], [0, 2, 4, 6, 8], [0, 4, 8, 12, 16], [0, 6, 12, 18, 24], [0, 8, 16, 24, 32]], [[0, 0, 0, 0, 0], [0, 3, 6, 9, 12], [0, 6, 12, 18, 24], [0, 9, 18, 27, 36], [0, 12, 24, 36, 48]], [[0, 0, 0, 0, 0], [0, 4, 8, 12, 16], [0, 8, 16, 24, 32], [0, 12, 24, 36, 48], [0, 16, 32, 48, 64]]])")
            print("Korrekt svar: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12], [0, 4, 8, 12, 16]], [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 3, 6, 9, 12], [0, 6, 12, 18, 24], [0, 9, 18, 27, 36], [0, 12, 24, 36, 48]], [[0, 0, 0, 0, 0], [0, 2, 4, 6, 8], [0, 4, 8, 12, 16], [0, 6, 12, 18, 24], [0, 8, 16, 24, 32]], [[0, 0, 0, 0, 0], [0, 4, 8, 12, 16], [0, 8, 16, 24, 32], [0, 12, 24, 36, 48], [0, 16, 32, 48, 64]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/48: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([(), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ()])
        exp = [(), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ()]
        if res != exp:
            print("Fel i test 2b/49: reverse_pairs_r([(), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ()])")
            print("Korrekt svar: (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ()")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/49: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])
        exp = [(0, 1), (0, 0), (1, 0), (0, 2), (1, 2), (1, 1), (2, 1), (2, 0), (2, 2)]
        if res != exp:
            print("Fel i test 2b/50: reverse_pairs_r([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])")
            print("Korrekt svar: (0, 1), (0, 0), (1, 0), (0, 2), (1, 2), (1, 1), (2, 1), (2, 0), (2, 2)")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/50: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}])
        exp = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
        if res != exp:
            print("Fel i test 2b/51: reverse_pairs_r([{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}])")
            print("Korrekt svar: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/51: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([{0: 0}, {1: 1}, {2: 2}, {3: 3}, {4: 4}, {5: 5}, {6: 6}, {7: 7}, {8: 8}, {9: 9}, {10: 10}, {11: 11}, {12: 12}, {13: 13}, {14: 14}, {15: 15}, {16: 16}, {17: 17}, {18: 18}, {19: 19}, {20: 20}, {21: 21}, {22: 22}, {23: 23}, {24: 24}, {25: 25}, {26: 26}, {27: 27}, {28: 28}, {29: 29}, {30: 30}, {31: 31}, {32: 32}, {33: 33}, {34: 34}, {35: 35}, {36: 36}, {37: 37}, {38: 38}, {39: 39}, {40: 40}, {41: 41}, {42: 42}, {43: 43}, {44: 44}, {45: 45}, {46: 46}, {47: 47}, {48: 48}, {49: 49}, {50: 50}, {51: 51}, {52: 52}, {53: 53}, {54: 54}, {55: 55}, {56: 56}, {57: 57}, {58: 58}, {59: 59}, {60: 60}, {61: 61}, {62: 62}, {63: 63}, {64: 64}, {65: 65}, {66: 66}, {67: 67}, {68: 68}, {69: 69}, {70: 70}, {71: 71}, {72: 72}, {73: 73}, {74: 74}, {75: 75}, {76: 76}, {77: 77}, {78: 78}, {79: 79}, {80: 80}, {81: 81}, {82: 82}, {83: 83}, {84: 84}, {85: 85}, {86: 86}, {87: 87}, {88: 88}, {89: 89}, {90: 90}, {91: 91}, {92: 92}, {93: 93}, {94: 94}, {95: 95}, {96: 96}, {97: 97}, {98: 98}, {99: 99}])
        exp = [{1: 1}, {0: 0}, {3: 3}, {2: 2}, {5: 5}, {4: 4}, {7: 7}, {6: 6}, {9: 9}, {8: 8}, {11: 11}, {10: 10}, {13: 13}, {12: 12}, {15: 15}, {14: 14}, {17: 17}, {16: 16}, {19: 19}, {18: 18}, {21: 21}, {20: 20}, {23: 23}, {22: 22}, {25: 25}, {24: 24}, {27: 27}, {26: 26}, {29: 29}, {28: 28}, {31: 31}, {30: 30}, {33: 33}, {32: 32}, {35: 35}, {34: 34}, {37: 37}, {36: 36}, {39: 39}, {38: 38}, {41: 41}, {40: 40}, {43: 43}, {42: 42}, {45: 45}, {44: 44}, {47: 47}, {46: 46}, {49: 49}, {48: 48}, {51: 51}, {50: 50}, {53: 53}, {52: 52}, {55: 55}, {54: 54}, {57: 57}, {56: 56}, {59: 59}, {58: 58}, {61: 61}, {60: 60}, {63: 63}, {62: 62}, {65: 65}, {64: 64}, {67: 67}, {66: 66}, {69: 69}, {68: 68}, {71: 71}, {70: 70}, {73: 73}, {72: 72}, {75: 75}, {74: 74}, {77: 77}, {76: 76}, {79: 79}, {78: 78}, {81: 81}, {80: 80}, {83: 83}, {82: 82}, {85: 85}, {84: 84}, {87: 87}, {86: 86}, {89: 89}, {88: 88}, {91: 91}, {90: 90}, {93: 93}, {92: 92}, {95: 95}, {94: 94}, {97: 97}, {96: 96}, {99: 99}, {98: 98}]
        if res != exp:
            print("Fel i test 2b/52: reverse_pairs_r([{0: 0}, {1: 1}, {2: 2}, {3: 3}, {4: 4}, {5: 5}, {6: 6}, {7: 7}, {8: 8}, {9: 9}, {10: 10}, {11: 11}, {12: 12}, {13: 13}, {14: 14}, {15: 15}, {16: 16}, {17: 17}, {18: 18}, {19: 19}, {20: 20}, {21: 21}, {22: 22}, {23: 23}, {24: 24}, {25: 25}, {26: 26}, {27: 27}, {28: 28}, {29: 29}, {30: 30}, {31: 31}, {32: 32}, {33: 33}, {34: 34}, {35: 35}, {36: 36}, {37: 37}, {38: 38}, {39: 39}, {40: 40}, {41: 41}, {42: 42}, {43: 43}, {44: 44}, {45: 45}, {46: 46}, {47: 47}, {48: 48}, {49: 49}, {50: 50}, {51: 51}, {52: 52}, {53: 53}, {54: 54}, {55: 55}, {56: 56}, {57: 57}, {58: 58}, {59: 59}, {60: 60}, {61: 61}, {62: 62}, {63: 63}, {64: 64}, {65: 65}, {66: 66}, {67: 67}, {68: 68}, {69: 69}, {70: 70}, {71: 71}, {72: 72}, {73: 73}, {74: 74}, {75: 75}, {76: 76}, {77: 77}, {78: 78}, {79: 79}, {80: 80}, {81: 81}, {82: 82}, {83: 83}, {84: 84}, {85: 85}, {86: 86}, {87: 87}, {88: 88}, {89: 89}, {90: 90}, {91: 91}, {92: 92}, {93: 93}, {94: 94}, {95: 95}, {96: 96}, {97: 97}, {98: 98}, {99: 99}])")
            print("Korrekt svar: {1: 1}, {0: 0}, {3: 3}, {2: 2}, {5: 5}, {4: 4}, {7: 7}, {6: 6}, {9: 9}, {8: 8}, {11: 11}, {10: 10}, {13: 13}, {12: 12}, {15: 15}, {14: 14}, {17: 17}, {16: 16}, {19: 19}, {18: 18}, {21: 21}, {20: 20}, {23: 23}, {22: 22}, {25: 25}, {24: 24}, {27: 27}, {26: 26}, {29: 29}, {28: 28}, {31: 31}, {30: 30}, {33: 33}, {32: 32}, {35: 35}, {34: 34}, {37: 37}, {36: 36}, {39: 39}, {38: 38}, {41: 41}, {40: 40}, {43: 43}, {42: 42}, {45: 45}, {44: 44}, {47: 47}, {46: 46}, {49: 49}, {48: 48}, {51: 51}, {50: 50}, {53: 53}, {52: 52}, {55: 55}, {54: 54}, {57: 57}, {56: 56}, {59: 59}, {58: 58}, {61: 61}, {60: 60}, {63: 63}, {62: 62}, {65: 65}, {64: 64}, {67: 67}, {66: 66}, {69: 69}, {68: 68}, {71: 71}, {70: 70}, {73: 73}, {72: 72}, {75: 75}, {74: 74}, {77: 77}, {76: 76}, {79: 79}, {78: 78}, {81: 81}, {80: 80}, {83: 83}, {82: 82}, {85: 85}, {84: 84}, {87: 87}, {86: 86}, {89: 89}, {88: 88}, {91: 91}, {90: 90}, {93: 93}, {92: 92}, {95: 95}, {94: 94}, {97: 97}, {96: 96}, {99: 99}, {98: 98}")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/52: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()])
        exp = [set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()]
        if res != exp:
            print("Fel i test 2b/53: reverse_pairs_r([set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()])")
            print("Korrekt svar: set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/53: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([{-100}, {-99}, {-98}, {-97}, {-96}, {-95}, {-94}, {-93}, {-92}, {-91}, {-90}, {-89}, {-88}, {-87}, {-86}, {-85}, {-84}, {-83}, {-82}, {-81}, {-80}, {-79}, {-78}, {-77}, {-76}, {-75}, {-74}, {-73}, {-72}, {-71}, {-70}, {-69}, {-68}, {-67}, {-66}, {-65}, {-64}, {-63}, {-62}, {-61}, {-60}, {-59}, {-58}, {-57}, {-56}, {-55}, {-54}, {-53}, {-52}, {-51}, {-50}, {-49}, {-48}, {-47}, {-46}, {-45}, {-44}, {-43}, {-42}, {-41}, {-40}, {-39}, {-38}, {-37}, {-36}, {-35}, {-34}, {-33}, {-32}, {-31}, {-30}, {-29}, {-28}, {-27}, {-26}, {-25}, {-24}, {-23}, {-22}, {-21}, {-20}, {-19}, {-18}, {-17}, {-16}, {-15}, {-14}, {-13}, {-12}, {-11}, {-10}, {-9}, {-8}, {-7}, {-6}, {-5}, {-4}, {-3}, {-2}, {-1}, {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}, {24}, {25}, {26}, {27}, {28}, {29}, {30}, {31}, {32}, {33}, {34}, {35}, {36}, {37}, {38}, {39}, {40}, {41}, {42}, {43}, {44}, {45}, {46}, {47}, {48}, {49}, {50}, {51}, {52}, {53}, {54}, {55}, {56}, {57}, {58}, {59}, {60}, {61}, {62}, {63}, {64}, {65}, {66}, {67}, {68}, {69}, {70}, {71}, {72}, {73}, {74}, {75}, {76}, {77}, {78}, {79}, {80}, {81}, {82}, {83}, {84}, {85}, {86}, {87}, {88}, {89}, {90}, {91}, {92}, {93}, {94}, {95}, {96}, {97}, {98}, {99}])
        exp = [{-99}, {-100}, {-97}, {-98}, {-95}, {-96}, {-93}, {-94}, {-91}, {-92}, {-89}, {-90}, {-87}, {-88}, {-85}, {-86}, {-83}, {-84}, {-81}, {-82}, {-79}, {-80}, {-77}, {-78}, {-75}, {-76}, {-73}, {-74}, {-71}, {-72}, {-69}, {-70}, {-67}, {-68}, {-65}, {-66}, {-63}, {-64}, {-61}, {-62}, {-59}, {-60}, {-57}, {-58}, {-55}, {-56}, {-53}, {-54}, {-51}, {-52}, {-49}, {-50}, {-47}, {-48}, {-45}, {-46}, {-43}, {-44}, {-41}, {-42}, {-39}, {-40}, {-37}, {-38}, {-35}, {-36}, {-33}, {-34}, {-31}, {-32}, {-29}, {-30}, {-27}, {-28}, {-25}, {-26}, {-23}, {-24}, {-21}, {-22}, {-19}, {-20}, {-17}, {-18}, {-15}, {-16}, {-13}, {-14}, {-11}, {-12}, {-9}, {-10}, {-7}, {-8}, {-5}, {-6}, {-3}, {-4}, {-1}, {-2}, {1}, {0}, {3}, {2}, {5}, {4}, {7}, {6}, {9}, {8}, {11}, {10}, {13}, {12}, {15}, {14}, {17}, {16}, {19}, {18}, {21}, {20}, {23}, {22}, {25}, {24}, {27}, {26}, {29}, {28}, {31}, {30}, {33}, {32}, {35}, {34}, {37}, {36}, {39}, {38}, {41}, {40}, {43}, {42}, {45}, {44}, {47}, {46}, {49}, {48}, {51}, {50}, {53}, {52}, {55}, {54}, {57}, {56}, {59}, {58}, {61}, {60}, {63}, {62}, {65}, {64}, {67}, {66}, {69}, {68}, {71}, {70}, {73}, {72}, {75}, {74}, {77}, {76}, {79}, {78}, {81}, {80}, {83}, {82}, {85}, {84}, {87}, {86}, {89}, {88}, {91}, {90}, {93}, {92}, {95}, {94}, {97}, {96}, {99}, {98}]
        if res != exp:
            print("Fel i test 2b/54: reverse_pairs_r([{-100}, {-99}, {-98}, {-97}, {-96}, {-95}, {-94}, {-93}, {-92}, {-91}, {-90}, {-89}, {-88}, {-87}, {-86}, {-85}, {-84}, {-83}, {-82}, {-81}, {-80}, {-79}, {-78}, {-77}, {-76}, {-75}, {-74}, {-73}, {-72}, {-71}, {-70}, {-69}, {-68}, {-67}, {-66}, {-65}, {-64}, {-63}, {-62}, {-61}, {-60}, {-59}, {-58}, {-57}, {-56}, {-55}, {-54}, {-53}, {-52}, {-51}, {-50}, {-49}, {-48}, {-47}, {-46}, {-45}, {-44}, {-43}, {-42}, {-41}, {-40}, {-39}, {-38}, {-37}, {-36}, {-35}, {-34}, {-33}, {-32}, {-31}, {-30}, {-29}, {-28}, {-27}, {-26}, {-25}, {-24}, {-23}, {-22}, {-21}, {-20}, {-19}, {-18}, {-17}, {-16}, {-15}, {-14}, {-13}, {-12}, {-11}, {-10}, {-9}, {-8}, {-7}, {-6}, {-5}, {-4}, {-3}, {-2}, {-1}, {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}, {24}, {25}, {26}, {27}, {28}, {29}, {30}, {31}, {32}, {33}, {34}, {35}, {36}, {37}, {38}, {39}, {40}, {41}, {42}, {43}, {44}, {45}, {46}, {47}, {48}, {49}, {50}, {51}, {52}, {53}, {54}, {55}, {56}, {57}, {58}, {59}, {60}, {61}, {62}, {63}, {64}, {65}, {66}, {67}, {68}, {69}, {70}, {71}, {72}, {73}, {74}, {75}, {76}, {77}, {78}, {79}, {80}, {81}, {82}, {83}, {84}, {85}, {86}, {87}, {88}, {89}, {90}, {91}, {92}, {93}, {94}, {95}, {96}, {97}, {98}, {99}])")
            print("Korrekt svar: {-99}, {-100}, {-97}, {-98}, {-95}, {-96}, {-93}, {-94}, {-91}, {-92}, {-89}, {-90}, {-87}, {-88}, {-85}, {-86}, {-83}, {-84}, {-81}, {-82}, {-79}, {-80}, {-77}, {-78}, {-75}, {-76}, {-73}, {-74}, {-71}, {-72}, {-69}, {-70}, {-67}, {-68}, {-65}, {-66}, {-63}, {-64}, {-61}, {-62}, {-59}, {-60}, {-57}, {-58}, {-55}, {-56}, {-53}, {-54}, {-51}, {-52}, {-49}, {-50}, {-47}, {-48}, {-45}, {-46}, {-43}, {-44}, {-41}, {-42}, {-39}, {-40}, {-37}, {-38}, {-35}, {-36}, {-33}, {-34}, {-31}, {-32}, {-29}, {-30}, {-27}, {-28}, {-25}, {-26}, {-23}, {-24}, {-21}, {-22}, {-19}, {-20}, {-17}, {-18}, {-15}, {-16}, {-13}, {-14}, {-11}, {-12}, {-9}, {-10}, {-7}, {-8}, {-5}, {-6}, {-3}, {-4}, {-1}, {-2}, {1}, {0}, {3}, {2}, {5}, {4}, {7}, {6}, {9}, {8}, {11}, {10}, {13}, {12}, {15}, {14}, {17}, {16}, {19}, {18}, {21}, {20}, {23}, {22}, {25}, {24}, {27}, {26}, {29}, {28}, {31}, {30}, {33}, {32}, {35}, {34}, {37}, {36}, {39}, {38}, {41}, {40}, {43}, {42}, {45}, {44}, {47}, {46}, {49}, {48}, {51}, {50}, {53}, {52}, {55}, {54}, {57}, {56}, {59}, {58}, {61}, {60}, {63}, {62}, {65}, {64}, {67}, {66}, {69}, {68}, {71}, {70}, {73}, {72}, {75}, {74}, {77}, {76}, {79}, {78}, {81}, {80}, {83}, {82}, {85}, {84}, {87}, {86}, {89}, {88}, {91}, {90}, {93}, {92}, {95}, {94}, {97}, {96}, {99}, {98}")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/54: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([{}, set(), (), []])
        exp = [set(), {}, [], ()]
        if res != exp:
            print("Fel i test 2b/55: reverse_pairs_r([{}, set(), (), []])")
            print("Korrekt svar: set(), {}, [], ()")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/55: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([{'3', 1, 2}, [1, '2', 3], {'1': 1, 2: '2', 3: '3'}, ('1', 2, '3')])
        exp = [[1, '2', 3], {'3', 1, 2}, ('1', 2, '3'), {'1': 1, 2: '2', 3: '3'}]
        if res != exp:
            print("Fel i test 2b/56: reverse_pairs_r([{'3', 1, 2}, [1, '2', 3], {'1': 1, 2: '2', 3: '3'}, ('1', 2, '3')])")
            print("Korrekt svar: [1, '2', 3], {'3', 1, 2}, ('1', 2, '3'), {'1': 1, 2: '2', 3: '3'}")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/56: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([[set(), (2, 'a'), {1: 'a'}], {2, 3, (1, 'a', False)}, {'1': [1, 2, 3], '2': {}}, (set(), [2], {1: '1'})])
        exp = [{2, 3, (1, 'a', False)}, [set(), (2, 'a'), {1: 'a'}], (set(), [2], {1: '1'}), {'1': [1, 2, 3], '2': {}}]
        if res != exp:
            print("Fel i test 2b/57: reverse_pairs_r([[set(), (2, 'a'), {1: 'a'}], {2, 3, (1, 'a', False)}, {'1': [1, 2, 3], '2': {}}, (set(), [2], {1: '1'})])")
            print("Korrekt svar: {2, 3, (1, 'a', False)}, [set(), (2, 'a'), {1: 'a'}], (set(), [2], {1: '1'}), {'1': [1, 2, 3], '2': {}}")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/57: Exception')
        print_exception()



    try:
        res = reverse_pairs_r([int])
        exp = [int]
        if res != exp:
            print("Fel i test 2b/60: reverse_pairs_r([int])")
            print("Korrekt svar: <class '__main__.int'>")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/60: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([int, list])
        exp = [list, int]
        if res != exp:
            print("Fel i test 2b/61: reverse_pairs_r([int, list])")
            print("Korrekt svar: <class '__main__.list'>, <class '__main__.int'>")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/61: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([1, {'a': 2}, 3])
        exp = [{'a': 2}, 1, 3]
        if res != exp:
            print("Fel i test 2b/62: reverse_pairs_r([1, {'a': 2}, 3])")
            print("Korrekt svar: {'a': 2}, 1, 3")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/62: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([[1, 2, 3], '123'])
        exp = ['123', [1, 2, 3]]
        if res != exp:
            print("Fel i test 2b/63: reverse_pairs_r([[1, 2, 3], '123'])")
            print("Korrekt svar: '123', [1, 2, 3]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/63: Exception')
        print_exception()


    try:
        res = reverse_pairs_r([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        exp = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if res != exp:
            print("Fel i test 2b/65: reverse_pairs_r([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])")
            print("Korrekt svar: 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/65: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999])
        exp = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26, 29, 28, 31, 30, 33, 32, 35, 34, 37, 36, 39, 38, 41, 40, 43, 42, 45, 44, 47, 46, 49, 48, 51, 50, 53, 52, 55, 54, 57, 56, 59, 58, 61, 60, 63, 62, 65, 64, 67, 66, 69, 68, 71, 70, 73, 72, 75, 74, 77, 76, 79, 78, 81, 80, 83, 82, 85, 84, 87, 86, 89, 88, 91, 90, 93, 92, 95, 94, 97, 96, 99, 98, 101, 100, 103, 102, 105, 104, 107, 106, 109, 108, 111, 110, 113, 112, 115, 114, 117, 116, 119, 118, 121, 120, 123, 122, 125, 124, 127, 126, 129, 128, 131, 130, 133, 132, 135, 134, 137, 136, 139, 138, 141, 140, 143, 142, 145, 144, 147, 146, 149, 148, 151, 150, 153, 152, 155, 154, 157, 156, 159, 158, 161, 160, 163, 162, 165, 164, 167, 166, 169, 168, 171, 170, 173, 172, 175, 174, 177, 176, 179, 178, 181, 180, 183, 182, 185, 184, 187, 186, 189, 188, 191, 190, 193, 192, 195, 194, 197, 196, 199, 198, 201, 200, 203, 202, 205, 204, 207, 206, 209, 208, 211, 210, 213, 212, 215, 214, 217, 216, 219, 218, 221, 220, 223, 222, 225, 224, 227, 226, 229, 228, 231, 230, 233, 232, 235, 234, 237, 236, 239, 238, 241, 240, 243, 242, 245, 244, 247, 246, 249, 248, 251, 250, 253, 252, 255, 254, 257, 256, 259, 258, 261, 260, 263, 262, 265, 264, 267, 266, 269, 268, 271, 270, 273, 272, 275, 274, 277, 276, 279, 278, 281, 280, 283, 282, 285, 284, 287, 286, 289, 288, 291, 290, 293, 292, 295, 294, 297, 296, 299, 298, 301, 300, 303, 302, 305, 304, 307, 306, 309, 308, 311, 310, 313, 312, 315, 314, 317, 316, 319, 318, 321, 320, 323, 322, 325, 324, 327, 326, 329, 328, 331, 330, 333, 332, 335, 334, 337, 336, 339, 338, 341, 340, 343, 342, 345, 344, 347, 346, 349, 348, 351, 350, 353, 352, 355, 354, 357, 356, 359, 358, 361, 360, 363, 362, 365, 364, 367, 366, 369, 368, 371, 370, 373, 372, 375, 374, 377, 376, 379, 378, 381, 380, 383, 382, 385, 384, 387, 386, 389, 388, 391, 390, 393, 392, 395, 394, 397, 396, 399, 398, 401, 400, 403, 402, 405, 404, 407, 406, 409, 408, 411, 410, 413, 412, 415, 414, 417, 416, 419, 418, 421, 420, 423, 422, 425, 424, 427, 426, 429, 428, 431, 430, 433, 432, 435, 434, 437, 436, 439, 438, 441, 440, 443, 442, 445, 444, 447, 446, 449, 448, 451, 450, 453, 452, 455, 454, 457, 456, 459, 458, 461, 460, 463, 462, 465, 464, 467, 466, 469, 468, 471, 470, 473, 472, 475, 474, 477, 476, 479, 478, 481, 480, 483, 482, 485, 484, 487, 486, 489, 488, 491, 490, 493, 492, 495, 494, 497, 496, 499, 498, 501, 500, 503, 502, 505, 504, 507, 506, 509, 508, 511, 510, 513, 512, 515, 514, 517, 516, 519, 518, 521, 520, 523, 522, 525, 524, 527, 526, 529, 528, 531, 530, 533, 532, 535, 534, 537, 536, 539, 538, 541, 540, 543, 542, 545, 544, 547, 546, 549, 548, 551, 550, 553, 552, 555, 554, 557, 556, 559, 558, 561, 560, 563, 562, 565, 564, 567, 566, 569, 568, 571, 570, 573, 572, 575, 574, 577, 576, 579, 578, 581, 580, 583, 582, 585, 584, 587, 586, 589, 588, 591, 590, 593, 592, 595, 594, 597, 596, 599, 598, 601, 600, 603, 602, 605, 604, 607, 606, 609, 608, 611, 610, 613, 612, 615, 614, 617, 616, 619, 618, 621, 620, 623, 622, 625, 624, 627, 626, 629, 628, 631, 630, 633, 632, 635, 634, 637, 636, 639, 638, 641, 640, 643, 642, 645, 644, 647, 646, 649, 648, 651, 650, 653, 652, 655, 654, 657, 656, 659, 658, 661, 660, 663, 662, 665, 664, 667, 666, 669, 668, 671, 670, 673, 672, 675, 674, 677, 676, 679, 678, 681, 680, 683, 682, 685, 684, 687, 686, 689, 688, 691, 690, 693, 692, 695, 694, 697, 696, 699, 698, 701, 700, 703, 702, 705, 704, 707, 706, 709, 708, 711, 710, 713, 712, 715, 714, 717, 716, 719, 718, 721, 720, 723, 722, 725, 724, 727, 726, 729, 728, 731, 730, 733, 732, 735, 734, 737, 736, 739, 738, 741, 740, 743, 742, 745, 744, 747, 746, 749, 748, 751, 750, 753, 752, 755, 754, 757, 756, 759, 758, 761, 760, 763, 762, 765, 764, 767, 766, 769, 768, 771, 770, 773, 772, 775, 774, 777, 776, 779, 778, 781, 780, 783, 782, 785, 784, 787, 786, 789, 788, 791, 790, 793, 792, 795, 794, 797, 796, 799, 798, 801, 800, 803, 802, 805, 804, 807, 806, 809, 808, 811, 810, 813, 812, 815, 814, 817, 816, 819, 818, 821, 820, 823, 822, 825, 824, 827, 826, 829, 828, 831, 830, 833, 832, 835, 834, 837, 836, 839, 838, 841, 840, 843, 842, 845, 844, 847, 846, 849, 848, 851, 850, 853, 852, 855, 854, 857, 856, 859, 858, 861, 860, 863, 862, 865, 864, 867, 866, 869, 868, 871, 870, 873, 872, 875, 874, 877, 876, 879, 878, 881, 880, 883, 882, 885, 884, 887, 886, 889, 888, 891, 890, 893, 892, 895, 894, 897, 896, 899, 898, 901, 900, 903, 902, 905, 904, 907, 906, 909, 908, 911, 910, 913, 912, 915, 914, 917, 916, 919, 918, 921, 920, 923, 922, 925, 924, 927, 926, 929, 928, 931, 930, 933, 932, 935, 934, 937, 936, 939, 938, 941, 940, 943, 942, 945, 944, 947, 946, 949, 948, 951, 950, 953, 952, 955, 954, 957, 956, 959, 958, 961, 960, 963, 962, 965, 964, 967, 966, 969, 968, 971, 970, 973, 972, 975, 974, 977, 976, 979, 978, 981, 980, 983, 982, 985, 984, 987, 986, 989, 988, 991, 990, 993, 992, 995, 994, 997, 996, 999, 998]
        if res != exp:
            print("Fel i test 2b/66: reverse_pairs_r([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999])")
            print("Korrekt svar: 1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26, 29, 28, 31, 30, 33, 32, 35, 34, 37, 36, 39, 38, 41, 40, 43, 42, 45, 44, 47, 46, 49, 48, 51, 50, 53, 52, 55, 54, 57, 56, 59, 58, 61, 60, 63, 62, 65, 64, 67, 66, 69, 68, 71, 70, 73, 72, 75, 74, 77, 76, 79, 78, 81, 80, 83, 82, 85, 84, 87, 86, 89, 88, 91, 90, 93, 92, 95, 94, 97, 96, 99, 98, 101, 100, 103, 102, 105, 104, 107, 106, 109, 108, 111, 110, 113, 112, 115, 114, 117, 116, 119, 118, 121, 120, 123, 122, 125, 124, 127, 126, 129, 128, 131, 130, 133, 132, 135, 134, 137, 136, 139, 138, 141, 140, 143, 142, 145, 144, 147, 146, 149, 148, 151, 150, 153, 152, 155, 154, 157, 156, 159, 158, 161, 160, 163, 162, 165, 164, 167, 166, 169, 168, 171, 170, 173, 172, 175, 174, 177, 176, 179, 178, 181, 180, 183, 182, 185, 184, 187, 186, 189, 188, 191, 190, 193, 192, 195, 194, 197, 196, 199, 198, 201, 200, 203, 202, 205, 204, 207, 206, 209, 208, 211, 210, 213, 212, 215, 214, 217, 216, 219, 218, 221, 220, 223, 222, 225, 224, 227, 226, 229, 228, 231, 230, 233, 232, 235, 234, 237, 236, 239, 238, 241, 240, 243, 242, 245, 244, 247, 246, 249, 248, 251, 250, 253, 252, 255, 254, 257, 256, 259, 258, 261, 260, 263, 262, 265, 264, 267, 266, 269, 268, 271, 270, 273, 272, 275, 274, 277, 276, 279, 278, 281, 280, 283, 282, 285, 284, 287, 286, 289, 288, 291, 290, 293, 292, 295, 294, 297, 296, 299, 298, 301, 300, 303, 302, 305, 304, 307, 306, 309, 308, 311, 310, 313, 312, 315, 314, 317, 316, 319, 318, 321, 320, 323, 322, 325, 324, 327, 326, 329, 328, 331, 330, 333, 332, 335, 334, 337, 336, 339, 338, 341, 340, 343, 342, 345, 344, 347, 346, 349, 348, 351, 350, 353, 352, 355, 354, 357, 356, 359, 358, 361, 360, 363, 362, 365, 364, 367, 366, 369, 368, 371, 370, 373, 372, 375, 374, 377, 376, 379, 378, 381, 380, 383, 382, 385, 384, 387, 386, 389, 388, 391, 390, 393, 392, 395, 394, 397, 396, 399, 398, 401, 400, 403, 402, 405, 404, 407, 406, 409, 408, 411, 410, 413, 412, 415, 414, 417, 416, 419, 418, 421, 420, 423, 422, 425, 424, 427, 426, 429, 428, 431, 430, 433, 432, 435, 434, 437, 436, 439, 438, 441, 440, 443, 442, 445, 444, 447, 446, 449, 448, 451, 450, 453, 452, 455, 454, 457, 456, 459, 458, 461, 460, 463, 462, 465, 464, 467, 466, 469, 468, 471, 470, 473, 472, 475, 474, 477, 476, 479, 478, 481, 480, 483, 482, 485, 484, 487, 486, 489, 488, 491, 490, 493, 492, 495, 494, 497, 496, 499, 498, 501, 500, 503, 502, 505, 504, 507, 506, 509, 508, 511, 510, 513, 512, 515, 514, 517, 516, 519, 518, 521, 520, 523, 522, 525, 524, 527, 526, 529, 528, 531, 530, 533, 532, 535, 534, 537, 536, 539, 538, 541, 540, 543, 542, 545, 544, 547, 546, 549, 548, 551, 550, 553, 552, 555, 554, 557, 556, 559, 558, 561, 560, 563, 562, 565, 564, 567, 566, 569, 568, 571, 570, 573, 572, 575, 574, 577, 576, 579, 578, 581, 580, 583, 582, 585, 584, 587, 586, 589, 588, 591, 590, 593, 592, 595, 594, 597, 596, 599, 598, 601, 600, 603, 602, 605, 604, 607, 606, 609, 608, 611, 610, 613, 612, 615, 614, 617, 616, 619, 618, 621, 620, 623, 622, 625, 624, 627, 626, 629, 628, 631, 630, 633, 632, 635, 634, 637, 636, 639, 638, 641, 640, 643, 642, 645, 644, 647, 646, 649, 648, 651, 650, 653, 652, 655, 654, 657, 656, 659, 658, 661, 660, 663, 662, 665, 664, 667, 666, 669, 668, 671, 670, 673, 672, 675, 674, 677, 676, 679, 678, 681, 680, 683, 682, 685, 684, 687, 686, 689, 688, 691, 690, 693, 692, 695, 694, 697, 696, 699, 698, 701, 700, 703, 702, 705, 704, 707, 706, 709, 708, 711, 710, 713, 712, 715, 714, 717, 716, 719, 718, 721, 720, 723, 722, 725, 724, 727, 726, 729, 728, 731, 730, 733, 732, 735, 734, 737, 736, 739, 738, 741, 740, 743, 742, 745, 744, 747, 746, 749, 748, 751, 750, 753, 752, 755, 754, 757, 756, 759, 758, 761, 760, 763, 762, 765, 764, 767, 766, 769, 768, 771, 770, 773, 772, 775, 774, 777, 776, 779, 778, 781, 780, 783, 782, 785, 784, 787, 786, 789, 788, 791, 790, 793, 792, 795, 794, 797, 796, 799, 798, 801, 800, 803, 802, 805, 804, 807, 806, 809, 808, 811, 810, 813, 812, 815, 814, 817, 816, 819, 818, 821, 820, 823, 822, 825, 824, 827, 826, 829, 828, 831, 830, 833, 832, 835, 834, 837, 836, 839, 838, 841, 840, 843, 842, 845, 844, 847, 846, 849, 848, 851, 850, 853, 852, 855, 854, 857, 856, 859, 858, 861, 860, 863, 862, 865, 864, 867, 866, 869, 868, 871, 870, 873, 872, 875, 874, 877, 876, 879, 878, 881, 880, 883, 882, 885, 884, 887, 886, 889, 888, 891, 890, 893, 892, 895, 894, 897, 896, 899, 898, 901, 900, 903, 902, 905, 904, 907, 906, 909, 908, 911, 910, 913, 912, 915, 914, 917, 916, 919, 918, 921, 920, 923, 922, 925, 924, 927, 926, 929, 928, 931, 930, 933, 932, 935, 934, 937, 936, 939, 938, 941, 940, 943, 942, 945, 944, 947, 946, 949, 948, 951, 950, 953, 952, 955, 954, 957, 956, 959, 958, 961, 960, 963, 962, 965, 964, 967, 966, 969, 968, 971, 970, 973, 972, 975, 974, 977, 976, 979, 978, 981, 980, 983, 982, 985, 984, 987, 986, 989, 988, 991, 990, 993, 992, 995, 994, 997, 996, 999, 998")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/66: Exception')
        print_exception()

    try:
        res = reverse_pairs_r(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176', '177', '178', '179', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191', '192', '193', '194', '195', '196', '197', '198', '199', '200', '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '211', '212', '213', '214', '215', '216', '217', '218', '219', '220', '221', '222', '223', '224', '225', '226', '227', '228', '229', '230', '231', '232', '233', '234', '235', '236', '237', '238', '239', '240', '241', '242', '243', '244', '245', '246', '247', '248', '249', '250', '251', '252', '253', '254', '255', '256', '257', '258', '259', '260', '261', '262', '263', '264', '265', '266', '267', '268', '269', '270', '271', '272', '273', '274', '275', '276', '277', '278', '279', '280', '281', '282', '283', '284', '285', '286', '287', '288', '289', '290', '291', '292', '293', '294', '295', '296', '297', '298', '299', '300', '301', '302', '303', '304', '305', '306', '307', '308', '309', '310', '311', '312', '313', '314', '315', '316', '317', '318', '319', '320', '321', '322', '323', '324', '325', '326', '327', '328', '329', '330', '331', '332', '333', '334', '335', '336', '337', '338', '339', '340', '341', '342', '343', '344', '345', '346', '347', '348', '349', '350', '351', '352', '353', '354', '355', '356', '357', '358', '359', '360', '361', '362', '363', '364', '365', '366', '367', '368', '369', '370', '371', '372', '373', '374', '375', '376', '377', '378', '379', '380', '381', '382', '383', '384', '385', '386', '387', '388', '389', '390', '391', '392', '393', '394', '395', '396', '397', '398', '399', '400', '401', '402', '403', '404', '405', '406', '407', '408', '409', '410', '411', '412', '413', '414', '415', '416', '417', '418', '419', '420', '421', '422', '423', '424', '425', '426', '427', '428', '429', '430', '431', '432', '433', '434', '435', '436', '437', '438', '439', '440', '441', '442', '443', '444', '445', '446', '447', '448', '449', '450', '451', '452', '453', '454', '455', '456', '457', '458', '459', '460', '461', '462', '463', '464', '465', '466', '467', '468', '469', '470', '471', '472', '473', '474', '475', '476', '477', '478', '479', '480', '481', '482', '483', '484', '485', '486', '487', '488', '489', '490', '491', '492', '493', '494', '495', '496', '497', '498', '499', '500', '501', '502', '503', '504', '505', '506', '507', '508', '509', '510', '511', '512', '513', '514', '515', '516', '517', '518', '519', '520', '521', '522', '523', '524', '525', '526', '527', '528', '529', '530', '531', '532', '533', '534', '535', '536', '537', '538', '539', '540', '541', '542', '543', '544', '545', '546', '547', '548', '549', '550', '551', '552', '553', '554', '555', '556', '557', '558', '559', '560', '561', '562', '563', '564', '565', '566', '567', '568', '569', '570', '571', '572', '573', '574', '575', '576', '577', '578', '579', '580', '581', '582', '583', '584', '585', '586', '587', '588', '589', '590', '591', '592', '593', '594', '595', '596', '597', '598', '599', '600', '601', '602', '603', '604', '605', '606', '607', '608', '609', '610', '611', '612', '613', '614', '615', '616', '617', '618', '619', '620', '621', '622', '623', '624', '625', '626', '627', '628', '629', '630', '631', '632', '633', '634', '635', '636', '637', '638', '639', '640', '641', '642', '643', '644', '645', '646', '647', '648', '649', '650', '651', '652', '653', '654', '655', '656', '657', '658', '659', '660', '661', '662', '663', '664', '665', '666', '667', '668', '669', '670', '671', '672', '673', '674', '675', '676', '677', '678', '679', '680', '681', '682', '683', '684', '685', '686', '687', '688', '689', '690', '691', '692', '693', '694', '695', '696', '697', '698', '699', '700', '701', '702', '703', '704', '705', '706', '707', '708', '709', '710', '711', '712', '713', '714', '715', '716', '717', '718', '719', '720', '721', '722', '723', '724', '725', '726', '727', '728', '729', '730', '731', '732', '733', '734', '735', '736', '737', '738', '739', '740', '741', '742', '743', '744', '745', '746', '747', '748', '749', '750', '751', '752', '753', '754', '755', '756', '757', '758', '759', '760', '761', '762', '763', '764', '765', '766', '767', '768', '769', '770', '771', '772', '773', '774', '775', '776', '777', '778', '779', '780', '781', '782', '783', '784', '785', '786', '787', '788', '789', '790', '791', '792', '793', '794', '795', '796', '797', '798', '799', '800', '801', '802', '803', '804', '805', '806', '807', '808', '809', '810', '811', '812', '813', '814', '815', '816', '817', '818', '819', '820', '821', '822', '823', '824', '825', '826', '827', '828', '829', '830', '831', '832', '833', '834', '835', '836', '837', '838', '839', '840', '841', '842', '843', '844', '845', '846', '847', '848', '849', '850', '851', '852', '853', '854', '855', '856', '857', '858', '859', '860', '861', '862', '863', '864', '865', '866', '867', '868', '869', '870', '871', '872', '873', '874', '875', '876', '877', '878', '879', '880', '881', '882', '883', '884', '885', '886', '887', '888', '889', '890', '891', '892', '893', '894', '895', '896', '897', '898', '899', '900', '901', '902', '903', '904', '905', '906', '907', '908', '909', '910', '911', '912', '913', '914', '915', '916', '917', '918', '919', '920', '921', '922', '923', '924', '925', '926', '927', '928', '929', '930', '931', '932', '933', '934', '935', '936', '937', '938', '939', '940', '941', '942', '943', '944', '945', '946', '947', '948', '949', '950', '951', '952', '953', '954', '955', '956', '957', '958', '959', '960', '961', '962', '963', '964', '965', '966', '967', '968', '969', '970', '971', '972', '973', '974', '975', '976', '977', '978', '979', '980', '981', '982', '983', '984', '985', '986', '987', '988', '989', '990', '991', '992', '993', '994', '995', '996', '997', '998', '999'])
        exp = ['1', '0', '3', '2', '5', '4', '7', '6', '9', '8', '11', '10', '13', '12', '15', '14', '17', '16', '19', '18', '21', '20', '23', '22', '25', '24', '27', '26', '29', '28', '31', '30', '33', '32', '35', '34', '37', '36', '39', '38', '41', '40', '43', '42', '45', '44', '47', '46', '49', '48', '51', '50', '53', '52', '55', '54', '57', '56', '59', '58', '61', '60', '63', '62', '65', '64', '67', '66', '69', '68', '71', '70', '73', '72', '75', '74', '77', '76', '79', '78', '81', '80', '83', '82', '85', '84', '87', '86', '89', '88', '91', '90', '93', '92', '95', '94', '97', '96', '99', '98', '101', '100', '103', '102', '105', '104', '107', '106', '109', '108', '111', '110', '113', '112', '115', '114', '117', '116', '119', '118', '121', '120', '123', '122', '125', '124', '127', '126', '129', '128', '131', '130', '133', '132', '135', '134', '137', '136', '139', '138', '141', '140', '143', '142', '145', '144', '147', '146', '149', '148', '151', '150', '153', '152', '155', '154', '157', '156', '159', '158', '161', '160', '163', '162', '165', '164', '167', '166', '169', '168', '171', '170', '173', '172', '175', '174', '177', '176', '179', '178', '181', '180', '183', '182', '185', '184', '187', '186', '189', '188', '191', '190', '193', '192', '195', '194', '197', '196', '199', '198', '201', '200', '203', '202', '205', '204', '207', '206', '209', '208', '211', '210', '213', '212', '215', '214', '217', '216', '219', '218', '221', '220', '223', '222', '225', '224', '227', '226', '229', '228', '231', '230', '233', '232', '235', '234', '237', '236', '239', '238', '241', '240', '243', '242', '245', '244', '247', '246', '249', '248', '251', '250', '253', '252', '255', '254', '257', '256', '259', '258', '261', '260', '263', '262', '265', '264', '267', '266', '269', '268', '271', '270', '273', '272', '275', '274', '277', '276', '279', '278', '281', '280', '283', '282', '285', '284', '287', '286', '289', '288', '291', '290', '293', '292', '295', '294', '297', '296', '299', '298', '301', '300', '303', '302', '305', '304', '307', '306', '309', '308', '311', '310', '313', '312', '315', '314', '317', '316', '319', '318', '321', '320', '323', '322', '325', '324', '327', '326', '329', '328', '331', '330', '333', '332', '335', '334', '337', '336', '339', '338', '341', '340', '343', '342', '345', '344', '347', '346', '349', '348', '351', '350', '353', '352', '355', '354', '357', '356', '359', '358', '361', '360', '363', '362', '365', '364', '367', '366', '369', '368', '371', '370', '373', '372', '375', '374', '377', '376', '379', '378', '381', '380', '383', '382', '385', '384', '387', '386', '389', '388', '391', '390', '393', '392', '395', '394', '397', '396', '399', '398', '401', '400', '403', '402', '405', '404', '407', '406', '409', '408', '411', '410', '413', '412', '415', '414', '417', '416', '419', '418', '421', '420', '423', '422', '425', '424', '427', '426', '429', '428', '431', '430', '433', '432', '435', '434', '437', '436', '439', '438', '441', '440', '443', '442', '445', '444', '447', '446', '449', '448', '451', '450', '453', '452', '455', '454', '457', '456', '459', '458', '461', '460', '463', '462', '465', '464', '467', '466', '469', '468', '471', '470', '473', '472', '475', '474', '477', '476', '479', '478', '481', '480', '483', '482', '485', '484', '487', '486', '489', '488', '491', '490', '493', '492', '495', '494', '497', '496', '499', '498', '501', '500', '503', '502', '505', '504', '507', '506', '509', '508', '511', '510', '513', '512', '515', '514', '517', '516', '519', '518', '521', '520', '523', '522', '525', '524', '527', '526', '529', '528', '531', '530', '533', '532', '535', '534', '537', '536', '539', '538', '541', '540', '543', '542', '545', '544', '547', '546', '549', '548', '551', '550', '553', '552', '555', '554', '557', '556', '559', '558', '561', '560', '563', '562', '565', '564', '567', '566', '569', '568', '571', '570', '573', '572', '575', '574', '577', '576', '579', '578', '581', '580', '583', '582', '585', '584', '587', '586', '589', '588', '591', '590', '593', '592', '595', '594', '597', '596', '599', '598', '601', '600', '603', '602', '605', '604', '607', '606', '609', '608', '611', '610', '613', '612', '615', '614', '617', '616', '619', '618', '621', '620', '623', '622', '625', '624', '627', '626', '629', '628', '631', '630', '633', '632', '635', '634', '637', '636', '639', '638', '641', '640', '643', '642', '645', '644', '647', '646', '649', '648', '651', '650', '653', '652', '655', '654', '657', '656', '659', '658', '661', '660', '663', '662', '665', '664', '667', '666', '669', '668', '671', '670', '673', '672', '675', '674', '677', '676', '679', '678', '681', '680', '683', '682', '685', '684', '687', '686', '689', '688', '691', '690', '693', '692', '695', '694', '697', '696', '699', '698', '701', '700', '703', '702', '705', '704', '707', '706', '709', '708', '711', '710', '713', '712', '715', '714', '717', '716', '719', '718', '721', '720', '723', '722', '725', '724', '727', '726', '729', '728', '731', '730', '733', '732', '735', '734', '737', '736', '739', '738', '741', '740', '743', '742', '745', '744', '747', '746', '749', '748', '751', '750', '753', '752', '755', '754', '757', '756', '759', '758', '761', '760', '763', '762', '765', '764', '767', '766', '769', '768', '771', '770', '773', '772', '775', '774', '777', '776', '779', '778', '781', '780', '783', '782', '785', '784', '787', '786', '789', '788', '791', '790', '793', '792', '795', '794', '797', '796', '799', '798', '801', '800', '803', '802', '805', '804', '807', '806', '809', '808', '811', '810', '813', '812', '815', '814', '817', '816', '819', '818', '821', '820', '823', '822', '825', '824', '827', '826', '829', '828', '831', '830', '833', '832', '835', '834', '837', '836', '839', '838', '841', '840', '843', '842', '845', '844', '847', '846', '849', '848', '851', '850', '853', '852', '855', '854', '857', '856', '859', '858', '861', '860', '863', '862', '865', '864', '867', '866', '869', '868', '871', '870', '873', '872', '875', '874', '877', '876', '879', '878', '881', '880', '883', '882', '885', '884', '887', '886', '889', '888', '891', '890', '893', '892', '895', '894', '897', '896', '899', '898', '901', '900', '903', '902', '905', '904', '907', '906', '909', '908', '911', '910', '913', '912', '915', '914', '917', '916', '919', '918', '921', '920', '923', '922', '925', '924', '927', '926', '929', '928', '931', '930', '933', '932', '935', '934', '937', '936', '939', '938', '941', '940', '943', '942', '945', '944', '947', '946', '949', '948', '951', '950', '953', '952', '955', '954', '957', '956', '959', '958', '961', '960', '963', '962', '965', '964', '967', '966', '969', '968', '971', '970', '973', '972', '975', '974', '977', '976', '979', '978', '981', '980', '983', '982', '985', '984', '987', '986', '989', '988', '991', '990', '993', '992', '995', '994', '997', '996', '999', '998']
        if res != exp:
            print("Fel i test 2b/67: reverse_pairs_r(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176', '177', '178', '179', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191', '192', '193', '194', '195', '196', '197', '198', '199', '200', '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '211', '212', '213', '214', '215', '216', '217', '218', '219', '220', '221', '222', '223', '224', '225', '226', '227', '228', '229', '230', '231', '232', '233', '234', '235', '236', '237', '238', '239', '240', '241', '242', '243', '244', '245', '246', '247', '248', '249', '250', '251', '252', '253', '254', '255', '256', '257', '258', '259', '260', '261', '262', '263', '264', '265', '266', '267', '268', '269', '270', '271', '272', '273', '274', '275', '276', '277', '278', '279', '280', '281', '282', '283', '284', '285', '286', '287', '288', '289', '290', '291', '292', '293', '294', '295', '296', '297', '298', '299', '300', '301', '302', '303', '304', '305', '306', '307', '308', '309', '310', '311', '312', '313', '314', '315', '316', '317', '318', '319', '320', '321', '322', '323', '324', '325', '326', '327', '328', '329', '330', '331', '332', '333', '334', '335', '336', '337', '338', '339', '340', '341', '342', '343', '344', '345', '346', '347', '348', '349', '350', '351', '352', '353', '354', '355', '356', '357', '358', '359', '360', '361', '362', '363', '364', '365', '366', '367', '368', '369', '370', '371', '372', '373', '374', '375', '376', '377', '378', '379', '380', '381', '382', '383', '384', '385', '386', '387', '388', '389', '390', '391', '392', '393', '394', '395', '396', '397', '398', '399', '400', '401', '402', '403', '404', '405', '406', '407', '408', '409', '410', '411', '412', '413', '414', '415', '416', '417', '418', '419', '420', '421', '422', '423', '424', '425', '426', '427', '428', '429', '430', '431', '432', '433', '434', '435', '436', '437', '438', '439', '440', '441', '442', '443', '444', '445', '446', '447', '448', '449', '450', '451', '452', '453', '454', '455', '456', '457', '458', '459', '460', '461', '462', '463', '464', '465', '466', '467', '468', '469', '470', '471', '472', '473', '474', '475', '476', '477', '478', '479', '480', '481', '482', '483', '484', '485', '486', '487', '488', '489', '490', '491', '492', '493', '494', '495', '496', '497', '498', '499', '500', '501', '502', '503', '504', '505', '506', '507', '508', '509', '510', '511', '512', '513', '514', '515', '516', '517', '518', '519', '520', '521', '522', '523', '524', '525', '526', '527', '528', '529', '530', '531', '532', '533', '534', '535', '536', '537', '538', '539', '540', '541', '542', '543', '544', '545', '546', '547', '548', '549', '550', '551', '552', '553', '554', '555', '556', '557', '558', '559', '560', '561', '562', '563', '564', '565', '566', '567', '568', '569', '570', '571', '572', '573', '574', '575', '576', '577', '578', '579', '580', '581', '582', '583', '584', '585', '586', '587', '588', '589', '590', '591', '592', '593', '594', '595', '596', '597', '598', '599', '600', '601', '602', '603', '604', '605', '606', '607', '608', '609', '610', '611', '612', '613', '614', '615', '616', '617', '618', '619', '620', '621', '622', '623', '624', '625', '626', '627', '628', '629', '630', '631', '632', '633', '634', '635', '636', '637', '638', '639', '640', '641', '642', '643', '644', '645', '646', '647', '648', '649', '650', '651', '652', '653', '654', '655', '656', '657', '658', '659', '660', '661', '662', '663', '664', '665', '666', '667', '668', '669', '670', '671', '672', '673', '674', '675', '676', '677', '678', '679', '680', '681', '682', '683', '684', '685', '686', '687', '688', '689', '690', '691', '692', '693', '694', '695', '696', '697', '698', '699', '700', '701', '702', '703', '704', '705', '706', '707', '708', '709', '710', '711', '712', '713', '714', '715', '716', '717', '718', '719', '720', '721', '722', '723', '724', '725', '726', '727', '728', '729', '730', '731', '732', '733', '734', '735', '736', '737', '738', '739', '740', '741', '742', '743', '744', '745', '746', '747', '748', '749', '750', '751', '752', '753', '754', '755', '756', '757', '758', '759', '760', '761', '762', '763', '764', '765', '766', '767', '768', '769', '770', '771', '772', '773', '774', '775', '776', '777', '778', '779', '780', '781', '782', '783', '784', '785', '786', '787', '788', '789', '790', '791', '792', '793', '794', '795', '796', '797', '798', '799', '800', '801', '802', '803', '804', '805', '806', '807', '808', '809', '810', '811', '812', '813', '814', '815', '816', '817', '818', '819', '820', '821', '822', '823', '824', '825', '826', '827', '828', '829', '830', '831', '832', '833', '834', '835', '836', '837', '838', '839', '840', '841', '842', '843', '844', '845', '846', '847', '848', '849', '850', '851', '852', '853', '854', '855', '856', '857', '858', '859', '860', '861', '862', '863', '864', '865', '866', '867', '868', '869', '870', '871', '872', '873', '874', '875', '876', '877', '878', '879', '880', '881', '882', '883', '884', '885', '886', '887', '888', '889', '890', '891', '892', '893', '894', '895', '896', '897', '898', '899', '900', '901', '902', '903', '904', '905', '906', '907', '908', '909', '910', '911', '912', '913', '914', '915', '916', '917', '918', '919', '920', '921', '922', '923', '924', '925', '926', '927', '928', '929', '930', '931', '932', '933', '934', '935', '936', '937', '938', '939', '940', '941', '942', '943', '944', '945', '946', '947', '948', '949', '950', '951', '952', '953', '954', '955', '956', '957', '958', '959', '960', '961', '962', '963', '964', '965', '966', '967', '968', '969', '970', '971', '972', '973', '974', '975', '976', '977', '978', '979', '980', '981', '982', '983', '984', '985', '986', '987', '988', '989', '990', '991', '992', '993', '994', '995', '996', '997', '998', '999'])")
            print("Korrekt svar: '1', '0', '3', '2', '5', '4', '7', '6', '9', '8', '11', '10', '13', '12', '15', '14', '17', '16', '19', '18', '21', '20', '23', '22', '25', '24', '27', '26', '29', '28', '31', '30', '33', '32', '35', '34', '37', '36', '39', '38', '41', '40', '43', '42', '45', '44', '47', '46', '49', '48', '51', '50', '53', '52', '55', '54', '57', '56', '59', '58', '61', '60', '63', '62', '65', '64', '67', '66', '69', '68', '71', '70', '73', '72', '75', '74', '77', '76', '79', '78', '81', '80', '83', '82', '85', '84', '87', '86', '89', '88', '91', '90', '93', '92', '95', '94', '97', '96', '99', '98', '101', '100', '103', '102', '105', '104', '107', '106', '109', '108', '111', '110', '113', '112', '115', '114', '117', '116', '119', '118', '121', '120', '123', '122', '125', '124', '127', '126', '129', '128', '131', '130', '133', '132', '135', '134', '137', '136', '139', '138', '141', '140', '143', '142', '145', '144', '147', '146', '149', '148', '151', '150', '153', '152', '155', '154', '157', '156', '159', '158', '161', '160', '163', '162', '165', '164', '167', '166', '169', '168', '171', '170', '173', '172', '175', '174', '177', '176', '179', '178', '181', '180', '183', '182', '185', '184', '187', '186', '189', '188', '191', '190', '193', '192', '195', '194', '197', '196', '199', '198', '201', '200', '203', '202', '205', '204', '207', '206', '209', '208', '211', '210', '213', '212', '215', '214', '217', '216', '219', '218', '221', '220', '223', '222', '225', '224', '227', '226', '229', '228', '231', '230', '233', '232', '235', '234', '237', '236', '239', '238', '241', '240', '243', '242', '245', '244', '247', '246', '249', '248', '251', '250', '253', '252', '255', '254', '257', '256', '259', '258', '261', '260', '263', '262', '265', '264', '267', '266', '269', '268', '271', '270', '273', '272', '275', '274', '277', '276', '279', '278', '281', '280', '283', '282', '285', '284', '287', '286', '289', '288', '291', '290', '293', '292', '295', '294', '297', '296', '299', '298', '301', '300', '303', '302', '305', '304', '307', '306', '309', '308', '311', '310', '313', '312', '315', '314', '317', '316', '319', '318', '321', '320', '323', '322', '325', '324', '327', '326', '329', '328', '331', '330', '333', '332', '335', '334', '337', '336', '339', '338', '341', '340', '343', '342', '345', '344', '347', '346', '349', '348', '351', '350', '353', '352', '355', '354', '357', '356', '359', '358', '361', '360', '363', '362', '365', '364', '367', '366', '369', '368', '371', '370', '373', '372', '375', '374', '377', '376', '379', '378', '381', '380', '383', '382', '385', '384', '387', '386', '389', '388', '391', '390', '393', '392', '395', '394', '397', '396', '399', '398', '401', '400', '403', '402', '405', '404', '407', '406', '409', '408', '411', '410', '413', '412', '415', '414', '417', '416', '419', '418', '421', '420', '423', '422', '425', '424', '427', '426', '429', '428', '431', '430', '433', '432', '435', '434', '437', '436', '439', '438', '441', '440', '443', '442', '445', '444', '447', '446', '449', '448', '451', '450', '453', '452', '455', '454', '457', '456', '459', '458', '461', '460', '463', '462', '465', '464', '467', '466', '469', '468', '471', '470', '473', '472', '475', '474', '477', '476', '479', '478', '481', '480', '483', '482', '485', '484', '487', '486', '489', '488', '491', '490', '493', '492', '495', '494', '497', '496', '499', '498', '501', '500', '503', '502', '505', '504', '507', '506', '509', '508', '511', '510', '513', '512', '515', '514', '517', '516', '519', '518', '521', '520', '523', '522', '525', '524', '527', '526', '529', '528', '531', '530', '533', '532', '535', '534', '537', '536', '539', '538', '541', '540', '543', '542', '545', '544', '547', '546', '549', '548', '551', '550', '553', '552', '555', '554', '557', '556', '559', '558', '561', '560', '563', '562', '565', '564', '567', '566', '569', '568', '571', '570', '573', '572', '575', '574', '577', '576', '579', '578', '581', '580', '583', '582', '585', '584', '587', '586', '589', '588', '591', '590', '593', '592', '595', '594', '597', '596', '599', '598', '601', '600', '603', '602', '605', '604', '607', '606', '609', '608', '611', '610', '613', '612', '615', '614', '617', '616', '619', '618', '621', '620', '623', '622', '625', '624', '627', '626', '629', '628', '631', '630', '633', '632', '635', '634', '637', '636', '639', '638', '641', '640', '643', '642', '645', '644', '647', '646', '649', '648', '651', '650', '653', '652', '655', '654', '657', '656', '659', '658', '661', '660', '663', '662', '665', '664', '667', '666', '669', '668', '671', '670', '673', '672', '675', '674', '677', '676', '679', '678', '681', '680', '683', '682', '685', '684', '687', '686', '689', '688', '691', '690', '693', '692', '695', '694', '697', '696', '699', '698', '701', '700', '703', '702', '705', '704', '707', '706', '709', '708', '711', '710', '713', '712', '715', '714', '717', '716', '719', '718', '721', '720', '723', '722', '725', '724', '727', '726', '729', '728', '731', '730', '733', '732', '735', '734', '737', '736', '739', '738', '741', '740', '743', '742', '745', '744', '747', '746', '749', '748', '751', '750', '753', '752', '755', '754', '757', '756', '759', '758', '761', '760', '763', '762', '765', '764', '767', '766', '769', '768', '771', '770', '773', '772', '775', '774', '777', '776', '779', '778', '781', '780', '783', '782', '785', '784', '787', '786', '789', '788', '791', '790', '793', '792', '795', '794', '797', '796', '799', '798', '801', '800', '803', '802', '805', '804', '807', '806', '809', '808', '811', '810', '813', '812', '815', '814', '817', '816', '819', '818', '821', '820', '823', '822', '825', '824', '827', '826', '829', '828', '831', '830', '833', '832', '835', '834', '837', '836', '839', '838', '841', '840', '843', '842', '845', '844', '847', '846', '849', '848', '851', '850', '853', '852', '855', '854', '857', '856', '859', '858', '861', '860', '863', '862', '865', '864', '867', '866', '869', '868', '871', '870', '873', '872', '875', '874', '877', '876', '879', '878', '881', '880', '883', '882', '885', '884', '887', '886', '889', '888', '891', '890', '893', '892', '895', '894', '897', '896', '899', '898', '901', '900', '903', '902', '905', '904', '907', '906', '909', '908', '911', '910', '913', '912', '915', '914', '917', '916', '919', '918', '921', '920', '923', '922', '925', '924', '927', '926', '929', '928', '931', '930', '933', '932', '935', '934', '937', '936', '939', '938', '941', '940', '943', '942', '945', '944', '947', '946', '949', '948', '951', '950', '953', '952', '955', '954', '957', '956', '959', '958', '961', '960', '963', '962', '965', '964', '967', '966', '969', '968', '971', '970', '973', '972', '975', '974', '977', '976', '979', '978', '981', '980', '983', '982', '985', '984', '987', '986', '989', '988', '991', '990', '993', '992', '995', '994', '997', '996', '999', '998'")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/67: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []])
        exp = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        if res != exp:
            print("Fel i test 2b/68: reverse_pairs_r([[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []])")
            print("Korrekt svar: [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/68: Exception')
        print_exception()

    try:
        res = reverse_pairs_r(['', '', '', '', '', '', '', '', ''])
        exp = ['', '', '', '', '', '', '', '', '']
        if res != exp:
            print("Fel i test 2b/69: reverse_pairs_r(['', '', '', '', '', '', '', '', ''])")
            print("Korrekt svar: '', '', '', '', '', '', '', '', ''")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/69: Exception')
        print_exception()

    try:
        res = reverse_pairs_r(['', '', '', '', '', '', '', '', '', ''])
        exp = ['', '', '', '', '', '', '', '', '', '']
        if res != exp:
            print("Fel i test 2b/70: reverse_pairs_r(['', '', '', '', '', '', '', '', '', ''])")
            print("Korrekt svar: '', '', '', '', '', '', '', '', '', ''")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/70: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
        exp = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        if res != exp:
            print("Fel i test 2b/71: reverse_pairs_r([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])")
            print("Korrekt svar: ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/71: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
        exp = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        if res != exp:
            print("Fel i test 2b/72: reverse_pairs_r([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])")
            print("Korrekt svar: ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/72: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([1, 1, 1, 1, 1, 1, 1, 1, 1])
        exp = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        if res != exp:
            print("Fel i test 2b/73: reverse_pairs_r([1, 1, 1, 1, 1, 1, 1, 1, 1])")
            print("Korrekt svar: 1, 1, 1, 1, 1, 1, 1, 1, 1")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/73: Exception')
        print_exception()

    try:
        res = reverse_pairs_r([2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
        exp = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        if res != exp:
            print("Fel i test 2b/74: reverse_pairs_r([2, 2, 2, 2, 2, 2, 2, 2, 2, 2])")
            print("Korrekt svar: 2, 2, 2, 2, 2, 2, 2, 2, 2, 2")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 2b/74: Exception')
        print_exception()


    print('Klar med tester fÃ¶r uppgift 2b')
    print()


def test_3():
    print('PÃ¥bÃ¶rjar tester fÃ¶r uppgift 3')

    try:
        res = doubled_odds([1, 2, 3])
        exp = [2, 2, 6]
        if res != exp:
            print("Fel i test 3/1: doubled_odds([1, 2, 3])")
            print("Korrekt svar: 2, 2, 6")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/1: Exception')
        print_exception()

    try:
        res = doubled_odds([-1, [2, 3], ['Hi', 4, [7]]])
        exp = [-2, [2, 6], ['Hi', 4, [14]]]
        if res != exp:
            print("Fel i test 3/2: doubled_odds([-1, [2, 3], ['Hi', 4, [7]]])")
            print("Korrekt svar: -2, [2, 6], ['Hi', 4, [14]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/2: Exception')
        print_exception()

    try:
        res = doubled_odds([-1, [2, 3], ('Hi', 4, [7])])
        exp = [-2, [2, 6], ('Hi', 4, [7])]
        if res != exp:
            print("Fel i test 3/3: doubled_odds([-1, [2, 3], ('Hi', 4, [7])])")
            print("Korrekt svar: -2, [2, 6], ('Hi', 4, [7])")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/3: Exception')
        print_exception()

    try:
        res = doubled_odds([1])
        exp = [2]
        if res != exp:
            print("Fel i test 3/4: doubled_odds([1])")
            print("Korrekt svar: 2")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/4: Exception')
        print_exception()

    try:
        res = doubled_odds(['a'])
        exp = ['a']
        if res != exp:
            print("Fel i test 3/5: doubled_odds(['a'])")
            print("Korrekt svar: 'a'")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/5: Exception')
        print_exception()

    try:
        res = doubled_odds([0.1])
        exp = [0.1]
        if res != exp:
            print("Fel i test 3/6: doubled_odds([0.1])")
            print("Korrekt svar: 0.1")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/6: Exception')
        print_exception()

    try:
        res = doubled_odds([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
        exp = [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90, 182, 92, 186, 94, 190, 96, 194, 98, 198]
        if res != exp:
            print("Fel i test 3/7: doubled_odds([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])")
            print("Korrekt svar: 0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90, 182, 92, 186, 94, 190, 96, 194, 98, 198")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/7: Exception')
        print_exception()

    try:
        res = doubled_odds([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        exp = [-10, -18, -8, -14, -6, -10, -4, -6, -2, -2, 0, 2, 2, 6, 4, 10, 6, 14, 8, 18]
        if res != exp:
            print("Fel i test 3/8: doubled_odds([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])")
            print("Korrekt svar: -10, -18, -8, -14, -6, -10, -4, -6, -2, -2, 0, 2, 2, 6, 4, 10, 6, 14, 8, 18")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/8: Exception')
        print_exception()

    try:
        res = doubled_odds([5, 467, 123, 4567, 878, 345, 89, 90, 78])
        exp = [10, 934, 246, 9134, 878, 690, 178, 90, 78]
        if res != exp:
            print("Fel i test 3/9: doubled_odds([5, 467, 123, 4567, 878, 345, 89, 90, 78])")
            print("Korrekt svar: 10, 934, 246, 9134, 878, 690, 178, 90, 78")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/9: Exception')
        print_exception()

    try:
        res = doubled_odds([0])
        exp = [0]
        if res != exp:
            print("Fel i test 3/10: doubled_odds([0])")
            print("Korrekt svar: 0")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/10: Exception')
        print_exception()

    try:
        res = doubled_odds([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        exp = [0, 2, 2, 6, 4, 10, 6, 14, 8, 18]
        if res != exp:
            print("Fel i test 3/11: doubled_odds([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])")
            print("Korrekt svar: 0, 2, 2, 6, 4, 10, 6, 14, 8, 18")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/11: Exception')
        print_exception()

    try:
        res = doubled_odds([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
        exp = [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90, 182, 92, 186, 94, 190, 96, 194, 98, 198]
        if res != exp:
            print("Fel i test 3/12: doubled_odds([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])")
            print("Korrekt svar: 0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90, 182, 92, 186, 94, 190, 96, 194, 98, 198")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/12: Exception')
        print_exception()

    try:
        res = doubled_odds([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9])
        exp = [10, 18, 8, 14, 6, 10, 4, 6, 2, 2, 0, -2, -2, -6, -4, -10, -6, -14, -8, -18]
        if res != exp:
            print("Fel i test 3/13: doubled_odds([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9])")
            print("Korrekt svar: 10, 18, 8, 14, 6, 10, 4, 6, 2, 2, 0, -2, -2, -6, -4, -10, -6, -14, -8, -18")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/13: Exception')
        print_exception()

    try:
        res = doubled_odds([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
        exp = [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2]
        if res != exp:
            print("Fel i test 3/14: doubled_odds([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])")
            print("Korrekt svar: 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/14: Exception')
        print_exception()

    try:
        res = doubled_odds([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
        exp = [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2]
        if res != exp:
            print("Fel i test 3/15: doubled_odds([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])")
            print("Korrekt svar: 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/15: Exception')
        print_exception()

    try:
        res = doubled_odds([0, 11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220, 231, 242, 253, 264, 275, 286, 297, 308, 319, 330, 341, 352, 363, 374, 385, 396, 407, 418, 429, 440, 451, 462, 473, 484, 495, 506, 517, 528, 539, 550, 561, 572, 583, 594, 605, 616, 627, 638, 649, 660, 671, 682, 693, 704, 715, 726, 737, 748, 759, 770, 781, 792, 803, 814, 825, 836, 847, 858, 869, 880, 891, 902, 913, 924, 935, 946, 957, 968, 979, 990])
        exp = [0, 22, 22, 66, 44, 110, 66, 154, 88, 198, 110, 242, 132, 286, 154, 330, 176, 374, 198, 418, 220, 462, 242, 506, 264, 550, 286, 594, 308, 638, 330, 682, 352, 726, 374, 770, 396, 814, 418, 858, 440, 902, 462, 946, 484, 990, 506, 1034, 528, 1078, 550, 1122, 572, 1166, 594, 1210, 616, 1254, 638, 1298, 660, 1342, 682, 1386, 704, 1430, 726, 1474, 748, 1518, 770, 1562, 792, 1606, 814, 1650, 836, 1694, 858, 1738, 880, 1782, 902, 1826, 924, 1870, 946, 1914, 968, 1958, 990]
        if res != exp:
            print("Fel i test 3/16: doubled_odds([0, 11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220, 231, 242, 253, 264, 275, 286, 297, 308, 319, 330, 341, 352, 363, 374, 385, 396, 407, 418, 429, 440, 451, 462, 473, 484, 495, 506, 517, 528, 539, 550, 561, 572, 583, 594, 605, 616, 627, 638, 649, 660, 671, 682, 693, 704, 715, 726, 737, 748, 759, 770, 781, 792, 803, 814, 825, 836, 847, 858, 869, 880, 891, 902, 913, 924, 935, 946, 957, 968, 979, 990])")
            print("Korrekt svar: 0, 22, 22, 66, 44, 110, 66, 154, 88, 198, 110, 242, 132, 286, 154, 330, 176, 374, 198, 418, 220, 462, 242, 506, 264, 550, 286, 594, 308, 638, 330, 682, 352, 726, 374, 770, 396, 814, 418, 858, 440, 902, 462, 946, 484, 990, 506, 1034, 528, 1078, 550, 1122, 572, 1166, 594, 1210, 616, 1254, 638, 1298, 660, 1342, 682, 1386, 704, 1430, 726, 1474, 748, 1518, 770, 1562, 792, 1606, 814, 1650, 836, 1694, 858, 1738, 880, 1782, 902, 1826, 924, 1870, 946, 1914, 968, 1958, 990")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/16: Exception')
        print_exception()

    try:
        res = doubled_odds(['1', '2', '3', '4', '5'])
        exp = ['1', '2', '3', '4', '5']
        if res != exp:
            print("Fel i test 3/17: doubled_odds(['1', '2', '3', '4', '5'])")
            print("Korrekt svar: '1', '2', '3', '4', '5'")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/17: Exception')
        print_exception()

    try:
        res = doubled_odds(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
        exp = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        if res != exp:
            print("Fel i test 3/18: doubled_odds(['a', 'b', 'c', 'd', 'e', 'f', 'g'])")
            print("Korrekt svar: 'a', 'b', 'c', 'd', 'e', 'f', 'g'")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/18: Exception')
        print_exception()

    try:
        res = doubled_odds(['Ã¥', 'Ã¤', 'Ã¶', 'Ã¢', 'Ã´', 'Ãª', 'Ã¡', 'Ã³', 'Ã©'])
        exp = ['Ã¥', 'Ã¤', 'Ã¶', 'Ã¢', 'Ã´', 'Ãª', 'Ã¡', 'Ã³', 'Ã©']
        if res != exp:
            print("Fel i test 3/19: doubled_odds(['Ã¥', 'Ã¤', 'Ã¶', 'Ã¢', 'Ã´', 'Ãª', 'Ã¡', 'Ã³', 'Ã©'])")
            print("Korrekt svar: 'Ã¥', 'Ã¤', 'Ã¶', 'Ã¢', 'Ã´', 'Ãª', 'Ã¡', 'Ã³', 'Ã©'")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/19: Exception')
        print_exception()

    try:
        res = doubled_odds(['', '', '', ''])
        exp = ['', '', '', '']
        if res != exp:
            print("Fel i test 3/20: doubled_odds(['', '', '', ''])")
            print("Korrekt svar: '', '', '', ''")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/20: Exception')
        print_exception()

    try:
        res = doubled_odds([' ', '', ' ', ''])
        exp = [' ', '', ' ', '']
        if res != exp:
            print("Fel i test 3/21: doubled_odds([' ', '', ' ', ''])")
            print("Korrekt svar: ' ', '', ' ', ''")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/21: Exception')
        print_exception()

    try:
        res = doubled_odds(['nÃ¥gra', 'strÃ¤ngar', 'av', 'olika', 'lÃ¤ngd', 'i', 'hav', 'totalfÃ¶rstÃ¶rt', 'frÃ¥n', 'laxmassor'])
        exp = ['nÃ¥gra', 'strÃ¤ngar', 'av', 'olika', 'lÃ¤ngd', 'i', 'hav', 'totalfÃ¶rstÃ¶rt', 'frÃ¥n', 'laxmassor']
        if res != exp:
            print("Fel i test 3/22: doubled_odds(['nÃ¥gra', 'strÃ¤ngar', 'av', 'olika', 'lÃ¤ngd', 'i', 'hav', 'totalfÃ¶rstÃ¶rt', 'frÃ¥n', 'laxmassor'])")
            print("Korrekt svar: 'nÃ¥gra', 'strÃ¤ngar', 'av', 'olika', 'lÃ¤ngd', 'i', 'hav', 'totalfÃ¶rstÃ¶rt', 'frÃ¥n', 'laxmassor'")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/22: Exception')
        print_exception()

    try:
        res = doubled_odds([' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', ''])
        exp = [' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '']
        if res != exp:
            print("Fel i test 3/23: doubled_odds([' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', ''])")
            print("Korrekt svar: ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', '', ' ', '', ''")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/23: Exception')
        print_exception()

    try:
        res = doubled_odds(['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '\x7f', '\x80', '\x81', '\x82', '\x83', '\x84', '\x85', '\x86', '\x87', '\x88', '\x89', '\x8a', '\x8b', '\x8c', '\x8d', '\x8e', '\x8f', '\x90', '\x91', '\x92', '\x93', '\x94', '\x95'])
        exp = ['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '\x7f', '\x80', '\x81', '\x82', '\x83', '\x84', '\x85', '\x86', '\x87', '\x88', '\x89', '\x8a', '\x8b', '\x8c', '\x8d', '\x8e', '\x8f', '\x90', '\x91', '\x92', '\x93', '\x94', '\x95']
        if res != exp:
            print("Fel i test 3/24: doubled_odds([\'\\x00\', \'\\x01\', \'\\x02\', \'\\x03\', \'\\x04\', \'\\x05\', \'\\x06\', \'\\x07\', \'\\x08\', \'\\t\', \'\\n\', \'\\x0b\', \'\\x0c\', \'\\r\', \'\\x0e\', \'\\x0f\', \'\\x10\', \'\\x11\', \'\\x12\', \'\\x13\', \'\\x14\', \'\\x15\', \'\\x16\', \'\\x17\', \'\\x18\', \'\\x19\', \'\\x1a\', \'\\x1b\', \'\\x1c\', \'\\x1d\', \'\\x1e\', \'\\x1f\', \' \', \'!\', \'\"\', \'#\', \'$\', \'%\', \'&\', \"\'\", \'(\', \')\', \'*\', \'+\', \',\', \'-\', \'.\', \'/\', \'0\', \'1\', \'2\', \'3\', \'4\', \'5\', \'6\', \'7\', \'8\', \'9\', \':\', \';\', \'<\', \'=\', \'>\', \'?\', \'@\', \'A\', \'B\', \'C\', \'D\', \'E\', \'F\', \'G\', \'H\', \'I\', \'J\', \'K\', \'L\', \'M\', \'N\', \'O\', \'P\', \'Q\', \'R\', \'S\', \'T\', \'U\', \'V\', \'W\', \'X\', \'Y\', \'Z\', \'[\', \'\\\\\', \']\', \'^\', \'_\', \'`\', \'a\', \'b\', \'c\', \'d\', \'e\', \'f\', \'g\', \'h\', \'i\', \'j\', \'k\', \'l\', \'m\', \'n\', \'o\', \'p\', \'q\', \'r\', \'s\', \'t\', \'u\', \'v\', \'w\', \'x\', \'y\', \'z\', \'{\', \'|\', \'}\', \'~\', \'\\x7f\', \'\\x80\', \'\\x81\', \'\\x82\', \'\\x83\', \'\\x84\', \'\\x85\', \'\\x86\', \'\\x87\', \'\\x88\', \'\\x89\', \'\\x8a\', \'\\x8b\', \'\\x8c\', \'\\x8d\', \'\\x8e\', \'\\x8f\', \'\\x90\', \'\\x91\', \'\\x92\', \'\\x93\', \'\\x94\', \'\\x95\'])")
            print("Korrekt svar: '\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', ' ', '!', '\"', '#', '$', '%', '&', \"'\", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '\x7f', '\x80', '\x81', '\x82', '\x83', '\x84', '\x85', '\x86', '\x87', '\x88', '\x89', '\x8a', '\x8b', '\x8c', '\x8d', '\x8e', '\x8f', '\x90', '\x91', '\x92', '\x93', '\x94', '\x95'")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/24: Exception')
        print_exception()

    try:
        res = doubled_odds(['', '\x01', '\x02\x02', '\x03\x03\x03', '\x04\x04\x04\x04', '\x05\x05\x05\x05\x05', '\x06\x06\x06\x06\x06\x06', '\x07\x07\x07\x07\x07\x07\x07', '\x08\x08\x08\x08\x08\x08\x08\x08', '\t\t\t\t\t\t\t\t\t', '\n\n\n\n\n\n\n\n\n\n', '\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b', '\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c', '\r\r\r\r\r\r\r\r\r\r\r\r\r', '\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e', '\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f', '\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10', '\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11', '\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12', '\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13', '\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14', '\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15', '\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16', '\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17', '\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18', '\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19', '\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a', '\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b', '\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c', '\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d', '\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e', '\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f', '                                ', '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', '""""""""""""""""""""""""""""""""""', '###################################', '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$', '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%', '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&', "'''''''''''''''''''''''''''''''''''''''", '((((((((((((((((((((((((((((((((((((((((', ')))))))))))))))))))))))))))))))))))))))))', '******************************************', '+++++++++++++++++++++++++++++++++++++++++++', ',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,', '---------------------------------------------', '..............................................', '///////////////////////////////////////////////', '000000000000000000000000000000000000000000000000', '1111111111111111111111111111111111111111111111111', '22222222222222222222222222222222222222222222222222', '333333333333333333333333333333333333333333333333333', '4444444444444444444444444444444444444444444444444444', '55555555555555555555555555555555555555555555555555555', '666666666666666666666666666666666666666666666666666666', '7777777777777777777777777777777777777777777777777777777', '88888888888888888888888888888888888888888888888888888888', '999999999999999999999999999999999999999999999999999999999', '::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', ';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;', '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<', '=============================================================', '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', '???????????????????????????????????????????????????????????????', '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB', 'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC', 'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD', 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE', 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF', 'GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG', 'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH', 'IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII', 'JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ', 'KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK', 'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL', 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM', 'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN', 'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO', 'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP', 'QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ', 'RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR', 'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS', 'TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT', 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU', 'VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV', 'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY', 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ', '[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[', '\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\', ']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]', '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^', '_______________________________________________________________________________________________', '````````````````````````````````````````````````````````````````````````````````````````````````', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb', 'ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'])
        exp = ['', '\x01', '\x02\x02', '\x03\x03\x03', '\x04\x04\x04\x04', '\x05\x05\x05\x05\x05', '\x06\x06\x06\x06\x06\x06', '\x07\x07\x07\x07\x07\x07\x07', '\x08\x08\x08\x08\x08\x08\x08\x08', '\t\t\t\t\t\t\t\t\t', '\n\n\n\n\n\n\n\n\n\n', '\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b', '\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c', '\r\r\r\r\r\r\r\r\r\r\r\r\r', '\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e', '\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f', '\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10', '\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11', '\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12', '\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13', '\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14', '\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15', '\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16', '\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17', '\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18', '\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19', '\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a', '\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b', '\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c', '\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d', '\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e', '\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f', '                                ', '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', '""""""""""""""""""""""""""""""""""', '###################################', '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$', '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%', '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&', "'''''''''''''''''''''''''''''''''''''''", '((((((((((((((((((((((((((((((((((((((((', ')))))))))))))))))))))))))))))))))))))))))', '******************************************', '+++++++++++++++++++++++++++++++++++++++++++', ',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,', '---------------------------------------------', '..............................................', '///////////////////////////////////////////////', '000000000000000000000000000000000000000000000000', '1111111111111111111111111111111111111111111111111', '22222222222222222222222222222222222222222222222222', '333333333333333333333333333333333333333333333333333', '4444444444444444444444444444444444444444444444444444', '55555555555555555555555555555555555555555555555555555', '666666666666666666666666666666666666666666666666666666', '7777777777777777777777777777777777777777777777777777777', '88888888888888888888888888888888888888888888888888888888', '999999999999999999999999999999999999999999999999999999999', '::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', ';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;', '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<', '=============================================================', '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', '???????????????????????????????????????????????????????????????', '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB', 'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC', 'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD', 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE', 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF', 'GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG', 'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH', 'IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII', 'JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ', 'KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK', 'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL', 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM', 'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN', 'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO', 'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP', 'QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ', 'RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR', 'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS', 'TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT', 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU', 'VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV', 'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY', 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ', '[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[', '\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\', ']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]', '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^', '_______________________________________________________________________________________________', '````````````````````````````````````````````````````````````````````````````````````````````````', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb', 'ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc']
        if res != exp:
            print("Fel i test 3/25: doubled_odds([\'\', \'\\x01\', \'\\x02\\x02\', \'\\x03\\x03\\x03\', \'\\x04\\x04\\x04\\x04\', \'\\x05\\x05\\x05\\x05\\x05\', \'\\x06\\x06\\x06\\x06\\x06\\x06\', \'\\x07\\x07\\x07\\x07\\x07\\x07\\x07\', \'\\x08\\x08\\x08\\x08\\x08\\x08\\x08\\x08\', \'\\t\\t\\t\\t\\t\\t\\t\\t\\t\', \'\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\', \'\\x0b\\x0b\\x0b\\x0b\\x0b\\x0b\\x0b\\x0b\\x0b\\x0b\\x0b\', \'\\x0c\\x0c\\x0c\\x0c\\x0c\\x0c\\x0c\\x0c\\x0c\\x0c\\x0c\\x0c\', \'\\r\\r\\r\\r\\r\\r\\r\\r\\r\\r\\r\\r\\r\', \'\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\\x0e\', \'\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\\x0f\', \'\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\\x10\', \'\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\\x11\', \'\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\\x12\', \'\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\\x13\', \'\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\\x14\', \'\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\\x15\', \'\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\\x16\', \'\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\\x17\', \'\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\\x18\', \'\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\\x19\', \'\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\\x1a\', \'\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\\x1b\', \'\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\\x1c\', \'\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\\x1d\', \'\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\\x1e\', \'\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\\x1f\', \'                                \', \'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\', \'\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\', \'###################################\', \'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\', \'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\', \'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\', \"\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\", \'((((((((((((((((((((((((((((((((((((((((\', \')))))))))))))))))))))))))))))))))))))))))\', \'******************************************\', \'+++++++++++++++++++++++++++++++++++++++++++\', \',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\', \'---------------------------------------------\', \'..............................................\', \'///////////////////////////////////////////////\', \'000000000000000000000000000000000000000000000000\', \'1111111111111111111111111111111111111111111111111\', \'22222222222222222222222222222222222222222222222222\', \'333333333333333333333333333333333333333333333333333\', \'4444444444444444444444444444444444444444444444444444\', \'55555555555555555555555555555555555555555555555555555\', \'666666666666666666666666666666666666666666666666666666\', \'7777777777777777777777777777777777777777777777777777777\', \'88888888888888888888888888888888888888888888888888888888\', \'999999999999999999999999999999999999999999999999999999999\', \'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\', \';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\', \'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\', \'=============================================================\', \'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\', \'???????????????????????????????????????????????????????????????\', \'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\', \'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\', \'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB\', \'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC\', \'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD\', \'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE\', \'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF\', \'GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG\', \'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\', \'IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII\', \'JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ\', \'KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK\', \'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL\', \'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\', \'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\', \'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\', \'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP\', \'QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ\', \'RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR\', \'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS\', \'TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT\', \'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU\', \'VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV\', \'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\', \'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\', \'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY\', \'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ\', \'[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[\', \'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\', \']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]\', \'^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\', \'_______________________________________________________________________________________________\', \'````````````````````````````````````````````````````````````````````````````````````````````````\', \'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\', \'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\', \'ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc\'])")
            print("Korrekt svar: '', '\x01', '\x02\x02', '\x03\x03\x03', '\x04\x04\x04\x04', '\x05\x05\x05\x05\x05', '\x06\x06\x06\x06\x06\x06', '\x07\x07\x07\x07\x07\x07\x07', '\x08\x08\x08\x08\x08\x08\x08\x08', '\t\t\t\t\t\t\t\t\t', '\n\n\n\n\n\n\n\n\n\n', '\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b', '\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c', '\r\r\r\r\r\r\r\r\r\r\r\r\r', '\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e', '\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f', '\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10', '\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11', '\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12\x12', '\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13\x13', '\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14', '\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15\x15', '\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16\x16', '\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17\x17', '\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18', '\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19\x19', '\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a\x1a', '\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b\x1b', '\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c\x1c', '\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d\x1d', '\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e\x1e', '\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f', '                                ', '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', '\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"', '###################################', '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$', '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%', '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&', \"'''''''''''''''''''''''''''''''''''''''\", '((((((((((((((((((((((((((((((((((((((((', ')))))))))))))))))))))))))))))))))))))))))', '******************************************', '+++++++++++++++++++++++++++++++++++++++++++', ',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,', '---------------------------------------------', '..............................................', '///////////////////////////////////////////////', '000000000000000000000000000000000000000000000000', '1111111111111111111111111111111111111111111111111', '22222222222222222222222222222222222222222222222222', '333333333333333333333333333333333333333333333333333', '4444444444444444444444444444444444444444444444444444', '55555555555555555555555555555555555555555555555555555', '666666666666666666666666666666666666666666666666666666', '7777777777777777777777777777777777777777777777777777777', '88888888888888888888888888888888888888888888888888888888', '999999999999999999999999999999999999999999999999999999999', '::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', ';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;', '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<', '=============================================================', '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', '???????????????????????????????????????????????????????????????', '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB', 'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC', 'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD', 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE', 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF', 'GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG', 'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH', 'IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII', 'JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ', 'KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK', 'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL', 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM', 'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN', 'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO', 'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP', 'QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ', 'RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR', 'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS', 'TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT', 'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU', 'VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV', 'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY', 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ', '[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[', '\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\', ']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]', '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^', '_______________________________________________________________________________________________', '````````````````````````````````````````````````````````````````````````````````````````````````', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb', 'ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/25: Exception')
        print_exception()

    try:
        res = doubled_odds([0.0, 1.0, 2.0])
        exp = [0.0, 1.0, 2.0]
        if res != exp:
            print("Fel i test 3/26: doubled_odds([0.0, 1.0, 2.0])")
            print("Korrekt svar: 0.0, 1.0, 2.0")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/26: Exception')
        print_exception()

    try:
        res = doubled_odds([1e-06, 0.123456789, 0.111111111, 123.3])
        exp = [1e-06, 0.123456789, 0.111111111, 123.3]
        if res != exp:
            print("Fel i test 3/27: doubled_odds([1e-06, 0.123456789, 0.111111111, 123.3])")
            print("Korrekt svar: 1e-06, 0.123456789, 0.111111111, 123.3")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/27: Exception')
        print_exception()

    try:
        res = doubled_odds([-25.0, -24.0, -23.0, -22.0, -21.0, -20.0, -19.0, -18.0, -17.0, -16.0, -15.0, -14.0, -13.0, -12.0, -11.0, -10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0])
        exp = [-25.0, -24.0, -23.0, -22.0, -21.0, -20.0, -19.0, -18.0, -17.0, -16.0, -15.0, -14.0, -13.0, -12.0, -11.0, -10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0]
        if res != exp:
            print("Fel i test 3/28: doubled_odds([-25.0, -24.0, -23.0, -22.0, -21.0, -20.0, -19.0, -18.0, -17.0, -16.0, -15.0, -14.0, -13.0, -12.0, -11.0, -10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0])")
            print("Korrekt svar: -25.0, -24.0, -23.0, -22.0, -21.0, -20.0, -19.0, -18.0, -17.0, -16.0, -15.0, -14.0, -13.0, -12.0, -11.0, -10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/28: Exception')
        print_exception()

    try:
        res = doubled_odds([-1.5e-06, -1.49e-06, -1.48e-06, -1.47e-06, -1.46e-06, -1.45e-06, -1.44e-06, -1.43e-06, -1.42e-06, -1.41e-06, -1.4e-06, -1.39e-06, -1.38e-06, -1.37e-06, -1.36e-06, -1.35e-06, -1.34e-06, -1.33e-06, -1.32e-06, -1.31e-06, -1.3e-06, -1.29e-06, -1.28e-06, -1.27e-06, -1.26e-06, -1.25e-06, -1.24e-06, -1.23e-06, -1.22e-06, -1.21e-06, -1.2e-06, -1.19e-06, -1.18e-06, -1.17e-06, -1.16e-06, -1.15e-06, -1.14e-06, -1.13e-06, -1.12e-06, -1.11e-06, -1.1e-06, -1.09e-06, -1.08e-06, -1.07e-06, -1.06e-06, -1.05e-06, -1.04e-06, -1.03e-06, -1.02e-06, -1.01e-06, -1e-06, -9.9e-07, -9.8e-07, -9.7e-07, -9.6e-07, -9.5e-07, -9.4e-07, -9.3e-07, -9.2e-07, -9.1e-07, -9e-07, -8.9e-07, -8.8e-07, -8.7e-07, -8.6e-07, -8.5e-07, -8.4e-07, -8.3e-07, -8.2e-07, -8.1e-07, -8e-07, -7.9e-07, -7.8e-07, -7.7e-07, -7.6e-07, -7.5e-07, -7.4e-07, -7.3e-07, -7.2e-07, -7.1e-07, -7e-07, -6.9e-07, -6.8e-07, -6.7e-07, -6.6e-07, -6.5e-07, -6.4e-07, -6.3e-07, -6.2e-07, -6.1e-07, -6e-07, -5.9e-07, -5.8e-07, -5.7e-07, -5.6e-07, -5.5e-07, -5.4e-07, -5.3e-07, -5.2e-07, -5.1e-07, -5e-07, -4.9e-07, -4.8e-07, -4.7e-07, -4.6e-07, -4.5e-07, -4.4e-07, -4.3e-07, -4.2e-07, -4.1e-07, -4e-07, -3.9e-07, -3.8e-07, -3.7e-07, -3.6e-07, -3.5e-07, -3.4e-07, -3.3e-07, -3.2e-07, -3.1e-07, -3e-07, -2.9e-07, -2.8e-07, -2.7e-07, -2.6e-07, -2.5e-07, -2.4e-07, -2.3e-07, -2.2e-07, -2.1e-07, -2e-07, -1.9e-07, -1.8e-07, -1.7e-07, -1.6e-07, -1.5e-07, -1.4e-07, -1.3e-07, -1.2e-07, -1.1e-07, -1e-07, -9e-08, -8e-08, -7e-08, -6e-08, -5e-08, -4e-08, -3e-08, -2e-08, -1e-08, 0.0, 1e-08, 2e-08, 3e-08, 4e-08, 5e-08, 6e-08, 7e-08, 8e-08, 9e-08, 1e-07, 1.1e-07, 1.2e-07, 1.3e-07, 1.4e-07, 1.5e-07, 1.6e-07, 1.7e-07, 1.8e-07, 1.9e-07, 2e-07, 2.1e-07, 2.2e-07, 2.3e-07, 2.4e-07, 2.5e-07, 2.6e-07, 2.7e-07, 2.8e-07, 2.9e-07, 3e-07, 3.1e-07, 3.2e-07, 3.3e-07, 3.4e-07, 3.5e-07, 3.6e-07, 3.7e-07, 3.8e-07, 3.9e-07, 4e-07, 4.1e-07, 4.2e-07, 4.3e-07, 4.4e-07, 4.5e-07, 4.6e-07, 4.7e-07, 4.8e-07, 4.9e-07, 5e-07, 5.1e-07, 5.2e-07, 5.3e-07, 5.4e-07, 5.5e-07, 5.6e-07, 5.7e-07, 5.8e-07, 5.9e-07, 6e-07, 6.1e-07, 6.2e-07, 6.3e-07, 6.4e-07, 6.5e-07, 6.6e-07, 6.7e-07, 6.8e-07, 6.9e-07, 7e-07, 7.1e-07, 7.2e-07, 7.3e-07, 7.4e-07, 7.5e-07, 7.6e-07, 7.7e-07, 7.8e-07, 7.9e-07, 8e-07, 8.1e-07, 8.2e-07, 8.3e-07, 8.4e-07, 8.5e-07, 8.6e-07, 8.7e-07, 8.8e-07, 8.9e-07, 9e-07, 9.1e-07, 9.2e-07, 9.3e-07, 9.4e-07, 9.5e-07, 9.6e-07, 9.7e-07, 9.8e-07, 9.9e-07, 1e-06, 1.01e-06, 1.02e-06, 1.03e-06, 1.04e-06, 1.05e-06, 1.06e-06, 1.07e-06, 1.08e-06, 1.09e-06, 1.1e-06, 1.11e-06, 1.12e-06, 1.13e-06, 1.14e-06, 1.15e-06, 1.16e-06, 1.17e-06, 1.18e-06, 1.19e-06, 1.2e-06, 1.21e-06, 1.22e-06, 1.23e-06, 1.24e-06, 1.25e-06, 1.26e-06, 1.27e-06, 1.28e-06, 1.29e-06, 1.3e-06, 1.31e-06, 1.32e-06, 1.33e-06, 1.34e-06, 1.35e-06, 1.36e-06, 1.37e-06, 1.38e-06, 1.39e-06, 1.4e-06, 1.41e-06, 1.42e-06, 1.43e-06, 1.44e-06, 1.45e-06, 1.46e-06, 1.47e-06, 1.48e-06, 1.49e-06])
        exp = [-1.5e-06, -1.49e-06, -1.48e-06, -1.47e-06, -1.46e-06, -1.45e-06, -1.44e-06, -1.43e-06, -1.42e-06, -1.41e-06, -1.4e-06, -1.39e-06, -1.38e-06, -1.37e-06, -1.36e-06, -1.35e-06, -1.34e-06, -1.33e-06, -1.32e-06, -1.31e-06, -1.3e-06, -1.29e-06, -1.28e-06, -1.27e-06, -1.26e-06, -1.25e-06, -1.24e-06, -1.23e-06, -1.22e-06, -1.21e-06, -1.2e-06, -1.19e-06, -1.18e-06, -1.17e-06, -1.16e-06, -1.15e-06, -1.14e-06, -1.13e-06, -1.12e-06, -1.11e-06, -1.1e-06, -1.09e-06, -1.08e-06, -1.07e-06, -1.06e-06, -1.05e-06, -1.04e-06, -1.03e-06, -1.02e-06, -1.01e-06, -1e-06, -9.9e-07, -9.8e-07, -9.7e-07, -9.6e-07, -9.5e-07, -9.4e-07, -9.3e-07, -9.2e-07, -9.1e-07, -9e-07, -8.9e-07, -8.8e-07, -8.7e-07, -8.6e-07, -8.5e-07, -8.4e-07, -8.3e-07, -8.2e-07, -8.1e-07, -8e-07, -7.9e-07, -7.8e-07, -7.7e-07, -7.6e-07, -7.5e-07, -7.4e-07, -7.3e-07, -7.2e-07, -7.1e-07, -7e-07, -6.9e-07, -6.8e-07, -6.7e-07, -6.6e-07, -6.5e-07, -6.4e-07, -6.3e-07, -6.2e-07, -6.1e-07, -6e-07, -5.9e-07, -5.8e-07, -5.7e-07, -5.6e-07, -5.5e-07, -5.4e-07, -5.3e-07, -5.2e-07, -5.1e-07, -5e-07, -4.9e-07, -4.8e-07, -4.7e-07, -4.6e-07, -4.5e-07, -4.4e-07, -4.3e-07, -4.2e-07, -4.1e-07, -4e-07, -3.9e-07, -3.8e-07, -3.7e-07, -3.6e-07, -3.5e-07, -3.4e-07, -3.3e-07, -3.2e-07, -3.1e-07, -3e-07, -2.9e-07, -2.8e-07, -2.7e-07, -2.6e-07, -2.5e-07, -2.4e-07, -2.3e-07, -2.2e-07, -2.1e-07, -2e-07, -1.9e-07, -1.8e-07, -1.7e-07, -1.6e-07, -1.5e-07, -1.4e-07, -1.3e-07, -1.2e-07, -1.1e-07, -1e-07, -9e-08, -8e-08, -7e-08, -6e-08, -5e-08, -4e-08, -3e-08, -2e-08, -1e-08, 0.0, 1e-08, 2e-08, 3e-08, 4e-08, 5e-08, 6e-08, 7e-08, 8e-08, 9e-08, 1e-07, 1.1e-07, 1.2e-07, 1.3e-07, 1.4e-07, 1.5e-07, 1.6e-07, 1.7e-07, 1.8e-07, 1.9e-07, 2e-07, 2.1e-07, 2.2e-07, 2.3e-07, 2.4e-07, 2.5e-07, 2.6e-07, 2.7e-07, 2.8e-07, 2.9e-07, 3e-07, 3.1e-07, 3.2e-07, 3.3e-07, 3.4e-07, 3.5e-07, 3.6e-07, 3.7e-07, 3.8e-07, 3.9e-07, 4e-07, 4.1e-07, 4.2e-07, 4.3e-07, 4.4e-07, 4.5e-07, 4.6e-07, 4.7e-07, 4.8e-07, 4.9e-07, 5e-07, 5.1e-07, 5.2e-07, 5.3e-07, 5.4e-07, 5.5e-07, 5.6e-07, 5.7e-07, 5.8e-07, 5.9e-07, 6e-07, 6.1e-07, 6.2e-07, 6.3e-07, 6.4e-07, 6.5e-07, 6.6e-07, 6.7e-07, 6.8e-07, 6.9e-07, 7e-07, 7.1e-07, 7.2e-07, 7.3e-07, 7.4e-07, 7.5e-07, 7.6e-07, 7.7e-07, 7.8e-07, 7.9e-07, 8e-07, 8.1e-07, 8.2e-07, 8.3e-07, 8.4e-07, 8.5e-07, 8.6e-07, 8.7e-07, 8.8e-07, 8.9e-07, 9e-07, 9.1e-07, 9.2e-07, 9.3e-07, 9.4e-07, 9.5e-07, 9.6e-07, 9.7e-07, 9.8e-07, 9.9e-07, 1e-06, 1.01e-06, 1.02e-06, 1.03e-06, 1.04e-06, 1.05e-06, 1.06e-06, 1.07e-06, 1.08e-06, 1.09e-06, 1.1e-06, 1.11e-06, 1.12e-06, 1.13e-06, 1.14e-06, 1.15e-06, 1.16e-06, 1.17e-06, 1.18e-06, 1.19e-06, 1.2e-06, 1.21e-06, 1.22e-06, 1.23e-06, 1.24e-06, 1.25e-06, 1.26e-06, 1.27e-06, 1.28e-06, 1.29e-06, 1.3e-06, 1.31e-06, 1.32e-06, 1.33e-06, 1.34e-06, 1.35e-06, 1.36e-06, 1.37e-06, 1.38e-06, 1.39e-06, 1.4e-06, 1.41e-06, 1.42e-06, 1.43e-06, 1.44e-06, 1.45e-06, 1.46e-06, 1.47e-06, 1.48e-06, 1.49e-06]
        if res != exp:
            print("Fel i test 3/29: doubled_odds([-1.5e-06, -1.49e-06, -1.48e-06, -1.47e-06, -1.46e-06, -1.45e-06, -1.44e-06, -1.43e-06, -1.42e-06, -1.41e-06, -1.4e-06, -1.39e-06, -1.38e-06, -1.37e-06, -1.36e-06, -1.35e-06, -1.34e-06, -1.33e-06, -1.32e-06, -1.31e-06, -1.3e-06, -1.29e-06, -1.28e-06, -1.27e-06, -1.26e-06, -1.25e-06, -1.24e-06, -1.23e-06, -1.22e-06, -1.21e-06, -1.2e-06, -1.19e-06, -1.18e-06, -1.17e-06, -1.16e-06, -1.15e-06, -1.14e-06, -1.13e-06, -1.12e-06, -1.11e-06, -1.1e-06, -1.09e-06, -1.08e-06, -1.07e-06, -1.06e-06, -1.05e-06, -1.04e-06, -1.03e-06, -1.02e-06, -1.01e-06, -1e-06, -9.9e-07, -9.8e-07, -9.7e-07, -9.6e-07, -9.5e-07, -9.4e-07, -9.3e-07, -9.2e-07, -9.1e-07, -9e-07, -8.9e-07, -8.8e-07, -8.7e-07, -8.6e-07, -8.5e-07, -8.4e-07, -8.3e-07, -8.2e-07, -8.1e-07, -8e-07, -7.9e-07, -7.8e-07, -7.7e-07, -7.6e-07, -7.5e-07, -7.4e-07, -7.3e-07, -7.2e-07, -7.1e-07, -7e-07, -6.9e-07, -6.8e-07, -6.7e-07, -6.6e-07, -6.5e-07, -6.4e-07, -6.3e-07, -6.2e-07, -6.1e-07, -6e-07, -5.9e-07, -5.8e-07, -5.7e-07, -5.6e-07, -5.5e-07, -5.4e-07, -5.3e-07, -5.2e-07, -5.1e-07, -5e-07, -4.9e-07, -4.8e-07, -4.7e-07, -4.6e-07, -4.5e-07, -4.4e-07, -4.3e-07, -4.2e-07, -4.1e-07, -4e-07, -3.9e-07, -3.8e-07, -3.7e-07, -3.6e-07, -3.5e-07, -3.4e-07, -3.3e-07, -3.2e-07, -3.1e-07, -3e-07, -2.9e-07, -2.8e-07, -2.7e-07, -2.6e-07, -2.5e-07, -2.4e-07, -2.3e-07, -2.2e-07, -2.1e-07, -2e-07, -1.9e-07, -1.8e-07, -1.7e-07, -1.6e-07, -1.5e-07, -1.4e-07, -1.3e-07, -1.2e-07, -1.1e-07, -1e-07, -9e-08, -8e-08, -7e-08, -6e-08, -5e-08, -4e-08, -3e-08, -2e-08, -1e-08, 0.0, 1e-08, 2e-08, 3e-08, 4e-08, 5e-08, 6e-08, 7e-08, 8e-08, 9e-08, 1e-07, 1.1e-07, 1.2e-07, 1.3e-07, 1.4e-07, 1.5e-07, 1.6e-07, 1.7e-07, 1.8e-07, 1.9e-07, 2e-07, 2.1e-07, 2.2e-07, 2.3e-07, 2.4e-07, 2.5e-07, 2.6e-07, 2.7e-07, 2.8e-07, 2.9e-07, 3e-07, 3.1e-07, 3.2e-07, 3.3e-07, 3.4e-07, 3.5e-07, 3.6e-07, 3.7e-07, 3.8e-07, 3.9e-07, 4e-07, 4.1e-07, 4.2e-07, 4.3e-07, 4.4e-07, 4.5e-07, 4.6e-07, 4.7e-07, 4.8e-07, 4.9e-07, 5e-07, 5.1e-07, 5.2e-07, 5.3e-07, 5.4e-07, 5.5e-07, 5.6e-07, 5.7e-07, 5.8e-07, 5.9e-07, 6e-07, 6.1e-07, 6.2e-07, 6.3e-07, 6.4e-07, 6.5e-07, 6.6e-07, 6.7e-07, 6.8e-07, 6.9e-07, 7e-07, 7.1e-07, 7.2e-07, 7.3e-07, 7.4e-07, 7.5e-07, 7.6e-07, 7.7e-07, 7.8e-07, 7.9e-07, 8e-07, 8.1e-07, 8.2e-07, 8.3e-07, 8.4e-07, 8.5e-07, 8.6e-07, 8.7e-07, 8.8e-07, 8.9e-07, 9e-07, 9.1e-07, 9.2e-07, 9.3e-07, 9.4e-07, 9.5e-07, 9.6e-07, 9.7e-07, 9.8e-07, 9.9e-07, 1e-06, 1.01e-06, 1.02e-06, 1.03e-06, 1.04e-06, 1.05e-06, 1.06e-06, 1.07e-06, 1.08e-06, 1.09e-06, 1.1e-06, 1.11e-06, 1.12e-06, 1.13e-06, 1.14e-06, 1.15e-06, 1.16e-06, 1.17e-06, 1.18e-06, 1.19e-06, 1.2e-06, 1.21e-06, 1.22e-06, 1.23e-06, 1.24e-06, 1.25e-06, 1.26e-06, 1.27e-06, 1.28e-06, 1.29e-06, 1.3e-06, 1.31e-06, 1.32e-06, 1.33e-06, 1.34e-06, 1.35e-06, 1.36e-06, 1.37e-06, 1.38e-06, 1.39e-06, 1.4e-06, 1.41e-06, 1.42e-06, 1.43e-06, 1.44e-06, 1.45e-06, 1.46e-06, 1.47e-06, 1.48e-06, 1.49e-06])")
            print("Korrekt svar: -1.5e-06, -1.49e-06, -1.48e-06, -1.47e-06, -1.46e-06, -1.45e-06, -1.44e-06, -1.43e-06, -1.42e-06, -1.41e-06, -1.4e-06, -1.39e-06, -1.38e-06, -1.37e-06, -1.36e-06, -1.35e-06, -1.34e-06, -1.33e-06, -1.32e-06, -1.31e-06, -1.3e-06, -1.29e-06, -1.28e-06, -1.27e-06, -1.26e-06, -1.25e-06, -1.24e-06, -1.23e-06, -1.22e-06, -1.21e-06, -1.2e-06, -1.19e-06, -1.18e-06, -1.17e-06, -1.16e-06, -1.15e-06, -1.14e-06, -1.13e-06, -1.12e-06, -1.11e-06, -1.1e-06, -1.09e-06, -1.08e-06, -1.07e-06, -1.06e-06, -1.05e-06, -1.04e-06, -1.03e-06, -1.02e-06, -1.01e-06, -1e-06, -9.9e-07, -9.8e-07, -9.7e-07, -9.6e-07, -9.5e-07, -9.4e-07, -9.3e-07, -9.2e-07, -9.1e-07, -9e-07, -8.9e-07, -8.8e-07, -8.7e-07, -8.6e-07, -8.5e-07, -8.4e-07, -8.3e-07, -8.2e-07, -8.1e-07, -8e-07, -7.9e-07, -7.8e-07, -7.7e-07, -7.6e-07, -7.5e-07, -7.4e-07, -7.3e-07, -7.2e-07, -7.1e-07, -7e-07, -6.9e-07, -6.8e-07, -6.7e-07, -6.6e-07, -6.5e-07, -6.4e-07, -6.3e-07, -6.2e-07, -6.1e-07, -6e-07, -5.9e-07, -5.8e-07, -5.7e-07, -5.6e-07, -5.5e-07, -5.4e-07, -5.3e-07, -5.2e-07, -5.1e-07, -5e-07, -4.9e-07, -4.8e-07, -4.7e-07, -4.6e-07, -4.5e-07, -4.4e-07, -4.3e-07, -4.2e-07, -4.1e-07, -4e-07, -3.9e-07, -3.8e-07, -3.7e-07, -3.6e-07, -3.5e-07, -3.4e-07, -3.3e-07, -3.2e-07, -3.1e-07, -3e-07, -2.9e-07, -2.8e-07, -2.7e-07, -2.6e-07, -2.5e-07, -2.4e-07, -2.3e-07, -2.2e-07, -2.1e-07, -2e-07, -1.9e-07, -1.8e-07, -1.7e-07, -1.6e-07, -1.5e-07, -1.4e-07, -1.3e-07, -1.2e-07, -1.1e-07, -1e-07, -9e-08, -8e-08, -7e-08, -6e-08, -5e-08, -4e-08, -3e-08, -2e-08, -1e-08, 0.0, 1e-08, 2e-08, 3e-08, 4e-08, 5e-08, 6e-08, 7e-08, 8e-08, 9e-08, 1e-07, 1.1e-07, 1.2e-07, 1.3e-07, 1.4e-07, 1.5e-07, 1.6e-07, 1.7e-07, 1.8e-07, 1.9e-07, 2e-07, 2.1e-07, 2.2e-07, 2.3e-07, 2.4e-07, 2.5e-07, 2.6e-07, 2.7e-07, 2.8e-07, 2.9e-07, 3e-07, 3.1e-07, 3.2e-07, 3.3e-07, 3.4e-07, 3.5e-07, 3.6e-07, 3.7e-07, 3.8e-07, 3.9e-07, 4e-07, 4.1e-07, 4.2e-07, 4.3e-07, 4.4e-07, 4.5e-07, 4.6e-07, 4.7e-07, 4.8e-07, 4.9e-07, 5e-07, 5.1e-07, 5.2e-07, 5.3e-07, 5.4e-07, 5.5e-07, 5.6e-07, 5.7e-07, 5.8e-07, 5.9e-07, 6e-07, 6.1e-07, 6.2e-07, 6.3e-07, 6.4e-07, 6.5e-07, 6.6e-07, 6.7e-07, 6.8e-07, 6.9e-07, 7e-07, 7.1e-07, 7.2e-07, 7.3e-07, 7.4e-07, 7.5e-07, 7.6e-07, 7.7e-07, 7.8e-07, 7.9e-07, 8e-07, 8.1e-07, 8.2e-07, 8.3e-07, 8.4e-07, 8.5e-07, 8.6e-07, 8.7e-07, 8.8e-07, 8.9e-07, 9e-07, 9.1e-07, 9.2e-07, 9.3e-07, 9.4e-07, 9.5e-07, 9.6e-07, 9.7e-07, 9.8e-07, 9.9e-07, 1e-06, 1.01e-06, 1.02e-06, 1.03e-06, 1.04e-06, 1.05e-06, 1.06e-06, 1.07e-06, 1.08e-06, 1.09e-06, 1.1e-06, 1.11e-06, 1.12e-06, 1.13e-06, 1.14e-06, 1.15e-06, 1.16e-06, 1.17e-06, 1.18e-06, 1.19e-06, 1.2e-06, 1.21e-06, 1.22e-06, 1.23e-06, 1.24e-06, 1.25e-06, 1.26e-06, 1.27e-06, 1.28e-06, 1.29e-06, 1.3e-06, 1.31e-06, 1.32e-06, 1.33e-06, 1.34e-06, 1.35e-06, 1.36e-06, 1.37e-06, 1.38e-06, 1.39e-06, 1.4e-06, 1.41e-06, 1.42e-06, 1.43e-06, 1.44e-06, 1.45e-06, 1.46e-06, 1.47e-06, 1.48e-06, 1.49e-06")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/29: Exception')
        print_exception()

    try:
        res = doubled_odds([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0, 33.5, 34.0, 34.5, 35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0, 42.5, 43.0, 43.5, 44.0, 44.5, 45.0, 45.5, 46.0, 46.5, 47.0, 47.5, 48.0, 48.5, 49.0, 49.5, 50.0, 50.5, 51.0, 51.5, 52.0, 52.5, 53.0, 53.5, 54.0, 54.5, 55.0, 55.5, 56.0, 56.5, 57.0, 57.5, 58.0, 58.5, 59.0, 59.5, 60.0, 60.5, 61.0, 61.5, 62.0, 62.5, 63.0, 63.5, 64.0, 64.5, 65.0, 65.5, 66.0, 66.5, 67.0, 67.5, 68.0, 68.5, 69.0, 69.5, 70.0, 70.5, 71.0, 71.5, 72.0, 72.5, 73.0, 73.5, 74.0, 74.5])
        exp = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0, 33.5, 34.0, 34.5, 35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0, 42.5, 43.0, 43.5, 44.0, 44.5, 45.0, 45.5, 46.0, 46.5, 47.0, 47.5, 48.0, 48.5, 49.0, 49.5, 50.0, 50.5, 51.0, 51.5, 52.0, 52.5, 53.0, 53.5, 54.0, 54.5, 55.0, 55.5, 56.0, 56.5, 57.0, 57.5, 58.0, 58.5, 59.0, 59.5, 60.0, 60.5, 61.0, 61.5, 62.0, 62.5, 63.0, 63.5, 64.0, 64.5, 65.0, 65.5, 66.0, 66.5, 67.0, 67.5, 68.0, 68.5, 69.0, 69.5, 70.0, 70.5, 71.0, 71.5, 72.0, 72.5, 73.0, 73.5, 74.0, 74.5]
        if res != exp:
            print("Fel i test 3/30: doubled_odds([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0, 33.5, 34.0, 34.5, 35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0, 42.5, 43.0, 43.5, 44.0, 44.5, 45.0, 45.5, 46.0, 46.5, 47.0, 47.5, 48.0, 48.5, 49.0, 49.5, 50.0, 50.5, 51.0, 51.5, 52.0, 52.5, 53.0, 53.5, 54.0, 54.5, 55.0, 55.5, 56.0, 56.5, 57.0, 57.5, 58.0, 58.5, 59.0, 59.5, 60.0, 60.5, 61.0, 61.5, 62.0, 62.5, 63.0, 63.5, 64.0, 64.5, 65.0, 65.5, 66.0, 66.5, 67.0, 67.5, 68.0, 68.5, 69.0, 69.5, 70.0, 70.5, 71.0, 71.5, 72.0, 72.5, 73.0, 73.5, 74.0, 74.5])")
            print("Korrekt svar: 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 32.5, 33.0, 33.5, 34.0, 34.5, 35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0, 42.5, 43.0, 43.5, 44.0, 44.5, 45.0, 45.5, 46.0, 46.5, 47.0, 47.5, 48.0, 48.5, 49.0, 49.5, 50.0, 50.5, 51.0, 51.5, 52.0, 52.5, 53.0, 53.5, 54.0, 54.5, 55.0, 55.5, 56.0, 56.5, 57.0, 57.5, 58.0, 58.5, 59.0, 59.5, 60.0, 60.5, 61.0, 61.5, 62.0, 62.5, 63.0, 63.5, 64.0, 64.5, 65.0, 65.5, 66.0, 66.5, 67.0, 67.5, 68.0, 68.5, 69.0, 69.5, 70.0, 70.5, 71.0, 71.5, 72.0, 72.5, 73.0, 73.5, 74.0, 74.5")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/30: Exception')
        print_exception()

    try:
        res = doubled_odds([7.6, 7.7, 7, 7.0])
        exp = [7.6, 7.7, 14, 7.0]
        if res != exp:
            print("Fel i test 3/31: doubled_odds([7.6, 7.7, 7, 7.0])")
            print("Korrekt svar: 7.6, 7.7, 14, 7.0")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/31: Exception')
        print_exception()

    try:
        res = doubled_odds([1, 1.0, 1, 1.0, 1, 1, 1.0])
        exp = [2, 1.0, 2, 1.0, 2, 2, 1.0]
        if res != exp:
            print("Fel i test 3/32: doubled_odds([1, 1.0, 1, 1.0, 1, 1, 1.0])")
            print("Korrekt svar: 2, 1.0, 2, 1.0, 2, 2, 1.0")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/32: Exception')
        print_exception()

    try:
        res = doubled_odds(['0', 1.0, 2, '3', 4.0, 5, '6', 7.0, 8, '9', 10.0, 11, '12', 13.0, 14, '15', 16.0, 17, '18', 19.0, 20, '21', 22.0, 23, '24', 25.0, 26, '27', 28.0, 29, '30', 31.0, 32, '33', 34.0, 35, '36', 37.0, 38, '39', 40.0, 41, '42', 43.0, 44, '45', 46.0, 47, '48', 49.0, 50, '51', 52.0, 53, '54', 55.0, 56, '57', 58.0, 59, '60', 61.0, 62, '63', 64.0, 65, '66', 67.0, 68, '69', 70.0, 71, '72', 73.0, 74, '75', 76.0, 77, '78', 79.0, 80, '81', 82.0, 83, '84', 85.0, 86, '87', 88.0, 89, '90', 91.0, 92, '93', 94.0, 95, '96', 97.0, 98, '99', 100.0, 101, '102', 103.0, 104, '105', 106.0, 107, '108', 109.0, 110, '111', 112.0, 113, '114', 115.0, 116, '117', 118.0, 119, '120', 121.0, 122, '123', 124.0, 125, '126', 127.0, 128, '129', 130.0, 131, '132', 133.0, 134, '135', 136.0, 137, '138', 139.0, 140, '141', 142.0, 143, '144', 145.0, 146, '147', 148.0, 149])
        exp = ['0', 1.0, 2, '3', 4.0, 10, '6', 7.0, 8, '9', 10.0, 22, '12', 13.0, 14, '15', 16.0, 34, '18', 19.0, 20, '21', 22.0, 46, '24', 25.0, 26, '27', 28.0, 58, '30', 31.0, 32, '33', 34.0, 70, '36', 37.0, 38, '39', 40.0, 82, '42', 43.0, 44, '45', 46.0, 94, '48', 49.0, 50, '51', 52.0, 106, '54', 55.0, 56, '57', 58.0, 118, '60', 61.0, 62, '63', 64.0, 130, '66', 67.0, 68, '69', 70.0, 142, '72', 73.0, 74, '75', 76.0, 154, '78', 79.0, 80, '81', 82.0, 166, '84', 85.0, 86, '87', 88.0, 178, '90', 91.0, 92, '93', 94.0, 190, '96', 97.0, 98, '99', 100.0, 202, '102', 103.0, 104, '105', 106.0, 214, '108', 109.0, 110, '111', 112.0, 226, '114', 115.0, 116, '117', 118.0, 238, '120', 121.0, 122, '123', 124.0, 250, '126', 127.0, 128, '129', 130.0, 262, '132', 133.0, 134, '135', 136.0, 274, '138', 139.0, 140, '141', 142.0, 286, '144', 145.0, 146, '147', 148.0, 298]
        if res != exp:
            print("Fel i test 3/33: doubled_odds(['0', 1.0, 2, '3', 4.0, 5, '6', 7.0, 8, '9', 10.0, 11, '12', 13.0, 14, '15', 16.0, 17, '18', 19.0, 20, '21', 22.0, 23, '24', 25.0, 26, '27', 28.0, 29, '30', 31.0, 32, '33', 34.0, 35, '36', 37.0, 38, '39', 40.0, 41, '42', 43.0, 44, '45', 46.0, 47, '48', 49.0, 50, '51', 52.0, 53, '54', 55.0, 56, '57', 58.0, 59, '60', 61.0, 62, '63', 64.0, 65, '66', 67.0, 68, '69', 70.0, 71, '72', 73.0, 74, '75', 76.0, 77, '78', 79.0, 80, '81', 82.0, 83, '84', 85.0, 86, '87', 88.0, 89, '90', 91.0, 92, '93', 94.0, 95, '96', 97.0, 98, '99', 100.0, 101, '102', 103.0, 104, '105', 106.0, 107, '108', 109.0, 110, '111', 112.0, 113, '114', 115.0, 116, '117', 118.0, 119, '120', 121.0, 122, '123', 124.0, 125, '126', 127.0, 128, '129', 130.0, 131, '132', 133.0, 134, '135', 136.0, 137, '138', 139.0, 140, '141', 142.0, 143, '144', 145.0, 146, '147', 148.0, 149])")
            print("Korrekt svar: '0', 1.0, 2, '3', 4.0, 10, '6', 7.0, 8, '9', 10.0, 22, '12', 13.0, 14, '15', 16.0, 34, '18', 19.0, 20, '21', 22.0, 46, '24', 25.0, 26, '27', 28.0, 58, '30', 31.0, 32, '33', 34.0, 70, '36', 37.0, 38, '39', 40.0, 82, '42', 43.0, 44, '45', 46.0, 94, '48', 49.0, 50, '51', 52.0, 106, '54', 55.0, 56, '57', 58.0, 118, '60', 61.0, 62, '63', 64.0, 130, '66', 67.0, 68, '69', 70.0, 142, '72', 73.0, 74, '75', 76.0, 154, '78', 79.0, 80, '81', 82.0, 166, '84', 85.0, 86, '87', 88.0, 178, '90', 91.0, 92, '93', 94.0, 190, '96', 97.0, 98, '99', 100.0, 202, '102', 103.0, 104, '105', 106.0, 214, '108', 109.0, 110, '111', 112.0, 226, '114', 115.0, 116, '117', 118.0, 238, '120', 121.0, 122, '123', 124.0, 250, '126', 127.0, 128, '129', 130.0, 262, '132', 133.0, 134, '135', 136.0, 274, '138', 139.0, 140, '141', 142.0, 286, '144', 145.0, 146, '147', 148.0, 298")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/33: Exception')
        print_exception()

    try:
        res = doubled_odds(['1', 1, 2, '2', '3', '3', 4, 4])
        exp = ['1', 2, 2, '2', '3', '3', 4, 4]
        if res != exp:
            print("Fel i test 3/34: doubled_odds(['1', 1, 2, '2', '3', '3', 4, 4])")
            print("Korrekt svar: '1', 2, 2, '2', '3', '3', 4, 4")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/34: Exception')
        print_exception()

    try:
        res = doubled_odds([])
        exp = []
        if res != exp:
            print("Fel i test 3/35: doubled_odds([])")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/35: Exception')
        print_exception()

    try:
        res = doubled_odds([[[[]]]])
        exp = [[[[]]]]
        if res != exp:
            print("Fel i test 3/36: doubled_odds([[[[]]]])")
            print("Korrekt svar: [[[]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/36: Exception')
        print_exception()

    try:
        res = doubled_odds([[]])
        exp = [[]]
        if res != exp:
            print("Fel i test 3/37: doubled_odds([[]])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/37: Exception')
        print_exception()

    try:
        res = doubled_odds([[], [[]]])
        exp = [[], [[]]]
        if res != exp:
            print("Fel i test 3/38: doubled_odds([[], [[]]])")
            print("Korrekt svar: [], [[]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/38: Exception')
        print_exception()

    try:
        res = doubled_odds([[[[[]]]], [], [[]]])
        exp = [[[[[]]]], [], [[]]]
        if res != exp:
            print("Fel i test 3/39: doubled_odds([[[[[]]]], [], [[]]])")
            print("Korrekt svar: [[[[]]]], [], [[]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/39: Exception')
        print_exception()

    try:
        res = doubled_odds([[]])
        exp = [[]]
        if res != exp:
            print("Fel i test 3/40: doubled_odds([[]])")
            print("Korrekt svar: []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/40: Exception')
        print_exception()

    try:
        res = doubled_odds([[[[[[[[[[[]]]]]]]]]]])
        exp = [[[[[[[[[[[]]]]]]]]]]]
        if res != exp:
            print("Fel i test 3/41: doubled_odds([[[[[[[[[[[]]]]]]]]]]])")
            print("Korrekt svar: [[[[[[[[[[]]]]]]]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/41: Exception')
        print_exception()

    try:
        res = doubled_odds([[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]])
        exp = [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
        if res != exp:
            print("Fel i test 3/42: doubled_odds([[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]])")
            print("Korrekt svar: [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/42: Exception')
        print_exception()

    try:
        res = doubled_odds([[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]])
        exp = [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
        if res != exp:
            print("Fel i test 3/43: doubled_odds([[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]])")
            print("Korrekt svar: [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/43: Exception')
        print_exception()

    try:
        res = doubled_odds([[[[5]]]])
        exp = [[[[10]]]]
        if res != exp:
            print("Fel i test 3/44: doubled_odds([[[[5]]]])")
            print("Korrekt svar: [[[10]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/44: Exception')
        print_exception()

    try:
        res = doubled_odds([[1], [2]])
        exp = [[2], [2]]
        if res != exp:
            print("Fel i test 3/45: doubled_odds([[1], [2]])")
            print("Korrekt svar: [2], [2]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/45: Exception')
        print_exception()

    try:
        res = doubled_odds([[1], [[2]], [[[3]]], [[[[4]]]]])
        exp = [[2], [[2]], [[[6]]], [[[[4]]]]]
        if res != exp:
            print("Fel i test 3/46: doubled_odds([[1], [[2]], [[[3]]], [[[[4]]]]])")
            print("Korrekt svar: [2], [[2]], [[[6]]], [[[[4]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/46: Exception')
        print_exception()

    try:
        res = doubled_odds([[-1], [[[2]]], 33, [[[[78]]]], [[[-123]]]])
        exp = [[-2], [[[2]]], 66, [[[[78]]]], [[[-246]]]]
        if res != exp:
            print("Fel i test 3/47: doubled_odds([[-1], [[[2]]], 33, [[[[78]]]], [[[-123]]]])")
            print("Korrekt svar: [-2], [[[2]]], 66, [[[[78]]]], [[[-246]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/47: Exception')
        print_exception()

    try:
        res = doubled_odds([[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12], [0, 4, 8, 12, 16]], [[0, 0, 0, 0, 0], [0, 2, 4, 6, 8], [0, 4, 8, 12, 16], [0, 6, 12, 18, 24], [0, 8, 16, 24, 32]], [[0, 0, 0, 0, 0], [0, 3, 6, 9, 12], [0, 6, 12, 18, 24], [0, 9, 18, 27, 36], [0, 12, 24, 36, 48]], [[0, 0, 0, 0, 0], [0, 4, 8, 12, 16], [0, 8, 16, 24, 32], [0, 12, 24, 36, 48], [0, 16, 32, 48, 64]]])
        exp = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 2, 2, 6, 4], [0, 2, 4, 6, 8], [0, 6, 6, 18, 12], [0, 4, 8, 12, 16]], [[0, 0, 0, 0, 0], [0, 2, 4, 6, 8], [0, 4, 8, 12, 16], [0, 6, 12, 18, 24], [0, 8, 16, 24, 32]], [[0, 0, 0, 0, 0], [0, 6, 6, 18, 12], [0, 6, 12, 18, 24], [0, 18, 18, 54, 36], [0, 12, 24, 36, 48]], [[0, 0, 0, 0, 0], [0, 4, 8, 12, 16], [0, 8, 16, 24, 32], [0, 12, 24, 36, 48], [0, 16, 32, 48, 64]]]
        if res != exp:
            print("Fel i test 3/48: doubled_odds([[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12], [0, 4, 8, 12, 16]], [[0, 0, 0, 0, 0], [0, 2, 4, 6, 8], [0, 4, 8, 12, 16], [0, 6, 12, 18, 24], [0, 8, 16, 24, 32]], [[0, 0, 0, 0, 0], [0, 3, 6, 9, 12], [0, 6, 12, 18, 24], [0, 9, 18, 27, 36], [0, 12, 24, 36, 48]], [[0, 0, 0, 0, 0], [0, 4, 8, 12, 16], [0, 8, 16, 24, 32], [0, 12, 24, 36, 48], [0, 16, 32, 48, 64]]])")
            print("Korrekt svar: [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 2, 2, 6, 4], [0, 2, 4, 6, 8], [0, 6, 6, 18, 12], [0, 4, 8, 12, 16]], [[0, 0, 0, 0, 0], [0, 2, 4, 6, 8], [0, 4, 8, 12, 16], [0, 6, 12, 18, 24], [0, 8, 16, 24, 32]], [[0, 0, 0, 0, 0], [0, 6, 6, 18, 12], [0, 6, 12, 18, 24], [0, 18, 18, 54, 36], [0, 12, 24, 36, 48]], [[0, 0, 0, 0, 0], [0, 4, 8, 12, 16], [0, 8, 16, 24, 32], [0, 12, 24, 36, 48], [0, 16, 32, 48, 64]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/48: Exception')
        print_exception()

    try:
        res = doubled_odds([[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, -1, -2, -3, -4], [0, -2, -4, -6, -8], [0, -3, -6, -9, -12], [0, -4, -8, -12, -16]], [[0, 0, 0, 0, 0], [0, -2, -4, -6, -8], [0, -4, -8, -12, -16], [0, -6, -12, -18, -24], [0, -8, -16, -24, -32]], [[0, 0, 0, 0, 0], [0, -3, -6, -9, -12], [0, -6, -12, -18, -24], [0, -9, -18, -27, -36], [0, -12, -24, -36, -48]], [[0, 0, 0, 0, 0], [0, -4, -8, -12, -16], [0, -8, -16, -24, -32], [0, -12, -24, -36, -48], [0, -16, -32, -48, -64]]])
        exp = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, -2, -2, -6, -4], [0, -2, -4, -6, -8], [0, -6, -6, -18, -12], [0, -4, -8, -12, -16]], [[0, 0, 0, 0, 0], [0, -2, -4, -6, -8], [0, -4, -8, -12, -16], [0, -6, -12, -18, -24], [0, -8, -16, -24, -32]], [[0, 0, 0, 0, 0], [0, -6, -6, -18, -12], [0, -6, -12, -18, -24], [0, -18, -18, -54, -36], [0, -12, -24, -36, -48]], [[0, 0, 0, 0, 0], [0, -4, -8, -12, -16], [0, -8, -16, -24, -32], [0, -12, -24, -36, -48], [0, -16, -32, -48, -64]]]
        if res != exp:
            print("Fel i test 3/49: doubled_odds([[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, -1, -2, -3, -4], [0, -2, -4, -6, -8], [0, -3, -6, -9, -12], [0, -4, -8, -12, -16]], [[0, 0, 0, 0, 0], [0, -2, -4, -6, -8], [0, -4, -8, -12, -16], [0, -6, -12, -18, -24], [0, -8, -16, -24, -32]], [[0, 0, 0, 0, 0], [0, -3, -6, -9, -12], [0, -6, -12, -18, -24], [0, -9, -18, -27, -36], [0, -12, -24, -36, -48]], [[0, 0, 0, 0, 0], [0, -4, -8, -12, -16], [0, -8, -16, -24, -32], [0, -12, -24, -36, -48], [0, -16, -32, -48, -64]]])")
            print("Korrekt svar: [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, -2, -2, -6, -4], [0, -2, -4, -6, -8], [0, -6, -6, -18, -12], [0, -4, -8, -12, -16]], [[0, 0, 0, 0, 0], [0, -2, -4, -6, -8], [0, -4, -8, -12, -16], [0, -6, -12, -18, -24], [0, -8, -16, -24, -32]], [[0, 0, 0, 0, 0], [0, -6, -6, -18, -12], [0, -6, -12, -18, -24], [0, -18, -18, -54, -36], [0, -12, -24, -36, -48]], [[0, 0, 0, 0, 0], [0, -4, -8, -12, -16], [0, -8, -16, -24, -32], [0, -12, -24, -36, -48], [0, -16, -32, -48, -64]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/49: Exception')
        print_exception()

    try:
        res = doubled_odds([[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]])
        exp = [[], [0], [0, 2], [0, 2, 2], [0, 2, 2, 6], [0, 2, 2, 6, 4], [0, 2, 2, 6, 4, 10], [0, 2, 2, 6, 4, 10, 6], [0, 2, 2, 6, 4, 10, 6, 14], [0, 2, 2, 6, 4, 10, 6, 14, 8], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90, 182], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90, 182, 92], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90, 182, 92, 186], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90, 182, 92, 186, 94], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90, 182, 92, 186, 94, 190], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90, 182, 92, 186, 94, 190, 96], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90, 182, 92, 186, 94, 190, 96, 194], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90, 182, 92, 186, 94, 190, 96, 194, 98]]
        if res != exp:
            print("Fel i test 3/50: doubled_odds([[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]])")
            print("Korrekt svar: [], [0], [0, 2], [0, 2, 2], [0, 2, 2, 6], [0, 2, 2, 6, 4], [0, 2, 2, 6, 4, 10], [0, 2, 2, 6, 4, 10, 6], [0, 2, 2, 6, 4, 10, 6, 14], [0, 2, 2, 6, 4, 10, 6, 14, 8], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90, 182], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90, 182, 92], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90, 182, 92, 186], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90, 182, 92, 186, 94], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90, 182, 92, 186, 94, 190], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90, 182, 92, 186, 94, 190, 96], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90, 182, 92, 186, 94, 190, 96, 194], [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90, 182, 92, 186, 94, 190, 96, 194, 98]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/50: Exception')
        print_exception()

    try:
        res = doubled_odds([[], [[0]], [[0], [1], [0], [1]], [[0], [1], [2], [0], [1], [2], [0], [1], [2]], [[0], [1], [2], [3], [0], [1], [2], [3], [0], [1], [2], [3], [0], [1], [2], [3]], [[0], [1], [2], [3], [4], [0], [1], [2], [3], [4], [0], [1], [2], [3], [4], [0], [1], [2], [3], [4], [0], [1], [2], [3], [4]], [[0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5]], [[0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6]], [[0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7]], [[0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8]]])
        exp = [[], [[0]], [[0], [2], [0], [2]], [[0], [2], [2], [0], [2], [2], [0], [2], [2]], [[0], [2], [2], [6], [0], [2], [2], [6], [0], [2], [2], [6], [0], [2], [2], [6]], [[0], [2], [2], [6], [4], [0], [2], [2], [6], [4], [0], [2], [2], [6], [4], [0], [2], [2], [6], [4], [0], [2], [2], [6], [4]], [[0], [2], [2], [6], [4], [10], [0], [2], [2], [6], [4], [10], [0], [2], [2], [6], [4], [10], [0], [2], [2], [6], [4], [10], [0], [2], [2], [6], [4], [10], [0], [2], [2], [6], [4], [10]], [[0], [2], [2], [6], [4], [10], [6], [0], [2], [2], [6], [4], [10], [6], [0], [2], [2], [6], [4], [10], [6], [0], [2], [2], [6], [4], [10], [6], [0], [2], [2], [6], [4], [10], [6], [0], [2], [2], [6], [4], [10], [6], [0], [2], [2], [6], [4], [10], [6]], [[0], [2], [2], [6], [4], [10], [6], [14], [0], [2], [2], [6], [4], [10], [6], [14], [0], [2], [2], [6], [4], [10], [6], [14], [0], [2], [2], [6], [4], [10], [6], [14], [0], [2], [2], [6], [4], [10], [6], [14], [0], [2], [2], [6], [4], [10], [6], [14], [0], [2], [2], [6], [4], [10], [6], [14], [0], [2], [2], [6], [4], [10], [6], [14]], [[0], [2], [2], [6], [4], [10], [6], [14], [8], [0], [2], [2], [6], [4], [10], [6], [14], [8], [0], [2], [2], [6], [4], [10], [6], [14], [8], [0], [2], [2], [6], [4], [10], [6], [14], [8], [0], [2], [2], [6], [4], [10], [6], [14], [8], [0], [2], [2], [6], [4], [10], [6], [14], [8], [0], [2], [2], [6], [4], [10], [6], [14], [8], [0], [2], [2], [6], [4], [10], [6], [14], [8], [0], [2], [2], [6], [4], [10], [6], [14], [8]]]
        if res != exp:
            print("Fel i test 3/51: doubled_odds([[], [[0]], [[0], [1], [0], [1]], [[0], [1], [2], [0], [1], [2], [0], [1], [2]], [[0], [1], [2], [3], [0], [1], [2], [3], [0], [1], [2], [3], [0], [1], [2], [3]], [[0], [1], [2], [3], [4], [0], [1], [2], [3], [4], [0], [1], [2], [3], [4], [0], [1], [2], [3], [4], [0], [1], [2], [3], [4]], [[0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5], [0], [1], [2], [3], [4], [5]], [[0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6], [0], [1], [2], [3], [4], [5], [6]], [[0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7], [0], [1], [2], [3], [4], [5], [6], [7]], [[0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8], [0], [1], [2], [3], [4], [5], [6], [7], [8]]])")
            print("Korrekt svar: [], [[0]], [[0], [2], [0], [2]], [[0], [2], [2], [0], [2], [2], [0], [2], [2]], [[0], [2], [2], [6], [0], [2], [2], [6], [0], [2], [2], [6], [0], [2], [2], [6]], [[0], [2], [2], [6], [4], [0], [2], [2], [6], [4], [0], [2], [2], [6], [4], [0], [2], [2], [6], [4], [0], [2], [2], [6], [4]], [[0], [2], [2], [6], [4], [10], [0], [2], [2], [6], [4], [10], [0], [2], [2], [6], [4], [10], [0], [2], [2], [6], [4], [10], [0], [2], [2], [6], [4], [10], [0], [2], [2], [6], [4], [10]], [[0], [2], [2], [6], [4], [10], [6], [0], [2], [2], [6], [4], [10], [6], [0], [2], [2], [6], [4], [10], [6], [0], [2], [2], [6], [4], [10], [6], [0], [2], [2], [6], [4], [10], [6], [0], [2], [2], [6], [4], [10], [6], [0], [2], [2], [6], [4], [10], [6]], [[0], [2], [2], [6], [4], [10], [6], [14], [0], [2], [2], [6], [4], [10], [6], [14], [0], [2], [2], [6], [4], [10], [6], [14], [0], [2], [2], [6], [4], [10], [6], [14], [0], [2], [2], [6], [4], [10], [6], [14], [0], [2], [2], [6], [4], [10], [6], [14], [0], [2], [2], [6], [4], [10], [6], [14], [0], [2], [2], [6], [4], [10], [6], [14]], [[0], [2], [2], [6], [4], [10], [6], [14], [8], [0], [2], [2], [6], [4], [10], [6], [14], [8], [0], [2], [2], [6], [4], [10], [6], [14], [8], [0], [2], [2], [6], [4], [10], [6], [14], [8], [0], [2], [2], [6], [4], [10], [6], [14], [8], [0], [2], [2], [6], [4], [10], [6], [14], [8], [0], [2], [2], [6], [4], [10], [6], [14], [8], [0], [2], [2], [6], [4], [10], [6], [14], [8], [0], [2], [2], [6], [4], [10], [6], [14], [8]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/51: Exception')
        print_exception()

    try:
        res = doubled_odds([[0], [[1]], [[[2]]], [[[[3]]]], [[[[[4]]]]], [[[[[[5]]]]]], [[[[[[[6]]]]]]], [[[[[[[[7]]]]]]]], [[[[[[[[[8]]]]]]]]], [[[[[[[[[[9]]]]]]]]]], [[[[[[[[[[[10]]]]]]]]]]], [[[[[[[[[[[[11]]]]]]]]]]]], [[[[[[[[[[[[[12]]]]]]]]]]]]], [[[[[[[[[[[[[[13]]]]]]]]]]]]]], [[[[[[[[[[[[[[[14]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[15]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[16]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[17]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[18]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[19]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[20]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[21]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[22]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[23]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[24]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[25]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[26]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[27]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[28]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[29]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[30]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[31]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[32]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[33]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[34]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[35]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[36]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[37]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[38]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[39]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[40]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[41]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[42]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[43]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[44]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[45]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[46]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[47]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[48]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[49]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[50]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[51]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[52]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[53]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[54]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[55]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[56]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[57]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[58]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[59]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[60]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[61]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[62]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[63]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[64]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[65]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[66]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[67]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[68]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[69]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[70]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[71]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[72]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[73]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[74]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[75]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[76]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[77]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[78]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[79]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[80]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[81]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[82]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[83]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[84]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[85]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[86]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]])
        exp = [[0], [[2]], [[[2]]], [[[[6]]]], [[[[[4]]]]], [[[[[[10]]]]]], [[[[[[[6]]]]]]], [[[[[[[[14]]]]]]]], [[[[[[[[[8]]]]]]]]], [[[[[[[[[[18]]]]]]]]]], [[[[[[[[[[[10]]]]]]]]]]], [[[[[[[[[[[[22]]]]]]]]]]]], [[[[[[[[[[[[[12]]]]]]]]]]]]], [[[[[[[[[[[[[[26]]]]]]]]]]]]]], [[[[[[[[[[[[[[[14]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[30]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[16]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[34]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[18]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[38]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[20]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[42]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[22]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[46]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[24]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[50]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[26]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[54]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[28]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[58]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[30]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[62]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[32]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[66]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[34]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[70]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[36]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[74]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[38]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[78]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[40]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[82]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[42]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[86]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[44]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[90]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[46]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[94]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[48]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[98]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[50]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[102]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[52]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[106]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[54]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[110]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[56]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[114]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[58]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[118]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[60]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[122]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[62]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[126]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[64]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[130]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[66]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[134]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[68]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[138]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[70]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[142]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[72]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[146]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[74]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[150]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[76]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[154]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[78]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[158]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[80]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[162]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[82]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[166]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[84]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[170]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[86]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
        if res != exp:
            print("Fel i test 3/52: doubled_odds([[0], [[1]], [[[2]]], [[[[3]]]], [[[[[4]]]]], [[[[[[5]]]]]], [[[[[[[6]]]]]]], [[[[[[[[7]]]]]]]], [[[[[[[[[8]]]]]]]]], [[[[[[[[[[9]]]]]]]]]], [[[[[[[[[[[10]]]]]]]]]]], [[[[[[[[[[[[11]]]]]]]]]]]], [[[[[[[[[[[[[12]]]]]]]]]]]]], [[[[[[[[[[[[[[13]]]]]]]]]]]]]], [[[[[[[[[[[[[[[14]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[15]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[16]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[17]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[18]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[19]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[20]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[21]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[22]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[23]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[24]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[25]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[26]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[27]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[28]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[29]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[30]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[31]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[32]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[33]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[34]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[35]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[36]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[37]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[38]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[39]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[40]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[41]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[42]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[43]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[44]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[45]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[46]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[47]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[48]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[49]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[50]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[51]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[52]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[53]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[54]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[55]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[56]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[57]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[58]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[59]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[60]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[61]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[62]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[63]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[64]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[65]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[66]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[67]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[68]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[69]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[70]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[71]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[72]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[73]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[74]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[75]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[76]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[77]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[78]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[79]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[80]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[81]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[82]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[83]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[84]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[85]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[86]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]])")
            print("Korrekt svar: [0], [[2]], [[[2]]], [[[[6]]]], [[[[[4]]]]], [[[[[[10]]]]]], [[[[[[[6]]]]]]], [[[[[[[[14]]]]]]]], [[[[[[[[[8]]]]]]]]], [[[[[[[[[[18]]]]]]]]]], [[[[[[[[[[[10]]]]]]]]]]], [[[[[[[[[[[[22]]]]]]]]]]]], [[[[[[[[[[[[[12]]]]]]]]]]]]], [[[[[[[[[[[[[[26]]]]]]]]]]]]]], [[[[[[[[[[[[[[[14]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[30]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[16]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[34]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[18]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[38]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[20]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[42]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[22]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[46]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[24]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[50]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[26]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[54]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[28]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[58]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[30]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[62]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[32]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[66]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[34]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[70]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[36]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[74]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[38]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[78]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[40]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[82]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[42]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[86]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[44]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[90]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[46]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[94]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[48]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[98]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[50]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[102]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[52]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[106]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[54]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[110]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[56]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[114]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[58]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[118]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[60]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[122]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[62]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[126]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[64]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[130]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[66]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[134]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[68]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[138]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[70]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[142]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[72]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[146]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[74]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[150]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[76]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[154]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[78]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[158]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[80]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[162]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[82]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[166]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[84]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[170]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[86]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/52: Exception')
        print_exception()

    try:
        res = doubled_odds([[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[9]]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[9]]]]]]]]]], [[[[[[[[[[10]]]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[9]]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[9]]]]]]]]]], [[[[[[[[[[10]]]]]]]]]]], [[[[[[[[[[[11]]]]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[9]]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[9]]]]]]]]]], [[[[[[[[[[10]]]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[9]]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[9]]]]]]]]]], [[[[[[[[[[10]]]]]]]]]]], [[[[[[[[[[[11]]]]]]]]]]]], [[[[[[[[[[[[12]]]]]]]]]]]]]])
        exp = [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[18]]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[18]]]]]]]]]], [[[[[[[[[[10]]]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[18]]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[18]]]]]]]]]], [[[[[[[[[[10]]]]]]]]]]], [[[[[[[[[[[22]]]]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[18]]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[18]]]]]]]]]], [[[[[[[[[[10]]]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[18]]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[18]]]]]]]]]], [[[[[[[[[[10]]]]]]]]]]], [[[[[[[[[[[22]]]]]]]]]]]], [[[[[[[[[[[[12]]]]]]]]]]]]]]
        if res != exp:
            print("Fel i test 3/53: doubled_odds([[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[9]]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[9]]]]]]]]]], [[[[[[[[[[10]]]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[9]]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[9]]]]]]]]]], [[[[[[[[[[10]]]]]]]]]]], [[[[[[[[[[[11]]]]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[9]]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[9]]]]]]]]]], [[[[[[[[[[10]]]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[9]]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[0], [[0], [1]], [[0], [[0], [1]], [[2]]], [[[3]]]], [[[[4]]]]], [[[[[5]]]]]], [[[[[[6]]]]]]], [[[[[[[7]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[9]]]]]]]]]], [[[[[[[[[[10]]]]]]]]]]], [[[[[[[[[[[11]]]]]]]]]]]], [[[[[[[[[[[[12]]]]]]]]]]]]]])")
            print("Korrekt svar: [0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[18]]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[18]]]]]]]]]], [[[[[[[[[[10]]]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[18]]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[18]]]]]]]]]], [[[[[[[[[[10]]]]]]]]]]], [[[[[[[[[[[22]]]]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[18]]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[18]]]]]]]]]], [[[[[[[[[[10]]]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[18]]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[0], [[0], [2]], [[0], [[0], [2]], [[2]]], [[[6]]]], [[[[4]]]]], [[[[[10]]]]]], [[[[[[6]]]]]]], [[[[[[[14]]]]]]]], [[[[[[[[8]]]]]]]]], [[[[[[[[[18]]]]]]]]]], [[[[[[[[[[10]]]]]]]]]]], [[[[[[[[[[[22]]]]]]]]]]]], [[[[[[[[[[[[12]]]]]]]]]]]]]")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/53: Exception')
        print_exception()

    try:
        res = doubled_odds([(), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ()])
        exp = [(), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ()]
        if res != exp:
            print("Fel i test 3/54: doubled_odds([(), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ()])")
            print("Korrekt svar: (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ()")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/54: Exception')
        print_exception()

    try:
        res = doubled_odds([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])
        exp = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        if res != exp:
            print("Fel i test 3/55: doubled_odds([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])")
            print("Korrekt svar: (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/55: Exception')
        print_exception()

    try:
        res = doubled_odds([{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}])
        exp = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
        if res != exp:
            print("Fel i test 3/56: doubled_odds([{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}])")
            print("Korrekt svar: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/56: Exception')
        print_exception()

    try:
        res = doubled_odds([{0: 0}, {1: 1}, {2: 2}, {3: 3}, {4: 4}, {5: 5}, {6: 6}, {7: 7}, {8: 8}, {9: 9}, {10: 10}, {11: 11}, {12: 12}, {13: 13}, {14: 14}, {15: 15}, {16: 16}, {17: 17}, {18: 18}, {19: 19}, {20: 20}, {21: 21}, {22: 22}, {23: 23}, {24: 24}, {25: 25}, {26: 26}, {27: 27}, {28: 28}, {29: 29}, {30: 30}, {31: 31}, {32: 32}, {33: 33}, {34: 34}, {35: 35}, {36: 36}, {37: 37}, {38: 38}, {39: 39}, {40: 40}, {41: 41}, {42: 42}, {43: 43}, {44: 44}, {45: 45}, {46: 46}, {47: 47}, {48: 48}, {49: 49}, {50: 50}, {51: 51}, {52: 52}, {53: 53}, {54: 54}, {55: 55}, {56: 56}, {57: 57}, {58: 58}, {59: 59}, {60: 60}, {61: 61}, {62: 62}, {63: 63}, {64: 64}, {65: 65}, {66: 66}, {67: 67}, {68: 68}, {69: 69}, {70: 70}, {71: 71}, {72: 72}, {73: 73}, {74: 74}, {75: 75}, {76: 76}, {77: 77}, {78: 78}, {79: 79}, {80: 80}, {81: 81}, {82: 82}, {83: 83}, {84: 84}, {85: 85}, {86: 86}, {87: 87}, {88: 88}, {89: 89}, {90: 90}, {91: 91}, {92: 92}, {93: 93}, {94: 94}, {95: 95}, {96: 96}, {97: 97}, {98: 98}, {99: 99}])
        exp = [{0: 0}, {1: 1}, {2: 2}, {3: 3}, {4: 4}, {5: 5}, {6: 6}, {7: 7}, {8: 8}, {9: 9}, {10: 10}, {11: 11}, {12: 12}, {13: 13}, {14: 14}, {15: 15}, {16: 16}, {17: 17}, {18: 18}, {19: 19}, {20: 20}, {21: 21}, {22: 22}, {23: 23}, {24: 24}, {25: 25}, {26: 26}, {27: 27}, {28: 28}, {29: 29}, {30: 30}, {31: 31}, {32: 32}, {33: 33}, {34: 34}, {35: 35}, {36: 36}, {37: 37}, {38: 38}, {39: 39}, {40: 40}, {41: 41}, {42: 42}, {43: 43}, {44: 44}, {45: 45}, {46: 46}, {47: 47}, {48: 48}, {49: 49}, {50: 50}, {51: 51}, {52: 52}, {53: 53}, {54: 54}, {55: 55}, {56: 56}, {57: 57}, {58: 58}, {59: 59}, {60: 60}, {61: 61}, {62: 62}, {63: 63}, {64: 64}, {65: 65}, {66: 66}, {67: 67}, {68: 68}, {69: 69}, {70: 70}, {71: 71}, {72: 72}, {73: 73}, {74: 74}, {75: 75}, {76: 76}, {77: 77}, {78: 78}, {79: 79}, {80: 80}, {81: 81}, {82: 82}, {83: 83}, {84: 84}, {85: 85}, {86: 86}, {87: 87}, {88: 88}, {89: 89}, {90: 90}, {91: 91}, {92: 92}, {93: 93}, {94: 94}, {95: 95}, {96: 96}, {97: 97}, {98: 98}, {99: 99}]
        if res != exp:
            print("Fel i test 3/57: doubled_odds([{0: 0}, {1: 1}, {2: 2}, {3: 3}, {4: 4}, {5: 5}, {6: 6}, {7: 7}, {8: 8}, {9: 9}, {10: 10}, {11: 11}, {12: 12}, {13: 13}, {14: 14}, {15: 15}, {16: 16}, {17: 17}, {18: 18}, {19: 19}, {20: 20}, {21: 21}, {22: 22}, {23: 23}, {24: 24}, {25: 25}, {26: 26}, {27: 27}, {28: 28}, {29: 29}, {30: 30}, {31: 31}, {32: 32}, {33: 33}, {34: 34}, {35: 35}, {36: 36}, {37: 37}, {38: 38}, {39: 39}, {40: 40}, {41: 41}, {42: 42}, {43: 43}, {44: 44}, {45: 45}, {46: 46}, {47: 47}, {48: 48}, {49: 49}, {50: 50}, {51: 51}, {52: 52}, {53: 53}, {54: 54}, {55: 55}, {56: 56}, {57: 57}, {58: 58}, {59: 59}, {60: 60}, {61: 61}, {62: 62}, {63: 63}, {64: 64}, {65: 65}, {66: 66}, {67: 67}, {68: 68}, {69: 69}, {70: 70}, {71: 71}, {72: 72}, {73: 73}, {74: 74}, {75: 75}, {76: 76}, {77: 77}, {78: 78}, {79: 79}, {80: 80}, {81: 81}, {82: 82}, {83: 83}, {84: 84}, {85: 85}, {86: 86}, {87: 87}, {88: 88}, {89: 89}, {90: 90}, {91: 91}, {92: 92}, {93: 93}, {94: 94}, {95: 95}, {96: 96}, {97: 97}, {98: 98}, {99: 99}])")
            print("Korrekt svar: {0: 0}, {1: 1}, {2: 2}, {3: 3}, {4: 4}, {5: 5}, {6: 6}, {7: 7}, {8: 8}, {9: 9}, {10: 10}, {11: 11}, {12: 12}, {13: 13}, {14: 14}, {15: 15}, {16: 16}, {17: 17}, {18: 18}, {19: 19}, {20: 20}, {21: 21}, {22: 22}, {23: 23}, {24: 24}, {25: 25}, {26: 26}, {27: 27}, {28: 28}, {29: 29}, {30: 30}, {31: 31}, {32: 32}, {33: 33}, {34: 34}, {35: 35}, {36: 36}, {37: 37}, {38: 38}, {39: 39}, {40: 40}, {41: 41}, {42: 42}, {43: 43}, {44: 44}, {45: 45}, {46: 46}, {47: 47}, {48: 48}, {49: 49}, {50: 50}, {51: 51}, {52: 52}, {53: 53}, {54: 54}, {55: 55}, {56: 56}, {57: 57}, {58: 58}, {59: 59}, {60: 60}, {61: 61}, {62: 62}, {63: 63}, {64: 64}, {65: 65}, {66: 66}, {67: 67}, {68: 68}, {69: 69}, {70: 70}, {71: 71}, {72: 72}, {73: 73}, {74: 74}, {75: 75}, {76: 76}, {77: 77}, {78: 78}, {79: 79}, {80: 80}, {81: 81}, {82: 82}, {83: 83}, {84: 84}, {85: 85}, {86: 86}, {87: 87}, {88: 88}, {89: 89}, {90: 90}, {91: 91}, {92: 92}, {93: 93}, {94: 94}, {95: 95}, {96: 96}, {97: 97}, {98: 98}, {99: 99}")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/57: Exception')
        print_exception()

    try:
        res = doubled_odds([set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()])
        exp = [set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()]
        if res != exp:
            print("Fel i test 3/58: doubled_odds([set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()])")
            print("Korrekt svar: set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/58: Exception')
        print_exception()

    try:
        res = doubled_odds([{-100}, {-99}, {-98}, {-97}, {-96}, {-95}, {-94}, {-93}, {-92}, {-91}, {-90}, {-89}, {-88}, {-87}, {-86}, {-85}, {-84}, {-83}, {-82}, {-81}, {-80}, {-79}, {-78}, {-77}, {-76}, {-75}, {-74}, {-73}, {-72}, {-71}, {-70}, {-69}, {-68}, {-67}, {-66}, {-65}, {-64}, {-63}, {-62}, {-61}, {-60}, {-59}, {-58}, {-57}, {-56}, {-55}, {-54}, {-53}, {-52}, {-51}, {-50}, {-49}, {-48}, {-47}, {-46}, {-45}, {-44}, {-43}, {-42}, {-41}, {-40}, {-39}, {-38}, {-37}, {-36}, {-35}, {-34}, {-33}, {-32}, {-31}, {-30}, {-29}, {-28}, {-27}, {-26}, {-25}, {-24}, {-23}, {-22}, {-21}, {-20}, {-19}, {-18}, {-17}, {-16}, {-15}, {-14}, {-13}, {-12}, {-11}, {-10}, {-9}, {-8}, {-7}, {-6}, {-5}, {-4}, {-3}, {-2}, {-1}, {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}, {24}, {25}, {26}, {27}, {28}, {29}, {30}, {31}, {32}, {33}, {34}, {35}, {36}, {37}, {38}, {39}, {40}, {41}, {42}, {43}, {44}, {45}, {46}, {47}, {48}, {49}, {50}, {51}, {52}, {53}, {54}, {55}, {56}, {57}, {58}, {59}, {60}, {61}, {62}, {63}, {64}, {65}, {66}, {67}, {68}, {69}, {70}, {71}, {72}, {73}, {74}, {75}, {76}, {77}, {78}, {79}, {80}, {81}, {82}, {83}, {84}, {85}, {86}, {87}, {88}, {89}, {90}, {91}, {92}, {93}, {94}, {95}, {96}, {97}, {98}, {99}])
        exp = [{-100}, {-99}, {-98}, {-97}, {-96}, {-95}, {-94}, {-93}, {-92}, {-91}, {-90}, {-89}, {-88}, {-87}, {-86}, {-85}, {-84}, {-83}, {-82}, {-81}, {-80}, {-79}, {-78}, {-77}, {-76}, {-75}, {-74}, {-73}, {-72}, {-71}, {-70}, {-69}, {-68}, {-67}, {-66}, {-65}, {-64}, {-63}, {-62}, {-61}, {-60}, {-59}, {-58}, {-57}, {-56}, {-55}, {-54}, {-53}, {-52}, {-51}, {-50}, {-49}, {-48}, {-47}, {-46}, {-45}, {-44}, {-43}, {-42}, {-41}, {-40}, {-39}, {-38}, {-37}, {-36}, {-35}, {-34}, {-33}, {-32}, {-31}, {-30}, {-29}, {-28}, {-27}, {-26}, {-25}, {-24}, {-23}, {-22}, {-21}, {-20}, {-19}, {-18}, {-17}, {-16}, {-15}, {-14}, {-13}, {-12}, {-11}, {-10}, {-9}, {-8}, {-7}, {-6}, {-5}, {-4}, {-3}, {-2}, {-1}, {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}, {24}, {25}, {26}, {27}, {28}, {29}, {30}, {31}, {32}, {33}, {34}, {35}, {36}, {37}, {38}, {39}, {40}, {41}, {42}, {43}, {44}, {45}, {46}, {47}, {48}, {49}, {50}, {51}, {52}, {53}, {54}, {55}, {56}, {57}, {58}, {59}, {60}, {61}, {62}, {63}, {64}, {65}, {66}, {67}, {68}, {69}, {70}, {71}, {72}, {73}, {74}, {75}, {76}, {77}, {78}, {79}, {80}, {81}, {82}, {83}, {84}, {85}, {86}, {87}, {88}, {89}, {90}, {91}, {92}, {93}, {94}, {95}, {96}, {97}, {98}, {99}]
        if res != exp:
            print("Fel i test 3/59: doubled_odds([{-100}, {-99}, {-98}, {-97}, {-96}, {-95}, {-94}, {-93}, {-92}, {-91}, {-90}, {-89}, {-88}, {-87}, {-86}, {-85}, {-84}, {-83}, {-82}, {-81}, {-80}, {-79}, {-78}, {-77}, {-76}, {-75}, {-74}, {-73}, {-72}, {-71}, {-70}, {-69}, {-68}, {-67}, {-66}, {-65}, {-64}, {-63}, {-62}, {-61}, {-60}, {-59}, {-58}, {-57}, {-56}, {-55}, {-54}, {-53}, {-52}, {-51}, {-50}, {-49}, {-48}, {-47}, {-46}, {-45}, {-44}, {-43}, {-42}, {-41}, {-40}, {-39}, {-38}, {-37}, {-36}, {-35}, {-34}, {-33}, {-32}, {-31}, {-30}, {-29}, {-28}, {-27}, {-26}, {-25}, {-24}, {-23}, {-22}, {-21}, {-20}, {-19}, {-18}, {-17}, {-16}, {-15}, {-14}, {-13}, {-12}, {-11}, {-10}, {-9}, {-8}, {-7}, {-6}, {-5}, {-4}, {-3}, {-2}, {-1}, {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}, {24}, {25}, {26}, {27}, {28}, {29}, {30}, {31}, {32}, {33}, {34}, {35}, {36}, {37}, {38}, {39}, {40}, {41}, {42}, {43}, {44}, {45}, {46}, {47}, {48}, {49}, {50}, {51}, {52}, {53}, {54}, {55}, {56}, {57}, {58}, {59}, {60}, {61}, {62}, {63}, {64}, {65}, {66}, {67}, {68}, {69}, {70}, {71}, {72}, {73}, {74}, {75}, {76}, {77}, {78}, {79}, {80}, {81}, {82}, {83}, {84}, {85}, {86}, {87}, {88}, {89}, {90}, {91}, {92}, {93}, {94}, {95}, {96}, {97}, {98}, {99}])")
            print("Korrekt svar: {-100}, {-99}, {-98}, {-97}, {-96}, {-95}, {-94}, {-93}, {-92}, {-91}, {-90}, {-89}, {-88}, {-87}, {-86}, {-85}, {-84}, {-83}, {-82}, {-81}, {-80}, {-79}, {-78}, {-77}, {-76}, {-75}, {-74}, {-73}, {-72}, {-71}, {-70}, {-69}, {-68}, {-67}, {-66}, {-65}, {-64}, {-63}, {-62}, {-61}, {-60}, {-59}, {-58}, {-57}, {-56}, {-55}, {-54}, {-53}, {-52}, {-51}, {-50}, {-49}, {-48}, {-47}, {-46}, {-45}, {-44}, {-43}, {-42}, {-41}, {-40}, {-39}, {-38}, {-37}, {-36}, {-35}, {-34}, {-33}, {-32}, {-31}, {-30}, {-29}, {-28}, {-27}, {-26}, {-25}, {-24}, {-23}, {-22}, {-21}, {-20}, {-19}, {-18}, {-17}, {-16}, {-15}, {-14}, {-13}, {-12}, {-11}, {-10}, {-9}, {-8}, {-7}, {-6}, {-5}, {-4}, {-3}, {-2}, {-1}, {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}, {24}, {25}, {26}, {27}, {28}, {29}, {30}, {31}, {32}, {33}, {34}, {35}, {36}, {37}, {38}, {39}, {40}, {41}, {42}, {43}, {44}, {45}, {46}, {47}, {48}, {49}, {50}, {51}, {52}, {53}, {54}, {55}, {56}, {57}, {58}, {59}, {60}, {61}, {62}, {63}, {64}, {65}, {66}, {67}, {68}, {69}, {70}, {71}, {72}, {73}, {74}, {75}, {76}, {77}, {78}, {79}, {80}, {81}, {82}, {83}, {84}, {85}, {86}, {87}, {88}, {89}, {90}, {91}, {92}, {93}, {94}, {95}, {96}, {97}, {98}, {99}")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/59: Exception')
        print_exception()

    try:
        res = doubled_odds([{}, set(), (), []])
        exp = [{}, set(), (), []]
        if res != exp:
            print("Fel i test 3/60: doubled_odds([{}, set(), (), []])")
            print("Korrekt svar: {}, set(), (), []")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/60: Exception')
        print_exception()

    try:
        res = doubled_odds([{1, 2, '3'}, [1, '2', 3], {'1': 1, 2: '2', 3: '3'}, (1, 2, '3')])
        exp = [{1, 2, '3'}, [2, '2', 6], {'1': 1, 2: '2', 3: '3'}, (1, 2, '3')]
        if res != exp:
            print("Fel i test 3/61: doubled_odds([{1, 2, '3'}, [1, '2', 3], {'1': 1, 2: '2', 3: '3'}, (1, 2, '3')])")
            print("Korrekt svar: {1, 2, '3'}, [2, '2', 6], {'1': 1, 2: '2', 3: '3'}, (1, 2, '3')")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/61: Exception')
        print_exception()

    try:
        res = doubled_odds([[set(), (2, 'a'), {1: 'a'}], {2, 3, (1, 'a', False)}, {'1': [1, 2, 3], '2': {}}, (set(), [2], {1: '1'})])
        exp = [[set(), (2, 'a'), {1: 'a'}], {2, 3, (1, 'a', False)}, {'1': [1, 2, 3], '2': {}}, (set(), [2], {1: '1'})]
        if res != exp:
            print("Fel i test 3/62: doubled_odds([[set(), (2, 'a'), {1: 'a'}], {2, 3, (1, 'a', False)}, {'1': [1, 2, 3], '2': {}}, (set(), [2], {1: '1'})])")
            print("Korrekt svar: [set(), (2, 'a'), {1: 'a'}], {2, 3, (1, 'a', False)}, {'1': [1, 2, 3], '2': {}}, (set(), [2], {1: '1'})")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/62: Exception')
        print_exception()



    try:
        res = doubled_odds([int])
        exp = [int]
        if res != exp:
            print("Fel i test 3/65: doubled_odds([int])")
            print("Korrekt svar: <class '__main__.int'>")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/65: Exception')
        print_exception()

    try:
        res = doubled_odds([int, list])
        exp = [int, list]
        if res != exp:
            print("Fel i test 3/66: doubled_odds([int, list])")
            print("Korrekt svar: <class '__main__.int'>, <class '__main__.list'>")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/66: Exception')
        print_exception()

    try:
        res = doubled_odds([1, {'a': 2}, 3])
        exp = [2, {'a': 2}, 6]
        if res != exp:
            print("Fel i test 3/67: doubled_odds([1, {'a': 2}, 3])")
            print("Korrekt svar: 2, {'a': 2}, 6")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/67: Exception')
        print_exception()

    try:
        res = doubled_odds([[1, 2, 3], '123'])
        exp = [[2, 2, 6], '123']
        if res != exp:
            print("Fel i test 3/68: doubled_odds([[1, 2, 3], '123'])")
            print("Korrekt svar: [2, 2, 6], '123'")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/68: Exception')
        print_exception()

    try:
        res = doubled_odds([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399])
        exp = [0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90, 182, 92, 186, 94, 190, 96, 194, 98, 198, 100, 202, 102, 206, 104, 210, 106, 214, 108, 218, 110, 222, 112, 226, 114, 230, 116, 234, 118, 238, 120, 242, 122, 246, 124, 250, 126, 254, 128, 258, 130, 262, 132, 266, 134, 270, 136, 274, 138, 278, 140, 282, 142, 286, 144, 290, 146, 294, 148, 298, 150, 302, 152, 306, 154, 310, 156, 314, 158, 318, 160, 322, 162, 326, 164, 330, 166, 334, 168, 338, 170, 342, 172, 346, 174, 350, 176, 354, 178, 358, 180, 362, 182, 366, 184, 370, 186, 374, 188, 378, 190, 382, 192, 386, 194, 390, 196, 394, 198, 398, 200, 402, 202, 406, 204, 410, 206, 414, 208, 418, 210, 422, 212, 426, 214, 430, 216, 434, 218, 438, 220, 442, 222, 446, 224, 450, 226, 454, 228, 458, 230, 462, 232, 466, 234, 470, 236, 474, 238, 478, 240, 482, 242, 486, 244, 490, 246, 494, 248, 498, 250, 502, 252, 506, 254, 510, 256, 514, 258, 518, 260, 522, 262, 526, 264, 530, 266, 534, 268, 538, 270, 542, 272, 546, 274, 550, 276, 554, 278, 558, 280, 562, 282, 566, 284, 570, 286, 574, 288, 578, 290, 582, 292, 586, 294, 590, 296, 594, 298, 598, 300, 602, 302, 606, 304, 610, 306, 614, 308, 618, 310, 622, 312, 626, 314, 630, 316, 634, 318, 638, 320, 642, 322, 646, 324, 650, 326, 654, 328, 658, 330, 662, 332, 666, 334, 670, 336, 674, 338, 678, 340, 682, 342, 686, 344, 690, 346, 694, 348, 698, 350, 702, 352, 706, 354, 710, 356, 714, 358, 718, 360, 722, 362, 726, 364, 730, 366, 734, 368, 738, 370, 742, 372, 746, 374, 750, 376, 754, 378, 758, 380, 762, 382, 766, 384, 770, 386, 774, 388, 778, 390, 782, 392, 786, 394, 790, 396, 794, 398, 798]
        if res != exp:
            print("Fel i test 3/69: doubled_odds([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399])")
            print("Korrekt svar: 0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90, 182, 92, 186, 94, 190, 96, 194, 98, 198, 100, 202, 102, 206, 104, 210, 106, 214, 108, 218, 110, 222, 112, 226, 114, 230, 116, 234, 118, 238, 120, 242, 122, 246, 124, 250, 126, 254, 128, 258, 130, 262, 132, 266, 134, 270, 136, 274, 138, 278, 140, 282, 142, 286, 144, 290, 146, 294, 148, 298, 150, 302, 152, 306, 154, 310, 156, 314, 158, 318, 160, 322, 162, 326, 164, 330, 166, 334, 168, 338, 170, 342, 172, 346, 174, 350, 176, 354, 178, 358, 180, 362, 182, 366, 184, 370, 186, 374, 188, 378, 190, 382, 192, 386, 194, 390, 196, 394, 198, 398, 200, 402, 202, 406, 204, 410, 206, 414, 208, 418, 210, 422, 212, 426, 214, 430, 216, 434, 218, 438, 220, 442, 222, 446, 224, 450, 226, 454, 228, 458, 230, 462, 232, 466, 234, 470, 236, 474, 238, 478, 240, 482, 242, 486, 244, 490, 246, 494, 248, 498, 250, 502, 252, 506, 254, 510, 256, 514, 258, 518, 260, 522, 262, 526, 264, 530, 266, 534, 268, 538, 270, 542, 272, 546, 274, 550, 276, 554, 278, 558, 280, 562, 282, 566, 284, 570, 286, 574, 288, 578, 290, 582, 292, 586, 294, 590, 296, 594, 298, 598, 300, 602, 302, 606, 304, 610, 306, 614, 308, 618, 310, 622, 312, 626, 314, 630, 316, 634, 318, 638, 320, 642, 322, 646, 324, 650, 326, 654, 328, 658, 330, 662, 332, 666, 334, 670, 336, 674, 338, 678, 340, 682, 342, 686, 344, 690, 346, 694, 348, 698, 350, 702, 352, 706, 354, 710, 356, 714, 358, 718, 360, 722, 362, 726, 364, 730, 366, 734, 368, 738, 370, 742, 372, 746, 374, 750, 376, 754, 378, 758, 380, 762, 382, 766, 384, 770, 386, 774, 388, 778, 390, 782, 392, 786, 394, 790, 396, 794, 398, 798")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/69: Exception')
        print_exception()

    try:
        res = doubled_odds([-400, -399, -398, -397, -396, -395, -394, -393, -392, -391, -390, -389, -388, -387, -386, -385, -384, -383, -382, -381, -380, -379, -378, -377, -376, -375, -374, -373, -372, -371, -370, -369, -368, -367, -366, -365, -364, -363, -362, -361, -360, -359, -358, -357, -356, -355, -354, -353, -352, -351, -350, -349, -348, -347, -346, -345, -344, -343, -342, -341, -340, -339, -338, -337, -336, -335, -334, -333, -332, -331, -330, -329, -328, -327, -326, -325, -324, -323, -322, -321, -320, -319, -318, -317, -316, -315, -314, -313, -312, -311, -310, -309, -308, -307, -306, -305, -304, -303, -302, -301, -300, -299, -298, -297, -296, -295, -294, -293, -292, -291, -290, -289, -288, -287, -286, -285, -284, -283, -282, -281, -280, -279, -278, -277, -276, -275, -274, -273, -272, -271, -270, -269, -268, -267, -266, -265, -264, -263, -262, -261, -260, -259, -258, -257, -256, -255, -254, -253, -252, -251, -250, -249, -248, -247, -246, -245, -244, -243, -242, -241, -240, -239, -238, -237, -236, -235, -234, -233, -232, -231, -230, -229, -228, -227, -226, -225, -224, -223, -222, -221, -220, -219, -218, -217, -216, -215, -214, -213, -212, -211, -210, -209, -208, -207, -206, -205, -204, -203, -202, -201, -200, -199, -198, -197, -196, -195, -194, -193, -192, -191, -190, -189, -188, -187, -186, -185, -184, -183, -182, -181, -180, -179, -178, -177, -176, -175, -174, -173, -172, -171, -170, -169, -168, -167, -166, -165, -164, -163, -162, -161, -160, -159, -158, -157, -156, -155, -154, -153, -152, -151, -150, -149, -148, -147, -146, -145, -144, -143, -142, -141, -140, -139, -138, -137, -136, -135, -134, -133, -132, -131, -130, -129, -128, -127, -126, -125, -124, -123, -122, -121, -120, -119, -118, -117, -116, -115, -114, -113, -112, -111, -110, -109, -108, -107, -106, -105, -104, -103, -102, -101, -100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399])
        exp = [-400, -798, -398, -794, -396, -790, -394, -786, -392, -782, -390, -778, -388, -774, -386, -770, -384, -766, -382, -762, -380, -758, -378, -754, -376, -750, -374, -746, -372, -742, -370, -738, -368, -734, -366, -730, -364, -726, -362, -722, -360, -718, -358, -714, -356, -710, -354, -706, -352, -702, -350, -698, -348, -694, -346, -690, -344, -686, -342, -682, -340, -678, -338, -674, -336, -670, -334, -666, -332, -662, -330, -658, -328, -654, -326, -650, -324, -646, -322, -642, -320, -638, -318, -634, -316, -630, -314, -626, -312, -622, -310, -618, -308, -614, -306, -610, -304, -606, -302, -602, -300, -598, -298, -594, -296, -590, -294, -586, -292, -582, -290, -578, -288, -574, -286, -570, -284, -566, -282, -562, -280, -558, -278, -554, -276, -550, -274, -546, -272, -542, -270, -538, -268, -534, -266, -530, -264, -526, -262, -522, -260, -518, -258, -514, -256, -510, -254, -506, -252, -502, -250, -498, -248, -494, -246, -490, -244, -486, -242, -482, -240, -478, -238, -474, -236, -470, -234, -466, -232, -462, -230, -458, -228, -454, -226, -450, -224, -446, -222, -442, -220, -438, -218, -434, -216, -430, -214, -426, -212, -422, -210, -418, -208, -414, -206, -410, -204, -406, -202, -402, -200, -398, -198, -394, -196, -390, -194, -386, -192, -382, -190, -378, -188, -374, -186, -370, -184, -366, -182, -362, -180, -358, -178, -354, -176, -350, -174, -346, -172, -342, -170, -338, -168, -334, -166, -330, -164, -326, -162, -322, -160, -318, -158, -314, -156, -310, -154, -306, -152, -302, -150, -298, -148, -294, -146, -290, -144, -286, -142, -282, -140, -278, -138, -274, -136, -270, -134, -266, -132, -262, -130, -258, -128, -254, -126, -250, -124, -246, -122, -242, -120, -238, -118, -234, -116, -230, -114, -226, -112, -222, -110, -218, -108, -214, -106, -210, -104, -206, -102, -202, -100, -198, -98, -194, -96, -190, -94, -186, -92, -182, -90, -178, -88, -174, -86, -170, -84, -166, -82, -162, -80, -158, -78, -154, -76, -150, -74, -146, -72, -142, -70, -138, -68, -134, -66, -130, -64, -126, -62, -122, -60, -118, -58, -114, -56, -110, -54, -106, -52, -102, -50, -98, -48, -94, -46, -90, -44, -86, -42, -82, -40, -78, -38, -74, -36, -70, -34, -66, -32, -62, -30, -58, -28, -54, -26, -50, -24, -46, -22, -42, -20, -38, -18, -34, -16, -30, -14, -26, -12, -22, -10, -18, -8, -14, -6, -10, -4, -6, -2, -2, 0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90, 182, 92, 186, 94, 190, 96, 194, 98, 198, 100, 202, 102, 206, 104, 210, 106, 214, 108, 218, 110, 222, 112, 226, 114, 230, 116, 234, 118, 238, 120, 242, 122, 246, 124, 250, 126, 254, 128, 258, 130, 262, 132, 266, 134, 270, 136, 274, 138, 278, 140, 282, 142, 286, 144, 290, 146, 294, 148, 298, 150, 302, 152, 306, 154, 310, 156, 314, 158, 318, 160, 322, 162, 326, 164, 330, 166, 334, 168, 338, 170, 342, 172, 346, 174, 350, 176, 354, 178, 358, 180, 362, 182, 366, 184, 370, 186, 374, 188, 378, 190, 382, 192, 386, 194, 390, 196, 394, 198, 398, 200, 402, 202, 406, 204, 410, 206, 414, 208, 418, 210, 422, 212, 426, 214, 430, 216, 434, 218, 438, 220, 442, 222, 446, 224, 450, 226, 454, 228, 458, 230, 462, 232, 466, 234, 470, 236, 474, 238, 478, 240, 482, 242, 486, 244, 490, 246, 494, 248, 498, 250, 502, 252, 506, 254, 510, 256, 514, 258, 518, 260, 522, 262, 526, 264, 530, 266, 534, 268, 538, 270, 542, 272, 546, 274, 550, 276, 554, 278, 558, 280, 562, 282, 566, 284, 570, 286, 574, 288, 578, 290, 582, 292, 586, 294, 590, 296, 594, 298, 598, 300, 602, 302, 606, 304, 610, 306, 614, 308, 618, 310, 622, 312, 626, 314, 630, 316, 634, 318, 638, 320, 642, 322, 646, 324, 650, 326, 654, 328, 658, 330, 662, 332, 666, 334, 670, 336, 674, 338, 678, 340, 682, 342, 686, 344, 690, 346, 694, 348, 698, 350, 702, 352, 706, 354, 710, 356, 714, 358, 718, 360, 722, 362, 726, 364, 730, 366, 734, 368, 738, 370, 742, 372, 746, 374, 750, 376, 754, 378, 758, 380, 762, 382, 766, 384, 770, 386, 774, 388, 778, 390, 782, 392, 786, 394, 790, 396, 794, 398, 798]
        if res != exp:
            print("Fel i test 3/70: doubled_odds([-400, -399, -398, -397, -396, -395, -394, -393, -392, -391, -390, -389, -388, -387, -386, -385, -384, -383, -382, -381, -380, -379, -378, -377, -376, -375, -374, -373, -372, -371, -370, -369, -368, -367, -366, -365, -364, -363, -362, -361, -360, -359, -358, -357, -356, -355, -354, -353, -352, -351, -350, -349, -348, -347, -346, -345, -344, -343, -342, -341, -340, -339, -338, -337, -336, -335, -334, -333, -332, -331, -330, -329, -328, -327, -326, -325, -324, -323, -322, -321, -320, -319, -318, -317, -316, -315, -314, -313, -312, -311, -310, -309, -308, -307, -306, -305, -304, -303, -302, -301, -300, -299, -298, -297, -296, -295, -294, -293, -292, -291, -290, -289, -288, -287, -286, -285, -284, -283, -282, -281, -280, -279, -278, -277, -276, -275, -274, -273, -272, -271, -270, -269, -268, -267, -266, -265, -264, -263, -262, -261, -260, -259, -258, -257, -256, -255, -254, -253, -252, -251, -250, -249, -248, -247, -246, -245, -244, -243, -242, -241, -240, -239, -238, -237, -236, -235, -234, -233, -232, -231, -230, -229, -228, -227, -226, -225, -224, -223, -222, -221, -220, -219, -218, -217, -216, -215, -214, -213, -212, -211, -210, -209, -208, -207, -206, -205, -204, -203, -202, -201, -200, -199, -198, -197, -196, -195, -194, -193, -192, -191, -190, -189, -188, -187, -186, -185, -184, -183, -182, -181, -180, -179, -178, -177, -176, -175, -174, -173, -172, -171, -170, -169, -168, -167, -166, -165, -164, -163, -162, -161, -160, -159, -158, -157, -156, -155, -154, -153, -152, -151, -150, -149, -148, -147, -146, -145, -144, -143, -142, -141, -140, -139, -138, -137, -136, -135, -134, -133, -132, -131, -130, -129, -128, -127, -126, -125, -124, -123, -122, -121, -120, -119, -118, -117, -116, -115, -114, -113, -112, -111, -110, -109, -108, -107, -106, -105, -104, -103, -102, -101, -100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399])")
            print("Korrekt svar: -400, -798, -398, -794, -396, -790, -394, -786, -392, -782, -390, -778, -388, -774, -386, -770, -384, -766, -382, -762, -380, -758, -378, -754, -376, -750, -374, -746, -372, -742, -370, -738, -368, -734, -366, -730, -364, -726, -362, -722, -360, -718, -358, -714, -356, -710, -354, -706, -352, -702, -350, -698, -348, -694, -346, -690, -344, -686, -342, -682, -340, -678, -338, -674, -336, -670, -334, -666, -332, -662, -330, -658, -328, -654, -326, -650, -324, -646, -322, -642, -320, -638, -318, -634, -316, -630, -314, -626, -312, -622, -310, -618, -308, -614, -306, -610, -304, -606, -302, -602, -300, -598, -298, -594, -296, -590, -294, -586, -292, -582, -290, -578, -288, -574, -286, -570, -284, -566, -282, -562, -280, -558, -278, -554, -276, -550, -274, -546, -272, -542, -270, -538, -268, -534, -266, -530, -264, -526, -262, -522, -260, -518, -258, -514, -256, -510, -254, -506, -252, -502, -250, -498, -248, -494, -246, -490, -244, -486, -242, -482, -240, -478, -238, -474, -236, -470, -234, -466, -232, -462, -230, -458, -228, -454, -226, -450, -224, -446, -222, -442, -220, -438, -218, -434, -216, -430, -214, -426, -212, -422, -210, -418, -208, -414, -206, -410, -204, -406, -202, -402, -200, -398, -198, -394, -196, -390, -194, -386, -192, -382, -190, -378, -188, -374, -186, -370, -184, -366, -182, -362, -180, -358, -178, -354, -176, -350, -174, -346, -172, -342, -170, -338, -168, -334, -166, -330, -164, -326, -162, -322, -160, -318, -158, -314, -156, -310, -154, -306, -152, -302, -150, -298, -148, -294, -146, -290, -144, -286, -142, -282, -140, -278, -138, -274, -136, -270, -134, -266, -132, -262, -130, -258, -128, -254, -126, -250, -124, -246, -122, -242, -120, -238, -118, -234, -116, -230, -114, -226, -112, -222, -110, -218, -108, -214, -106, -210, -104, -206, -102, -202, -100, -198, -98, -194, -96, -190, -94, -186, -92, -182, -90, -178, -88, -174, -86, -170, -84, -166, -82, -162, -80, -158, -78, -154, -76, -150, -74, -146, -72, -142, -70, -138, -68, -134, -66, -130, -64, -126, -62, -122, -60, -118, -58, -114, -56, -110, -54, -106, -52, -102, -50, -98, -48, -94, -46, -90, -44, -86, -42, -82, -40, -78, -38, -74, -36, -70, -34, -66, -32, -62, -30, -58, -28, -54, -26, -50, -24, -46, -22, -42, -20, -38, -18, -34, -16, -30, -14, -26, -12, -22, -10, -18, -8, -14, -6, -10, -4, -6, -2, -2, 0, 2, 2, 6, 4, 10, 6, 14, 8, 18, 10, 22, 12, 26, 14, 30, 16, 34, 18, 38, 20, 42, 22, 46, 24, 50, 26, 54, 28, 58, 30, 62, 32, 66, 34, 70, 36, 74, 38, 78, 40, 82, 42, 86, 44, 90, 46, 94, 48, 98, 50, 102, 52, 106, 54, 110, 56, 114, 58, 118, 60, 122, 62, 126, 64, 130, 66, 134, 68, 138, 70, 142, 72, 146, 74, 150, 76, 154, 78, 158, 80, 162, 82, 166, 84, 170, 86, 174, 88, 178, 90, 182, 92, 186, 94, 190, 96, 194, 98, 198, 100, 202, 102, 206, 104, 210, 106, 214, 108, 218, 110, 222, 112, 226, 114, 230, 116, 234, 118, 238, 120, 242, 122, 246, 124, 250, 126, 254, 128, 258, 130, 262, 132, 266, 134, 270, 136, 274, 138, 278, 140, 282, 142, 286, 144, 290, 146, 294, 148, 298, 150, 302, 152, 306, 154, 310, 156, 314, 158, 318, 160, 322, 162, 326, 164, 330, 166, 334, 168, 338, 170, 342, 172, 346, 174, 350, 176, 354, 178, 358, 180, 362, 182, 366, 184, 370, 186, 374, 188, 378, 190, 382, 192, 386, 194, 390, 196, 394, 198, 398, 200, 402, 202, 406, 204, 410, 206, 414, 208, 418, 210, 422, 212, 426, 214, 430, 216, 434, 218, 438, 220, 442, 222, 446, 224, 450, 226, 454, 228, 458, 230, 462, 232, 466, 234, 470, 236, 474, 238, 478, 240, 482, 242, 486, 244, 490, 246, 494, 248, 498, 250, 502, 252, 506, 254, 510, 256, 514, 258, 518, 260, 522, 262, 526, 264, 530, 266, 534, 268, 538, 270, 542, 272, 546, 274, 550, 276, 554, 278, 558, 280, 562, 282, 566, 284, 570, 286, 574, 288, 578, 290, 582, 292, 586, 294, 590, 296, 594, 298, 598, 300, 602, 302, 606, 304, 610, 306, 614, 308, 618, 310, 622, 312, 626, 314, 630, 316, 634, 318, 638, 320, 642, 322, 646, 324, 650, 326, 654, 328, 658, 330, 662, 332, 666, 334, 670, 336, 674, 338, 678, 340, 682, 342, 686, 344, 690, 346, 694, 348, 698, 350, 702, 352, 706, 354, 710, 356, 714, 358, 718, 360, 722, 362, 726, 364, 730, 366, 734, 368, 738, 370, 742, 372, 746, 374, 750, 376, 754, 378, 758, 380, 762, 382, 766, 384, 770, 386, 774, 388, 778, 390, 782, 392, 786, 394, 790, 396, 794, 398, 798")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 3/70: Exception')
        print_exception()


    print('Klar med tester fÃ¶r uppgift 3')
    print()


def test_4a():
    print('PÃ¥bÃ¶rjar tester fÃ¶r uppgift 4a')


    try:
        res = multiple_apply(plus_one, 10)(0)
        exp = 10
        if res != exp:
            print("Fel i test 4a/2: multiple_apply(plus_one, 10)(0)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/2: Exception')
        print_exception()

    try:
        res = multiple_apply(plus_one, 0)(0)
        exp = 0
        if res != exp:
            print("Fel i test 4a/4: multiple_apply(plus_one, 0)(0)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/4: Exception')
        print_exception()

    try:
        res = multiple_apply(const_one, 0)(0)
        exp = 0
        if res != exp:
            print("Fel i test 4a/6: multiple_apply(const_one, 0)(0)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/6: Exception')
        print_exception()

    try:
        res = multiple_apply(plus_one, 0)(-7)
        exp = -7
        if res != exp:
            print("Fel i test 4a/8: multiple_apply(plus_one, 0)(-7)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/8: Exception')
        print_exception()

    try:
        res = multiple_apply(const_one, 10)(3)
        exp = 1
        if res != exp:
            print("Fel i test 4a/10: multiple_apply(const_one, 10)(3)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/10: Exception')
        print_exception()

    try:
        res = multiple_apply(lambda x: x, 10)(3)
        exp = 3
        if res != exp:
            print("Fel i test 4a/12: multiple_apply(lambda x: x, 10)(3)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/12: Exception')
        print_exception()

    try:
        res = multiple_apply(plus_one, 10)(3)
        exp = 13
        if res != exp:
            print("Fel i test 4a/14: multiple_apply(plus_one, 10)(3)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/14: Exception')
        print_exception()

    try:
        res = multiple_apply(minus_one, 10)(3)
        exp = -7
        if res != exp:
            print("Fel i test 4a/16: multiple_apply(minus_one, 10)(3)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/16: Exception')
        print_exception()

    try:
        res = multiple_apply(times_two, 4)(3)
        exp = 48
        if res != exp:
            print("Fel i test 4a/18: multiple_apply(times_two, 4)(3)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/18: Exception')
        print_exception()

    try:
        res = multiple_apply(lambda x: x / 1, 10)(-3)
        exp = -3
        if res != exp:
            print("Fel i test 4a/20: multiple_apply(lambda x: x / 1, 10)(-3)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/20: Exception')
        print_exception()

    try:
        res = multiple_apply(lambda x: x % 16, 10)(17)
        exp = 1
        if res != exp:
            print("Fel i test 4a/22: multiple_apply(lambda x: x % 16, 10)(17)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/22: Exception')
        print_exception()

    try:
        res = multiple_apply(lambda x: x ** 2, 3)(2)
        exp = 256
        if res != exp:
            print("Fel i test 4a/24: multiple_apply(lambda x: x ** 2, 3)(2)")
            print("Korrekt svar: 5")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/24: Exception')
        print_exception()

    try:
        res = multiple_apply(lambda x: x + float(x), 5)(3)
        exp = 96.0
        if res != exp:
            print("Fel i test 4a/26: multiple_apply(lambda x: x + float(x), 5)(3)")
            print("Korrekt svar: 6.")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/26: Exception')
        print_exception()

    try:
        res = multiple_apply(lambda x: x + abs(x - 10), 10)(1)
        exp = 10
        if res != exp:
            print("Fel i test 4a/28: multiple_apply(lambda x: x + abs(x - 10), 10)(1)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/28: Exception')
        print_exception()

    try:
        res = multiple_apply(lambda x: max(x - 1, x // 2), 10)(100)
        exp = 90
        if res != exp:
            print("Fel i test 4a/30: multiple_apply(lambda x: max(x - 1, x // 2), 10)(100)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/30: Exception')
        print_exception()

    try:
        res = multiple_apply(lambda x: min(x, x + 1), 10)(-5)
        exp = -5
        if res != exp:
            print("Fel i test 4a/32: multiple_apply(lambda x: min(x, x + 1), 10)(-5)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/32: Exception')
        print_exception()

    try:
        res = multiple_apply(lambda x: ord(chr(x)), 10)(41)
        exp = 41
        if res != exp:
            print("Fel i test 4a/34: multiple_apply(lambda x: ord(chr(x)), 10)(41)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/34: Exception')
        print_exception()

    try:
        res = multiple_apply(lambda x: round(x + x / 2), 10)(-274)
        exp = -15786
        if res != exp:
            print("Fel i test 4a/36: multiple_apply(lambda x: round(x + x / 2), 10)(-274)")
            print("Korrekt svar: 1578")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/36: Exception')
        print_exception()

    try:
        res = multiple_apply(lambda x: (x + 1 - 3) * 2 % 17, 10)(3)
        exp = 0
        if res != exp:
            print("Fel i test 4a/38: multiple_apply(lambda x: (x + 1 - 3) * 2 % 17, 10)(3)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/38: Exception')
        print_exception()

    try:
        res = multiple_apply(recursive, 2)(999)
        exp = 55
        if res != exp:
            print("Fel i test 4a/40: multiple_apply(recursive, 2)(999)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/40: Exception')
        print_exception()

    try:
        res = multiple_apply(fib, 3)(6)
        exp = 10946
        if res != exp:
            print("Fel i test 4a/42: multiple_apply(fib, 3)(6)")
            print("Korrekt svar: 094")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/42: Exception')
        print_exception()

    try:
        res = multiple_apply(const_one, 1000)(0)
        exp = 1
        if res != exp:
            print("Fel i test 4a/44: multiple_apply(const_one, 1000)(0)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/44: Exception')
        print_exception()

    try:
        res = multiple_apply(plus_one, 1000)(0)
        exp = 1000
        if res != exp:
            print("Fel i test 4a/46: multiple_apply(plus_one, 1000)(0)")
            print("Korrekt svar: 00")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/46: Exception')
        print_exception()

    try:
        res = multiple_apply(lambda x: x - 3, 250)(999999999999)
        exp = 999999999249
        if res != exp:
            print("Fel i test 4a/48: multiple_apply(lambda x: x - 3, 250)(999999999999)")
            print("Korrekt svar: 9999999924")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/48: Exception')
        print_exception()

    try:
        res = multiple_apply(lambda x: x // 2, 35)(999999999999)
        exp = 29
        if res != exp:
            print("Fel i test 4a/50: multiple_apply(lambda x: x // 2, 35)(999999999999)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/50: Exception')
        print_exception()

    try:
        res = multiple_apply(lambda x: x + 13, 987)(-7653680964356)
        exp = -7653680951525
        if res != exp:
            print("Fel i test 4a/52: multiple_apply(lambda x: x + 13, 987)(-7653680964356)")
            print("Korrekt svar: 765368095152")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/52: Exception')
        print_exception()

    try:
        res = multiple_apply(lambda x: x + abs(x // 2), 47)(-7653680964356)
        exp = 0
        if res != exp:
            print("Fel i test 4a/54: multiple_apply(lambda x: x + abs(x // 2), 47)(-7653680964356)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/54: Exception')
        print_exception()

    try:
        res = multiple_apply(plus_one, 1)(0)
        exp = 1
        if res != exp:
            print("Fel i test 4a/56: multiple_apply(plus_one, 1)(0)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/56: Exception')
        print_exception()

    try:
        res = multiple_apply(const_one, 1)(0)
        exp = 1
        if res != exp:
            print("Fel i test 4a/58: multiple_apply(const_one, 1)(0)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/58: Exception')
        print_exception()

    try:
        res = multiple_apply(plus_one, 1)(-7)
        exp = -6
        if res != exp:
            print("Fel i test 4a/60: multiple_apply(plus_one, 1)(-7)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/60: Exception')
        print_exception()

    try:
        res = multiple_apply(plus_one, 2)(0)
        exp = 2
        if res != exp:
            print("Fel i test 4a/62: multiple_apply(plus_one, 2)(0)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/62: Exception')
        print_exception()

    try:
        res = multiple_apply(const_one, 2)(0)
        exp = 1
        if res != exp:
            print("Fel i test 4a/64: multiple_apply(const_one, 2)(0)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/64: Exception')
        print_exception()

    try:
        res = multiple_apply(plus_one, 2)(-7)
        exp = -5
        if res != exp:
            print("Fel i test 4a/66: multiple_apply(plus_one, 2)(-7)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/66: Exception')
        print_exception()

    try:
        res = multiple_apply(plus_one, 3)(0)
        exp = 3
        if res != exp:
            print("Fel i test 4a/68: multiple_apply(plus_one, 3)(0)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/68: Exception')
        print_exception()

    try:
        res = multiple_apply(const_one, 3)(0)
        exp = 1
        if res != exp:
            print("Fel i test 4a/70: multiple_apply(const_one, 3)(0)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/70: Exception')
        print_exception()

    try:
        res = multiple_apply(plus_one, 3)(-7)
        exp = -4
        if res != exp:
            print("Fel i test 4a/72: multiple_apply(plus_one, 3)(-7)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/72: Exception')
        print_exception()

    try:
        res = multiple_apply(plus_one, 1)(0.5)
        exp = 1.5
        if res != exp:
            print("Fel i test 4a/74: multiple_apply(plus_one, 1)(0.5)")
            print("Korrekt svar: .")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/74: Exception')
        print_exception()

    try:
        res = multiple_apply(plus_one_point_five, 1)(0.5)
        exp = 2.0
        if res != exp:
            print("Fel i test 4a/76: multiple_apply(plus_one_point_five, 1)(0.5)")
            print("Korrekt svar: .")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/76: Exception')
        print_exception()

    try:
        res = multiple_apply(plus_one, 2)(0.5)
        exp = 2.5
        if res != exp:
            print("Fel i test 4a/78: multiple_apply(plus_one, 2)(0.5)")
            print("Korrekt svar: .")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/78: Exception')
        print_exception()

    try:
        res = multiple_apply(plus_one_point_five, 2)(0.5)
        exp = 3.5
        if res != exp:
            print("Fel i test 4a/80: multiple_apply(plus_one_point_five, 2)(0.5)")
            print("Korrekt svar: .")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/80: Exception')
        print_exception()

    try:
        res = multiple_apply(plus_one, 3)(0.5)
        exp = 3.5
        if res != exp:
            print("Fel i test 4a/82: multiple_apply(plus_one, 3)(0.5)")
            print("Korrekt svar: .")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/82: Exception')
        print_exception()

    try:
        res = multiple_apply(plus_one_point_five, 3)(0.5)
        exp = 5.0
        if res != exp:
            print("Fel i test 4a/84: multiple_apply(plus_one_point_five, 3)(0.5)")
            print("Korrekt svar: .")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4a/84: Exception')
        print_exception()

    print('Klar med tester fÃ¶r uppgift 4a')
    print()


def test_4b():
    print('PÃ¥bÃ¶rjar tester fÃ¶r uppgift 4b')

    try:
        res = pow2mult(3, 1)
        exp = 8
        if res != exp:
            print("Fel i test 4b/1: pow2mult(3, 1)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4b/1: Exception')
        print_exception()

    try:
        res = pow2mult(3, 3)
        exp = 24
        if res != exp:
            print("Fel i test 4b/2: pow2mult(3, 3)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4b/2: Exception')
        print_exception()

    try:
        res = pow2mult(0, 3)
        exp = 3
        if res != exp:
            print("Fel i test 4b/3: pow2mult(0, 3)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4b/3: Exception')
        print_exception()

    try:
        res = pow2mult(15, 0)
        exp = 0
        if res != exp:
            print("Fel i test 4b/4: pow2mult(15, 0)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4b/4: Exception')
        print_exception()

    try:
        res = pow2mult(0, 0)
        exp = 0
        if res != exp:
            print("Fel i test 4b/5: pow2mult(0, 0)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4b/5: Exception')
        print_exception()

    try:
        res = pow2mult(0, -4)
        exp = -4
        if res != exp:
            print("Fel i test 4b/6: pow2mult(0, -4)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4b/6: Exception')
        print_exception()

    try:
        res = pow2mult(1, 0)
        exp = 0
        if res != exp:
            print("Fel i test 4b/7: pow2mult(1, 0)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4b/7: Exception')
        print_exception()

    try:
        res = pow2mult(17, 0)
        exp = 0
        if res != exp:
            print("Fel i test 4b/8: pow2mult(17, 0)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4b/8: Exception')
        print_exception()

    try:
        res = pow2mult(500, 0)
        exp = 0
        if res != exp:
            print("Fel i test 4b/9: pow2mult(500, 0)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4b/9: Exception')
        print_exception()

    try:
        res = pow2mult(1, 4)
        exp = 8
        if res != exp:
            print("Fel i test 4b/10: pow2mult(1, 4)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4b/10: Exception')
        print_exception()

    try:
        res = pow2mult(1, -4)
        exp = -8
        if res != exp:
            print("Fel i test 4b/11: pow2mult(1, -4)")
            print("Korrekt svar: ")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4b/11: Exception')
        print_exception()

    try:
        res = pow2mult(5, -14)
        exp = -448
        if res != exp:
            print("Fel i test 4b/12: pow2mult(5, -14)")
            print("Korrekt svar: 44")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4b/12: Exception')
        print_exception()

    try:
        res = pow2mult(1, -14765354)
        exp = -29530708
        if res != exp:
            print("Fel i test 4b/13: pow2mult(1, -14765354)")
            print("Korrekt svar: 2953070")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4b/13: Exception')
        print_exception()

    try:
        res = pow2mult(1, 111111111111)
        exp = 222222222222
        if res != exp:
            print("Fel i test 4b/14: pow2mult(1, 111111111111)")
            print("Korrekt svar: 2222222222")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4b/14: Exception')
        print_exception()

    try:
        res = pow2mult(1, 123123123123123)
        exp = 246246246246246
        if res != exp:
            print("Fel i test 4b/15: pow2mult(1, 123123123123123)")
            print("Korrekt svar: 4624624624624")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4b/15: Exception')
        print_exception()

    try:
        res = pow2mult(32, 1)
        exp = 4294967296
        if res != exp:
            print("Fel i test 4b/16: pow2mult(32, 1)")
            print("Korrekt svar: 29496729")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4b/16: Exception')
        print_exception()

    try:
        res = pow2mult(64, 4096)
        exp = 75557863725914323419136
        if res != exp:
            print("Fel i test 4b/17: pow2mult(64, 4096)")
            print("Korrekt svar: 555786372591432341913")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 4b/17: Exception')
        print_exception()


    print('Klar med tester fÃ¶r uppgift 4b')
    print()


def test_5a():
    print('PÃ¥bÃ¶rjar tester fÃ¶r uppgift 5a')

    try:
        if is_prime(1):
            print('Fel i test 5a/1: is_prime(1)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/1: Exception')
        print_exception()

    try:
        if not is_prime(2):
            print('Fel i test 5a/2: is_prime(2)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5a/2: Exception')
        print_exception()

    try:
        if not is_prime(3):
            print('Fel i test 5a/3: is_prime(3)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5a/3: Exception')
        print_exception()

    try:
        if is_prime(4):
            print('Fel i test 5a/4: is_prime(4)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/4: Exception')
        print_exception()

    try:
        if not is_prime(5):
            print('Fel i test 5a/5: is_prime(5)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5a/5: Exception')
        print_exception()

    try:
        if is_prime(6):
            print('Fel i test 5a/6: is_prime(6)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/6: Exception')
        print_exception()

    try:
        if not is_prime(7):
            print('Fel i test 5a/7: is_prime(7)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5a/7: Exception')
        print_exception()

    try:
        if is_prime(8):
            print('Fel i test 5a/8: is_prime(8)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/8: Exception')
        print_exception()

    try:
        if is_prime(9):
            print('Fel i test 5a/9: is_prime(9)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/9: Exception')
        print_exception()

    try:
        if is_prime(10):
            print('Fel i test 5a/10: is_prime(10)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/10: Exception')
        print_exception()

    try:
        if not is_prime(11):
            print('Fel i test 5a/11: is_prime(11)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5a/11: Exception')
        print_exception()

    try:
        if is_prime(12):
            print('Fel i test 5a/12: is_prime(12)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/12: Exception')
        print_exception()

    try:
        if not is_prime(13):
            print('Fel i test 5a/13: is_prime(13)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5a/13: Exception')
        print_exception()

    try:
        if is_prime(14):
            print('Fel i test 5a/14: is_prime(14)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/14: Exception')
        print_exception()

    try:
        if is_prime(15):
            print('Fel i test 5a/15: is_prime(15)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/15: Exception')
        print_exception()

    try:
        if is_prime(16):
            print('Fel i test 5a/16: is_prime(16)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/16: Exception')
        print_exception()

    try:
        if not is_prime(17):
            print('Fel i test 5a/17: is_prime(17)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5a/17: Exception')
        print_exception()

    try:
        if is_prime(18):
            print('Fel i test 5a/18: is_prime(18)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/18: Exception')
        print_exception()

    try:
        if not is_prime(19):
            print('Fel i test 5a/19: is_prime(19)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5a/19: Exception')
        print_exception()

    try:
        if is_prime(20):
            print('Fel i test 5a/20: is_prime(20)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/20: Exception')
        print_exception()

    try:
        if is_prime(21):
            print('Fel i test 5a/21: is_prime(21)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/21: Exception')
        print_exception()

    try:
        if is_prime(22):
            print('Fel i test 5a/22: is_prime(22)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/22: Exception')
        print_exception()

    try:
        if not is_prime(23):
            print('Fel i test 5a/23: is_prime(23)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5a/23: Exception')
        print_exception()

    try:
        if is_prime(24):
            print('Fel i test 5a/24: is_prime(24)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/24: Exception')
        print_exception()

    try:
        if is_prime(25):
            print('Fel i test 5a/25: is_prime(25)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/25: Exception')
        print_exception()

    try:
        if is_prime(26):
            print('Fel i test 5a/26: is_prime(26)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/26: Exception')
        print_exception()

    try:
        if is_prime(27):
            print('Fel i test 5a/27: is_prime(27)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/27: Exception')
        print_exception()

    try:
        if is_prime(28):
            print('Fel i test 5a/28: is_prime(28)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/28: Exception')
        print_exception()

    try:
        if not is_prime(29):
            print('Fel i test 5a/29: is_prime(29)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5a/29: Exception')
        print_exception()

    try:
        if is_prime(30):
            print('Fel i test 5a/30: is_prime(30)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/30: Exception')
        print_exception()

    try:
        if not is_prime(31):
            print('Fel i test 5a/31: is_prime(31)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5a/31: Exception')
        print_exception()

    try:
        if is_prime(32):
            print('Fel i test 5a/32: is_prime(32)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/32: Exception')
        print_exception()

    try:
        if is_prime(33):
            print('Fel i test 5a/33: is_prime(33)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/33: Exception')
        print_exception()

    try:
        if is_prime(34):
            print('Fel i test 5a/34: is_prime(34)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/34: Exception')
        print_exception()

    try:
        if is_prime(35):
            print('Fel i test 5a/35: is_prime(35)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/35: Exception')
        print_exception()

    try:
        if is_prime(36):
            print('Fel i test 5a/36: is_prime(36)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/36: Exception')
        print_exception()

    try:
        if not is_prime(37):
            print('Fel i test 5a/37: is_prime(37)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5a/37: Exception')
        print_exception()

    try:
        if is_prime(38):
            print('Fel i test 5a/38: is_prime(38)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/38: Exception')
        print_exception()

    try:
        if is_prime(39):
            print('Fel i test 5a/39: is_prime(39)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5a/39: Exception')
        print_exception()

    try:
        if not is_prime(1000003):
            print('Fel i test 5a/40: is_prime(1000003)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5a/40: Exception')
        print_exception()

    try:
        if not is_prime(10000019):
            print('Fel i test 5a/41: is_prime(10000019)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5a/41: Exception')
        print_exception()

    try:
        if not is_prime(100000073):
            print('Fel i test 5a/42: is_prime(100000073)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5a/42: Exception')
        print_exception()

    try:
        if not is_prime(1000000007):
            print('Fel i test 5a/43: is_prime(1000000007)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5a/43: Exception')
        print_exception()


    print('Klar med tester fÃ¶r uppgift 5a')
    print()


def test_5b():
    print('PÃ¥bÃ¶rjar tester fÃ¶r uppgift 5b')

    try:
        res = prime_factors(2)
        exp = [2]
        if res != exp:
            print("Fel i test 5b/1: prime_factors(2)")
            print("Korrekt svar: 2")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/1: Exception')
        print_exception()

    try:
        res = prime_factors(3)
        exp = [3]
        if res != exp:
            print("Fel i test 5b/2: prime_factors(3)")
            print("Korrekt svar: 3")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/2: Exception')
        print_exception()

    try:
        res = prime_factors(4)
        exp = [2, 2]
        if res != exp:
            print("Fel i test 5b/3: prime_factors(4)")
            print("Korrekt svar: 2, 2")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/3: Exception')
        print_exception()

    try:
        res = prime_factors(5)
        exp = [5]
        if res != exp:
            print("Fel i test 5b/4: prime_factors(5)")
            print("Korrekt svar: 5")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/4: Exception')
        print_exception()

    try:
        res = prime_factors(6)
        exp = [2, 3]
        if res != exp:
            print("Fel i test 5b/5: prime_factors(6)")
            print("Korrekt svar: 2, 3")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/5: Exception')
        print_exception()

    try:
        res = prime_factors(7)
        exp = [7]
        if res != exp:
            print("Fel i test 5b/6: prime_factors(7)")
            print("Korrekt svar: 7")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/6: Exception')
        print_exception()

    try:
        res = prime_factors(8)
        exp = [2, 2, 2]
        if res != exp:
            print("Fel i test 5b/7: prime_factors(8)")
            print("Korrekt svar: 2, 2, 2")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/7: Exception')
        print_exception()

    try:
        res = prime_factors(9)
        exp = [3, 3]
        if res != exp:
            print("Fel i test 5b/8: prime_factors(9)")
            print("Korrekt svar: 3, 3")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/8: Exception')
        print_exception()

    try:
        res = prime_factors(10)
        exp = [2, 5]
        if res != exp:
            print("Fel i test 5b/9: prime_factors(10)")
            print("Korrekt svar: 2, 5")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/9: Exception')
        print_exception()

    try:
        res = prime_factors(11)
        exp = [11]
        if res != exp:
            print("Fel i test 5b/10: prime_factors(11)")
            print("Korrekt svar: 11")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/10: Exception')
        print_exception()

    try:
        res = prime_factors(12)
        exp = [2, 2, 3]
        if res != exp:
            print("Fel i test 5b/11: prime_factors(12)")
            print("Korrekt svar: 2, 2, 3")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/11: Exception')
        print_exception()

    try:
        res = prime_factors(13)
        exp = [13]
        if res != exp:
            print("Fel i test 5b/12: prime_factors(13)")
            print("Korrekt svar: 13")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/12: Exception')
        print_exception()

    try:
        res = prime_factors(14)
        exp = [2, 7]
        if res != exp:
            print("Fel i test 5b/13: prime_factors(14)")
            print("Korrekt svar: 2, 7")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/13: Exception')
        print_exception()

    try:
        res = prime_factors(15)
        exp = [3, 5]
        if res != exp:
            print("Fel i test 5b/14: prime_factors(15)")
            print("Korrekt svar: 3, 5")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/14: Exception')
        print_exception()

    try:
        res = prime_factors(16)
        exp = [2, 2, 2, 2]
        if res != exp:
            print("Fel i test 5b/15: prime_factors(16)")
            print("Korrekt svar: 2, 2, 2, 2")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/15: Exception')
        print_exception()

    try:
        res = prime_factors(17)
        exp = [17]
        if res != exp:
            print("Fel i test 5b/16: prime_factors(17)")
            print("Korrekt svar: 17")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/16: Exception')
        print_exception()

    try:
        res = prime_factors(18)
        exp = [2, 3, 3]
        if res != exp:
            print("Fel i test 5b/17: prime_factors(18)")
            print("Korrekt svar: 2, 3, 3")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/17: Exception')
        print_exception()

    try:
        res = prime_factors(19)
        exp = [19]
        if res != exp:
            print("Fel i test 5b/18: prime_factors(19)")
            print("Korrekt svar: 19")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/18: Exception')
        print_exception()

    try:
        res = prime_factors(20)
        exp = [2, 2, 5]
        if res != exp:
            print("Fel i test 5b/19: prime_factors(20)")
            print("Korrekt svar: 2, 2, 5")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/19: Exception')
        print_exception()

    try:
        res = prime_factors(21)
        exp = [3, 7]
        if res != exp:
            print("Fel i test 5b/20: prime_factors(21)")
            print("Korrekt svar: 3, 7")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/20: Exception')
        print_exception()

    try:
        res = prime_factors(22)
        exp = [2, 11]
        if res != exp:
            print("Fel i test 5b/21: prime_factors(22)")
            print("Korrekt svar: 2, 11")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/21: Exception')
        print_exception()

    try:
        res = prime_factors(23)
        exp = [23]
        if res != exp:
            print("Fel i test 5b/22: prime_factors(23)")
            print("Korrekt svar: 23")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/22: Exception')
        print_exception()

    try:
        res = prime_factors(24)
        exp = [2, 2, 2, 3]
        if res != exp:
            print("Fel i test 5b/23: prime_factors(24)")
            print("Korrekt svar: 2, 2, 2, 3")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/23: Exception')
        print_exception()

    try:
        res = prime_factors(25)
        exp = [5, 5]
        if res != exp:
            print("Fel i test 5b/24: prime_factors(25)")
            print("Korrekt svar: 5, 5")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/24: Exception')
        print_exception()

    try:
        res = prime_factors(26)
        exp = [2, 13]
        if res != exp:
            print("Fel i test 5b/25: prime_factors(26)")
            print("Korrekt svar: 2, 13")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/25: Exception')
        print_exception()

    try:
        res = prime_factors(27)
        exp = [3, 3, 3]
        if res != exp:
            print("Fel i test 5b/26: prime_factors(27)")
            print("Korrekt svar: 3, 3, 3")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/26: Exception')
        print_exception()

    try:
        res = prime_factors(28)
        exp = [2, 2, 7]
        if res != exp:
            print("Fel i test 5b/27: prime_factors(28)")
            print("Korrekt svar: 2, 2, 7")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/27: Exception')
        print_exception()

    try:
        res = prime_factors(29)
        exp = [29]
        if res != exp:
            print("Fel i test 5b/28: prime_factors(29)")
            print("Korrekt svar: 29")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/28: Exception')
        print_exception()

    try:
        res = prime_factors(30)
        exp = [2, 3, 5]
        if res != exp:
            print("Fel i test 5b/29: prime_factors(30)")
            print("Korrekt svar: 2, 3, 5")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/29: Exception')
        print_exception()

    try:
        res = prime_factors(31)
        exp = [31]
        if res != exp:
            print("Fel i test 5b/30: prime_factors(31)")
            print("Korrekt svar: 31")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/30: Exception')
        print_exception()

    try:
        res = prime_factors(32)
        exp = [2, 2, 2, 2, 2]
        if res != exp:
            print("Fel i test 5b/31: prime_factors(32)")
            print("Korrekt svar: 2, 2, 2, 2, 2")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/31: Exception')
        print_exception()

    try:
        res = prime_factors(33)
        exp = [3, 11]
        if res != exp:
            print("Fel i test 5b/32: prime_factors(33)")
            print("Korrekt svar: 3, 11")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/32: Exception')
        print_exception()

    try:
        res = prime_factors(34)
        exp = [2, 17]
        if res != exp:
            print("Fel i test 5b/33: prime_factors(34)")
            print("Korrekt svar: 2, 17")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/33: Exception')
        print_exception()

    try:
        res = prime_factors(35)
        exp = [5, 7]
        if res != exp:
            print("Fel i test 5b/34: prime_factors(35)")
            print("Korrekt svar: 5, 7")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/34: Exception')
        print_exception()

    try:
        res = prime_factors(36)
        exp = [2, 2, 3, 3]
        if res != exp:
            print("Fel i test 5b/35: prime_factors(36)")
            print("Korrekt svar: 2, 2, 3, 3")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/35: Exception')
        print_exception()

    try:
        res = prime_factors(37)
        exp = [37]
        if res != exp:
            print("Fel i test 5b/36: prime_factors(37)")
            print("Korrekt svar: 37")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/36: Exception')
        print_exception()

    try:
        res = prime_factors(38)
        exp = [2, 19]
        if res != exp:
            print("Fel i test 5b/37: prime_factors(38)")
            print("Korrekt svar: 2, 19")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/37: Exception')
        print_exception()

    try:
        res = prime_factors(39)
        exp = [3, 13]
        if res != exp:
            print("Fel i test 5b/38: prime_factors(39)")
            print("Korrekt svar: 3, 13")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/38: Exception')
        print_exception()

    try:
        res = prime_factors(40)
        exp = [2, 2, 2, 5]
        if res != exp:
            print("Fel i test 5b/39: prime_factors(40)")
            print("Korrekt svar: 2, 2, 2, 5")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/39: Exception')
        print_exception()

    try:
        res = prime_factors(41)
        exp = [41]
        if res != exp:
            print("Fel i test 5b/40: prime_factors(41)")
            print("Korrekt svar: 41")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/40: Exception')
        print_exception()

    try:
        res = prime_factors(42)
        exp = [2, 3, 7]
        if res != exp:
            print("Fel i test 5b/41: prime_factors(42)")
            print("Korrekt svar: 2, 3, 7")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/41: Exception')
        print_exception()

    try:
        res = prime_factors(43)
        exp = [43]
        if res != exp:
            print("Fel i test 5b/42: prime_factors(43)")
            print("Korrekt svar: 43")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/42: Exception')
        print_exception()

    try:
        res = prime_factors(44)
        exp = [2, 2, 11]
        if res != exp:
            print("Fel i test 5b/43: prime_factors(44)")
            print("Korrekt svar: 2, 2, 11")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/43: Exception')
        print_exception()

    try:
        res = prime_factors(45)
        exp = [3, 3, 5]
        if res != exp:
            print("Fel i test 5b/44: prime_factors(45)")
            print("Korrekt svar: 3, 3, 5")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/44: Exception')
        print_exception()

    try:
        res = prime_factors(46)
        exp = [2, 23]
        if res != exp:
            print("Fel i test 5b/45: prime_factors(46)")
            print("Korrekt svar: 2, 23")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/45: Exception')
        print_exception()

    try:
        res = prime_factors(47)
        exp = [47]
        if res != exp:
            print("Fel i test 5b/46: prime_factors(47)")
            print("Korrekt svar: 47")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/46: Exception')
        print_exception()

    try:
        res = prime_factors(48)
        exp = [2, 2, 2, 2, 3]
        if res != exp:
            print("Fel i test 5b/47: prime_factors(48)")
            print("Korrekt svar: 2, 2, 2, 2, 3")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/47: Exception')
        print_exception()

    try:
        res = prime_factors(49)
        exp = [7, 7]
        if res != exp:
            print("Fel i test 5b/48: prime_factors(49)")
            print("Korrekt svar: 7, 7")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/48: Exception')
        print_exception()

    try:
        res = prime_factors(100)
        exp = [2, 2, 5, 5]
        if res != exp:
            print("Fel i test 5b/49: prime_factors(100)")
            print("Korrekt svar: 2, 2, 5, 5")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/49: Exception')
        print_exception()

    try:
        res = prime_factors(101)
        exp = [101]
        if res != exp:
            print("Fel i test 5b/50: prime_factors(101)")
            print("Korrekt svar: 101")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/50: Exception')
        print_exception()

    try:
        res = prime_factors(150)
        exp = [2, 3, 5, 5]
        if res != exp:
            print("Fel i test 5b/51: prime_factors(150)")
            print("Korrekt svar: 2, 3, 5, 5")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/51: Exception')
        print_exception()

    try:
        res = prime_factors(151)
        exp = [151]
        if res != exp:
            print("Fel i test 5b/52: prime_factors(151)")
            print("Korrekt svar: 151")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/52: Exception')
        print_exception()

    try:
        res = prime_factors(200)
        exp = [2, 2, 2, 5, 5]
        if res != exp:
            print("Fel i test 5b/53: prime_factors(200)")
            print("Korrekt svar: 2, 2, 2, 5, 5")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/53: Exception')
        print_exception()

    try:
        res = prime_factors(211)
        exp = [211]
        if res != exp:
            print("Fel i test 5b/54: prime_factors(211)")
            print("Korrekt svar: 211")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/54: Exception')
        print_exception()

    try:
        res = prime_factors(121)
        exp = [11, 11]
        if res != exp:
            print("Fel i test 5b/55: prime_factors(121)")
            print("Korrekt svar: 11, 11")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/55: Exception')
        print_exception()

    try:
        res = prime_factors(289)
        exp = [17, 17]
        if res != exp:
            print("Fel i test 5b/56: prime_factors(289)")
            print("Korrekt svar: 17, 17")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/56: Exception')
        print_exception()

    try:
        res = prime_factors(529)
        exp = [23, 23]
        if res != exp:
            print("Fel i test 5b/57: prime_factors(529)")
            print("Korrekt svar: 23, 23")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/57: Exception')
        print_exception()

    try:
        res = prime_factors(108)
        exp = [2, 2, 3, 3, 3]
        if res != exp:
            print("Fel i test 5b/58: prime_factors(108)")
            print("Korrekt svar: 2, 2, 3, 3, 3")
            print("Fel svar:     " + repr(res))
            print()
    except:
        print(f'Fel i test 5b/58: Exception')
        print_exception()


    print('Klar med tester fÃ¶r uppgift 5b')
    print()


def test_5c():
    print('PÃ¥bÃ¶rjar tester fÃ¶r uppgift 5c')

    try:
        if is_attractive(16):
            print('Fel i test 5c/1: is_attractive(16)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5c/1: Exception')
        print_exception()

    try:
        if not is_attractive(20):
            print('Fel i test 5c/2: is_attractive(20)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/2: Exception')
        print_exception()

    try:
        if not is_attractive(21):
            print('Fel i test 5c/3: is_attractive(21)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/3: Exception')
        print_exception()

    try:
        if not is_attractive(22):
            print('Fel i test 5c/4: is_attractive(22)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/4: Exception')
        print_exception()

    try:
        if is_attractive(23):
            print('Fel i test 5c/5: is_attractive(23)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5c/5: Exception')
        print_exception()

    try:
        if is_attractive(24):
            print('Fel i test 5c/6: is_attractive(24)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5c/6: Exception')
        print_exception()

    try:
        if not is_attractive(55):
            print('Fel i test 5c/7: is_attractive(55)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/7: Exception')
        print_exception()

    try:
        if is_attractive(100):
            print('Fel i test 5c/8: is_attractive(100)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5c/8: Exception')
        print_exception()

    try:
        if is_attractive(101):
            print('Fel i test 5c/9: is_attractive(101)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5c/9: Exception')
        print_exception()

    try:
        if not is_attractive(102):
            print('Fel i test 5c/10: is_attractive(102)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/10: Exception')
        print_exception()

    try:
        if is_attractive(103):
            print('Fel i test 5c/11: is_attractive(103)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5c/11: Exception')
        print_exception()

    try:
        if is_attractive(104):
            print('Fel i test 5c/12: is_attractive(104)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5c/12: Exception')
        print_exception()

    try:
        if not is_attractive(105):
            print('Fel i test 5c/13: is_attractive(105)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/13: Exception')
        print_exception()

    try:
        if not is_attractive(106):
            print('Fel i test 5c/14: is_attractive(106)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/14: Exception')
        print_exception()

    try:
        if is_attractive(107):
            print('Fel i test 5c/15: is_attractive(107)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5c/15: Exception')
        print_exception()

    try:
        if not is_attractive(108):
            print('Fel i test 5c/16: is_attractive(108)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/16: Exception')
        print_exception()

    try:
        if is_attractive(109):
            print('Fel i test 5c/17: is_attractive(109)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5c/17: Exception')
        print_exception()

    try:
        if not is_attractive(110):
            print('Fel i test 5c/18: is_attractive(110)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/18: Exception')
        print_exception()

    try:
        if not is_attractive(111):
            print('Fel i test 5c/19: is_attractive(111)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/19: Exception')
        print_exception()

    try:
        if not is_attractive(112):
            print('Fel i test 5c/20: is_attractive(112)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/20: Exception')
        print_exception()

    try:
        if is_attractive(113):
            print('Fel i test 5c/21: is_attractive(113)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5c/21: Exception')
        print_exception()

    try:
        if not is_attractive(114):
            print('Fel i test 5c/22: is_attractive(114)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/22: Exception')
        print_exception()

    try:
        if not is_attractive(115):
            print('Fel i test 5c/23: is_attractive(115)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/23: Exception')
        print_exception()

    try:
        if not is_attractive(116):
            print('Fel i test 5c/24: is_attractive(116)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/24: Exception')
        print_exception()

    try:
        if not is_attractive(117):
            print('Fel i test 5c/25: is_attractive(117)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/25: Exception')
        print_exception()

    try:
        if not is_attractive(118):
            print('Fel i test 5c/26: is_attractive(118)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/26: Exception')
        print_exception()

    try:
        if not is_attractive(119):
            print('Fel i test 5c/27: is_attractive(119)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/27: Exception')
        print_exception()

    try:
        if not is_attractive(120):
            print('Fel i test 5c/28: is_attractive(120)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/28: Exception')
        print_exception()

    try:
        if not is_attractive(121):
            print('Fel i test 5c/29: is_attractive(121)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/29: Exception')
        print_exception()

    try:
        if not is_attractive(122):
            print('Fel i test 5c/30: is_attractive(122)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/30: Exception')
        print_exception()

    try:
        if not is_attractive(123):
            print('Fel i test 5c/31: is_attractive(123)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/31: Exception')
        print_exception()

    try:
        if not is_attractive(124):
            print('Fel i test 5c/32: is_attractive(124)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/32: Exception')
        print_exception()

    try:
        if not is_attractive(125):
            print('Fel i test 5c/33: is_attractive(125)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/33: Exception')
        print_exception()

    try:
        if is_attractive(126):
            print('Fel i test 5c/34: is_attractive(126)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5c/34: Exception')
        print_exception()

    try:
        if is_attractive(127):
            print('Fel i test 5c/35: is_attractive(127)')
            print('Svaret ska vara False')
    except:
        print(f'Fel i test 5c/35: Exception')
        print_exception()

    try:
        if not is_attractive(128):
            print('Fel i test 5c/36: is_attractive(128)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/36: Exception')
        print_exception()

    try:
        if not is_attractive(129):
            print('Fel i test 5c/37: is_attractive(129)')
            print('Svaret ska vara True')
    except:
        print(f'Fel i test 5c/37: Exception')
        print_exception()


    print('Klar med tester fÃ¶r uppgift 5c')
    print()


def test_6():
    print('PÃ¥bÃ¶rjar tester fÃ¶r uppgift 6')

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion

    # Hoppar Ã¶ver komplext test definierat med separat testfunktion


    print('Klar med tester fÃ¶r uppgift 6')
    print()

if __name__ == '__main__':
    test_1()
    test_2a()
    test_2b()
    test_3()
    test_4a()
    test_4b()
    test_5a()
    test_5b()
    test_5c()
    test_6()
