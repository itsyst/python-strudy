"""
LÃ¶sningsfÃ¶rslag fÃ¶r tenta i TDDE24 2021-08-17.

TÃ¤nk pÃ¥ att detta Ã¤r *fÃ¶rslag* pÃ¥ lÃ¶sningar.  Det finns mÃ¥nga olika sÃ¤tt
att lÃ¶sa uppgifterna!

Testfall finns pÃ¥ slutet.  TÃ¤nk pÃ¥ att de allra flesta problem som vi
ser i inlÃ¤mningarna skulle ha upptÃ¤ckts med en *mycket* mindre uppsÃ¤ttning
testfall, som inte alls hade tagit mycket tid att skapa.  Att vi anvÃ¤nder
sÃ¥ mÃ¥nga testfall beror pÃ¥ att det underlÃ¤ttar nÃ¤r man har mÃ¥nga
inlÃ¤mningar:

1) Vi anvÃ¤nder inte bara testfall fÃ¶r att *upptÃ¤cka* problem utan ocksÃ¥
fÃ¶r att gruppera och *kategorisera* dem.  FÃ¶r er kan det gÃ¥ snabbare att
hitta exakt vad felet var genom att gÃ¥ genom er egen kod noggrannt.  FÃ¶r
oss kan det gÃ¥ snabbare att skriva extra testfall sÃ¥ vi kan se mÃ¶nster i
alla inlÃ¤mningar: "NÃ¤r dessa 17 testfall misslyckas, men inte de andra 83
testfallen, brukar det bero pÃ¥ ...".

2) Vi mÃ¥ste lÃ¤gga ner mycket arbete pÃ¥ att bedÃ¶ma alla pÃ¥ ett likvÃ¤rdigt
sÃ¤tt, med likvÃ¤rdiga poÃ¤ng.  Att ha mÃ¥nga testfall hjÃ¤lper oss att fÃ¥ en
*konsistent* bedÃ¶mning av alla inlÃ¤mningar.

3) Det finns *vÃ¤ldigt* mÃ¥nga sÃ¤tt att lÃ¶sa en uppgift, och tanken bakom
en lÃ¶sning Ã¤r ofta inte uppenbar fÃ¶r den som inte skrev den.  DÃ¤r
fÃ¶rfattaren Ã¤ven kan felsÃ¶ka sin egen *idÃ©* om hur lÃ¶sningen ska fungera,
har vi bara tillgÃ¥ng till programkoden och behÃ¶ver fler testfall fÃ¶r att
fÃ¶rstÃ¥ hur koden fungerar.
"""

# ======================================================================
# Uppgift 1
# ======================================================================

"""
Denna uppgift testar enklare programmering i Python, med hantering av listor och tupler.  

Vanligaste felet Ã¤r att man modifierar indata. TÃ¤nk pÃ¥ att "lista1 = lista2" inte gÃ¶r nÃ¥gon kopia!

Eftersom det inte stÃ¥r nÃ¥got sÃ¤rskilt om hur man ska behandla olika typer av element, ska man t.ex. inte behandla 
listelement annorlunda -- det handlar bara om elementen som faktiskt finns i seq, och dessa element kan rÃ¥ka vara 
listor eller tupler eller heltal eller vad som helst.  
"""


def facit_tuplify(seq: list):
    result = []
    # Denna lÃ¶sning sÃ¤tter om listan i varje steg.
    # Det gÃ¥r ocksÃ¥ att t.ex. iterera Ã¶ver index.
    while seq:
        if len(seq) < 2:
            # Bara 1 element kvar.  Om det fanns 0 element kvar skulle
            # vi inte ha gÃ¥tt in i loopen.
            result.append((seq[0],))
            return result
        else:
            # FÃ¶rsta och sista
            result.append((seq[0], seq[-1]))
            # Slicing skapar en NY lista med vissa av elementen i den
            # ursprungliga.  Detta Ã¤ndrar INTE pÃ¥ indata.
            seq = seq[1:-1]
    return result


assert facit_tuplify([1]) == [(1,)]

assert facit_tuplify(['hello', 'hello', 'world']) == [('hello', 'world'), ('hello',)]

assert facit_tuplify([1, 2, 3, 4]) == [(1, 4), (2, 3)]

assert facit_tuplify([1, 2, 3, 4, 5]) == [(1, 5), (2, 4), (3,)]

assert facit_tuplify([1, 2, 3, 4, 5, 6]) == [(1, 6), (2, 5), (3, 4)]

assert facit_tuplify([[1, 2], 3, 'hej', (53,), 'pi']) == [([1, 2], 'pi'), (3, (53,)), ('hej',)]

assert facit_tuplify([[1, 2], [3, 4], [5, 6]]) == [([1, 2], [5, 6]), ([3, 4],)]

assert facit_tuplify([[1, 2], (3, 4), [5, 6]]) == [([1, 2], [5, 6]), ((3, 4),)]

assert facit_tuplify([(1, 2), (3, 4), (5, 6)]) == [((1, 2), (5, 6)), ((3, 4),)]

assert facit_tuplify([(1, 2), (3, 4), (5, 6), [7, 8]]) == [((1, 2), [7, 8]), ((3, 4), (5, 6))]

assert facit_tuplify([(1, (2, 3)), ((3, 4), 4), ([5, 2], 6), [7, 8]]) == [((1, (2, 3)), [7, 8]),
                                                                          (((3, 4), 4), ([5, 2], 6))]

# ======================================================================
# Uppgift 2
# ======================================================================

"""
Uppgift 2a testar ocksÃ¥ frÃ¤mst enklare programmering i Python, med hantering av listor och tupler.  HÃ¤r fÃ¥r vi ocksÃ¥ 
"komplikationen" att dela upp strÃ¤ngar i tecken, att konvertera sifferstrÃ¤ngar till tal, och att hantera tomma listor.

NÃ¥gra lÃ¶sningar ger fel resultat nÃ¤r sizes innehÃ¥ller 0, och oftast dÃ¥ nÃ¤r sizes *slutar* med "0".  Vi har poÃ¤ngterat i 
uppgiften att 0 kan finnas "pÃ¥ godtycklig position" och att det ska returneras en "lista av len(sizes) listor", och om 
man hoppar Ã¶ver avslutande nollor i sekvensen bryter man mot detta.  Det kan ocksÃ¥ bli fel nÃ¤r sizes *bÃ¶rjar* med "0".

Ã„ven i denna uppgift hÃ¤nder det att man modifierar sina indata.  Ett sÃ¤tt att testa detta Ã¤r att skriva ut vÃ¤rdet av 
alla parametrar innan man returnerar frÃ¥n funktionen, och se om det ser ut att vara identiskt med ursprungliga indata.

I stort har det gÃ¥tt bra pÃ¥ denna uppgift, lika bra som fÃ¶r uppgift 1.

Uppgift 2b testar ocksÃ¥ att gÃ¶ra en rekursiv implementation.  HÃ¤r har vi en betydligt lÃ¤gre lÃ¶sningsgrad, vilket beror
pÃ¥ att man inte har implementerat funktionen alls (i hÃ¤lften av fallen) men ocksÃ¥ pÃ¥ att fler fÃ¥r problem nÃ¤r sizes
slutar med "0".  HÃ¤r kan det t.ex. hÃ¤nda att man "inga element kvar att leta upp" som ett basfall och att man dÃ¥ 
ignorerar att det finns siffror (nollor) kvar att behandla.
"""


def facit_split_lists(seq: list, sizes: str):
    result = []

    # For every number of elements...
    for count in sizes:
        count = int(count)
        if len(seq) < count:
            # Not enough elements left
            return None, None

        # OK, pick the desired number of elements (0 or more)
        # and step forward in the sequence (creates a copy of the sequence)
        result.append(seq[:count])
        seq = seq[count:]
    if seq:
        # Too many elements in seq
        return None, None
    else:
        # Got exactly as many elements as we needed
        return result


def facit_split_lists_rec(seq: list, sizes: str):
    if not sizes:
        # Base case: No more sublists to create.
        if not seq:
            # Reached the end of seq; all is good
            return []
        else:
            # There are elements left but we don't want any...
            return None, None

    # OK, we do need to create at least one more sublist.  How many elements?
    count = int(sizes[0])
    if len(seq) < count:
        # Not enough elements left
        return None, None

    tail = facit_split_lists_rec(seq[count:], sizes[1:])
    if tail == (None, None):
        # Failed to solve the subproblem
        return None, None

    return [seq[:count]] + tail


assert facit_split_lists([1, 2, 3, 'x'], "12") == (None, None)

assert facit_split_lists([1, 2], "12") == (None, None)

assert facit_split_lists([1, 2, 0, 4, 7, 6], "132") == [[1], [2, 0, 4], [7, 6]]

assert facit_split_lists([1, 2, 3], "102") == [[1], [], [2, 3]]

assert facit_split_lists([1, 2, 3], "1020") == [[1], [], [2, 3], []]

assert facit_split_lists([1, 2, 3], "10200") == [[1], [], [2, 3], [], []]

assert facit_split_lists([1, 2, 3], "12") == [[1], [2, 3]]

assert facit_split_lists([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "1273") == [[1], [2, 3], [4, 5, 6, 7, 8, 9, 10],
                                                                                  [11, 12, 13]]

assert facit_split_lists([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "12703") == [[1], [2, 3], [4, 5, 6, 7, 8, 9, 10],
                                                                                   [], [11, 12, 13]]

assert facit_split_lists([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "127003") == [[1], [2, 3], [4, 5, 6, 7, 8, 9, 10],
                                                                                    [], [], [11, 12, 13]]

assert facit_split_lists([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "1270003") == [[1], [2, 3],
                                                                                     [4, 5, 6, 7, 8, 9, 10], [], [], [],
                                                                                     [11, 12, 13]]

assert facit_split_lists([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "01273") == [[], [1], [2, 3],
                                                                                   [4, 5, 6, 7, 8, 9, 10], [11, 12, 13]]

assert facit_split_lists([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "1274") == (None, None)

assert facit_split_lists([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "1272") == (None, None)

assert facit_split_lists([1, 2, 3], "0102") == [[], [1], [], [2, 3]]

assert facit_split_lists([1, 2, 3], "01020") == [[], [1], [], [2, 3], []]

assert facit_split_lists([1, 2, 3], "010200") == [[], [1], [], [2, 3], [], []]

assert facit_split_lists([1, 2, 0, 4, 7, 6], "0132") == [[], [1], [2, 0, 4], [7, 6]]

assert facit_split_lists_rec([1, 2, 3, 'x'], "12") == (None, None)

assert facit_split_lists_rec([1, 2], "12") == (None, None)

assert facit_split_lists_rec([1, 2, 0, 4, 7, 6], "132") == [[1], [2, 0, 4], [7, 6]]

assert facit_split_lists_rec([1, 2, 3], "102") == [[1], [], [2, 3]]

assert facit_split_lists_rec([1, 2, 3], "1020") == [[1], [], [2, 3], []]

assert facit_split_lists_rec([1, 2, 3], "10200") == [[1], [], [2, 3], [], []]

assert facit_split_lists_rec([1, 2, 3], "12") == [[1], [2, 3]]

assert facit_split_lists_rec([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "1273") == [[1], [2, 3],
                                                                                      [4, 5, 6, 7, 8, 9, 10],
                                                                                      [11, 12, 13]]

assert facit_split_lists_rec([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "12703") == [[1], [2, 3],
                                                                                       [4, 5, 6, 7, 8, 9, 10], [],
                                                                                       [11, 12, 13]]

assert facit_split_lists_rec([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "127003") == [[1], [2, 3],
                                                                                        [4, 5, 6, 7, 8, 9, 10], [], [],
                                                                                        [11, 12, 13]]

assert facit_split_lists_rec([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "1270003") == [[1], [2, 3],
                                                                                         [4, 5, 6, 7, 8, 9, 10], [], [],
                                                                                         [], [11, 12, 13]]

assert facit_split_lists_rec([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "01273") == [[], [1], [2, 3],
                                                                                       [4, 5, 6, 7, 8, 9, 10],
                                                                                       [11, 12, 13]]

assert facit_split_lists_rec([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "1274") == (None, None)

assert facit_split_lists_rec([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "1272") == (None, None)

assert facit_split_lists_rec([1, 2, 3], "0102") == [[], [1], [], [2, 3]]

assert facit_split_lists_rec([1, 2, 3], "01020") == [[], [1], [], [2, 3], []]

assert facit_split_lists_rec([1, 2, 3], "010200") == [[], [1], [], [2, 3], [], []]

assert facit_split_lists_rec([1, 2, 0, 4, 7, 6], "0132") == [[], [1], [2, 0, 4], [7, 6]]

# ======================================================================
# Uppgift 3
# ======================================================================

"""
Uppgift 3 gÃ¥r vidare med att testa en nÃ¥got mer komplicerad struktur, dÃ¤r man ska hoppa framÃ¥t och bakÃ¥t i tvÃ¥ 
sekvenser pÃ¥ samma gÃ¥ng (hanterar tvÃ¥ index) och dÃ¤r man ska ha flera olika slutvillkor.

MÃ¥nga av problemen i denna lÃ¶sning beror pÃ¥ att man inte fÃ¶ljer den uppstÃ¤llda hanteringen av slutvillkoren, kanske fÃ¶r
att man vill skriva mindre kod.  Vi skriver uttryckligen nÃ¤r villkor ska testas:

- Om vi JUST HAR HOPPAT, OCH RESULTATET Ã„R... men de villkoren har ibland t.ex. flyttats till bÃ¶rjan av en loop, dÃ¤r man 
(a) kanske inte har gjort nÃ¥got hopp Ã¤n, (b) kanske har gjort nÃ¥got annat test fÃ¶re.

- Om vi JUST HAR HOPPAT UTAN ATT NÃ… FRAM... men ibland testas detta i fel ordning, sÃ¥ det triggas trots att man faktiskt
har nÃ¥tt fram.

- Om vi Ã„R PÃ… VÃ„G ATT HOPPA, MEN... men ibland flyttas det till andra platser dÃ¤r vi t.ex. just HAR hoppat, sÃ¥ man 
kanske missar att gÃ¶ra testet innan allra fÃ¶rsta hoppet, eller gÃ¶r det i fel ordning relativt andra tester.

Vi skriver ocksÃ¥ "TÃ¤nk pÃ¥ att slutvillkoren mÃ¥ste testas vid varje hopp, inte bara efter att tvÃ¥ hopp har gjorts!" och
detta ignoreras ibland, vilket ger problem om man ska fÃ¥ ett visst resultat efter ett udda antal hopp.  De angivna 
testfallen anvÃ¤nder visserligen ett jÃ¤mnt antal hopp, men man mÃ¥ste ocksÃ¥ testa alternativ.

Man behÃ¶ver ocksÃ¥ testa fler fall dÃ¤r maxjumps Ã¤r LITET eller STORT.  Det krÃ¤vs inte mycket arbete fÃ¶r att stoppa in 
testerna i en loop:  for maxjumps in (1, 2, 3, 4, 10, 1000): gÃ¶r-alla-tester.  DÃ¥ ser man t.ex. om det kraschar vid
vissa indata, Ã¤ven om man inte vet korrekta resultaten.

Ytterligare felfall kan komma frÃ¥n att man t.ex. plockar ut mittvÃ¤rde frÃ¥n seq1 pÃ¥ nÃ¥got sÃ¤tt, och sedan fÃ¶rsÃ¶ker 
hitta dess position med seq1.index(mittvÃ¤rde).  Det fungerar inte dÃ¥ mittvÃ¤rde finns flera gÃ¥nger i seq1!  Se t.ex. 
testfallet alternating_jumps([2], [1, 1, -10, 5], 10), som visar att samma vÃ¤rde kan finnas flera gÃ¥nger.  Slutsats:
AnvÃ¤nd aldrig index() om du vill veta var DU har fÃ¥tt ett element ifrÃ¥n.  Se alltid till att spara undan indexet nÃ¤r
du plockar ut elementet.
"""


def facit_alternating_jumps(seq1, seq2, max_jumps):
    pos1 = 0
    pos2 = 0
    jumps_done = 0
    jumps = []

    # Might be a good idea to give names to the strange constants,
    # so the code becomes easier to read
    would_jump_out_of_bounds = -42
    reached_the_end = -4711
    too_many_jumps = -49152

    while jumps_done < max_jumps:
        # How far would we jump, and where would we end up?
        distance = seq1[pos1]
        pos2 += distance

        # Can we actually do this?
        if pos2 < 0 or pos2 >= len(seq2):
            # No, would go too far
            return (would_jump_out_of_bounds, jumps)

        # OK, we can perform the jump.
        jumps.append(distance)
        jumps_done += 1

        # After the jump, did we reach the last element of both sequences?
        if pos1 == len(seq1) - 1 and pos2 == len(seq2) - 1:
            # Yes!  We're done.
            return (reached_the_end, jumps)

        # Did we already reach the max number of jumps without reaching the
        # last element of both sequences?
        if jumps_done == max_jumps:
            return (too_many_jumps, jumps)

        # To avoid complications, let's just repeat what we did above,
        # but with the other sequence.
        distance = seq2[pos2]
        pos1 += distance

        if pos1 < 0 or pos1 >= len(seq1):
            return (would_jump_out_of_bounds, jumps)

        jumps.append(distance)
        jumps_done += 1

        if pos1 == len(seq1) - 1 and pos2 == len(seq2) - 1:
            return (reached_the_end, jumps)

        # After the jump, did we reach the last element of both sequences?
        # Then we'll just fall out of the loop

    # Reached the maximum number of jumps
    return (too_many_jumps, jumps)


# It might also be a good idea to break out some helper functions
# in order to make the code more readable and less repeated:
def facit_alternating_jumps_optimized(seq1, seq2, max_jumps):
    pos1 = 0
    pos2 = 0
    jumps_done = 0
    jumps = []

    def went_too_far():
        return pos1 < 0 or pos1 >= len(seq1) or pos2 < 0 or pos2 >= len(seq2)

    def at_end():
        return pos1 == len(seq1) - 1 and pos2 == len(seq2) - 1

    # Continue as above, but using the nested functions...


assert facit_alternating_jumps([1, -42], [-42, 1], 10) == (-4711, [1, 1])

assert facit_alternating_jumps([3, -42], [-42, 12, 34, 1], 10) == (-4711, [3, 1])

assert facit_alternating_jumps([1, -1, 14], [-1, 1, 14], 10) == (-49152, [1, 1, -1, -1, 1, 1, -1, -1, 1, 1])

assert facit_alternating_jumps([2], [1, 1, -10, 5], 10) == (-42, [2])

assert facit_alternating_jumps([2, -42, -43, 42], [1, 1, 3], 10) == (-4711, [2, 3])

assert facit_alternating_jumps([-1, -1], [-1, -1], 10) == (-42, [])

assert facit_alternating_jumps([1, -1], [2, 3], 10) == (-42, [1])

assert facit_alternating_jumps([1, 2, 3, 1, 2], [1, 2, 3, 4, 5], 10) == (-42, [1, 2, 3])

assert facit_alternating_jumps([1, 2, 3], [1, 2, 3, 4, 5], 10) == (-4711, [1, 2, 3])

assert facit_alternating_jumps([1, 2, 3, 1], [1, 2, 3, 4, 1, 1], 10) == (-4711, [1, 2, 3, 1, 1])

assert facit_alternating_jumps([1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], 10) == (
-49152, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

assert facit_alternating_jumps([2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], 10) == (-42, [2, 2, 2, 2, 2, 2])

assert facit_alternating_jumps([3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3], 10) == (-42, [3, 3, 3, 3])

assert facit_alternating_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], 10) == (
-49152, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

assert facit_alternating_jumps([2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2], 10) == (
-4711, [2, 2, 2, 2, 2, 2, 2, 2])

assert facit_alternating_jumps([3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3], 10) == (-42, [3, 3, 3, 3])

assert facit_alternating_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10) == (
-49152, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

assert facit_alternating_jumps([2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 10) == (
-42, [2, 2, 2, 2, 2, 2, 2, 2])

assert facit_alternating_jumps([3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 10) == (
-4711, [3, 3, 3, 3, 3, 3])

assert facit_alternating_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10) == (
-49152, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

assert facit_alternating_jumps([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 10) == (
-4711, [2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

assert facit_alternating_jumps([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 10) == (
-42, [3, 3, 3, 3, 3, 3])

assert facit_alternating_jumps([1, -42], [-42, 1], 20) == (-4711, [1, 1])

assert facit_alternating_jumps([3, -42], [-42, 12, 34, 1], 20) == (-4711, [3, 1])

assert facit_alternating_jumps([1, -1, 14], [-1, 1, 14], 20) == (
-49152, [1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1])

assert facit_alternating_jumps([2], [1, 1, -10, 5], 20) == (-42, [2])

assert facit_alternating_jumps([2, -42, -43, 42], [1, 1, 3], 20) == (-4711, [2, 3])

assert facit_alternating_jumps([-1, -1], [-1, -1], 20) == (-42, [])

assert facit_alternating_jumps([1, -1], [2, 3], 20) == (-42, [1])

assert facit_alternating_jumps([1, 2, 3, 1, 2], [1, 2, 3, 4, 5], 20) == (-42, [1, 2, 3])

assert facit_alternating_jumps([1, 2, 3], [1, 2, 3, 4, 5], 20) == (-4711, [1, 2, 3])

assert facit_alternating_jumps([1, 2, 3, 1], [1, 2, 3, 4, 1, 1], 20) == (-4711, [1, 2, 3, 1, 1])

assert facit_alternating_jumps([1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], 20) == (
-4711, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

assert facit_alternating_jumps([2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], 20) == (-42, [2, 2, 2, 2, 2, 2])

assert facit_alternating_jumps([3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3], 20) == (-42, [3, 3, 3, 3])

assert facit_alternating_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], 20) == (
-4711, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

assert facit_alternating_jumps([2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2], 20) == (
-4711, [2, 2, 2, 2, 2, 2, 2, 2])

assert facit_alternating_jumps([3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3], 20) == (-42, [3, 3, 3, 3])

assert facit_alternating_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 20) == (
-4711, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

assert facit_alternating_jumps([2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 20) == (
-42, [2, 2, 2, 2, 2, 2, 2, 2])

assert facit_alternating_jumps([3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 20) == (
-4711, [3, 3, 3, 3, 3, 3])

assert facit_alternating_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 20) == (
-4711, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

assert facit_alternating_jumps([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 20) == (
-4711, [2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

assert facit_alternating_jumps([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 20) == (
-42, [3, 3, 3, 3, 3, 3])

assert facit_alternating_jumps([1, -42], [-42, 1], 1000) == (-4711, [1, 1])

assert facit_alternating_jumps([3, -42], [-42, 12, 34, 1], 1000) == (-4711, [3, 1])

assert facit_alternating_jumps([1, -1, 14], [-1, 1, 14], 1000) == (-49152,
                                                                   [1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1,
                                                                    -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1,
                                                                    -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1,
                                                                    1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1,
                                                                    1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1,
                                                                    -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1,
                                                                    -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1,
                                                                    1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1,
                                                                    1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1,
                                                                    -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1,
                                                                    -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1,
                                                                    1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1,
                                                                    1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1,
                                                                    -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1,
                                                                    -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1,
                                                                    1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1,
                                                                    1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1,
                                                                    -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1,
                                                                    -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1,
                                                                    1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1,
                                                                    1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1,
                                                                    -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1,
                                                                    -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1,
                                                                    1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1,
                                                                    1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1,
                                                                    -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1,
                                                                    -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1,
                                                                    1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1,
                                                                    1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1,
                                                                    -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1,
                                                                    -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1,
                                                                    1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1,
                                                                    1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1,
                                                                    -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1,
                                                                    -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1,
                                                                    1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1,
                                                                    1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1,
                                                                    -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1,
                                                                    -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1,
                                                                    1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1,
                                                                    1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1,
                                                                    -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1,
                                                                    -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1,
                                                                    1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1,
                                                                    1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1,
                                                                    -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1,
                                                                    -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1,
                                                                    1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1,
                                                                    1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1,
                                                                    -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1,
                                                                    -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1,
                                                                    1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1,
                                                                    1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1,
                                                                    -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1,
                                                                    -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1,
                                                                    1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1,
                                                                    1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1,
                                                                    -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1,
                                                                    -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1,
                                                                    1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1,
                                                                    1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1,
                                                                    -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1,
                                                                    -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1,
                                                                    1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1,
                                                                    1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1,
                                                                    -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1,
                                                                    -1, -1, 1, 1, -1, -1, 1, 1, -1, -1])

assert facit_alternating_jumps([2], [1, 1, -10, 5], 1000) == (-42, [2])

assert facit_alternating_jumps([2, -42, -43, 42], [1, 1, 3], 1000) == (-4711, [2, 3])

assert facit_alternating_jumps([-1, -1], [-1, -1], 1000) == (-42, [])

assert facit_alternating_jumps([1, -1], [2, 3], 1000) == (-42, [1])

assert facit_alternating_jumps([1, 2, 3, 1, 2], [1, 2, 3, 4, 5], 1000) == (-42, [1, 2, 3])

assert facit_alternating_jumps([1, 2, 3], [1, 2, 3, 4, 5], 1000) == (-4711, [1, 2, 3])

assert facit_alternating_jumps([1, 2, 3, 1], [1, 2, 3, 4, 1, 1], 1000) == (-4711, [1, 2, 3, 1, 1])

assert facit_alternating_jumps([1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], 1000) == (
-4711, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

assert facit_alternating_jumps([2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], 1000) == (-42, [2, 2, 2, 2, 2, 2])

assert facit_alternating_jumps([3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3], 1000) == (-42, [3, 3, 3, 3])

assert facit_alternating_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], 1000) == (
-4711, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

assert facit_alternating_jumps([2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2], 1000) == (
-4711, [2, 2, 2, 2, 2, 2, 2, 2])

assert facit_alternating_jumps([3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3], 1000) == (-42, [3, 3, 3, 3])

assert facit_alternating_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1000) == (
-4711, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

assert facit_alternating_jumps([2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 1000) == (
-42, [2, 2, 2, 2, 2, 2, 2, 2])

assert facit_alternating_jumps([3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 1000) == (
-4711, [3, 3, 3, 3, 3, 3])

assert facit_alternating_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1000) == (
-4711, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

assert facit_alternating_jumps([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 1000) == (
-4711, [2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

assert facit_alternating_jumps([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 1000) == (
-42, [3, 3, 3, 3, 3, 3])

assert facit_alternating_jumps([1, -42], [-42, 1], 1) == (-49152, [1])

assert facit_alternating_jumps([3, -42], [-42, 12, 34, 1], 1) == (-49152, [3])

assert facit_alternating_jumps([1, -1, 14], [-1, 1, 14], 1) == (-49152, [1])

assert facit_alternating_jumps([2], [1, 1, -10, 5], 1) == (-49152, [2])

assert facit_alternating_jumps([2, -42, -43, 42], [1, 1, 3], 1) == (-49152, [2])

assert facit_alternating_jumps([-1, -1], [-1, -1], 1) == (-42, [])

assert facit_alternating_jumps([1, -1], [2, 3], 1) == (-49152, [1])

assert facit_alternating_jumps([1, 2, 3, 1, 2], [1, 2, 3, 4, 5], 1) == (-49152, [1])

assert facit_alternating_jumps([1, 2, 3], [1, 2, 3, 4, 5], 1) == (-49152, [1])

assert facit_alternating_jumps([1, 2, 3, 1], [1, 2, 3, 4, 1, 1], 1) == (-49152, [1])

assert facit_alternating_jumps([1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], 1) == (-49152, [1])

assert facit_alternating_jumps([2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], 1) == (-49152, [2])

assert facit_alternating_jumps([3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3], 1) == (-49152, [3])

assert facit_alternating_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], 1) == (-49152, [1])

assert facit_alternating_jumps([2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2], 1) == (-49152, [2])

assert facit_alternating_jumps([3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3], 1) == (-49152, [3])

assert facit_alternating_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1) == (-49152, [1])

assert facit_alternating_jumps([2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 1) == (-49152, [2])

assert facit_alternating_jumps([3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 1) == (-49152, [3])

assert facit_alternating_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1) == (-49152, [1])

assert facit_alternating_jumps([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 1) == (-49152, [2])

assert facit_alternating_jumps([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 1) == (-49152, [3])

assert facit_alternating_jumps([1, -42], [-42, 1], 2) == (-4711, [1, 1])

assert facit_alternating_jumps([3, -42], [-42, 12, 34, 1], 2) == (-4711, [3, 1])

assert facit_alternating_jumps([1, -1, 14], [-1, 1, 14], 2) == (-49152, [1, 1])

assert facit_alternating_jumps([2], [1, 1, -10, 5], 2) == (-42, [2])

assert facit_alternating_jumps([2, -42, -43, 42], [1, 1, 3], 2) == (-4711, [2, 3])

assert facit_alternating_jumps([-1, -1], [-1, -1], 2) == (-42, [])

assert facit_alternating_jumps([1, -1], [2, 3], 2) == (-42, [1])

assert facit_alternating_jumps([1, 2, 3, 1, 2], [1, 2, 3, 4, 5], 2) == (-49152, [1, 2])

assert facit_alternating_jumps([1, 2, 3], [1, 2, 3, 4, 5], 2) == (-49152, [1, 2])

assert facit_alternating_jumps([1, 2, 3, 1], [1, 2, 3, 4, 1, 1], 2) == (-49152, [1, 2])

assert facit_alternating_jumps([1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], 2) == (-49152, [1, 1])

assert facit_alternating_jumps([2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], 2) == (-49152, [2, 2])

assert facit_alternating_jumps([3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3], 2) == (-49152, [3, 3])

assert facit_alternating_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], 2) == (-49152, [1, 1])

assert facit_alternating_jumps([2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2], 2) == (-49152, [2, 2])

assert facit_alternating_jumps([3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3], 2) == (-49152, [3, 3])

assert facit_alternating_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 2) == (-49152, [1, 1])

assert facit_alternating_jumps([2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 2) == (-49152, [2, 2])

assert facit_alternating_jumps([3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 2) == (-49152, [3, 3])

assert facit_alternating_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 2) == (
-49152, [1, 1])

assert facit_alternating_jumps([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 2) == (
-49152, [2, 2])

assert facit_alternating_jumps([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 2) == (
-49152, [3, 3])

assert facit_alternating_jumps([1, -42], [-42, 1], 3) == (-4711, [1, 1])

assert facit_alternating_jumps([3, -42], [-42, 12, 34, 1], 3) == (-4711, [3, 1])

assert facit_alternating_jumps([1, -1, 14], [-1, 1, 14], 3) == (-49152, [1, 1, -1])

assert facit_alternating_jumps([2], [1, 1, -10, 5], 3) == (-42, [2])

assert facit_alternating_jumps([2, -42, -43, 42], [1, 1, 3], 3) == (-4711, [2, 3])

assert facit_alternating_jumps([-1, -1], [-1, -1], 3) == (-42, [])

assert facit_alternating_jumps([1, -1], [2, 3], 3) == (-42, [1])

assert facit_alternating_jumps([1, 2, 3, 1, 2], [1, 2, 3, 4, 5], 3) == (-49152, [1, 2, 3])

assert facit_alternating_jumps([1, 2, 3], [1, 2, 3, 4, 5], 3) == (-4711, [1, 2, 3])

assert facit_alternating_jumps([1, 2, 3, 1], [1, 2, 3, 4, 1, 1], 3) == (-49152, [1, 2, 3])

assert facit_alternating_jumps([1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], 3) == (-49152, [1, 1, 1])

assert facit_alternating_jumps([2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], 3) == (-49152, [2, 2, 2])

assert facit_alternating_jumps([3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3], 3) == (-49152, [3, 3, 3])

assert facit_alternating_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], 3) == (-49152, [1, 1, 1])

assert facit_alternating_jumps([2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2], 3) == (-49152, [2, 2, 2])

assert facit_alternating_jumps([3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3], 3) == (-49152, [3, 3, 3])

assert facit_alternating_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 3) == (-49152, [1, 1, 1])

assert facit_alternating_jumps([2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 3) == (-49152, [2, 2, 2])

assert facit_alternating_jumps([3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 3) == (-49152, [3, 3, 3])

assert facit_alternating_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 3) == (
-49152, [1, 1, 1])

assert facit_alternating_jumps([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 3) == (
-49152, [2, 2, 2])

assert facit_alternating_jumps([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 3) == (
-49152, [3, 3, 3])

assert facit_alternating_jumps([-1000, 2], [-4, 3], 3) == (-42, [])

assert facit_alternating_jumps([1000, 2], [-4, 3], 3) == (-42, [])

assert facit_alternating_jumps([-3, 2], [-4, 3], 3) == (-42, [])

assert facit_alternating_jumps([-4, 2], [-4, 3, 2], 3) == (-42, [])

assert facit_alternating_jumps([-2, 2], [-4, 3], 3) == (-42, [])

assert facit_alternating_jumps([-3, 2], [-4, 3, 2], 3) == (-42, [])

# ======================================================================
# Uppgift 4
# ======================================================================

"""
Denna frÃ¥ga testar behandling av nÃ¤stlade strukturer, dÃ¤r det Ã¤r naturligt att anvÃ¤nda rekursion fÃ¶r att fÃ¶renkla 
problemlÃ¶sningen (Ã¤ven om det ocksÃ¥ kan lÃ¶sas pÃ¥ andra sÃ¤tt).

Ett antal har inte lÃ¤mnat in nÃ¥gon lÃ¶sning.  I vissa fall har det blivit problem med rekursionen eller 
evalueringsordningen.
"""


def facit_treeval(tree):
    """
    TrÃ¤d: [nodvÃ¤rde, barn1, barn2, ...]
    """

    # Might be a good idea to check that you get the expected input.
    assert isinstance(tree, tuple), f"{tree}"
    nodeval = tree[0]
    children = tree[1]

    # Initial result value...
    result = nodeval

    opnum = 0
    for child in children:
        # Each child is a separate tree that is handled just like this one.
        # This means we want to use recursion.
        if opnum == 0:
            result -= facit_treeval(child)
        elif opnum == 1:
            result += facit_treeval(child)
        else:
            assert opnum == 2
            result *= facit_treeval(child)

        # Increase the operator number, but fall back to 0
        # if we go too far
        opnum += 1
        if opnum == 3:
            opnum = 0

        # Alternatively:
        # opnum = (opnum + 1) % 3

    return result


def facit_treeval_generalized(tree):
    """
    TrÃ¤d: [nodvÃ¤rde, barn1, barn2, ...]
    """

    nodeval = tree[0]
    children = tree[1]

    result = nodeval

    # This version of the implementation does not have a hardcoded if-elif
    # sequence.  Instead we have an array of operations, which could be
    # sent in as a parameter if we wanted.
    ops = [
        lambda x, y: x - y,
        lambda x, y: x + y,
        lambda x, y: x * y
    ]

    opnum = 0
    for child in children:
        op = ops[opnum]
        result = op(result, facit_treeval_generalized(child))
        opnum = (opnum + 1) % len(ops)

    return result


assert facit_treeval((1, [])) == 1

assert facit_treeval((1, [(2, [])])) == -1

assert facit_treeval((1, [(-3, []), (0, []), (-4, [])])) == -16

assert facit_treeval((1, [(-3, [(7, []), (3, []), (5, [])]), (0, []), (-4, []), (4, [])])) == -148

assert facit_treeval(
    (1, [(-3, [(7, [(42, []), (14, [])]), (123, []), (456, [])]), (75, []), (-44, []), (4, [])])) == 2825676

assert facit_treeval((1, [(-3, []), (0, []), (-4, []), (4, [])])) == -20

assert facit_treeval((77, [(42, []), (1, []), (12, []), (4, []), (4, []), (4, []), (4, []), (4, [])])) == 1728

assert facit_treeval((77, [(42, [(1, [])])])) == 36

assert facit_treeval((77, [(42, [(1, [(12, [])])])])) == 24

assert facit_treeval((77, [(42, [(1, [(12, [(4, [(12, [(55, [])])])])])])])) == 71

assert facit_treeval((77, [(42, [(1, [(12, [(4, [(12, [(55, [])])], [(12, [(55, [])])])])])])])) == 71

assert facit_treeval((77, [(42, [(1, [(12, [(4, []), (4, []), (4, []), (4, []), (4, [])])])])])) == -12

assert facit_treeval((1.2, [(-3.5, []), (0, [])])) == 4.7

assert facit_treeval((1.2, [(-3.5, []), (0, []), (-4, [])])) == -18.8

assert facit_treeval(('Hello', [])) == "Hello"

assert facit_treeval(([12], [])) == [12]

assert facit_treeval((None, [])) is None

assert facit_treeval(((42, 55), [])) == (42, 55)

assert facit_treeval(((1 + 2j), [])) == (1 + 2j)

assert facit_treeval(((1 + 2j), [((3 + 4j), [])])) == (-2 - 2j)

assert facit_treeval(({1, 2, 3}, [])) == {1, 2, 3}

assert facit_treeval(({1, 3}, [({2}, [])])) == {1, 3}

assert facit_treeval(({1, 3}, [({2}, [({7, 15}, [])])])) == {1, 3}

# ======================================================================
# Uppgift 5
# ======================================================================

"""
HÃ¤r testar vi vissa former av hÃ¶gre ordningens funktioner: Att ta in en funktion som parameter och applicera den,
och att definiera en funktion som returnerar en ny funktion.

Relativt mÃ¥nga har lÃ¤mnat in en lÃ¶sning, och fÃ¶r dessa finns bara ett fÃ¥tal poÃ¤ngavdrag, bl.a. fÃ¶r att inte ha 
implementerat flip() eller fÃ¶r att apply_to_both() inte fungerar dÃ¥ *fÃ¶rsta* sekvensen Ã¤r lÃ¤ngre.
"""


def facit_apply_to_both(seq1, seq2, f):
    result = []
    while seq1 and seq2:
        result.append(f(seq1[0], seq2[0]))
        seq1 = seq1[1:]
        seq2 = seq2[1:]
    return result


def facit_flip(f):
    return lambda a, b: f(b, a)


assert facit_apply_to_both([1, 2, 'x'], [float, int, str], isinstance) == [False, True, True]

assert facit_apply_to_both([1, 2, 3], [4, 5, 6], int.__mul__) == [4, 10, 18]

assert facit_apply_to_both([1, 2, 3], [4, 5, 6, 7], int.__mul__) == [4, 10, 18]

assert facit_apply_to_both([1, 2, 3, 42], [4, 5, 6], int.__mul__) == [4, 10, 18]

assert facit_apply_to_both([1, 2, 3, 42, 43], [4, 5, 6], int.__mul__) == [4, 10, 18]

assert facit_apply_to_both([1, 2, 3, 42, 43], (), int.__mul__) == []

assert facit_apply_to_both((1, 2, 3, 42), (4, 5, 6), int.__mul__) == [4, 10, 18]

assert facit_apply_to_both(['a', 'b', 'c'], ['d', 'e', 'f'], str.__add__) == ['ad', 'be', 'cf']

assert facit_flip(isinstance)(int, 12)

assert facit_flip(int.__sub__)(10, 4) == -6

assert facit_flip(int.__divmod__)(5, 30) == (6, 0)

# ======================================================================
# Uppgift 6
# ======================================================================

"""
HÃ¤r ger vi en sista uppgift som anvÃ¤nder sig av kombinatorik, nÃ¥got som ocksÃ¥ finns i mÃ¥nga gamla tentafrÃ¥gor.

Tidigare har studenter ofta fÃ¶rsÃ¶kt "optimera" sina kombinatoriska lÃ¶sningar genom att inte testa alla varianter,
vilket tyvÃ¤rr alltid ger fall som inte fungerar.  FÃ¶r att undvika det problemet har vi denna gÃ¥ng sett till att man 
fÃ¶rst ska returnera just alla varianter, sÃ¥ man inte ska tÃ¤nka att en optimering kan fungera.
"""


def facit_find_variants(numbers: list[int]):
    # There are at least two numbers in the original input.  Recursive calls
    # only remove one number at a time, and recursion is terminated when only
    # one number remains.  Therefore we should never get an empty list.
    assert len(numbers) > 0

    if len(numbers) == 1:
        # Recursive base case:  There is only one number "left", so the only variant
        # uses *no* operators.  Its result is the first (only) number.
        only_variant = ([], numbers[0])
        return [only_variant]

    # OK, we have at least two numbers.
    # Now we need to recurse, but in what sub-problem?
    # The task states:
    #
    # NÃ¤r vi skriver 1+2-3+4-5 menar vi ((((1+2)-3)+4)-5),
    # sÃ¥ vi bÃ¶rjar med att rÃ¤kna ut 1+2 och subtraherar sedan 3,
    # precis som nÃ¤r man skriver in ett tal i en gammaldags
    # minirÃ¤knare.
    #
    # This means that we have to handle (((1+2)-3)+4) first,
    # and *then* deal with the 5.  In other words, given the
    # list [1,2,3,4,5], we recurse on [1,2,3,4], and when we
    # get the result, we have to deal with the 5.  This means
    # recursing on numbers[:-1].

    result = []
    sub_variants = facit_find_variants(numbers[:-1])

    # Now sub_variants contains all the variants of
    # [1,2,3,4] in the example.  For example, (['+','+','+'],10) and
    # (['-','-','-'],-8) would be in the sub_variants list.

    # Each such variant has to be expanded to 3 new variants: One
    # where we add 5, one where we subtract 5, and one where we
    # multiply by 5.

    for variant in sub_variants:
        operations, subresult = variant

        # The old operations plus the new operation;
        # the old result modified with the new number
        mod1 = (operations + ["+"], subresult + numbers[-1])
        result.append(mod1)

        mod2 = (operations + ["-"], subresult - numbers[-1])
        result.append(mod2)

        mod3 = (operations + ["*"], subresult * numbers[-1])
        result.append(mod3)

    # Now len(result) == 3*len(sub_variants), and we return all the
    # variants.
    return result


def facit_find_matching(numbers: list[int], wanted: int):
    return [(operations, result) for operations, result in facit_find_variants(numbers) if result == wanted]


assert facit_find_variants([12, 34]) == [(['+'], 46), (['-'], -22), (['*'], 408)]

assert facit_find_variants([3, 5, 11]) == [(['+', '+'], 19), (['+', '-'], -3), (['+', '*'], 88), (['-', '+'], 9),
                                           (['-', '-'], -13), (['-', '*'], -22), (['*', '+'], 26), (['*', '-'], 4),
                                           (['*', '*'], 165)]

assert facit_find_variants([-12, 42]) == [(['+'], 30), (['-'], -54), (['*'], -504)]

assert facit_find_variants([-12, 42, 73]) == [(['+', '+'], 103), (['+', '-'], -43), (['+', '*'], 2190),
                                              (['-', '+'], 19), (['-', '-'], -127), (['-', '*'], -3942),
                                              (['*', '+'], -431), (['*', '-'], -577), (['*', '*'], -36792)]

assert facit_find_variants([-12, 42, 0]) == [(['+', '+'], 30), (['+', '-'], 30), (['+', '*'], 0), (['-', '+'], -54),
                                             (['-', '-'], -54), (['-', '*'], 0), (['*', '+'], -504), (['*', '-'], -504),
                                             (['*', '*'], 0)]

assert facit_find_variants([98, 76, 54, 32]) == [(['+', '+', '+'], 260), (['+', '+', '-'], 196),
                                                 (['+', '+', '*'], 7296), (['+', '-', '+'], 152), (['+', '-', '-'], 88),
                                                 (['+', '-', '*'], 3840), (['+', '*', '+'], 9428),
                                                 (['+', '*', '-'], 9364), (['+', '*', '*'], 300672),
                                                 (['-', '+', '+'], 108), (['-', '+', '-'], 44), (['-', '+', '*'], 2432),
                                                 (['-', '-', '+'], 0), (['-', '-', '-'], -64), (['-', '-', '*'], -1024),
                                                 (['-', '*', '+'], 1220), (['-', '*', '-'], 1156),
                                                 (['-', '*', '*'], 38016), (['*', '+', '+'], 7534),
                                                 (['*', '+', '-'], 7470), (['*', '+', '*'], 240064),
                                                 (['*', '-', '+'], 7426), (['*', '-', '-'], 7362),
                                                 (['*', '-', '*'], 236608), (['*', '*', '+'], 402224),
                                                 (['*', '*', '-'], 402160), (['*', '*', '*'], 12870144)]

assert facit_find_variants([-12, 42, 12, 4, 182, 1, 5]) == [(['+', '+', '+', '+', '+', '+'], 234),
                                                            (['+', '+', '+', '+', '+', '-'], 224),
                                                            (['+', '+', '+', '+', '+', '*'], 1145),
                                                            (['+', '+', '+', '+', '-', '+'], 232),
                                                            (['+', '+', '+', '+', '-', '-'], 222),
                                                            (['+', '+', '+', '+', '-', '*'], 1135),
                                                            (['+', '+', '+', '+', '*', '+'], 233),
                                                            (['+', '+', '+', '+', '*', '-'], 223),
                                                            (['+', '+', '+', '+', '*', '*'], 1140),
                                                            (['+', '+', '+', '-', '+', '+'], -130),
                                                            (['+', '+', '+', '-', '+', '-'], -140),
                                                            (['+', '+', '+', '-', '+', '*'], -675),
                                                            (['+', '+', '+', '-', '-', '+'], -132),
                                                            (['+', '+', '+', '-', '-', '-'], -142),
                                                            (['+', '+', '+', '-', '-', '*'], -685),
                                                            (['+', '+', '+', '-', '*', '+'], -131),
                                                            (['+', '+', '+', '-', '*', '-'], -141),
                                                            (['+', '+', '+', '-', '*', '*'], -680),
                                                            (['+', '+', '+', '*', '+', '+'], 8378),
                                                            (['+', '+', '+', '*', '+', '-'], 8368),
                                                            (['+', '+', '+', '*', '+', '*'], 41865),
                                                            (['+', '+', '+', '*', '-', '+'], 8376),
                                                            (['+', '+', '+', '*', '-', '-'], 8366),
                                                            (['+', '+', '+', '*', '-', '*'], 41855),
                                                            (['+', '+', '+', '*', '*', '+'], 8377),
                                                            (['+', '+', '+', '*', '*', '-'], 8367),
                                                            (['+', '+', '+', '*', '*', '*'], 41860),
                                                            (['+', '+', '-', '+', '+', '+'], 226),
                                                            (['+', '+', '-', '+', '+', '-'], 216),
                                                            (['+', '+', '-', '+', '+', '*'], 1105),
                                                            (['+', '+', '-', '+', '-', '+'], 224),
                                                            (['+', '+', '-', '+', '-', '-'], 214),
                                                            (['+', '+', '-', '+', '-', '*'], 1095),
                                                            (['+', '+', '-', '+', '*', '+'], 225),
                                                            (['+', '+', '-', '+', '*', '-'], 215),
                                                            (['+', '+', '-', '+', '*', '*'], 1100),
                                                            (['+', '+', '-', '-', '+', '+'], -138),
                                                            (['+', '+', '-', '-', '+', '-'], -148),
                                                            (['+', '+', '-', '-', '+', '*'], -715),
                                                            (['+', '+', '-', '-', '-', '+'], -140),
                                                            (['+', '+', '-', '-', '-', '-'], -150),
                                                            (['+', '+', '-', '-', '-', '*'], -725),
                                                            (['+', '+', '-', '-', '*', '+'], -139),
                                                            (['+', '+', '-', '-', '*', '-'], -149),
                                                            (['+', '+', '-', '-', '*', '*'], -720),
                                                            (['+', '+', '-', '*', '+', '+'], 6922),
                                                            (['+', '+', '-', '*', '+', '-'], 6912),
                                                            (['+', '+', '-', '*', '+', '*'], 34585),
                                                            (['+', '+', '-', '*', '-', '+'], 6920),
                                                            (['+', '+', '-', '*', '-', '-'], 6910),
                                                            (['+', '+', '-', '*', '-', '*'], 34575),
                                                            (['+', '+', '-', '*', '*', '+'], 6921),
                                                            (['+', '+', '-', '*', '*', '-'], 6911),
                                                            (['+', '+', '-', '*', '*', '*'], 34580),
                                                            (['+', '+', '*', '+', '+', '+'], 356),
                                                            (['+', '+', '*', '+', '+', '-'], 346),
                                                            (['+', '+', '*', '+', '+', '*'], 1755),
                                                            (['+', '+', '*', '+', '-', '+'], 354),
                                                            (['+', '+', '*', '+', '-', '-'], 344),
                                                            (['+', '+', '*', '+', '-', '*'], 1745),
                                                            (['+', '+', '*', '+', '*', '+'], 355),
                                                            (['+', '+', '*', '+', '*', '-'], 345),
                                                            (['+', '+', '*', '+', '*', '*'], 1750),
                                                            (['+', '+', '*', '-', '+', '+'], -8),
                                                            (['+', '+', '*', '-', '+', '-'], -18),
                                                            (['+', '+', '*', '-', '+', '*'], -65),
                                                            (['+', '+', '*', '-', '-', '+'], -10),
                                                            (['+', '+', '*', '-', '-', '-'], -20),
                                                            (['+', '+', '*', '-', '-', '*'], -75),
                                                            (['+', '+', '*', '-', '*', '+'], -9),
                                                            (['+', '+', '*', '-', '*', '-'], -19),
                                                            (['+', '+', '*', '-', '*', '*'], -70),
                                                            (['+', '+', '*', '*', '+', '+'], 30582),
                                                            (['+', '+', '*', '*', '+', '-'], 30572),
                                                            (['+', '+', '*', '*', '+', '*'], 152885),
                                                            (['+', '+', '*', '*', '-', '+'], 30580),
                                                            (['+', '+', '*', '*', '-', '-'], 30570),
                                                            (['+', '+', '*', '*', '-', '*'], 152875),
                                                            (['+', '+', '*', '*', '*', '+'], 30581),
                                                            (['+', '+', '*', '*', '*', '-'], 30571),
                                                            (['+', '+', '*', '*', '*', '*'], 152880),
                                                            (['+', '-', '+', '+', '+', '+'], 210),
                                                            (['+', '-', '+', '+', '+', '-'], 200),
                                                            (['+', '-', '+', '+', '+', '*'], 1025),
                                                            (['+', '-', '+', '+', '-', '+'], 208),
                                                            (['+', '-', '+', '+', '-', '-'], 198),
                                                            (['+', '-', '+', '+', '-', '*'], 1015),
                                                            (['+', '-', '+', '+', '*', '+'], 209),
                                                            (['+', '-', '+', '+', '*', '-'], 199),
                                                            (['+', '-', '+', '+', '*', '*'], 1020),
                                                            (['+', '-', '+', '-', '+', '+'], -154),
                                                            (['+', '-', '+', '-', '+', '-'], -164),
                                                            (['+', '-', '+', '-', '+', '*'], -795),
                                                            (['+', '-', '+', '-', '-', '+'], -156),
                                                            (['+', '-', '+', '-', '-', '-'], -166),
                                                            (['+', '-', '+', '-', '-', '*'], -805),
                                                            (['+', '-', '+', '-', '*', '+'], -155),
                                                            (['+', '-', '+', '-', '*', '-'], -165),
                                                            (['+', '-', '+', '-', '*', '*'], -800),
                                                            (['+', '-', '+', '*', '+', '+'], 4010),
                                                            (['+', '-', '+', '*', '+', '-'], 4000),
                                                            (['+', '-', '+', '*', '+', '*'], 20025),
                                                            (['+', '-', '+', '*', '-', '+'], 4008),
                                                            (['+', '-', '+', '*', '-', '-'], 3998),
                                                            (['+', '-', '+', '*', '-', '*'], 20015),
                                                            (['+', '-', '+', '*', '*', '+'], 4009),
                                                            (['+', '-', '+', '*', '*', '-'], 3999),
                                                            (['+', '-', '+', '*', '*', '*'], 20020),
                                                            (['+', '-', '-', '+', '+', '+'], 202),
                                                            (['+', '-', '-', '+', '+', '-'], 192),
                                                            (['+', '-', '-', '+', '+', '*'], 985),
                                                            (['+', '-', '-', '+', '-', '+'], 200),
                                                            (['+', '-', '-', '+', '-', '-'], 190),
                                                            (['+', '-', '-', '+', '-', '*'], 975),
                                                            (['+', '-', '-', '+', '*', '+'], 201),
                                                            (['+', '-', '-', '+', '*', '-'], 191),
                                                            (['+', '-', '-', '+', '*', '*'], 980),
                                                            (['+', '-', '-', '-', '+', '+'], -162),
                                                            (['+', '-', '-', '-', '+', '-'], -172),
                                                            (['+', '-', '-', '-', '+', '*'], -835),
                                                            (['+', '-', '-', '-', '-', '+'], -164),
                                                            (['+', '-', '-', '-', '-', '-'], -174),
                                                            (['+', '-', '-', '-', '-', '*'], -845),
                                                            (['+', '-', '-', '-', '*', '+'], -163),
                                                            (['+', '-', '-', '-', '*', '-'], -173),
                                                            (['+', '-', '-', '-', '*', '*'], -840),
                                                            (['+', '-', '-', '*', '+', '+'], 2554),
                                                            (['+', '-', '-', '*', '+', '-'], 2544),
                                                            (['+', '-', '-', '*', '+', '*'], 12745),
                                                            (['+', '-', '-', '*', '-', '+'], 2552),
                                                            (['+', '-', '-', '*', '-', '-'], 2542),
                                                            (['+', '-', '-', '*', '-', '*'], 12735),
                                                            (['+', '-', '-', '*', '*', '+'], 2553),
                                                            (['+', '-', '-', '*', '*', '-'], 2543),
                                                            (['+', '-', '-', '*', '*', '*'], 12740),
                                                            (['+', '-', '*', '+', '+', '+'], 260),
                                                            (['+', '-', '*', '+', '+', '-'], 250),
                                                            (['+', '-', '*', '+', '+', '*'], 1275),
                                                            (['+', '-', '*', '+', '-', '+'], 258),
                                                            (['+', '-', '*', '+', '-', '-'], 248),
                                                            (['+', '-', '*', '+', '-', '*'], 1265),
                                                            (['+', '-', '*', '+', '*', '+'], 259),
                                                            (['+', '-', '*', '+', '*', '-'], 249),
                                                            (['+', '-', '*', '+', '*', '*'], 1270),
                                                            (['+', '-', '*', '-', '+', '+'], -104),
                                                            (['+', '-', '*', '-', '+', '-'], -114),
                                                            (['+', '-', '*', '-', '+', '*'], -545),
                                                            (['+', '-', '*', '-', '-', '+'], -106),
                                                            (['+', '-', '*', '-', '-', '-'], -116),
                                                            (['+', '-', '*', '-', '-', '*'], -555),
                                                            (['+', '-', '*', '-', '*', '+'], -105),
                                                            (['+', '-', '*', '-', '*', '-'], -115),
                                                            (['+', '-', '*', '-', '*', '*'], -550),
                                                            (['+', '-', '*', '*', '+', '+'], 13110),
                                                            (['+', '-', '*', '*', '+', '-'], 13100),
                                                            (['+', '-', '*', '*', '+', '*'], 65525),
                                                            (['+', '-', '*', '*', '-', '+'], 13108),
                                                            (['+', '-', '*', '*', '-', '-'], 13098),
                                                            (['+', '-', '*', '*', '-', '*'], 65515),
                                                            (['+', '-', '*', '*', '*', '+'], 13109),
                                                            (['+', '-', '*', '*', '*', '-'], 13099),
                                                            (['+', '-', '*', '*', '*', '*'], 65520),
                                                            (['+', '*', '+', '+', '+', '+'], 552),
                                                            (['+', '*', '+', '+', '+', '-'], 542),
                                                            (['+', '*', '+', '+', '+', '*'], 2735),
                                                            (['+', '*', '+', '+', '-', '+'], 550),
                                                            (['+', '*', '+', '+', '-', '-'], 540),
                                                            (['+', '*', '+', '+', '-', '*'], 2725),
                                                            (['+', '*', '+', '+', '*', '+'], 551),
                                                            (['+', '*', '+', '+', '*', '-'], 541),
                                                            (['+', '*', '+', '+', '*', '*'], 2730),
                                                            (['+', '*', '+', '-', '+', '+'], 188),
                                                            (['+', '*', '+', '-', '+', '-'], 178),
                                                            (['+', '*', '+', '-', '+', '*'], 915),
                                                            (['+', '*', '+', '-', '-', '+'], 186),
                                                            (['+', '*', '+', '-', '-', '-'], 176),
                                                            (['+', '*', '+', '-', '-', '*'], 905),
                                                            (['+', '*', '+', '-', '*', '+'], 187),
                                                            (['+', '*', '+', '-', '*', '-'], 177),
                                                            (['+', '*', '+', '-', '*', '*'], 910),
                                                            (['+', '*', '+', '*', '+', '+'], 66254),
                                                            (['+', '*', '+', '*', '+', '-'], 66244),
                                                            (['+', '*', '+', '*', '+', '*'], 331245),
                                                            (['+', '*', '+', '*', '-', '+'], 66252),
                                                            (['+', '*', '+', '*', '-', '-'], 66242),
                                                            (['+', '*', '+', '*', '-', '*'], 331235),
                                                            (['+', '*', '+', '*', '*', '+'], 66253),
                                                            (['+', '*', '+', '*', '*', '-'], 66243),
                                                            (['+', '*', '+', '*', '*', '*'], 331240),
                                                            (['+', '*', '-', '+', '+', '+'], 544),
                                                            (['+', '*', '-', '+', '+', '-'], 534),
                                                            (['+', '*', '-', '+', '+', '*'], 2695),
                                                            (['+', '*', '-', '+', '-', '+'], 542),
                                                            (['+', '*', '-', '+', '-', '-'], 532),
                                                            (['+', '*', '-', '+', '-', '*'], 2685),
                                                            (['+', '*', '-', '+', '*', '+'], 543),
                                                            (['+', '*', '-', '+', '*', '-'], 533),
                                                            (['+', '*', '-', '+', '*', '*'], 2690),
                                                            (['+', '*', '-', '-', '+', '+'], 180),
                                                            (['+', '*', '-', '-', '+', '-'], 170),
                                                            (['+', '*', '-', '-', '+', '*'], 875),
                                                            (['+', '*', '-', '-', '-', '+'], 178),
                                                            (['+', '*', '-', '-', '-', '-'], 168),
                                                            (['+', '*', '-', '-', '-', '*'], 865),
                                                            (['+', '*', '-', '-', '*', '+'], 179),
                                                            (['+', '*', '-', '-', '*', '-'], 169),
                                                            (['+', '*', '-', '-', '*', '*'], 870),
                                                            (['+', '*', '-', '*', '+', '+'], 64798),
                                                            (['+', '*', '-', '*', '+', '-'], 64788),
                                                            (['+', '*', '-', '*', '+', '*'], 323965),
                                                            (['+', '*', '-', '*', '-', '+'], 64796),
                                                            (['+', '*', '-', '*', '-', '-'], 64786),
                                                            (['+', '*', '-', '*', '-', '*'], 323955),
                                                            (['+', '*', '-', '*', '*', '+'], 64797),
                                                            (['+', '*', '-', '*', '*', '-'], 64787),
                                                            (['+', '*', '-', '*', '*', '*'], 323960),
                                                            (['+', '*', '*', '+', '+', '+'], 1628),
                                                            (['+', '*', '*', '+', '+', '-'], 1618),
                                                            (['+', '*', '*', '+', '+', '*'], 8115),
                                                            (['+', '*', '*', '+', '-', '+'], 1626),
                                                            (['+', '*', '*', '+', '-', '-'], 1616),
                                                            (['+', '*', '*', '+', '-', '*'], 8105),
                                                            (['+', '*', '*', '+', '*', '+'], 1627),
                                                            (['+', '*', '*', '+', '*', '-'], 1617),
                                                            (['+', '*', '*', '+', '*', '*'], 8110),
                                                            (['+', '*', '*', '-', '+', '+'], 1264),
                                                            (['+', '*', '*', '-', '+', '-'], 1254),
                                                            (['+', '*', '*', '-', '+', '*'], 6295),
                                                            (['+', '*', '*', '-', '-', '+'], 1262),
                                                            (['+', '*', '*', '-', '-', '-'], 1252),
                                                            (['+', '*', '*', '-', '-', '*'], 6285),
                                                            (['+', '*', '*', '-', '*', '+'], 1263),
                                                            (['+', '*', '*', '-', '*', '-'], 1253),
                                                            (['+', '*', '*', '-', '*', '*'], 6290),
                                                            (['+', '*', '*', '*', '+', '+'], 262086),
                                                            (['+', '*', '*', '*', '+', '-'], 262076),
                                                            (['+', '*', '*', '*', '+', '*'], 1310405),
                                                            (['+', '*', '*', '*', '-', '+'], 262084),
                                                            (['+', '*', '*', '*', '-', '-'], 262074),
                                                            (['+', '*', '*', '*', '-', '*'], 1310395),
                                                            (['+', '*', '*', '*', '*', '+'], 262085),
                                                            (['+', '*', '*', '*', '*', '-'], 262075),
                                                            (['+', '*', '*', '*', '*', '*'], 1310400),
                                                            (['-', '+', '+', '+', '+', '+'], 150),
                                                            (['-', '+', '+', '+', '+', '-'], 140),
                                                            (['-', '+', '+', '+', '+', '*'], 725),
                                                            (['-', '+', '+', '+', '-', '+'], 148),
                                                            (['-', '+', '+', '+', '-', '-'], 138),
                                                            (['-', '+', '+', '+', '-', '*'], 715),
                                                            (['-', '+', '+', '+', '*', '+'], 149),
                                                            (['-', '+', '+', '+', '*', '-'], 139),
                                                            (['-', '+', '+', '+', '*', '*'], 720),
                                                            (['-', '+', '+', '-', '+', '+'], -214),
                                                            (['-', '+', '+', '-', '+', '-'], -224),
                                                            (['-', '+', '+', '-', '+', '*'], -1095),
                                                            (['-', '+', '+', '-', '-', '+'], -216),
                                                            (['-', '+', '+', '-', '-', '-'], -226),
                                                            (['-', '+', '+', '-', '-', '*'], -1105),
                                                            (['-', '+', '+', '-', '*', '+'], -215),
                                                            (['-', '+', '+', '-', '*', '-'], -225),
                                                            (['-', '+', '+', '-', '*', '*'], -1100),
                                                            (['-', '+', '+', '*', '+', '+'], -6910),
                                                            (['-', '+', '+', '*', '+', '-'], -6920),
                                                            (['-', '+', '+', '*', '+', '*'], -34575),
                                                            (['-', '+', '+', '*', '-', '+'], -6912),
                                                            (['-', '+', '+', '*', '-', '-'], -6922),
                                                            (['-', '+', '+', '*', '-', '*'], -34585),
                                                            (['-', '+', '+', '*', '*', '+'], -6911),
                                                            (['-', '+', '+', '*', '*', '-'], -6921),
                                                            (['-', '+', '+', '*', '*', '*'], -34580),
                                                            (['-', '+', '-', '+', '+', '+'], 142),
                                                            (['-', '+', '-', '+', '+', '-'], 132),
                                                            (['-', '+', '-', '+', '+', '*'], 685),
                                                            (['-', '+', '-', '+', '-', '+'], 140),
                                                            (['-', '+', '-', '+', '-', '-'], 130),
                                                            (['-', '+', '-', '+', '-', '*'], 675),
                                                            (['-', '+', '-', '+', '*', '+'], 141),
                                                            (['-', '+', '-', '+', '*', '-'], 131),
                                                            (['-', '+', '-', '+', '*', '*'], 680),
                                                            (['-', '+', '-', '-', '+', '+'], -222),
                                                            (['-', '+', '-', '-', '+', '-'], -232),
                                                            (['-', '+', '-', '-', '+', '*'], -1135),
                                                            (['-', '+', '-', '-', '-', '+'], -224),
                                                            (['-', '+', '-', '-', '-', '-'], -234),
                                                            (['-', '+', '-', '-', '-', '*'], -1145),
                                                            (['-', '+', '-', '-', '*', '+'], -223),
                                                            (['-', '+', '-', '-', '*', '-'], -233),
                                                            (['-', '+', '-', '-', '*', '*'], -1140),
                                                            (['-', '+', '-', '*', '+', '+'], -8366),
                                                            (['-', '+', '-', '*', '+', '-'], -8376),
                                                            (['-', '+', '-', '*', '+', '*'], -41855),
                                                            (['-', '+', '-', '*', '-', '+'], -8368),
                                                            (['-', '+', '-', '*', '-', '-'], -8378),
                                                            (['-', '+', '-', '*', '-', '*'], -41865),
                                                            (['-', '+', '-', '*', '*', '+'], -8367),
                                                            (['-', '+', '-', '*', '*', '-'], -8377),
                                                            (['-', '+', '-', '*', '*', '*'], -41860),
                                                            (['-', '+', '*', '+', '+', '+'], 20),
                                                            (['-', '+', '*', '+', '+', '-'], 10),
                                                            (['-', '+', '*', '+', '+', '*'], 75),
                                                            (['-', '+', '*', '+', '-', '+'], 18),
                                                            (['-', '+', '*', '+', '-', '-'], 8),
                                                            (['-', '+', '*', '+', '-', '*'], 65),
                                                            (['-', '+', '*', '+', '*', '+'], 19),
                                                            (['-', '+', '*', '+', '*', '-'], 9),
                                                            (['-', '+', '*', '+', '*', '*'], 70),
                                                            (['-', '+', '*', '-', '+', '+'], -344),
                                                            (['-', '+', '*', '-', '+', '-'], -354),
                                                            (['-', '+', '*', '-', '+', '*'], -1745),
                                                            (['-', '+', '*', '-', '-', '+'], -346),
                                                            (['-', '+', '*', '-', '-', '-'], -356),
                                                            (['-', '+', '*', '-', '-', '*'], -1755),
                                                            (['-', '+', '*', '-', '*', '+'], -345),
                                                            (['-', '+', '*', '-', '*', '-'], -355),
                                                            (['-', '+', '*', '-', '*', '*'], -1750),
                                                            (['-', '+', '*', '*', '+', '+'], -30570),
                                                            (['-', '+', '*', '*', '+', '-'], -30580),
                                                            (['-', '+', '*', '*', '+', '*'], -152875),
                                                            (['-', '+', '*', '*', '-', '+'], -30572),
                                                            (['-', '+', '*', '*', '-', '-'], -30582),
                                                            (['-', '+', '*', '*', '-', '*'], -152885),
                                                            (['-', '+', '*', '*', '*', '+'], -30571),
                                                            (['-', '+', '*', '*', '*', '-'], -30581),
                                                            (['-', '+', '*', '*', '*', '*'], -152880),
                                                            (['-', '-', '+', '+', '+', '+'], 126),
                                                            (['-', '-', '+', '+', '+', '-'], 116),
                                                            (['-', '-', '+', '+', '+', '*'], 605),
                                                            (['-', '-', '+', '+', '-', '+'], 124),
                                                            (['-', '-', '+', '+', '-', '-'], 114),
                                                            (['-', '-', '+', '+', '-', '*'], 595),
                                                            (['-', '-', '+', '+', '*', '+'], 125),
                                                            (['-', '-', '+', '+', '*', '-'], 115),
                                                            (['-', '-', '+', '+', '*', '*'], 600),
                                                            (['-', '-', '+', '-', '+', '+'], -238),
                                                            (['-', '-', '+', '-', '+', '-'], -248),
                                                            (['-', '-', '+', '-', '+', '*'], -1215),
                                                            (['-', '-', '+', '-', '-', '+'], -240),
                                                            (['-', '-', '+', '-', '-', '-'], -250),
                                                            (['-', '-', '+', '-', '-', '*'], -1225),
                                                            (['-', '-', '+', '-', '*', '+'], -239),
                                                            (['-', '-', '+', '-', '*', '-'], -249),
                                                            (['-', '-', '+', '-', '*', '*'], -1220),
                                                            (['-', '-', '+', '*', '+', '+'], -11278),
                                                            (['-', '-', '+', '*', '+', '-'], -11288),
                                                            (['-', '-', '+', '*', '+', '*'], -56415),
                                                            (['-', '-', '+', '*', '-', '+'], -11280),
                                                            (['-', '-', '+', '*', '-', '-'], -11290),
                                                            (['-', '-', '+', '*', '-', '*'], -56425),
                                                            (['-', '-', '+', '*', '*', '+'], -11279),
                                                            (['-', '-', '+', '*', '*', '-'], -11289),
                                                            (['-', '-', '+', '*', '*', '*'], -56420),
                                                            (['-', '-', '-', '+', '+', '+'], 118),
                                                            (['-', '-', '-', '+', '+', '-'], 108),
                                                            (['-', '-', '-', '+', '+', '*'], 565),
                                                            (['-', '-', '-', '+', '-', '+'], 116),
                                                            (['-', '-', '-', '+', '-', '-'], 106),
                                                            (['-', '-', '-', '+', '-', '*'], 555),
                                                            (['-', '-', '-', '+', '*', '+'], 117),
                                                            (['-', '-', '-', '+', '*', '-'], 107),
                                                            (['-', '-', '-', '+', '*', '*'], 560),
                                                            (['-', '-', '-', '-', '+', '+'], -246),
                                                            (['-', '-', '-', '-', '+', '-'], -256),
                                                            (['-', '-', '-', '-', '+', '*'], -1255),
                                                            (['-', '-', '-', '-', '-', '+'], -248),
                                                            (['-', '-', '-', '-', '-', '-'], -258),
                                                            (['-', '-', '-', '-', '-', '*'], -1265),
                                                            (['-', '-', '-', '-', '*', '+'], -247),
                                                            (['-', '-', '-', '-', '*', '-'], -257),
                                                            (['-', '-', '-', '-', '*', '*'], -1260),
                                                            (['-', '-', '-', '*', '+', '+'], -12734),
                                                            (['-', '-', '-', '*', '+', '-'], -12744),
                                                            (['-', '-', '-', '*', '+', '*'], -63695),
                                                            (['-', '-', '-', '*', '-', '+'], -12736),
                                                            (['-', '-', '-', '*', '-', '-'], -12746),
                                                            (['-', '-', '-', '*', '-', '*'], -63705),
                                                            (['-', '-', '-', '*', '*', '+'], -12735),
                                                            (['-', '-', '-', '*', '*', '-'], -12745),
                                                            (['-', '-', '-', '*', '*', '*'], -63700),
                                                            (['-', '-', '*', '+', '+', '+'], -76),
                                                            (['-', '-', '*', '+', '+', '-'], -86),
                                                            (['-', '-', '*', '+', '+', '*'], -405),
                                                            (['-', '-', '*', '+', '-', '+'], -78),
                                                            (['-', '-', '*', '+', '-', '-'], -88),
                                                            (['-', '-', '*', '+', '-', '*'], -415),
                                                            (['-', '-', '*', '+', '*', '+'], -77),
                                                            (['-', '-', '*', '+', '*', '-'], -87),
                                                            (['-', '-', '*', '+', '*', '*'], -410),
                                                            (['-', '-', '*', '-', '+', '+'], -440),
                                                            (['-', '-', '*', '-', '+', '-'], -450),
                                                            (['-', '-', '*', '-', '+', '*'], -2225),
                                                            (['-', '-', '*', '-', '-', '+'], -442),
                                                            (['-', '-', '*', '-', '-', '-'], -452),
                                                            (['-', '-', '*', '-', '-', '*'], -2235),
                                                            (['-', '-', '*', '-', '*', '+'], -441),
                                                            (['-', '-', '*', '-', '*', '-'], -451),
                                                            (['-', '-', '*', '-', '*', '*'], -2230),
                                                            (['-', '-', '*', '*', '+', '+'], -48042),
                                                            (['-', '-', '*', '*', '+', '-'], -48052),
                                                            (['-', '-', '*', '*', '+', '*'], -240235),
                                                            (['-', '-', '*', '*', '-', '+'], -48044),
                                                            (['-', '-', '*', '*', '-', '-'], -48054),
                                                            (['-', '-', '*', '*', '-', '*'], -240245),
                                                            (['-', '-', '*', '*', '*', '+'], -48043),
                                                            (['-', '-', '*', '*', '*', '-'], -48053),
                                                            (['-', '-', '*', '*', '*', '*'], -240240),
                                                            (['-', '*', '+', '+', '+', '+'], -456),
                                                            (['-', '*', '+', '+', '+', '-'], -466),
                                                            (['-', '*', '+', '+', '+', '*'], -2305),
                                                            (['-', '*', '+', '+', '-', '+'], -458),
                                                            (['-', '*', '+', '+', '-', '-'], -468),
                                                            (['-', '*', '+', '+', '-', '*'], -2315),
                                                            (['-', '*', '+', '+', '*', '+'], -457),
                                                            (['-', '*', '+', '+', '*', '-'], -467),
                                                            (['-', '*', '+', '+', '*', '*'], -2310),
                                                            (['-', '*', '+', '-', '+', '+'], -820),
                                                            (['-', '*', '+', '-', '+', '-'], -830),
                                                            (['-', '*', '+', '-', '+', '*'], -4125),
                                                            (['-', '*', '+', '-', '-', '+'], -822),
                                                            (['-', '*', '+', '-', '-', '-'], -832),
                                                            (['-', '*', '+', '-', '-', '*'], -4135),
                                                            (['-', '*', '+', '-', '*', '+'], -821),
                                                            (['-', '*', '+', '-', '*', '-'], -831),
                                                            (['-', '*', '+', '-', '*', '*'], -4130),
                                                            (['-', '*', '+', '*', '+', '+'], -117202),
                                                            (['-', '*', '+', '*', '+', '-'], -117212),
                                                            (['-', '*', '+', '*', '+', '*'], -586035),
                                                            (['-', '*', '+', '*', '-', '+'], -117204),
                                                            (['-', '*', '+', '*', '-', '-'], -117214),
                                                            (['-', '*', '+', '*', '-', '*'], -586045),
                                                            (['-', '*', '+', '*', '*', '+'], -117203),
                                                            (['-', '*', '+', '*', '*', '-'], -117213),
                                                            (['-', '*', '+', '*', '*', '*'], -586040),
                                                            (['-', '*', '-', '+', '+', '+'], -464),
                                                            (['-', '*', '-', '+', '+', '-'], -474),
                                                            (['-', '*', '-', '+', '+', '*'], -2345),
                                                            (['-', '*', '-', '+', '-', '+'], -466),
                                                            (['-', '*', '-', '+', '-', '-'], -476),
                                                            (['-', '*', '-', '+', '-', '*'], -2355),
                                                            (['-', '*', '-', '+', '*', '+'], -465),
                                                            (['-', '*', '-', '+', '*', '-'], -475),
                                                            (['-', '*', '-', '+', '*', '*'], -2350),
                                                            (['-', '*', '-', '-', '+', '+'], -828),
                                                            (['-', '*', '-', '-', '+', '-'], -838),
                                                            (['-', '*', '-', '-', '+', '*'], -4165),
                                                            (['-', '*', '-', '-', '-', '+'], -830),
                                                            (['-', '*', '-', '-', '-', '-'], -840),
                                                            (['-', '*', '-', '-', '-', '*'], -4175),
                                                            (['-', '*', '-', '-', '*', '+'], -829),
                                                            (['-', '*', '-', '-', '*', '-'], -839),
                                                            (['-', '*', '-', '-', '*', '*'], -4170),
                                                            (['-', '*', '-', '*', '+', '+'], -118658),
                                                            (['-', '*', '-', '*', '+', '-'], -118668),
                                                            (['-', '*', '-', '*', '+', '*'], -593315),
                                                            (['-', '*', '-', '*', '-', '+'], -118660),
                                                            (['-', '*', '-', '*', '-', '-'], -118670),
                                                            (['-', '*', '-', '*', '-', '*'], -593325),
                                                            (['-', '*', '-', '*', '*', '+'], -118659),
                                                            (['-', '*', '-', '*', '*', '-'], -118669),
                                                            (['-', '*', '-', '*', '*', '*'], -593320),
                                                            (['-', '*', '*', '+', '+', '+'], -2404),
                                                            (['-', '*', '*', '+', '+', '-'], -2414),
                                                            (['-', '*', '*', '+', '+', '*'], -12045),
                                                            (['-', '*', '*', '+', '-', '+'], -2406),
                                                            (['-', '*', '*', '+', '-', '-'], -2416),
                                                            (['-', '*', '*', '+', '-', '*'], -12055),
                                                            (['-', '*', '*', '+', '*', '+'], -2405),
                                                            (['-', '*', '*', '+', '*', '-'], -2415),
                                                            (['-', '*', '*', '+', '*', '*'], -12050),
                                                            (['-', '*', '*', '-', '+', '+'], -2768),
                                                            (['-', '*', '*', '-', '+', '-'], -2778),
                                                            (['-', '*', '*', '-', '+', '*'], -13865),
                                                            (['-', '*', '*', '-', '-', '+'], -2770),
                                                            (['-', '*', '*', '-', '-', '-'], -2780),
                                                            (['-', '*', '*', '-', '-', '*'], -13875),
                                                            (['-', '*', '*', '-', '*', '+'], -2769),
                                                            (['-', '*', '*', '-', '*', '-'], -2779),
                                                            (['-', '*', '*', '-', '*', '*'], -13870),
                                                            (['-', '*', '*', '*', '+', '+'], -471738),
                                                            (['-', '*', '*', '*', '+', '-'], -471748),
                                                            (['-', '*', '*', '*', '+', '*'], -2358715),
                                                            (['-', '*', '*', '*', '-', '+'], -471740),
                                                            (['-', '*', '*', '*', '-', '-'], -471750),
                                                            (['-', '*', '*', '*', '-', '*'], -2358725),
                                                            (['-', '*', '*', '*', '*', '+'], -471739),
                                                            (['-', '*', '*', '*', '*', '-'], -471749),
                                                            (['-', '*', '*', '*', '*', '*'], -2358720),
                                                            (['*', '+', '+', '+', '+', '+'], -300),
                                                            (['*', '+', '+', '+', '+', '-'], -310),
                                                            (['*', '+', '+', '+', '+', '*'], -1525),
                                                            (['*', '+', '+', '+', '-', '+'], -302),
                                                            (['*', '+', '+', '+', '-', '-'], -312),
                                                            (['*', '+', '+', '+', '-', '*'], -1535),
                                                            (['*', '+', '+', '+', '*', '+'], -301),
                                                            (['*', '+', '+', '+', '*', '-'], -311),
                                                            (['*', '+', '+', '+', '*', '*'], -1530),
                                                            (['*', '+', '+', '-', '+', '+'], -664),
                                                            (['*', '+', '+', '-', '+', '-'], -674),
                                                            (['*', '+', '+', '-', '+', '*'], -3345),
                                                            (['*', '+', '+', '-', '-', '+'], -666),
                                                            (['*', '+', '+', '-', '-', '-'], -676),
                                                            (['*', '+', '+', '-', '-', '*'], -3355),
                                                            (['*', '+', '+', '-', '*', '+'], -665),
                                                            (['*', '+', '+', '-', '*', '-'], -675),
                                                            (['*', '+', '+', '-', '*', '*'], -3350),
                                                            (['*', '+', '+', '*', '+', '+'], -88810),
                                                            (['*', '+', '+', '*', '+', '-'], -88820),
                                                            (['*', '+', '+', '*', '+', '*'], -444075),
                                                            (['*', '+', '+', '*', '-', '+'], -88812),
                                                            (['*', '+', '+', '*', '-', '-'], -88822),
                                                            (['*', '+', '+', '*', '-', '*'], -444085),
                                                            (['*', '+', '+', '*', '*', '+'], -88811),
                                                            (['*', '+', '+', '*', '*', '-'], -88821),
                                                            (['*', '+', '+', '*', '*', '*'], -444080),
                                                            (['*', '+', '-', '+', '+', '+'], -308),
                                                            (['*', '+', '-', '+', '+', '-'], -318),
                                                            (['*', '+', '-', '+', '+', '*'], -1565),
                                                            (['*', '+', '-', '+', '-', '+'], -310),
                                                            (['*', '+', '-', '+', '-', '-'], -320),
                                                            (['*', '+', '-', '+', '-', '*'], -1575),
                                                            (['*', '+', '-', '+', '*', '+'], -309),
                                                            (['*', '+', '-', '+', '*', '-'], -319),
                                                            (['*', '+', '-', '+', '*', '*'], -1570),
                                                            (['*', '+', '-', '-', '+', '+'], -672),
                                                            (['*', '+', '-', '-', '+', '-'], -682),
                                                            (['*', '+', '-', '-', '+', '*'], -3385),
                                                            (['*', '+', '-', '-', '-', '+'], -674),
                                                            (['*', '+', '-', '-', '-', '-'], -684),
                                                            (['*', '+', '-', '-', '-', '*'], -3395),
                                                            (['*', '+', '-', '-', '*', '+'], -673),
                                                            (['*', '+', '-', '-', '*', '-'], -683),
                                                            (['*', '+', '-', '-', '*', '*'], -3390),
                                                            (['*', '+', '-', '*', '+', '+'], -90266),
                                                            (['*', '+', '-', '*', '+', '-'], -90276),
                                                            (['*', '+', '-', '*', '+', '*'], -451355),
                                                            (['*', '+', '-', '*', '-', '+'], -90268),
                                                            (['*', '+', '-', '*', '-', '-'], -90278),
                                                            (['*', '+', '-', '*', '-', '*'], -451365),
                                                            (['*', '+', '-', '*', '*', '+'], -90267),
                                                            (['*', '+', '-', '*', '*', '-'], -90277),
                                                            (['*', '+', '-', '*', '*', '*'], -451360),
                                                            (['*', '+', '*', '+', '+', '+'], -1780),
                                                            (['*', '+', '*', '+', '+', '-'], -1790),
                                                            (['*', '+', '*', '+', '+', '*'], -8925),
                                                            (['*', '+', '*', '+', '-', '+'], -1782),
                                                            (['*', '+', '*', '+', '-', '-'], -1792),
                                                            (['*', '+', '*', '+', '-', '*'], -8935),
                                                            (['*', '+', '*', '+', '*', '+'], -1781),
                                                            (['*', '+', '*', '+', '*', '-'], -1791),
                                                            (['*', '+', '*', '+', '*', '*'], -8930),
                                                            (['*', '+', '*', '-', '+', '+'], -2144),
                                                            (['*', '+', '*', '-', '+', '-'], -2154),
                                                            (['*', '+', '*', '-', '+', '*'], -10745),
                                                            (['*', '+', '*', '-', '-', '+'], -2146),
                                                            (['*', '+', '*', '-', '-', '-'], -2156),
                                                            (['*', '+', '*', '-', '-', '*'], -10755),
                                                            (['*', '+', '*', '-', '*', '+'], -2145),
                                                            (['*', '+', '*', '-', '*', '-'], -2155),
                                                            (['*', '+', '*', '-', '*', '*'], -10750),
                                                            (['*', '+', '*', '*', '+', '+'], -358170),
                                                            (['*', '+', '*', '*', '+', '-'], -358180),
                                                            (['*', '+', '*', '*', '+', '*'], -1790875),
                                                            (['*', '+', '*', '*', '-', '+'], -358172),
                                                            (['*', '+', '*', '*', '-', '-'], -358182),
                                                            (['*', '+', '*', '*', '-', '*'], -1790885),
                                                            (['*', '+', '*', '*', '*', '+'], -358171),
                                                            (['*', '+', '*', '*', '*', '-'], -358181),
                                                            (['*', '+', '*', '*', '*', '*'], -1790880),
                                                            (['*', '-', '+', '+', '+', '+'], -324),
                                                            (['*', '-', '+', '+', '+', '-'], -334),
                                                            (['*', '-', '+', '+', '+', '*'], -1645),
                                                            (['*', '-', '+', '+', '-', '+'], -326),
                                                            (['*', '-', '+', '+', '-', '-'], -336),
                                                            (['*', '-', '+', '+', '-', '*'], -1655),
                                                            (['*', '-', '+', '+', '*', '+'], -325),
                                                            (['*', '-', '+', '+', '*', '-'], -335),
                                                            (['*', '-', '+', '+', '*', '*'], -1650),
                                                            (['*', '-', '+', '-', '+', '+'], -688),
                                                            (['*', '-', '+', '-', '+', '-'], -698),
                                                            (['*', '-', '+', '-', '+', '*'], -3465),
                                                            (['*', '-', '+', '-', '-', '+'], -690),
                                                            (['*', '-', '+', '-', '-', '-'], -700),
                                                            (['*', '-', '+', '-', '-', '*'], -3475),
                                                            (['*', '-', '+', '-', '*', '+'], -689),
                                                            (['*', '-', '+', '-', '*', '-'], -699),
                                                            (['*', '-', '+', '-', '*', '*'], -3470),
                                                            (['*', '-', '+', '*', '+', '+'], -93178),
                                                            (['*', '-', '+', '*', '+', '-'], -93188),
                                                            (['*', '-', '+', '*', '+', '*'], -465915),
                                                            (['*', '-', '+', '*', '-', '+'], -93180),
                                                            (['*', '-', '+', '*', '-', '-'], -93190),
                                                            (['*', '-', '+', '*', '-', '*'], -465925),
                                                            (['*', '-', '+', '*', '*', '+'], -93179),
                                                            (['*', '-', '+', '*', '*', '-'], -93189),
                                                            (['*', '-', '+', '*', '*', '*'], -465920),
                                                            (['*', '-', '-', '+', '+', '+'], -332),
                                                            (['*', '-', '-', '+', '+', '-'], -342),
                                                            (['*', '-', '-', '+', '+', '*'], -1685),
                                                            (['*', '-', '-', '+', '-', '+'], -334),
                                                            (['*', '-', '-', '+', '-', '-'], -344),
                                                            (['*', '-', '-', '+', '-', '*'], -1695),
                                                            (['*', '-', '-', '+', '*', '+'], -333),
                                                            (['*', '-', '-', '+', '*', '-'], -343),
                                                            (['*', '-', '-', '+', '*', '*'], -1690),
                                                            (['*', '-', '-', '-', '+', '+'], -696),
                                                            (['*', '-', '-', '-', '+', '-'], -706),
                                                            (['*', '-', '-', '-', '+', '*'], -3505),
                                                            (['*', '-', '-', '-', '-', '+'], -698),
                                                            (['*', '-', '-', '-', '-', '-'], -708),
                                                            (['*', '-', '-', '-', '-', '*'], -3515),
                                                            (['*', '-', '-', '-', '*', '+'], -697),
                                                            (['*', '-', '-', '-', '*', '-'], -707),
                                                            (['*', '-', '-', '-', '*', '*'], -3510),
                                                            (['*', '-', '-', '*', '+', '+'], -94634),
                                                            (['*', '-', '-', '*', '+', '-'], -94644),
                                                            (['*', '-', '-', '*', '+', '*'], -473195),
                                                            (['*', '-', '-', '*', '-', '+'], -94636),
                                                            (['*', '-', '-', '*', '-', '-'], -94646),
                                                            (['*', '-', '-', '*', '-', '*'], -473205),
                                                            (['*', '-', '-', '*', '*', '+'], -94635),
                                                            (['*', '-', '-', '*', '*', '-'], -94645),
                                                            (['*', '-', '-', '*', '*', '*'], -473200),
                                                            (['*', '-', '*', '+', '+', '+'], -1876),
                                                            (['*', '-', '*', '+', '+', '-'], -1886),
                                                            (['*', '-', '*', '+', '+', '*'], -9405),
                                                            (['*', '-', '*', '+', '-', '+'], -1878),
                                                            (['*', '-', '*', '+', '-', '-'], -1888),
                                                            (['*', '-', '*', '+', '-', '*'], -9415),
                                                            (['*', '-', '*', '+', '*', '+'], -1877),
                                                            (['*', '-', '*', '+', '*', '-'], -1887),
                                                            (['*', '-', '*', '+', '*', '*'], -9410),
                                                            (['*', '-', '*', '-', '+', '+'], -2240),
                                                            (['*', '-', '*', '-', '+', '-'], -2250),
                                                            (['*', '-', '*', '-', '+', '*'], -11225),
                                                            (['*', '-', '*', '-', '-', '+'], -2242),
                                                            (['*', '-', '*', '-', '-', '-'], -2252),
                                                            (['*', '-', '*', '-', '-', '*'], -11235),
                                                            (['*', '-', '*', '-', '*', '+'], -2241),
                                                            (['*', '-', '*', '-', '*', '-'], -2251),
                                                            (['*', '-', '*', '-', '*', '*'], -11230),
                                                            (['*', '-', '*', '*', '+', '+'], -375642),
                                                            (['*', '-', '*', '*', '+', '-'], -375652),
                                                            (['*', '-', '*', '*', '+', '*'], -1878235),
                                                            (['*', '-', '*', '*', '-', '+'], -375644),
                                                            (['*', '-', '*', '*', '-', '-'], -375654),
                                                            (['*', '-', '*', '*', '-', '*'], -1878245),
                                                            (['*', '-', '*', '*', '*', '+'], -375643),
                                                            (['*', '-', '*', '*', '*', '-'], -375653),
                                                            (['*', '-', '*', '*', '*', '*'], -1878240),
                                                            (['*', '*', '+', '+', '+', '+'], -5856),
                                                            (['*', '*', '+', '+', '+', '-'], -5866),
                                                            (['*', '*', '+', '+', '+', '*'], -29305),
                                                            (['*', '*', '+', '+', '-', '+'], -5858),
                                                            (['*', '*', '+', '+', '-', '-'], -5868),
                                                            (['*', '*', '+', '+', '-', '*'], -29315),
                                                            (['*', '*', '+', '+', '*', '+'], -5857),
                                                            (['*', '*', '+', '+', '*', '-'], -5867),
                                                            (['*', '*', '+', '+', '*', '*'], -29310),
                                                            (['*', '*', '+', '-', '+', '+'], -6220),
                                                            (['*', '*', '+', '-', '+', '-'], -6230),
                                                            (['*', '*', '+', '-', '+', '*'], -31125),
                                                            (['*', '*', '+', '-', '-', '+'], -6222),
                                                            (['*', '*', '+', '-', '-', '-'], -6232),
                                                            (['*', '*', '+', '-', '-', '*'], -31135),
                                                            (['*', '*', '+', '-', '*', '+'], -6221),
                                                            (['*', '*', '+', '-', '*', '-'], -6231),
                                                            (['*', '*', '+', '-', '*', '*'], -31130),
                                                            (['*', '*', '+', '*', '+', '+'], -1100002),
                                                            (['*', '*', '+', '*', '+', '-'], -1100012),
                                                            (['*', '*', '+', '*', '+', '*'], -5500035),
                                                            (['*', '*', '+', '*', '-', '+'], -1100004),
                                                            (['*', '*', '+', '*', '-', '-'], -1100014),
                                                            (['*', '*', '+', '*', '-', '*'], -5500045),
                                                            (['*', '*', '+', '*', '*', '+'], -1100003),
                                                            (['*', '*', '+', '*', '*', '-'], -1100013),
                                                            (['*', '*', '+', '*', '*', '*'], -5500040),
                                                            (['*', '*', '-', '+', '+', '+'], -5864),
                                                            (['*', '*', '-', '+', '+', '-'], -5874),
                                                            (['*', '*', '-', '+', '+', '*'], -29345),
                                                            (['*', '*', '-', '+', '-', '+'], -5866),
                                                            (['*', '*', '-', '+', '-', '-'], -5876),
                                                            (['*', '*', '-', '+', '-', '*'], -29355),
                                                            (['*', '*', '-', '+', '*', '+'], -5865),
                                                            (['*', '*', '-', '+', '*', '-'], -5875),
                                                            (['*', '*', '-', '+', '*', '*'], -29350),
                                                            (['*', '*', '-', '-', '+', '+'], -6228),
                                                            (['*', '*', '-', '-', '+', '-'], -6238),
                                                            (['*', '*', '-', '-', '+', '*'], -31165),
                                                            (['*', '*', '-', '-', '-', '+'], -6230),
                                                            (['*', '*', '-', '-', '-', '-'], -6240),
                                                            (['*', '*', '-', '-', '-', '*'], -31175),
                                                            (['*', '*', '-', '-', '*', '+'], -6229),
                                                            (['*', '*', '-', '-', '*', '-'], -6239),
                                                            (['*', '*', '-', '-', '*', '*'], -31170),
                                                            (['*', '*', '-', '*', '+', '+'], -1101458),
                                                            (['*', '*', '-', '*', '+', '-'], -1101468),
                                                            (['*', '*', '-', '*', '+', '*'], -5507315),
                                                            (['*', '*', '-', '*', '-', '+'], -1101460),
                                                            (['*', '*', '-', '*', '-', '-'], -1101470),
                                                            (['*', '*', '-', '*', '-', '*'], -5507325),
                                                            (['*', '*', '-', '*', '*', '+'], -1101459),
                                                            (['*', '*', '-', '*', '*', '-'], -1101469),
                                                            (['*', '*', '-', '*', '*', '*'], -5507320),
                                                            (['*', '*', '*', '+', '+', '+'], -24004),
                                                            (['*', '*', '*', '+', '+', '-'], -24014),
                                                            (['*', '*', '*', '+', '+', '*'], -120045),
                                                            (['*', '*', '*', '+', '-', '+'], -24006),
                                                            (['*', '*', '*', '+', '-', '-'], -24016),
                                                            (['*', '*', '*', '+', '-', '*'], -120055),
                                                            (['*', '*', '*', '+', '*', '+'], -24005),
                                                            (['*', '*', '*', '+', '*', '-'], -24015),
                                                            (['*', '*', '*', '+', '*', '*'], -120050),
                                                            (['*', '*', '*', '-', '+', '+'], -24368),
                                                            (['*', '*', '*', '-', '+', '-'], -24378),
                                                            (['*', '*', '*', '-', '+', '*'], -121865),
                                                            (['*', '*', '*', '-', '-', '+'], -24370),
                                                            (['*', '*', '*', '-', '-', '-'], -24380),
                                                            (['*', '*', '*', '-', '-', '*'], -121875),
                                                            (['*', '*', '*', '-', '*', '+'], -24369),
                                                            (['*', '*', '*', '-', '*', '-'], -24379),
                                                            (['*', '*', '*', '-', '*', '*'], -121870),
                                                            (['*', '*', '*', '*', '+', '+'], -4402938),
                                                            (['*', '*', '*', '*', '+', '-'], -4402948),
                                                            (['*', '*', '*', '*', '+', '*'], -22014715),
                                                            (['*', '*', '*', '*', '-', '+'], -4402940),
                                                            (['*', '*', '*', '*', '-', '-'], -4402950),
                                                            (['*', '*', '*', '*', '-', '*'], -22014725),
                                                            (['*', '*', '*', '*', '*', '+'], -4402939),
                                                            (['*', '*', '*', '*', '*', '-'], -4402949),
                                                            (['*', '*', '*', '*', '*', '*'], -22014720)]

assert facit_find_matching([3, 5, 11], 165) == [(['*', '*'], 165)]

assert facit_find_matching([1, 1, 1], 1) == [(['+', '-'], 1), (['-', '+'], 1), (['*', '*'], 1)]
