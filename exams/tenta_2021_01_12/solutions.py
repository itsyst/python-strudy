import math

"""
LÃ¶sningsfÃ¶rslag fÃ¶r tenta i TDDE24 2021-01-12.

TÃ¤nk pÃ¥ att detta Ã¤r *fÃ¶rslag* pÃ¥ lÃ¶sningar.  Det finns mÃ¥nga olika sÃ¤tt
att lÃ¶sa uppgifterna!

Testfall finns pÃ¥ slutet.  TÃ¤nk pÃ¥ att de allra flesta problem som vi
ser i inlÃ¤mningarna skulle ha upptÃ¤ckts med en *mycket* mindre uppsÃ¤ttning
testfall, som inte alls hade tagit mycket tid att skapa.  Att vi anvÃ¤nder
sÃ¥ mÃ¥nga testfall beror pÃ¥ att det underlÃ¤ttar nÃ¤r man har 160-170
inlÃ¤mningar:

1) Vi anvÃ¤nder inte bara testfall fÃ¶r att *upptÃ¤cka* problem utan ocksÃ¥
fÃ¶r att grupper och *kategorisera* dem.  FÃ¶r er kan det gÃ¥ snabbare att
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

def inside_oval(width, height, col, row):
    row = row - height / 2 + 0.5
    col = col - width / 2 + 0.5
    return row * row / (height * height) + col * col / (width * width) <= 0.25


# HÃ¤r har vi en kort lÃ¶sning som anvÃ¤nder listbyggare och
# konstruktionen "x if sanningsvÃ¤rde else y".
def oval(width, height):
    return [["X" if inside_oval(width, height, col, row) else "."
             for col in range(width)]
            for row in range(height)]


# Det gÃ¥r sÃ¥ klart utmÃ¤rkt att anvÃ¤nda vanliga nÃ¤stlade loopar,
# med append() och vanliga if-else-satser.
def oval_alternative(width, height):
    result = []
    for row in range(height):
        subresult = []
        for col in range(width):
            if inside_oval(width, height, col, row):
                subresult.append("X")
            else:
                subresult.append(".")
        result.append(subresult)
    return result


# ======================================================================
# Uppgift 2
# ======================================================================

# HÃ¤r kommer en fullstÃ¤ndig lÃ¶sning pÃ¥ uppgift 2a-2b-2c.

def eval_pyassm(prog):
    vals = {}

    # Om man vill bÃ¶rja med en tom dictionary Ã¤r det bra att skapa en
    # sÃ¤rskild hjÃ¤lpfunktion som tittar pÃ¥ innehÃ¥llet, sÃ¥ man slipper
    # att testa "if r in vals" om och om igen i resten av koden.
    def read_reg(r):
        assert r in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if r in vals:
            return vals[r]
        return 0

    # En stack med returadresser fÃ¶r JSR/RET
    return_addresses = []

    # Eftersom vi ska kunna hoppa runt Ã¤r det bra att anvÃ¤nda ett index
    # fÃ¶r "nuvarande instruktion" (instruktionspekare ip).
    ip = 0

    # Instruktionerna sÃ¤ger att vi ska avsluta sÃ¥ snart som vi hoppar till
    # en position som Ã¤r efter slutet av programmet.
    while ip < len(prog):

        # Spara undan instruktionen vi Ã¤r intresserade av och stega fram
        # indexet till nÃ¤sta instruktion.
        inst = prog[ip]
        op = inst[0]
        ip += 1

        if op == "LOG":
            print(f"[{inst[1]}={read_reg(inst[1])}]")
        elif op == "CPY":
            vals[inst[1]] = read_reg(inst[2])
        elif op == "SET":
            vals[inst[1]] = inst[2]
        elif op == "ADD":
            vals[inst[1]] = read_reg(inst[1]) + inst[2]
        elif op == "MUL":
            vals[inst[1]] = read_reg(inst[1]) * inst[2]
        elif op == "JEQ":
            if read_reg(inst[1]) == read_reg(inst[2]):
                # Har redan stegat fram med 1, sÃ¥ Ã¶ka bara med inst[3]-1
                ip += inst[3] - 1
        elif op == "JNE":
            if read_reg(inst[1]) != read_reg(inst[2]):
                # Har redan stegat fram med 1, sÃ¥ Ã¶ka bara med inst[3]-1
                ip += inst[3] - 1
        elif op == "JSR":
            return_addresses.append(ip)
            # I och med att ip+=1 redan Ã¤r utfÃ¶rt behÃ¶ver vi bara gÃ¶ra
            # en enkel tilldelning hÃ¤r.  Hade vi ip+=1 i slutet av loopen
            # skulle vi fÃ¥ sÃ¤tta ip=inst[1]-1 hÃ¤r istÃ¤llet.
            ip = inst[1]
        elif op == "RET":
            ip = return_addresses.pop()
        elif op == "NOP":
            pass
        else:
            # Kan lika gÃ¤rna ha med en extra test hÃ¤r sÃ¥ att vi upptÃ¤cker
            # om vi t.ex. har stavat fel i ett test.
            raise ValueError(f"invalid opcode {op}")


# ======================================================================
# Uppgift 3a
# ======================================================================

def treeval(tree):
    # Ett trÃ¤d Ã¤r en nÃ¤stlad struktur dÃ¤r nodernas barn ocksÃ¥ Ã¤r trÃ¤d,
    # sÃ¥ det Ã¤r rimligt att anvÃ¤nda rekursion pÃ¥ djupet.  Samtidigt
    # kan vi vÃ¤lja att anvÃ¤nda vanlig iteration "Ã¥t hÃ¶ger" fÃ¶r barnen.

    if len(tree) == 1:
        # Kan inte vara en multiplikation, sÃ¥ trÃ¤dvÃ¤rde = nodvÃ¤rde
        val = tree[0]
    elif tree[0] == "*":
        # Multiplicera trÃ¤dvÃ¤rdena fÃ¶r alla barnnoder
        val = treeval(tree[1])
        for node in tree[2:]:
            val *= treeval(node)
    else:
        # Addera nodvÃ¤rdet med trÃ¤dvÃ¤rdena fÃ¶r alla barnnoder
        val = tree[0]
        for node in tree[1:]:
            val += treeval(node)
    return val


def treeval_shorter(tree):
    # Vi kan gÃ¶ra det hela kortare genom att anvÃ¤nda sum() och math.prod()
    # fÃ¶r att slippa att addera/multiplicera med ett barn i taget.
    import math
    if len(tree) == 1:
        val = tree[0]
    elif tree[0] == "*":
        val = math.prod(treeval_shorter(node) for node in tree[1:])
    else:
        val = tree[0] + sum(treeval_shorter(node) for node in tree[1:])
    return val


# ======================================================================
# Uppgift 3b
# ======================================================================

# HÃ¤r har vi ett par alternativ...

def treeval2(tree, always_multiply=False):
    # HÃ¤r mÃ¥ste vi pÃ¥ nÃ¥got sÃ¤tt hÃ¥lla reda pÃ¥ om noden ligger under
    # "***" (dÃ¥ ska vi multiplicera Ã¤ven nÃ¤r det normalt skulle vara
    # addition).  Ett sÃ¤tt att gÃ¶ra det Ã¤r att ha parametern
    # always_multiply med defaultvÃ¤rde False.

    if len(tree) == 1:
        # Som tidigare
        return tree[0]
    elif tree[0] == "*":
        # Som tidigare, men kom ihÃ¥g om vi Ã¤r i "multiplikationslÃ¤ge"
        val = treeval2(tree[1], always_multiply=always_multiply)
        for node in tree[2:]:
            val *= treeval2(node, always_multiply=always_multiply)
    elif tree[0] == "***":
        # Multiplicera, och berÃ¤kna alla barn i "multiplikationslÃ¤ge"
        val = treeval2(tree[1], always_multiply=True)
        for node in tree[2:]:
            val *= treeval2(node, always_multiply=True)
    elif always_multiply:
        # Inte "*" eller "***", sÃ¥ det skulle normalt vara addition
        # men vi Ã¤r i multiplikationslÃ¤ge
        val = tree[0]
        for node in tree[1:]:
            val *= treeval2(node, always_multiply=always_multiply)
    else:
        # Inte "*" eller "***", sÃ¥ det skulle normalt vara addition
        # och vi Ã¤r INTE i multiplikationslÃ¤ge
        val = tree[0]
        for node in tree[1:]:
            val += treeval2(node, always_multiply=always_multiply)
    return val


# HÃ¤r Ã¤r en alternativ lÃ¶sning.  IstÃ¤llet fÃ¶r att ha defaultargument
# hoppar vi in i en annan rekursiv funktion om vi hittar "***".

def treeval2_alternative(tree):
    if len(tree) == 1:
        val = tree[0]
    elif tree[0] == "*":
        val = treeval2_alternative(tree[1])
        for node in tree[2:]:
            val *= treeval2_alternative(node)
    elif tree[0] == "***":
        # Multiplikation OCH anvÃ¤nd treeval2_always_multiply fÃ¶r att
        # berÃ¤kna trÃ¤dvÃ¤rdena
        val = treeval2_always_multiply(tree[1])
        for node in tree[2:]:
            val *= treeval2_always_multiply(node)
    else:
        val = tree[0]
        for node in tree[1:]:
            val += treeval2_alternative(node)
    return val


def treeval2_always_multiply(tree):
    if len(tree) == 1:
        val = tree[0]
    elif tree[0] in ("*", "***"):
        # TvÃ¥ olika former av multiplikation
        val = treeval2_always_multiply(tree[1])
        for node in tree[2:]:
            val *= treeval2_always_multiply(node)
    else:
        # Skulle normalt vara addition, men vi anvÃ¤nder Ã¤ndÃ¥ *=
        # eftersom vi Ã¤r i "multiplikationslÃ¤ge".
        val = tree[0]
        for node in tree[1:]:
            val *= treeval2_always_multiply(node)
    return val


# ======================================================================
# Uppgift 4a
# ======================================================================

def traverse2(array):
    # HÃ¥ll reda pÃ¥ om vi traverserar Ã¥t hÃ¶ger eller vÃ¤nster
    right = True
    result = []
    for row in array:
        # Vi mÃ¥ste iterera Ã¥t olika hÃ¥ll beroende pÃ¥ vÃ¤rdet av 'right'.
        # Det kan gÃ¶ras pÃ¥ olika sÃ¤tt -- man kan iterera baklÃ¤nges Ã¶ver
        # index, till exempel.  Ett kortfattat sÃ¤tt Ã¤r att anvÃ¤nda
        # reversed(seq), eller seq[::-1], vilket returnerar en reverserad
        # *kopia* av raden.  Att kÃ¶ra row.reverse() *Ã¤ndrar* istÃ¤llet
        # i raden vilket inte Ã¤r bra.
        for element in (row if right else reversed(row)):
            if element is not None:
                result.append(element)
        # Byt riktning
        right = not right
    return result


# ======================================================================
# Uppgift 4b
# ======================================================================

# Exakt samma, utom att vi tar in ett predikat och kollar pred(element)
# istÃ¤llet fÃ¶r 'element is not None'.

def traverse2p(array, pred):
    right = True
    result = []
    for row in array:
        for element in (row if right else row[::-1]):
            if pred(element):
                result.append(element)
        right = not right
    return result


# ======================================================================
# Uppgift 4c
# ======================================================================

# Nu har vi godtyckligt antal nivÃ¥er och Ã¤r det inte lÃ¤ngre rimligt att
# anvÃ¤nda nÃ¤stlade loopar.  IstÃ¤llet hamnar vi Ã¥terigen i en nÃ¤stlad
# struktur som bÃ¤st hanteras med rekursion.

# Dessutom ska vi inte lÃ¤ngre gÃ¥ baklÃ¤nges i varannan *rad*, utan pÃ¥
# varannan *nivÃ¥*.  DÃ¥ kan vi anvÃ¤nda ett defaultargument som hÃ¥ller reda
# pÃ¥ vilken nivÃ¥ vi har.  Alternativt kunde vi sÃ¥ klart ha definierat
# en hjÃ¤lpmetod traverseNp_helper() som har motsvarande tre argument
# som *inte* har defaultvÃ¤rden (sÃ¥ man behÃ¶vde inte veta hur man
# anvÃ¤nder defaultvÃ¤rden fÃ¶r att lÃ¶sa detta).

def traverseNp(array, pred, right=True):
    result = []

    # Iterera Ã¶ver alla element i den ordning vi ska ha pÃ¥ denna nivÃ¥
    for element in (array if right else array[::-1]):

        # Ã„r elementet en lista?  DÃ¥ sÃ¤ger instruktionerna att den
        # ocksÃ¥ ska traverseras, eftersom den ocksÃ¥ Ã¤r ett rutnÃ¤t.
        if isinstance(element, list):
            # Traverseringsordningen fÃ¶r listan Ã¤r den omvÃ¤nda,
            # eftersom listan ligger pÃ¥ nÃ¤sta nivÃ¥.
            subresult = traverseNp(element, pred, not right)

            # Resultatet subresult blir en lista element, och vi
            # utÃ¶kar vÃ¥rt fullstÃ¤ndiga resultat med alla dessa element.
            result.extend(subresult)

        elif pred(element):
            # Elementet Ã¤r inte en lista, sÃ¥ det Ã¤r ett vanligt
            # element som ska lÃ¤ggas till.
            result.append(element)

    # Klart!
    return result


# ======================================================================
# Uppgift 5a
# ======================================================================

def find_subseq(subseq, seq):
    positions = []

    pos = 0
    for element in subseq:
        # Nu behÃ¶ver vi fÃ¶rsÃ¶ka hitta detta element med start pÃ¥
        # position pos.  Iterera till vi hittar det!
        found = False
        while not found:
            # Har elementen i seq tagit slut?  DÃ¥ har vi
            # misslyckats helt och hÃ¥llet!
            if pos == len(seq):
                return None

            # Ã„r det pÃ¥ *den hÃ¤r* positionen i seq?  Hurra!
            if seq[pos] == element:
                positions.append(pos)
                found = True

            # OK, vi har inte hittat elementet men kanske det finns pÃ¥
            # en senare position.  GÃ¥ till nÃ¤sta.
            pos += 1
        # Om vi kommer hit (en iteration av for-loopen Ã¤r klar) har vi
        # hittat nuvarande element i subseq och kan gÃ¥ vidare med nÃ¤sta
    # Om vi kommer hit (hela for-loopen Ã¤r klar) har vi hittat alla
    # element i subseq och kan returnera
    return positions


# HÃ¤r kommer ett kortare alternativ.
def find_subseq_shorter(subseq, seq):
    positions = []

    # Vi behÃ¶ver se till att elementen hittas i rÃ¤tt ordning, sÃ¥ vi
    # hÃ¥ller reda pÃ¥ en startposition.
    searchfrom = 0
    for element in subseq:
        if element in seq[searchfrom:]:
            # Elementet finns nÃ¥gonstans efter det fÃ¶rra elementet
            # vi hittade, sÃ¥ ta fram positionen fÃ¶r det.
            pos = searchfrom + seq[searchfrom:].index(element)
            positions.append(pos)
            # NÃ¤sta element i subseq fÃ¥r inte hittas fÃ¶re pos+1.
            searchfrom = pos + 1
        else:
            # Elementet fanns inte pÃ¥ rÃ¤tt plats.
            return None
    return positions


# ======================================================================
# Uppgift 5b
# ======================================================================


def find_with_max_distance(subseq, seq, maxdist, steps_left=None, pos=0):
    if not subseq:
        # Subseq Ã¤r tom, sÃ¥ "alla element i subseq" finns pÃ¥ positionerna [].
        return []

    if not seq:
        # Vi har fÃ¥tt slut pÃ¥ element i seq, sÃ¥ det finns ingen lÃ¶sning
        # (i alla fall inte i den hÃ¤r grenen av sÃ¶kningen)
        return None

    if subseq[0] == seq[0]:
        # Elementet fÃ¶rst i subseq matchar elementet fÃ¶rst i seq.
        # GÃ¥r det att hitta en lÃ¶sning genom att TA MED detta elements
        # index i vÃ¥r lÃ¶sning?  Vi provar, genom att Ã¤ta upp ett element
        # frÃ¥n bÃ¥de subseq och seq.  DÃ¥ mÃ¥ste nÃ¤sta *element* hittas inom
        # steps_left=maxdist frÃ¥n den *nya* positionen pos+1.
        maybe = find_with_max_distance(subseq[1:], seq[1:], maxdist,
                                       steps_left=maxdist, pos=pos + 1)

        if maybe is not None:
            # Hurra!  Det fungerade!
            return [pos] + maybe

    # OK, det fungerade inte.  Kan vi stega framÃ¥t och hitta subseq[0] pÃ¥
    # en senare plats i seq, sÃ¥ att vi INTE TAR MED detta elements index
    # i vÃ¥r lÃ¶sning?  Kanske vi hittar en kopia till av subseq[0] innan
    # steps_left har tagit slut.

    if steps_left is None:
        # Vi hÃ¥ller pÃ¥ att hitta vÃ¥rt fÃ¶rsta element, sÃ¥ "antal steg kvar"
        # Ã¤r irrelevant Ã¤n sÃ¥ lÃ¤nge.
        return find_with_max_distance(subseq, seq[1:], maxdist, None, pos + 1)
    elif steps_left > 1:
        # Vi har utrymme att gÃ¥ minst ett steg till innan vi nÃ¥r maxdist,
        # men vi mÃ¥ste rÃ¤kna ner antalet steg vi har kvar
        return find_with_max_distance(subseq, seq[1:], maxdist, steps_left - 1, pos + 1)
    else:
        # Vi har redan stegat fram det maximala antalet steg sedan det
        # fÃ¶rra elementet hittades.  GÃ¥r vi vidare i den hÃ¤r grenen av vÃ¥r
        # dubbelrekursion kommer vi bara att hitta "lÃ¶sningar" dÃ¤r vi
        # Ã¶verskrider det maximala avstÃ¥ndet, sÃ¥ vi ger upp i den hÃ¤r
        # grenen.  NÃ¤r vi har returnerat kanske den som anropade oss hittar
        # en lÃ¶sning i en annan gren.
        return None


# ======================================================================
# Uppgift 1:  Testfall
# ======================================================================

assert oval(0, 1) == [[]]
assert oval(1, 1) == [['X']]
assert oval(3, 3) == [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]
assert oval(4, 3) == [['.', 'X', 'X', '.'], ['X', 'X', 'X', 'X'], ['.', 'X', 'X', '.']]
assert oval(5, 6) == [['.', 'X', 'X', 'X', '.'], ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['.', 'X', 'X', 'X', '.']]
assert oval(0, 0) == []
assert oval(0, 1) == [[]]
assert oval(0, 2) == [[], []]
assert oval(0, 3) == [[], [], []]
assert oval(0, 4) == [[], [], [], []]
assert oval(0, 5) == [[], [], [], [], []]
assert oval(1, 0) == []
assert oval(1, 1) == [['X']]
assert oval(1, 2) == [['X'], ['X']]
assert oval(1, 3) == [['X'], ['X'], ['X']]
assert oval(1, 4) == [['X'], ['X'], ['X'], ['X']]
assert oval(1, 5) == [['X'], ['X'], ['X'], ['X'], ['X']]
assert oval(2, 0) == []
assert oval(2, 1) == [['X', 'X']]
assert oval(2, 2) == [['X', 'X'], ['X', 'X']]
assert oval(2, 3) == [['X', 'X'], ['X', 'X'], ['X', 'X']]
assert oval(2, 4) == [['X', 'X'], ['X', 'X'], ['X', 'X'], ['X', 'X']]
assert oval(2, 5) == [['X', 'X'], ['X', 'X'], ['X', 'X'], ['X', 'X'], ['X', 'X']]
assert oval(3, 0) == []
assert oval(3, 1) == [['X', 'X', 'X']]
assert oval(3, 2) == [['X', 'X', 'X'], ['X', 'X', 'X']]
assert oval(3, 3) == [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]
assert oval(3, 4) == [['.', 'X', '.'], ['X', 'X', 'X'], ['X', 'X', 'X'], ['.', 'X', '.']]
assert oval(3, 5) == [['.', 'X', '.'], ['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X'], ['.', 'X', '.']]
assert oval(4, 0) == []
assert oval(4, 1) == [['X', 'X', 'X', 'X']]
assert oval(4, 2) == [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X']]
assert oval(4, 3) == [['.', 'X', 'X', '.'], ['X', 'X', 'X', 'X'], ['.', 'X', 'X', '.']]
assert oval(4, 4) == [['.', 'X', 'X', '.'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['.', 'X', 'X', '.']]
assert oval(4, 5) == [['.', 'X', 'X', '.'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'],
                      ['.', 'X', 'X', '.']]
assert oval(5, 0) == []
assert oval(5, 1) == [['X', 'X', 'X', 'X', 'X']]
assert oval(5, 2) == [['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X']]
assert oval(5, 3) == [['.', 'X', 'X', 'X', '.'], ['X', 'X', 'X', 'X', 'X'], ['.', 'X', 'X', 'X', '.']]
assert oval(5, 4) == [['.', 'X', 'X', 'X', '.'], ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'],
                      ['.', 'X', 'X', 'X', '.']]
assert oval(5, 5) == [['.', 'X', 'X', 'X', '.'], ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', 'X', 'X'], ['.', 'X', 'X', 'X', '.']]
assert oval(7, 7) == [['.', '.', 'X', 'X', 'X', '.', '.'], ['.', 'X', 'X', 'X', 'X', 'X', '.'],
                      ['X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', 'X', 'X', 'X', 'X'], ['.', 'X', 'X', 'X', 'X', 'X', '.'],
                      ['.', '.', 'X', 'X', 'X', '.', '.']]
assert oval(7, 11) == [['.', '.', 'X', 'X', 'X', '.', '.'], ['.', 'X', 'X', 'X', 'X', 'X', '.'],
                       ['.', 'X', 'X', 'X', 'X', 'X', '.'], ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
                       ['X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
                       ['X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
                       ['.', 'X', 'X', 'X', 'X', 'X', '.'], ['.', 'X', 'X', 'X', 'X', 'X', '.'],
                       ['.', '.', 'X', 'X', 'X', '.', '.']]
assert oval(7, 15) == [['.', '.', 'X', 'X', 'X', '.', '.'], ['.', 'X', 'X', 'X', 'X', 'X', '.'],
                       ['.', 'X', 'X', 'X', 'X', 'X', '.'], ['.', 'X', 'X', 'X', 'X', 'X', '.'],
                       ['X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
                       ['X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
                       ['X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
                       ['X', 'X', 'X', 'X', 'X', 'X', 'X'], ['.', 'X', 'X', 'X', 'X', 'X', '.'],
                       ['.', 'X', 'X', 'X', 'X', 'X', '.'], ['.', 'X', 'X', 'X', 'X', 'X', '.'],
                       ['.', '.', 'X', 'X', 'X', '.', '.']]
assert oval(11, 7) == [['.', '.', '.', 'X', 'X', 'X', 'X', 'X', '.', '.', '.'],
                       ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                       ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                       ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                       ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                       ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                       ['.', '.', '.', 'X', 'X', 'X', 'X', 'X', '.', '.', '.']]
assert oval(11, 11) == [['.', '.', '.', 'X', 'X', 'X', 'X', 'X', '.', '.', '.'],
                        ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
                        ['.', '.', '.', 'X', 'X', 'X', 'X', 'X', '.', '.', '.']]
assert oval(11, 15) == [['.', '.', '.', '.', 'X', 'X', 'X', '.', '.', '.', '.'],
                        ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
                        ['.', '.', '.', '.', 'X', 'X', 'X', '.', '.', '.', '.']]
assert oval(15, 7) == [['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.'],
                       ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                       ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                       ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                       ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                       ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                       ['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.']]
assert oval(15, 11) == [['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.'],
                        ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
                        ['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.']]
assert oval(15, 15) == [['.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.'],
                        ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
                        ['.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.']]
assert oval(0, 10) == [[], [], [], [], [], [], [], [], [], []]
assert oval(10, 0) == []
assert oval(100, 1) == [
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
assert oval(1, 100) == [['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'],
                        ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'],
                        ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'],
                        ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'],
                        ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'],
                        ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'],
                        ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'],
                        ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X'], ['X']]
assert oval(10, 10) == [['.', '.', '.', 'X', 'X', 'X', 'X', '.', '.', '.'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['.', '.', '.', 'X', 'X', 'X', 'X', '.', '.', '.']]
assert oval(15, 15) == [['.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.'],
                        ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
                        ['.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.']]
assert oval(17, 17) == [['.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.'],
                        ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
                        ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                        ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
                        ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
                        ['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.']]
assert oval(30, 30) == [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.',
     '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.',
     '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', '.', '.', '.', '.'],
    ['.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', '.', '.', '.'],
    ['.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', '.', '.', '.'],
    ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', '.', '.'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', '.'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', '.'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', '.'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', '.'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', '.'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', '.'],
    ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', '.', '.'],
    ['.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', '.', '.', '.'],
    ['.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', '.', '.', '.'],
    ['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.',
     '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.',
     '.', '.', '.', '.', '.', '.', '.']]
assert oval(93, 33) == [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.',
     '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.',
     '.'],
    ['.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.',
     '.'],
    ['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.',
     '.'],
    ['.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.',
     '.'],
    ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.',
     '.'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     '.'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     '.'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     '.'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     '.'],
    ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.',
     '.'],
    ['.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.',
     '.'],
    ['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.',
     '.'],
    ['.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.',
     '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.',
     '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.',
     '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.']]
assert oval(33, 93) == [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.',
     '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.',
     '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.',
     '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.'],
    ['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.'],
    ['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.'],
    ['.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.'],
    ['.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.'],
    ['.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.'],
    ['.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.'],
    ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
    ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
    ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
    ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
    ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
    ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
    ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
    ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
    ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
    ['.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
    ['.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.'],
    ['.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.'],
    ['.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.'],
    ['.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.'],
    ['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.'],
    ['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.'],
    ['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     'X', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
     '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.',
     '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.',
     '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.',
     '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]

# ======================================================================
# Uppgift 2:  Testfall
# ======================================================================

# Vi testade dessa program med eval_pyassm().

eval_pyassm([['LOG', 'A']])
eval_pyassm(
    [['SET', 'A', 10], ['MUL', 'A', 5], ['ADD', 'A', 5.25], ['LOG', 'A'], ['CPY', 'B', 'A'], ['LOG', 'A'],
     ['LOG', 'B']])
eval_pyassm([['ADD', 'A', 222]])
eval_pyassm([['ADD', 'A', 222], ['LOG', 'A']])
eval_pyassm([['MUL', 'A', 10], ['LOG', 'A']])
eval_pyassm([['SET', 'F', 10], ['LOG', 'F']])
eval_pyassm([['LOG', 'F']])
eval_pyassm([['SET', 'A', 12], ['LOG', 'W']])
eval_pyassm([['LOG', 'B']])
eval_pyassm([['SET', 'A', 10], ['LOG', 'A']])
eval_pyassm([['SET', 'A', 10], ['LOG', 'U']])
eval_pyassm([['CPY', 'W', 'U'], ['LOG', 'U']])
eval_pyassm([['SET', 'A', 424.5], ['LOG', 'A']])
eval_pyassm([['SET', 'W', 424.5], ['LOG', 'W']])
eval_pyassm(
    [['SET', 'W', 1], ['MUL', 'W', 10], ['MUL', 'W', 10], ['MUL', 'W', 10], ['LOG', 'W']])
eval_pyassm([['SET', 'A', 10], ['CPY', 'X', 'A'], ['SET', 'A', 5], ['LOG', 'A'], ['LOG', 'X']])
eval_pyassm([['SET', 'A', 10], ['CPY', 'A', 'U'], ['LOG', 'A'], ['LOG', 'U']])
eval_pyassm([['SET', 'A', 22.5], ['CPY', 'A', 'U'], ['LOG', 'U']])
eval_pyassm([['SET', 'A', 22.5], ['CPY', 'A', 'U'], ['LOG', 'A']])
eval_pyassm([['SET', 'A', 10], ['LOG', 'A'], ['LOG', 'A']])
eval_pyassm([['SET', 'A', 10], ['LOG', 'A'], ['LOG', 'B']])
eval_pyassm(
    [['SET', 'A', 0], ['SET', 'B', 1], ['SET', 'C', 2], ['SET', 'D', 3], ['SET', 'E', 4], ['SET', 'F', 5],
     ['SET', 'G', 6], ['SET', 'H', 7], ['SET', 'I', 8], ['SET', 'J', 9], ['SET', 'K', 10], ['SET', 'L', 11],
     ['SET', 'M', 12], ['SET', 'N', 13], ['SET', 'O', 14], ['SET', 'P', 15], ['SET', 'Q', 16], ['SET', 'R', 17],
     ['SET', 'S', 18], ['SET', 'T', 19], ['SET', 'U', 20], ['SET', 'V', 21], ['SET', 'W', 22], ['SET', 'X', 23],
     ['SET', 'Y', 24], ['SET', 'Z', 25]])
eval_pyassm(
    [['LOG', 'A'], ['LOG', 'B'], ['LOG', 'C'], ['LOG', 'D'], ['LOG', 'E'], ['LOG', 'F'], ['LOG', 'G'], ['LOG', 'H'],
     ['LOG', 'I'], ['LOG', 'J'], ['LOG', 'K'], ['LOG', 'L'], ['LOG', 'M'], ['LOG', 'N'], ['LOG', 'O'], ['LOG', 'P'],
     ['LOG', 'Q'], ['LOG', 'R'], ['LOG', 'S'], ['LOG', 'T'], ['LOG', 'U'], ['LOG', 'V'], ['LOG', 'W'], ['LOG', 'X'],
     ['LOG', 'Y'], ['LOG', 'Z']])
eval_pyassm(
    [['SET', 'A', 0], ['SET', 'B', 1], ['SET', 'C', 2], ['SET', 'D', 3], ['SET', 'E', 4], ['SET', 'F', 5],
     ['SET', 'G', 6], ['SET', 'H', 7], ['SET', 'I', 8], ['SET', 'J', 9], ['SET', 'K', 10], ['SET', 'L', 11],
     ['SET', 'M', 12], ['SET', 'N', 13], ['SET', 'O', 14], ['SET', 'P', 15], ['SET', 'Q', 16], ['SET', 'R', 17],
     ['SET', 'S', 18], ['SET', 'T', 19], ['SET', 'U', 20], ['SET', 'V', 21], ['SET', 'W', 22], ['SET', 'X', 23],
     ['SET', 'Y', 24], ['SET', 'Z', 25], ['MUL', 'A', 3], ['MUL', 'B', 3], ['MUL', 'C', 3], ['MUL', 'D', 3],
     ['MUL', 'E', 3], ['MUL', 'F', 3], ['MUL', 'G', 3], ['MUL', 'H', 3], ['MUL', 'I', 3], ['MUL', 'J', 3],
     ['MUL', 'K', 3], ['MUL', 'L', 3], ['MUL', 'M', 3], ['MUL', 'N', 3], ['MUL', 'O', 3], ['MUL', 'P', 3],
     ['MUL', 'Q', 3], ['MUL', 'R', 3], ['MUL', 'S', 3], ['MUL', 'T', 3], ['MUL', 'U', 3], ['MUL', 'V', 3],
     ['MUL', 'W', 3], ['MUL', 'X', 3], ['MUL', 'Y', 3], ['MUL', 'Z', 3], ['LOG', 'A'], ['LOG', 'B'], ['LOG', 'C'],
     ['LOG', 'D'], ['LOG', 'E'], ['LOG', 'F'], ['LOG', 'G'], ['LOG', 'H'], ['LOG', 'I'], ['LOG', 'J'], ['LOG', 'K'],
     ['LOG', 'L'], ['LOG', 'M'], ['LOG', 'N'], ['LOG', 'O'], ['LOG', 'P'], ['LOG', 'Q'], ['LOG', 'R'], ['LOG', 'S'],
     ['LOG', 'T'], ['LOG', 'U'], ['LOG', 'V'], ['LOG', 'W'], ['LOG', 'X'], ['LOG', 'Y'], ['LOG', 'Z']])
eval_pyassm([['LOG', 'W']])
eval_pyassm([['SET', 'B', 12], ['LOG', 'W']])
eval_pyassm([['SET', 'X', 12], ['MUL', 'X', 5], ['LOG', 'X']])
eval_pyassm([['SET', 'X', 12], ['LOG', 'X'], ['MUL', 'X', 5], ['LOG', 'X']])
eval_pyassm([['SET', 'B', 12], ['CPY', 'X', 'Y'], ['ADD', 'F', 10]])
eval_pyassm([['SET', 'B', 12], ['CPY', 'X', 'Y'], ['ADD', 'F', 10], ['LOG', 'W']])
eval_pyassm([['CPY', 'B', 'A'], ['ADD', 'B', 5]])
eval_pyassm(
    [['SET', 'A', -5], ['SET', 'B', 2.5], ['SET', 'C', 0], ['MUL', 'A', 5], ['MUL', 'B', 5], ['MUL', 'C', 5],
     ['ADD', 'A', 1.5], ['ADD', 'A', 1.5], ['ADD', 'A', 1.5], ['LOG', 'A'], ['LOG', 'B'], ['LOG', 'C']])
eval_pyassm(
    [['SET', 'A', 10], ['SET', 'Q', 8], ['ADD', 'C', 5], ['LOG', 'C'], ['LOG', 'A'], ['CPY', 'K', 'Q'], ['MUL', 'Q', 8],
     ['LOG', 'B'], ['LOG', 'K'], ['ADD', 'A', 15], ['LOG', 'A'], ['LOG', 'Q']])
eval_pyassm(
    [['SET', 'A', 1], ['MUL', 'A', 15], ['ADD', 'A', 1.5], ['LOG', 'A'], ['CPY', 'B', 'A'], ['ADD', 'A', 1.5],
     ['LOG', 'A'], ['LOG', 'B']])
eval_pyassm(
    [['SET', 'A', 5], ['SET', 'B', 1], ['SET', 'C', 3], ['SET', 'A', 1], ['ADD', 'B', 1], ['LOG', 'A'],
     ['CPY', 'B', 'A'], ['LOG', 'A'], ['LOG', 'B']])
eval_pyassm([['ADD', 'A', 1], ['MUL', 'A', 10], ['ADD', 'B', 1], ['JEQ', 'B', 'A', 100], ['LOG', 'B'],
             ['JEQ', 'B', 'B', -3]])
eval_pyassm([['ADD', 'A', 1], ['MUL', 'A', 10], ['ADD', 'B', 1], ['JEQ', 'B', 'A', 100], ['LOG', 'B'],
             ['JNE', 'P', 'A', -3]])
eval_pyassm([['ADD', 'A', 1], ['MUL', 'A', 10], ['ADD', 'B', 1], ['JEQ', 'B', 'A', 3], ['LOG', 'B'],
             ['JEQ', 'B', 'B', -3]])
eval_pyassm(
    [['ADD', 'A', 1], ['MUL', 'A', 10], ['ADD', 'B', 1], ['JEQ', 'B', 'A', 1], ['JEQ', 'B', 'A', 3], ['LOG', 'B'],
     ['JEQ', 'B', 'B', -4]])
eval_pyassm(
    [['ADD', 'A', 1], ['MUL', 'A', 10], ['ADD', 'B', 1], ['JNE', 'B', 'A', 2], ['JEQ', 'X', 'X', 100], ['LOG', 'B'],
     ['JEQ', 'B', 'B', -4]])
eval_pyassm(
    [['ADD', 'A', 1], ['MUL', 'A', 10], ['ADD', 'B', 1], ['JNE', 'B', 'A', 2], ['JEQ', 'X', 'X', 3], ['LOG', 'B'],
     ['JEQ', 'B', 'B', -4]])
eval_pyassm([['ADD', 'A', 1], ['ADD', 'A', 9], ['ADD', 'B', 1], ['JEQ', 'B', 'A', 100], ['LOG', 'B'],
             ['JEQ', 'B', 'B', -3]])
eval_pyassm(
    [['ADD', 'A', 2], ['MUL', 'A', 2], ['ADD', 'B', 4], ['JEQ', 'B', 'A', 15], ['LOG', 'B']])
eval_pyassm(
    [['ADD', 'A', 2], ['MUL', 'A', 2], ['ADD', 'B', 4], ['JNE', 'B', 'A', 15], ['LOG', 'B']])
eval_pyassm(
    [['SET', 'A', -5], ['SET', 'B', -5], ['SET', 'C', 0], ['JEQ', 'A', 'B', 8], ['MUL', 'A', 5], ['MUL', 'B', 5],
     ['MUL', 'C', 5], ['ADD', 'A', 1.5], ['ADD', 'A', 1.5], ['ADD', 'A', 1.5], ['LOG', 'A'], ['LOG', 'B'],
     ['LOG', 'C']])
eval_pyassm(
    [['ADD', 'A', 1], ['JSR', 5], ['NOP'], ['NOP'], ['JEQ', 'B', 'B', 10000], ['LOG', 'A'], ['RET']])
eval_pyassm(
    [['ADD', 'A', 1], ['NOP'], ['JSR', 5], ['NOP'], ['JEQ', 'B', 'B', 10000], ['LOG', 'A'], ['RET']])
eval_pyassm(
    [['ADD', 'A', 1], ['NOP'], ['JSR', 5], ['JSR', 5], ['JEQ', 'B', 'B', 10000], ['LOG', 'A'], ['LOG', 'B'],
     ['RET']])
eval_pyassm(
    [['ADD', 'A', 1], ['NOP'], ['JSR', 5], ['JSR', 5], ['JEQ', 'B', 'B', 10000], ['LOG', 'A'], ['LOG', 'B'],
     ['RET']])
eval_pyassm(
    [['ADD', 'A', 1], ['JSR', 5], ['LOG', 'D'], ['NOP'], ['JEQ', 'B', 'B', 10000], ['LOG', 'A'], ['JSR', 10],
     ['LOG', 'C'], ['RET'], ['NOP'], ['LOG', 'B'], ['RET']])
eval_pyassm(
    [['ADD', 'A', 1], ['JSR', 5], ['JSR', 5], ['LOG', 'D'], ['JEQ', 'B', 'B', 10000], ['LOG', 'A'], ['JSR', 10],
     ['LOG', 'C'], ['RET'], ['NOP'], ['LOG', 'B'], ['RET']])
eval_pyassm(
    [['ADD', 'A', 1], ['JSR', 5], ['JSR', 5], ['LOG', 'D'], ['JEQ', 'B', 'B', 10000], ['LOG', 'A'], ['JSR', 10],
     ['LOG', 'C'], ['RET'], ['NOP'], ['LOG', 'B'], ['JSR', 13], ['RET'], ['LOG', 'P'], ['RET']])

# ======================================================================
# Uppgift 3:  Testfall
# ======================================================================

assert treeval([10]) == 10
assert treeval(['*', [10]]) == 10
assert treeval(['*', ['*', [10], [20]], [15], [10, [11]]]) == 63000
assert treeval([555, ['*', [10], [20]], [15], [10, [11]]]) == 791
assert treeval([0, [15], [10, [11]]]) == 36
assert treeval([0, [10, [11]]]) == 21
assert treeval([10, [11]]) == 21
assert treeval([10, [-11]]) == -1
assert treeval([-1, [-12.5]]) == -13.5
assert treeval([15, [16], [17]]) == 48
assert treeval(['*', [0], [10, [15]]]) == 0
assert treeval(['*', [10, [15]], [0]]) == 0
assert treeval(['*', [10, [15]], [1, [-1]]]) == 0
assert treeval(['*', [0], [0], [0], [0], [0], [0], [0], [0]]) == 0
assert treeval([10, [15, ['*', [10], [5]]]]) == 75
assert treeval([0, [0, [0, [0, [0]]]]]) == 0
assert treeval([0, [0], [0], [0], [0], [0], [0], [0], [0]]) == 0
assert treeval([0, [0, [0], [0]], [0, [0], [0]]]) == 0
assert treeval([0, [0, [0, [0], [0], [0]]], [0], [0]]) == 0
assert treeval([1, [1], [1]]) == 3
assert treeval([1, [1], [1], [1], [1], [1], [1], [1], [1], [1]]) == 10
assert treeval([1, [2]]) == 3
assert treeval([1, [2], [3]]) == 6
assert treeval([1, [2], [3], [4]]) == 10
assert treeval([1, [2], [3], [4], [5]]) == 15
assert treeval([1, [2], [3], [4], [5], [6]]) == 21
assert treeval([1, [2], [3], [4], [5], [6], [7]]) == 28
assert treeval([1, [2], [3], [4], [5], [6], [7], [8]]) == 36
assert treeval([1, [2], [3], [4], [5], [6], [7], [8], [9]]) == 45
assert treeval([1, [2], [3], [4], [5], [6], [7], [8], [9], [10]]) == 55
assert treeval([1, [1, [1]], [1, [5]], [1], [1], [1], [1], [1], [1], [1, [2]]]) == 18
assert treeval(['*', [2], [2], [2], [2], [2], [2], [2], [2], [2]]) == 512
assert treeval(['*', [2], [2], [2], [2], [-2], [2], [2], [2], [2]]) == -512
assert treeval(['*', [2], [2], [2], [2], [-2], [-2], [2], [2], [2]]) == 512
assert treeval(['*', [-5]]) == -5
assert treeval(['*', [2, [2]], [2, [2]], [2, [4]]]) == 96
assert treeval(['*', [2, [3]], [2, [2]], [2, [4]]]) == 120
assert treeval(['*', [2, [2]], [2, [2]], [2, [4]], [2, [4]]]) == 576
assert treeval(['*', [2, [2]], [2, [2]], [2, [4]], [2, [4]], [5]]) == 2880
assert treeval([0, ['*', [2, [2]], [2, [2]], [2, [4]], [2, [4]], [5]], [2.5, [0.5], [1.5], [4.0]]]) == 2888.5
assert treeval(['*', [2], [3.5]]) == 7.0
assert treeval(['*', [0.3333333333333333], [0.3333333333333333], [3.0], [3.0]]) == 1.0
assert treeval(['*', ['*', [0.3333333333333333], [0.3333333333333333]], [1.5]]) == 0.16666666666666666
assert treeval([0.4, [0.6]]) == 1.0
assert treeval([2.5, [0.5], [1.5], [4.0]]) == 8.5
assert treeval([3.6, [0.4, [0.6, [0.4]]]]) == 5.0
assert treeval([0.4, ['*', [0.3], [2]]]) == 1.0
assert treeval(['*', [0.3], [2]]) == 0.6
assert treeval(['*', [0.3], [1.5]]) == 0.44999999999999996
assert treeval(['*', [0.3, [0.3], [0.2]], [1, [1]]]) == 1.6
assert treeval([10, ['*', [0.3, [0.3], [5]], [1, [1]]]]) == 21.2
assert treeval([10, ['*', [0.3, [2, [2]], [0.3], [5]], [1, [1]]]]) == 29.2
assert treeval(['*', [3, [5, [7]]], [11]]) == 165
assert treeval([10, ['*', [5, [6]], [7, [8]]], [15, [10]]]) == 200
assert treeval([0, [10, ['*', [10], [0]]]]) == 10
assert treeval([123, [1], [2], [3]]) == 129
assert treeval([123, [1], [2], [3], [4]]) == 133
assert treeval([123, [1], [2], [3], [4], [5]]) == 138
assert treeval([123, [1], [2], [3], [4], [5], [6]]) == 144
assert treeval([123, [1], [2], [3], [4], [5], [6], [7]]) == 151
assert treeval([123, [1], [2], [3], [4], [5], [6], [7], [8]]) == 159
assert treeval([12, [123, [1], [2], [3]]]) == 141
assert treeval([12, [123, [1], [2], [3], [4]]]) == 145
assert treeval([12, [123, [1], [2], [3], [4], [5]]]) == 150
assert treeval([12, [123, [1], [2], [3], [4], [5], [6]]]) == 156
assert treeval([12, [123, [1], [2], [3], [4], [5], [6], [7]]]) == 163
assert treeval([12, [123, [1], [2], [3], [4], [5], [6], [7], [8]]]) == 171
assert treeval(['*', [1], [2], [3]]) == 6
assert treeval(['*', [1], [2], [3], [4]]) == 24
assert treeval(['*', [1], [2], [3], [4], [5]]) == 120
assert treeval(['*', [1], [2], [3], [4], [5], [6]]) == 720
assert treeval(['*', [1], [2], [3], [4], [5], [6], [7]]) == 5040
assert treeval(['*', [1], [2], [3], [4], [5], [6], [7], [8]]) == 40320
assert treeval([12, ['*', [1], [2], [3]]]) == 18
assert treeval([12, ['*', [1], [2], [3], [4]]]) == 36
assert treeval([12, ['*', [1], [2], [3], [4], [5]]]) == 132
assert treeval([12, ['*', [1], [2], [3], [4], [5], [6]]]) == 732
assert treeval([12, ['*', [1], [2], [3], [4], [5], [6], [7]]]) == 5052
assert treeval([12, ['*', [1], [2], [3], [4], [5], [6], [7], [8]]]) == 40332
assert treeval(['*', [1], [2], [3], [0]]) == 0
assert treeval(['*', [1], [2], [3], [4], [0]]) == 0
assert treeval(['*', [1], [2], [3], [4], [5], [0]]) == 0
assert treeval(['*', [1], [2], [3], [4], [5], [6], [0]]) == 0
assert treeval(['*', [1], [2], [3], [4], [5], [6], [7], [0]]) == 0
assert treeval(['*', [1], [2], [3], [4], [5], [6], [7], [8], [0]]) == 0
assert treeval([12, ['*', [1], [2], [3], [0]]]) == 12
assert treeval([12, ['*', [1], [2], [3], [4], [0]]]) == 12
assert treeval([12, ['*', [1], [2], [3], [4], [5], [0]]]) == 12
assert treeval([12, ['*', [1], [2], [3], [4], [5], [6], [0]]]) == 12
assert treeval([12, ['*', [1], [2], [3], [4], [5], [6], [7], [0]]]) == 12
assert treeval([12, ['*', [1], [2], [3], [4], [5], [6], [7], [8], [0]]]) == 12
assert treeval2([10]) == 10
assert treeval2(['*', [10]]) == 10
assert treeval2(['*', ['*', [10], [20]], [15], [10, [11]]]) == 63000
assert treeval2([555, ['*', [10], [20]], [15], [10, [11]]]) == 791
assert treeval2([0, [15], [10, [11]]]) == 36
assert treeval2([0, [10, [11]]]) == 21
assert treeval2([10, [11]]) == 21
assert treeval2([10, [-11]]) == -1
assert treeval2([-1, [-12.5]]) == -13.5
assert treeval2([15, [16], [17]]) == 48
assert treeval2(['*', [0], [10, [15]]]) == 0
assert treeval2(['*', [10, [15]], [0]]) == 0
assert treeval2(['*', [10, [15]], [1, [-1]]]) == 0
assert treeval2(['*', [0], [0], [0], [0], [0], [0], [0], [0]]) == 0
assert treeval2([10, [15, ['*', [10], [5]]]]) == 75
assert treeval2([0, [0, [0, [0, [0]]]]]) == 0
assert treeval2([0, [0], [0], [0], [0], [0], [0], [0], [0]]) == 0
assert treeval2([0, [0, [0], [0]], [0, [0], [0]]]) == 0
assert treeval2([0, [0, [0, [0], [0], [0]]], [0], [0]]) == 0
assert treeval2([1, [1], [1]]) == 3
assert treeval2([1, [1], [1], [1], [1], [1], [1], [1], [1], [1]]) == 10
assert treeval2([1, [2]]) == 3
assert treeval2([1, [2], [3]]) == 6
assert treeval2([1, [2], [3], [4]]) == 10
assert treeval2([1, [2], [3], [4], [5]]) == 15
assert treeval2([1, [2], [3], [4], [5], [6]]) == 21
assert treeval2([1, [2], [3], [4], [5], [6], [7]]) == 28
assert treeval2([1, [2], [3], [4], [5], [6], [7], [8]]) == 36
assert treeval2([1, [2], [3], [4], [5], [6], [7], [8], [9]]) == 45
assert treeval2([1, [2], [3], [4], [5], [6], [7], [8], [9], [10]]) == 55
assert treeval2([1, [1, [1]], [1, [5]], [1], [1], [1], [1], [1], [1], [1, [2]]]) == 18
assert treeval2(['*', [2], [2], [2], [2], [2], [2], [2], [2], [2]]) == 512
assert treeval2(['*', [2], [2], [2], [2], [-2], [2], [2], [2], [2]]) == -512
assert treeval2(['*', [2], [2], [2], [2], [-2], [-2], [2], [2], [2]]) == 512
assert treeval2(['*', [-5]]) == -5
assert treeval2(['*', [2, [2]], [2, [2]], [2, [4]]]) == 96
assert treeval2(['*', [2, [3]], [2, [2]], [2, [4]]]) == 120
assert treeval2(['*', [2, [2]], [2, [2]], [2, [4]], [2, [4]]]) == 576
assert treeval2(['*', [2, [2]], [2, [2]], [2, [4]], [2, [4]], [5]]) == 2880
assert treeval2([0, ['*', [2, [2]], [2, [2]], [2, [4]], [2, [4]], [5]], [2.5, [0.5], [1.5], [4.0]]]) == 2888.5
assert treeval2(['*', [2], [3.5]]) == 7.0
assert treeval2(['*', [0.3333333333333333], [0.3333333333333333], [3.0], [3.0]]) == 1.0
assert treeval2(['*', ['*', [0.3333333333333333], [0.3333333333333333]], [1.5]]) == 0.16666666666666666
assert treeval2([0.4, [0.6]]) == 1.0
assert treeval2([2.5, [0.5], [1.5], [4.0]]) == 8.5
assert treeval2([3.6, [0.4, [0.6, [0.4]]]]) == 5.0
assert treeval2([0.4, ['*', [0.3], [2]]]) == 1.0
assert treeval2(['*', [0.3], [2]]) == 0.6
assert treeval2(['*', [0.3], [1.5]]) == 0.44999999999999996
assert treeval2(['*', [0.3, [0.3], [0.2]], [1, [1]]]) == 1.6
assert treeval2([10, ['*', [0.3, [0.3], [5]], [1, [1]]]]) == 21.2
assert treeval2([10, ['*', [0.3, [2, [2]], [0.3], [5]], [1, [1]]]]) == 29.2
assert treeval2(['*', [3, [5, [7]]], [11]]) == 165
assert treeval2([10, ['*', [5, [6]], [7, [8]]], [15, [10]]]) == 200
assert treeval2([0, [10, ['*', [10], [0]]]]) == 10
assert treeval2([123, [1], [2], [3]]) == 129
assert treeval2([123, [1], [2], [3], [4]]) == 133
assert treeval2([123, [1], [2], [3], [4], [5]]) == 138
assert treeval2([123, [1], [2], [3], [4], [5], [6]]) == 144
assert treeval2([123, [1], [2], [3], [4], [5], [6], [7]]) == 151
assert treeval2([123, [1], [2], [3], [4], [5], [6], [7], [8]]) == 159
assert treeval2([12, [123, [1], [2], [3]]]) == 141
assert treeval2([12, [123, [1], [2], [3], [4]]]) == 145
assert treeval2([12, [123, [1], [2], [3], [4], [5]]]) == 150
assert treeval2([12, [123, [1], [2], [3], [4], [5], [6]]]) == 156
assert treeval2([12, [123, [1], [2], [3], [4], [5], [6], [7]]]) == 163
assert treeval2([12, [123, [1], [2], [3], [4], [5], [6], [7], [8]]]) == 171
assert treeval2(['*', [1], [2], [3]]) == 6
assert treeval2(['*', [1], [2], [3], [4]]) == 24
assert treeval2(['*', [1], [2], [3], [4], [5]]) == 120
assert treeval2(['*', [1], [2], [3], [4], [5], [6]]) == 720
assert treeval2(['*', [1], [2], [3], [4], [5], [6], [7]]) == 5040
assert treeval2(['*', [1], [2], [3], [4], [5], [6], [7], [8]]) == 40320
assert treeval2([12, ['*', [1], [2], [3]]]) == 18
assert treeval2([12, ['*', [1], [2], [3], [4]]]) == 36
assert treeval2([12, ['*', [1], [2], [3], [4], [5]]]) == 132
assert treeval2([12, ['*', [1], [2], [3], [4], [5], [6]]]) == 732
assert treeval2([12, ['*', [1], [2], [3], [4], [5], [6], [7]]]) == 5052
assert treeval2([12, ['*', [1], [2], [3], [4], [5], [6], [7], [8]]]) == 40332
assert treeval2(['*', [1], [2], [3], [0]]) == 0
assert treeval2(['*', [1], [2], [3], [4], [0]]) == 0
assert treeval2(['*', [1], [2], [3], [4], [5], [0]]) == 0
assert treeval2(['*', [1], [2], [3], [4], [5], [6], [0]]) == 0
assert treeval2(['*', [1], [2], [3], [4], [5], [6], [7], [0]]) == 0
assert treeval2(['*', [1], [2], [3], [4], [5], [6], [7], [8], [0]]) == 0
assert treeval2([12, ['*', [1], [2], [3], [0]]]) == 12
assert treeval2([12, ['*', [1], [2], [3], [4], [0]]]) == 12
assert treeval2([12, ['*', [1], [2], [3], [4], [5], [0]]]) == 12
assert treeval2([12, ['*', [1], [2], [3], [4], [5], [6], [0]]]) == 12
assert treeval2([12, ['*', [1], [2], [3], [4], [5], [6], [7], [0]]]) == 12
assert treeval2([12, ['*', [1], [2], [3], [4], [5], [6], [7], [8], [0]]]) == 12
assert treeval2(['***', [3, [5, [7]]], [11]]) == 1155
assert treeval2([10, ['***', [5, [6]], [7, [8]]], [15, [10]]]) == 1715
assert treeval2(['***', [10, [0], [2]]]) == 0
assert treeval2([50, ['***', [15], [25]], [15]]) == 440
assert treeval2([5, ['***', ['***', [5], [10], [5]]]]) == 255
assert treeval2(['***', ['***', [5], [10], [5]]]) == 250
assert treeval2(['***', [10, ['***', [5], [10], [5]], [2]]]) == 5000
assert treeval2([0, ['***', [10], [1]]]) == 10
assert treeval2([0, [10, ['***', [10], [0]]]]) == 10
assert treeval2([10, ['***', [50, [2], [3]]]]) == 310
assert treeval2([10, ['***', ['*', [2], [5]], [5]]]) == 60
assert treeval2([10, ['*', ['***', [2], [5]], [5]]]) == 60
assert treeval2([1, ['***', [10], [1]]]) == 11
assert treeval2([1, [10, ['***', [10], [1]]]]) == 21
assert treeval2(['***', [10, [1], [2]]]) == 20
assert treeval2([50, ['***', [15], [25]], [0]]) == 425
assert treeval2([5, ['***', ['***', [0], [10], [5]]]]) == 5
assert treeval2(['***', ['***', [0], [10], [0]]]) == 0
assert treeval2(['***', ['***', [0], [10.5, [0]], [0]]]) == 0.0
assert treeval2(['***', ['***', ['***', [5], [10], [5]]]]) == 250
assert treeval2(['***', ['*', ['***', [5], [10], [5]]]]) == 250
assert treeval2(['***', ['*', ['***', [5], [10.5], [5]]]]) == 262.5
assert treeval2(['***', ['*', ['***', [5], [37], [5], [1, [2, [3, [4, [5]]]]]]]]) == 111000
assert treeval2(['***', [1], [2], [3]]) == 6
assert treeval2(['***', [1], [2], [3], [4]]) == 24
assert treeval2(['***', [1], [2], [3], [4], [5]]) == 120
assert treeval2(['***', [1], [2], [3], [4], [5], [6]]) == 720
assert treeval2(['***', [1], [2], [3], [4], [5], [6], [7]]) == 5040
assert treeval2(['***', [1], [2], [3], [4], [5], [6], [7], [8]]) == 40320
assert treeval2([12, ['***', [1], [2], [3]]]) == 18
assert treeval2([12, ['***', [1], [2], [3], [4]]]) == 36
assert treeval2([12, ['***', [1], [2], [3], [4], [5]]]) == 132
assert treeval2([12, ['***', [1], [2], [3], [4], [5], [6]]]) == 732
assert treeval2([12, ['***', [1], [2], [3], [4], [5], [6], [7]]]) == 5052
assert treeval2([12, ['***', [1], [2], [3], [4], [5], [6], [7], [8]]]) == 40332
assert treeval2(['***', [1], [2], [3], [0]]) == 0
assert treeval2(['***', [1], [2], [3], [4], [0]]) == 0
assert treeval2(['***', [1], [2], [3], [4], [5], [0]]) == 0
assert treeval2(['***', [1], [2], [3], [4], [5], [6], [0]]) == 0
assert treeval2(['***', [1], [2], [3], [4], [5], [6], [7], [0]]) == 0
assert treeval2(['***', [1], [2], [3], [4], [5], [6], [7], [8], [0]]) == 0
assert treeval2([12, ['***', [1], [2], [3], [0]]]) == 12
assert treeval2([12, ['***', [1], [2], [3], [4], [0]]]) == 12
assert treeval2([12, ['***', [1], [2], [3], [4], [5], [0]]]) == 12
assert treeval2([12, ['***', [1], [2], [3], [4], [5], [6], [0]]]) == 12
assert treeval2([12, ['***', [1], [2], [3], [4], [5], [6], [7], [0]]]) == 12
assert treeval2([12, ['***', [1], [2], [3], [4], [5], [6], [7], [8], [0]]]) == 12
assert treeval2(['***', [1.5], [2.5], [3.5]]) == 13.125
assert treeval2([50.5, ['***', [15.5], [25]], [15]]) == 453.0
assert treeval2([50.5, ['***', [15], [25]], [15], ['***', [12], [34]]]) == 848.5
assert treeval2([1, [10, ['***', [10], [1]]], ['***', [17], [2]], [10, [23, ['***', [22], [7]], [5]]]]) == 247
assert treeval2(['***', [1], [2.5], [3], [4]]) == 30.0
assert treeval2(['***', [1], [2], [3.5], [4], [5]]) == 140.0
assert treeval2(['***', [12], ['***', [12], ['***', [5], [10], [5]]]]) == 36000
assert treeval2(['***', [12], ['*', ['***', [5], [10], [5]]]]) == 3000
assert treeval2(['***', [12], ['*', ['***', [5], [10.5], [5]]]]) == 3150.0
assert treeval2(['***', [12], ['*', ['***', [5], [37], [5], [1, [2, [3, [4, [5]]]]]]]]) == 1332000


# ======================================================================
# Uppgift 4:  Testfall
# ======================================================================

def is_even_int(x):
    return isinstance(x, int) and x % 2 == 0


def is_odd_int(x):
    return isinstance(x, int) and x % 2 == 1


def is_int_divisible_by_3(x):
    return isinstance(x, int) and x % 3 == 0


def is_int_above_8(x):
    return isinstance(x, int) and x > 8


def is_any(x):
    return True


def always_false(x):
    return False


def is_true_as_bool(x):
    return bool(x)


def is_int(x):
    return isinstance(x, int)


def is_none(x):
    return x is None


def is_not_none(x):
    return x is not None


def is_dict(x):
    return isinstance(x, dict)


assert (traverse2([[1, 2, 3], [4, 5, 6], [7, 8]])
        == [1, 2, 3, 6, 5, 4, 7, 8])
assert (traverse2([[1, 2, None], [3, None, 'a'], [12, 34]])
        == [1, 2, 'a', 3, 12, 34])
assert (traverse2([[3, None, 'a'], [1, 2, None], [12, 34]])
        == [3, 'a', 2, 1, 12, 34])
assert (traverse2([[1]])
        == [1])
assert (traverse2([[1.0]])
        == [1.0])
assert (traverse2([['a']])
        == ['a'])
assert (traverse2([[None]])
        == [])
assert (traverse2([[()]])
        == [()])
assert (traverse2([[{}]])
        == [{}])
assert (traverse2([[set()]])
        == [set()])
assert (traverse2([[(2, 3, 4)]])
        == [(2, 3, 4)])
assert (traverse2([[{'test': 1, 'test2': 2}]])
        == [{'test': 1, 'test2': 2}])
assert (traverse2([[1, 1.0, 'a', None], [1, 1.0, 'a', None], [1, 1.0, 'a', None], [1, 1.0, 'a', None]])
        == [1, 1.0, 'a', 'a', 1.0, 1, 1, 1.0, 'a', 'a', 1.0, 1])
assert (traverse2(
    [[1, 1.0, 'a', None], [1, 1.0, 'a', None], [1, 1.0, 'a', None], [1, 1.0, 'a', None], [1, 1.0, 'a', None]])
        == [1, 1.0, 'a', 'a', 1.0, 1, 1, 1.0, 'a', 'a', 1.0, 1, 1, 1.0, 'a'])
assert (traverse2([[1.0, 1, 'b', 'c'], [1.0, 1, 'b', 'c'], [1.0, 1, 'b', 'c'], [1.0, 1, 'b', 'c'], [1.0, 1, 'b', 'c']])
        == [1.0, 1, 'b', 'c', 'c', 'b', 1, 1.0, 1.0, 1, 'b', 'c', 'c', 'b', 1, 1.0, 1.0, 1, 'b', 'c'])
assert (traverse2([[1, 1, 1], [1, 1, 1, 1, 1, 1.5, 1.5, 1.5]])
        == [1, 1, 1, 1.5, 1.5, 1.5, 1, 1, 1, 1, 1])
assert (traverse2([[1, 1, 1, 1, 1], [2, 2, 2, 1, 1, 1]])
        == [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2])
assert (traverse2([[1, 2, 3], [1, 'a', 'c', 'd'], [1.0, 72, math.inf]])
        == [1, 2, 3, 'd', 'c', 'a', 1, 1.0, 72, math.inf])
assert (traverse2([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        == [1, 2, 3, 6, 5, 4, 7, 8, 9])
assert (traverse2([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
        == [1, 2, 3, 6, 5, 4, 7, 8, 9, 12, 11, 10])
assert (traverse2([[1, 2, 3, 'a'], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
        == [1, 2, 3, 'a', 6, 5, 4, 7, 8, 9, 12, 11, 10])
assert (traverse2([[1, 2, 3], [4, 5, 6], [7, 8, 9, 9.5], [10, 11, 12]])
        == [1, 2, 3, 6, 5, 4, 7, 8, 9, 9.5, 12, 11, 10])
assert (traverse2([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]])
        == [1, 2, 3, 6, 5, 4, 7, 8, 9, 12, 11, 10, 13, 14, 15, 16])
assert (traverse2([[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]])
        == [6, 5, 4, 7, 8, 9, 12, 11, 10, 13, 14, 15, 16])
assert (traverse2([[], [], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]])
        == [7, 8, 9, 12, 11, 10, 13, 14, 15, 16])
assert (traverse2([[], [], [7, 8, 9], [], [13, 14, 15, 16]])
        == [7, 8, 9, 13, 14, 15, 16])
assert (traverse2([[1, 2, 3, 4], [5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])
        == [1, 2, 3, 4, 6, 5, 7, 8, 9, 12, 11, 10, 13, 14, 15])
assert (traverse2([[0, 2, 3], [4, 5, 0], [7, 8, 9]])
        == [0, 2, 3, 0, 5, 4, 7, 8, 9])
assert (traverse2([[0, 2, 3], [4, 5, 0], [7, 8, 9], [10, 11, 12]])
        == [0, 2, 3, 0, 5, 4, 7, 8, 9, 12, 11, 10])
assert (traverse2([[0, 2, 3, 'a'], [4, 5, 0], [7, 8, 9], [10, 11, 12]])
        == [0, 2, 3, 'a', 0, 5, 4, 7, 8, 9, 12, 11, 10])
assert (traverse2([[0, 2, 3], [4, 5, 0], [7, 8, 9, 9.5], [10, 11, 12]])
        == [0, 2, 3, 0, 5, 4, 7, 8, 9, 9.5, 12, 11, 10])
assert (traverse2([[0, 2, 3], [4, 5, None], [7, 8, 9, 9.5], [10, 11, 12]])
        == [0, 2, 3, 5, 4, 7, 8, 9, 9.5, 12, 11, 10])
assert (traverse2([[0, 2, 3], [4, None, 0], [7, 8, None, 9.5], [10, 11, None]])
        == [0, 2, 3, 0, 4, 7, 8, 9.5, 11, 10])
assert (traverse2([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 1.5], [1, 1.5], [1, 1.5]])
        == [1, 2, 3, 3, 2, 1, 1, 2, 3, 1.5, 1, 1, 1.5, 1.5, 1])
assert (traverse2([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2], [1, 2], [1, 2]])
        == [1, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 1, 1, 2, 2, 1, 1, 2])
assert (traverse2([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]])
        == [1, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 1, 1, 2, 3])
assert (traverse2([[1, 2, 3], [1, 2, 3], [1, 2, 3], [4, 5, 6], [4, 5, 6], [4, 5, 6]])
        == [1, 2, 3, 3, 2, 1, 1, 2, 3, 6, 5, 4, 4, 5, 6, 6, 5, 4])
assert (traverse2([[1, 2, 3], [1, 2, 3], [1, 2, 3], [4, 5, 6], [4, 5, 6], [4, 5, 6], [7, 8]])
        == [1, 2, 3, 3, 2, 1, 1, 2, 3, 6, 5, 4, 4, 5, 6, 6, 5, 4, 7, 8])
assert (traverse2p([[1, 2, None], [3, None, 'a'], [12, 34]], is_even_int)
        == [2, 12, 34])
assert (traverse2p([[1]], is_any)
        == [1])
assert (traverse2p([[1]], always_false)
        == [])
assert (traverse2p([[1.0]], is_any)
        == [1.0])
assert (traverse2p([[1.0]], always_false)
        == [])
assert (traverse2p([['a']], is_any)
        == ['a'])
assert (traverse2p([['a']], always_false)
        == [])
assert (traverse2p([[None]], is_any)
        == [None])
assert (traverse2p([[None]], always_false)
        == [])
assert (traverse2p([[1, 2, 3]], is_any)
        == [1, 2, 3])
assert (traverse2p([[1, 2, 3]], always_false)
        == [])
assert (traverse2p([[0, 2, 3]], is_true_as_bool)
        == [2, 3])
assert (traverse2p([[1, 2, 'a', None, 'q'], [2, 7, 5]], is_int)
        == [1, 2, 5, 7, 2])
assert (traverse2p([[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]], is_not_none)
        == [1, 2, 'a', 'q', 'test', 'a', 2.0, 'tset', 7, 8989])
assert (traverse2p([[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]], is_none)
        == [None])
assert (traverse2p([[0, 2, 3], [4, 5, None], [7, 8, 9, 9.5], [10, 11, 12]], is_none)
        == [None])
assert (traverse2p([[0, 2, 3], [4, None, 0], [7, 8, None, 9.5], [10, 11, None]], is_none)
        == [None, None, None])
assert (traverse2p([[1, 2, 3], [4, 5, 6], [7, 8, 9]], is_even_int)
        == [2, 6, 4, 8])
assert (traverse2p([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], is_even_int)
        == [2, 6, 4, 8, 12, 10])
assert (traverse2p([[1, 2, 3, 'a'], [4, 5, 6], [7, 8, 9], [10, 11, 12]], is_even_int)
        == [2, 6, 4, 8, 12, 10])
assert (traverse2p([[1, 2, 3], [4, 5, 6], [7, 8, 9, 9.5], [10, 11, 12]], is_even_int)
        == [2, 6, 4, 8, 12, 10])
assert (traverse2p([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]], is_even_int)
        == [2, 6, 4, 8, 12, 10, 14, 16])
assert (traverse2p([[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]], is_even_int)
        == [6, 4, 8, 12, 10, 14, 16])
assert (traverse2p([[], [], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]], is_even_int)
        == [8, 12, 10, 14, 16])
assert (traverse2p([[], [], [7, 8, 9], [], [13, 14, 15, 16]], is_even_int)
        == [8, 14, 16])
assert (traverse2p([[1, 2, 3, 4], [5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]], is_even_int)
        == [2, 4, 6, 8, 12, 10, 14])
assert (traverse2p(
    [[5, 6, 20, 21, 22, 23, 24, 25], [7, 8, 9, 15, 20, 88], [10, 11, 12, 29, 27, 12, 0], [13, 14, 15, 10, 32, 1]],
    is_even_int)
        == [6, 20, 22, 24, 88, 20, 8, 10, 12, 12, 0, 32, 10, 14])
assert (traverse2p([[1, 2, 3, 4], [5, 6, 20, 21, 22, 23, 24, 25], [7, 8, 9], [10, 11, 12], [13, 14, 15]], is_even_int)
        == [2, 4, 24, 22, 20, 6, 8, 12, 10, 14])
assert (traverse2p([[0, 2, 3], [4, 5, 0], [7, 8, 9]], is_even_int)
        == [0, 2, 0, 4, 8])
assert (traverse2p([[0, 2, 3], [4, 5, 0], [7, 8, 9], [10, 11, 12]], is_even_int)
        == [0, 2, 0, 4, 8, 12, 10])
assert (traverse2p([[0, 2, 3, 'a'], [4, 5, 0], [7, 8, 9], [10, 11, 12]], is_even_int)
        == [0, 2, 0, 4, 8, 12, 10])
assert (traverse2p([[0, 2, 3], [4, 5, 0], [7, 8, 9, 9.5], [10, 11, 12]], is_even_int)
        == [0, 2, 0, 4, 8, 12, 10])
assert (traverse2p([[0, 2, 3], [4, 5, None], [7, 8, 9, 9.5], [10, 11, 12]], is_even_int)
        == [0, 2, 4, 8, 12, 10])
assert (traverse2p([[0, 2, 3], [4, None, 0], [7, 8, None, 9.5], [10, 11, None]], is_even_int)
        == [0, 2, 0, 4, 8, 10])
assert (traverse2p([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 1.5], [1, 1.5], [1, 1.5]], is_even_int)
        == [2, 2, 2])
assert (traverse2p([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2], [1, 2], [1, 2]], is_even_int)
        == [2, 2, 2, 2, 2, 2, 2])
assert (traverse2p([[1, 2, 3], [4, 5, 6], [7, 8, 9]], is_int_above_8)
        == [9])
assert (traverse2p([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], is_int_above_8)
        == [9, 12, 11, 10])
assert (traverse2p([[1, 2, 3, 'a'], [4, 5, 6], [7, 8, 9], [10, 11, 12]], is_int_above_8)
        == [9, 12, 11, 10])
assert (traverse2p([[1, 2, 3], [4, 5, 6], [7, 8, 9, 9.5], [10, 11, 12]], is_int_above_8)
        == [9, 12, 11, 10])
assert (traverse2p([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]], is_int_above_8)
        == [9, 12, 11, 10, 13, 14, 15, 16])
assert (traverse2p([[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]], is_int_above_8)
        == [9, 12, 11, 10, 13, 14, 15, 16])
assert (traverse2p([[], [], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]], is_int_above_8)
        == [9, 12, 11, 10, 13, 14, 15, 16])
assert (traverse2p([[], [], [7, 8, 9], [], [13, 14, 15, 16]], is_int_above_8)
        == [9, 13, 14, 15, 16])
assert (traverse2p([[1, 2, 3, 4], [5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]], is_int_above_8)
        == [9, 12, 11, 10, 13, 14, 15])
assert (traverse2p(
    [[5, 6, 20, 21, 22, 23, 24, 25], [7, 8, 9, 15, 20, 88], [10, 11, 12, 29, 27, 12, 0], [13, 14, 15, 10, 32, 1]],
    is_int_above_8)
        == [20, 21, 22, 23, 24, 25, 88, 20, 15, 9, 10, 11, 12, 29, 27, 12, 32, 10, 15, 14, 13])
assert (traverse2p([[1, 2, 3, 4], [5, 6, 20, 21, 22, 23, 24, 25], [7, 8, 9], [10, 11, 12], [13, 14, 15]],
                   is_int_above_8)
        == [25, 24, 23, 22, 21, 20, 9, 12, 11, 10, 13, 14, 15])
assert (traverse2p([[0, 2, 3], [4, 5, 0], [7, 8, 9]], is_int_above_8)
        == [9])
assert (traverse2p([[0, 2, 3], [4, 5, 0], [7, 8, 9], [10, 11, 12]], is_int_above_8)
        == [9, 12, 11, 10])
assert (traverse2p([[0, 2, 3, 'a'], [4, 5, 0], [7, 8, 9], [10, 11, 12]], is_int_above_8)
        == [9, 12, 11, 10])
assert (traverse2p([[0, 2, 3], [4, 5, 0], [7, 8, 9, 9.5], [10, 11, 12]], is_int_above_8)
        == [9, 12, 11, 10])
assert (traverse2p([[0, 2, 3], [4, 5, None], [7, 8, 9, 9.5], [10, 11, 12]], is_int_above_8)
        == [9, 12, 11, 10])
assert (traverse2p([[0, 2, 3], [4, None, 0], [7, 8, None, 9.5], [10, 11, None]], is_int_above_8)
        == [11, 10])
assert (traverse2p([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 1.5], [1, 1.5], [1, 1.5]], is_int_above_8)
        == [])
assert (traverse2p([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2], [1, 2], [1, 2]], is_int_above_8)
        == [])
assert (traverse2p([[1, 2, 3], [4, 5, 6], [7, 8, 9]], is_int_divisible_by_3)
        == [3, 6, 9])
assert (traverse2p([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], is_int_divisible_by_3)
        == [3, 6, 9, 12])
assert (traverse2p([[1, 2, 3, 'a'], [4, 5, 6], [7, 8, 9], [10, 11, 12]], is_int_divisible_by_3)
        == [3, 6, 9, 12])
assert (traverse2p([[1, 2, 3], [4, 5, 6], [7, 8, 9, 9.5], [10, 11, 12]], is_int_divisible_by_3)
        == [3, 6, 9, 12])
assert (traverse2p([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]], is_int_divisible_by_3)
        == [3, 6, 9, 12, 15])
assert (traverse2p([[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]], is_int_divisible_by_3)
        == [6, 9, 12, 15])
assert (traverse2p([[], [], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]], is_int_divisible_by_3)
        == [9, 12, 15])
assert (traverse2p([[], [], [7, 8, 9], [], [13, 14, 15, 16]], is_int_divisible_by_3)
        == [9, 15])
assert (traverse2p([[1, 2, 3, 4], [5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]], is_int_divisible_by_3)
        == [3, 6, 9, 12, 15])
assert (traverse2p(
    [[5, 6, 20, 21, 22, 23, 24, 25], [7, 8, 9, 15, 20, 88], [10, 11, 12, 29, 27, 12, 0], [13, 14, 15, 10, 32, 1]],
    is_int_divisible_by_3)
        == [6, 21, 24, 15, 9, 12, 27, 12, 0, 15])
assert (traverse2p([[1, 2, 3, 4], [5, 6, 20, 21, 22, 23, 24, 25], [7, 8, 9], [10, 11, 12], [13, 14, 15]],
                   is_int_divisible_by_3)
        == [3, 24, 21, 6, 9, 12, 15])
assert (traverse2p([[0, 2, 3], [4, 5, 0], [7, 8, 9]], is_int_divisible_by_3)
        == [0, 3, 0, 9])
assert (traverse2p([[0, 2, 3], [4, 5, 0], [7, 8, 9], [10, 11, 12]], is_int_divisible_by_3)
        == [0, 3, 0, 9, 12])
assert (traverse2p([[0, 2, 3, 'a'], [4, 5, 0], [7, 8, 9], [10, 11, 12]], is_int_divisible_by_3)
        == [0, 3, 0, 9, 12])
assert (traverse2p([[0, 2, 3], [4, 5, 0], [7, 8, 9, 9.5], [10, 11, 12]], is_int_divisible_by_3)
        == [0, 3, 0, 9, 12])
assert (traverse2p([[0, 2, 3], [4, 5, None], [7, 8, 9, 9.5], [10, 11, 12]], is_int_divisible_by_3)
        == [0, 3, 9, 12])
assert (traverse2p([[0, 2, 3], [4, None, 0], [7, 8, None, 9.5], [10, 11, None]], is_int_divisible_by_3)
        == [0, 3, 0])
assert (traverse2p([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 1.5], [1, 1.5], [1, 1.5]], is_int_divisible_by_3)
        == [3, 3, 3])
assert (traverse2p([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2], [1, 2], [1, 2]], is_int_divisible_by_3)
        == [3, 3, 3, 3])
assert (traverse2p([[()]], is_even_int)
        == [])
assert (traverse2p([[{}]], is_even_int)
        == [])
assert (traverse2p([[set()]], is_even_int)
        == [])
assert (traverse2p([[()]], is_any)
        == [()])
assert (traverse2p([[{}]], is_any)
        == [{}])
assert (traverse2p([[set()]], is_any)
        == [set()])
assert (traverseNp([1, 2, 3], is_any)
        == [1, 2, 3])
assert (traverseNp([[1, 2, 3]], is_any)
        == [3, 2, 1])
assert (traverseNp([[[1, 2, 3]]], is_any)
        == [1, 2, 3])
assert (traverseNp([[1, 2, 3], [[3, 4], [5, 6], [7, 8]]], is_any)
        == [3, 2, 1, 7, 8, 5, 6, 3, 4])
assert (traverseNp([[1, 2, 3], [4, 5, 6], [[7, 8], [9, 10], [11, 12]]], is_any)
        == [3, 2, 1, 6, 5, 4, 11, 12, 9, 10, 7, 8])
assert (traverseNp([[1, 2, 3, 4], [4, 5, 6], [[7, 8], [9, 10], [11, 12]]], is_any)
        == [4, 3, 2, 1, 6, 5, 4, 11, 12, 9, 10, 7, 8])
assert (traverseNp([[None]], is_any)
        == [None])
assert (traverseNp([1, 2, 3], is_dict)
        == [])
assert (traverseNp([[1, 2], [[3, 4]], [[[5, 6]]], [[[[7, 8]]]], [[[[[9, 10]]]]], [[[[[[11, 12]]]]]]], is_any)
        == [2, 1, 3, 4, 6, 5, 7, 8, 10, 9, 11, 12])
assert (traverseNp([[[[[[[[[[[[[[[[[[[[20]]]]]]]]]]]]]]]]]]]], is_any)
        == [20])
assert (traverseNp([[[[[[[[[[[[[[[[[[[[[[[[[[[[[[30, 1]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], is_any)
        == [1, 30])
assert (traverseNp([[0, 1, 2, 3], [4, None, 0], [7, 8, None, 9.5], [10, 11, None]], is_any)
        == [3, 2, 1, 0, 0, None, 4, 9.5, None, 8, 7, None, 11, 10])
assert (traverseNp([[0, 1, 2, 3], [4, None, 0], [7, 8, None, 9.5], [10, 11, None]], is_any)
        == [3, 2, 1, 0, 0, None, 4, 9.5, None, 8, 7, None, 11, 10])
assert (traverseNp([], is_any)
        == [])
assert (traverseNp([[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]], is_none)
        == [None])
assert (traverseNp([[0, 2, 3], [4, 5, None], [7, 8, 9, 9.5], [10, 11, 12]], is_none)
        == [None])
assert (traverseNp([[0, 2, 3], [4, None, 0], [7, 8, None, 9.5], [10, 11, None]], is_none)
        == [None, None, None])
assert (traverseNp([1, 2], is_even_int)
        == [2])
assert (traverseNp([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], is_even_int)
        == [2, 4, 6, 8, 10])
assert (traverseNp([1, 2, 'hello', 'goodbye'], is_even_int)
        == [2])
assert (traverseNp([(1, 2), (3, 4), (5, 6)], is_even_int)
        == [])
assert (traverseNp([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]],
                    [[0, 2, 3], [4, 5, 0], [7, 8, 9]]], is_even_int)
        == [8, 4, 6, 2, 14, 16, 10, 12, 8, 4, 6, 8, 4, 0, 0, 2])
assert (traverseNp([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]],
                    [[0, 2, 3], [4, 5, 0], [7, 8, 9]],
                    [[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]]], is_even_int)
        == [8, 4, 6, 2, 14, 16, 10, 12, 8, 4, 6, 8, 4, 0, 0, 2, 2])
assert (traverseNp([[[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]],
                     [[0, 2, 3], [4, 5, 0], [7, 8, 9]]],
                    [[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]]], is_even_int)
        == [2, 0, 0, 4, 8, 6, 4, 8, 12, 10, 16, 14, 2, 6, 4, 8, 2])
assert (traverseNp([[[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]],
                    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]],
                     [[0, 2, 3], [4, 5, 0], [7, 8, 9]]],
                    [[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]]], is_even_int)
        == [2, 2, 0, 0, 4, 8, 6, 4, 8, 12, 10, 16, 14, 2, 6, 4, 8, 2])
assert (traverseNp([[[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]],
                    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                     [[[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]], [[0, 2, 3], [4, 5, 0], [7, 8, 9]]]],
                    [[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]]], is_even_int)
        == [2, 14, 16, 10, 12, 8, 4, 6, 8, 4, 0, 0, 2, 2, 6, 4, 8, 2])
assert (traverseNp([[[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]],
                    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                     [[[[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]], [[0, 2, 3], [4, 5, 0], [7, 8, 9]]]]],
                    [[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]]], is_even_int)
        == [2, 2, 0, 0, 4, 8, 6, 4, 8, 12, 10, 16, 14, 2, 6, 4, 8, 2])
assert (traverseNp([[1, 2, 3], [4, 5, 6], [7, 8, 9]], is_even_int)
        == [2, 6, 4, 8])
assert (traverseNp([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], is_even_int)
        == [2, 6, 4, 8, 12, 10])
assert (traverseNp([[1, 2, 3, 'a'], [4, 5, 6], [7, 8, 9], [10, 11, 12]], is_even_int)
        == [2, 6, 4, 8, 12, 10])
assert (traverseNp([[1, 2, 3], [4, 5, 6, 12], [[7], [8], [9]], [10, 11, 12]], is_even_int)
        == [2, 12, 6, 4, 8, 12, 10])
assert (traverseNp([[1, 2, 3], [4, 5, 6], [7, 8, 9, 9.5], [10, 11, 12]], is_even_int)
        == [2, 6, 4, 8, 12, 10])
assert (traverseNp([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]], is_even_int)
        == [2, 6, 4, 8, 12, 10, 16, 14])
assert (traverseNp([[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]], is_even_int)
        == [6, 4, 8, 12, 10, 16, 14])
assert (traverseNp([[], [], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]], is_even_int)
        == [8, 12, 10, 16, 14])
assert (traverseNp([[], [], [7, 8, 9], [], [13, 14, 15, 16]], is_even_int)
        == [8, 16, 14])
assert (traverseNp([[1, 2, 3, 4], [5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]], is_even_int)
        == [4, 2, 6, 8, 12, 10, 14])
assert (traverseNp([[0, 2, 3], [4, 5, 0], [7, 8, 9]], is_even_int)
        == [2, 0, 0, 4, 8])
assert (traverseNp([[0, 2, 3], [4, 5, 0], [7, 8, 9], [10, 11, 12]], is_even_int)
        == [2, 0, 0, 4, 8, 12, 10])
assert (traverseNp([[0, 2, 3, 'a'], [4, 5, 0], [7, 8, 9], [10, 11, 12]], is_even_int)
        == [2, 0, 0, 4, 8, 12, 10])
assert (traverseNp([[0, 2, 3], [4, 5, 0, 12], [[7], [8], [9]], [10, 11, 12]], is_even_int)
        == [2, 0, 12, 0, 4, 8, 12, 10])
assert (traverseNp([[0, 2, 3], [4, 5, 0], [7, 8, 9, 9.5], [10, 11, 12]], is_even_int)
        == [2, 0, 0, 4, 8, 12, 10])
assert (traverseNp([[0, 2, 3], [4, 5, None], [7, 8, 9, 9.5], [10, 11, 12]], is_even_int)
        == [2, 0, 4, 8, 12, 10])
assert (traverseNp([[0, 2, 3], [4, None, 0], [7, 8, None, 9.5], [10, 11, None]], is_even_int)
        == [2, 0, 0, 4, 8, 10])
assert (traverseNp([[0, 2, 3, (1, 4, 8)], [4, 5, 0], [7, 8, 9], [10, 11, 12]], is_even_int)
        == [2, 0, 0, 4, 8, 12, 10])
assert (traverseNp([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 1.5], [1, 1.5], [1, 1.5]], is_even_int)
        == [2, 2, 2])
assert (traverseNp([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2], [1, 2], [1, 2]], is_even_int)
        == [2, 2, 2, 2, 2, 2, 2])
assert (traverseNp([1, 2], is_int_above_8)
        == [])
assert (traverseNp([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], is_int_above_8)
        == [9, 10])
assert (traverseNp([1, 2, 'hello', 'goodbye'], is_int_above_8)
        == [])
assert (traverseNp([(1, 2), (3, 4), (5, 6)], is_int_above_8)
        == [])
assert (traverseNp([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]],
                    [[0, 2, 3], [4, 5, 0], [7, 8, 9]]], is_int_above_8)
        == [9, 13, 14, 15, 16, 10, 11, 12, 9, 9])
assert (traverseNp([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]],
                    [[0, 2, 3], [4, 5, 0], [7, 8, 9]],
                    [[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]]], is_int_above_8)
        == [9, 13, 14, 15, 16, 10, 11, 12, 9, 9, 8989])
assert (traverseNp([[[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]],
                     [[0, 2, 3], [4, 5, 0], [7, 8, 9]]],
                    [[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]]], is_int_above_8)
        == [9, 9, 12, 11, 10, 16, 15, 14, 13, 9, 8989])
assert (traverseNp([[[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]],
                    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]],
                     [[0, 2, 3], [4, 5, 0], [7, 8, 9]]],
                    [[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]]], is_int_above_8)
        == [8989, 9, 9, 12, 11, 10, 16, 15, 14, 13, 9, 8989])
assert (traverseNp([[[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]],
                    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                     [[[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]], [[0, 2, 3], [4, 5, 0], [7, 8, 9]]]],
                    [[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]]], is_int_above_8)
        == [8989, 13, 14, 15, 16, 10, 11, 12, 9, 9, 9, 8989])
assert (traverseNp([[[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]],
                    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                     [[[[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]], [[0, 2, 3], [4, 5, 0], [7, 8, 9]]]]],
                    [[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]]], is_int_above_8)
        == [8989, 9, 9, 12, 11, 10, 16, 15, 14, 13, 9, 8989])
assert (traverseNp([[1, 2, 3], [4, 5, 6], [7, 8, 9]], is_int_above_8)
        == [9])
assert (traverseNp([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], is_int_above_8)
        == [9, 12, 11, 10])
assert (traverseNp([[1, 2, 3, 'a'], [4, 5, 6], [7, 8, 9], [10, 11, 12]], is_int_above_8)
        == [9, 12, 11, 10])
assert (traverseNp([[1, 2, 3], [4, 5, 6, 12], [[7], [8], [9]], [10, 11, 12]], is_int_above_8)
        == [12, 9, 12, 11, 10])
assert (traverseNp([[1, 2, 3], [4, 5, 6], [7, 8, 9, 9.5], [10, 11, 12]], is_int_above_8)
        == [9, 12, 11, 10])
assert (traverseNp([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]], is_int_above_8)
        == [9, 12, 11, 10, 16, 15, 14, 13])
assert (traverseNp([[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]], is_int_above_8)
        == [9, 12, 11, 10, 16, 15, 14, 13])
assert (traverseNp([[], [], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]], is_int_above_8)
        == [9, 12, 11, 10, 16, 15, 14, 13])
assert (traverseNp([[], [], [7, 8, 9], [], [13, 14, 15, 16]], is_int_above_8)
        == [9, 16, 15, 14, 13])
assert (traverseNp([[1, 2, 3, 4], [5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]], is_int_above_8)
        == [9, 12, 11, 10, 15, 14, 13])
assert (traverseNp([[0, 2, 3], [4, 5, 0], [7, 8, 9]], is_int_above_8)
        == [9])
assert (traverseNp([[0, 2, 3], [4, 5, 0], [7, 8, 9], [10, 11, 12]], is_int_above_8)
        == [9, 12, 11, 10])
assert (traverseNp([[0, 2, 3, 'a'], [4, 5, 0], [7, 8, 9], [10, 11, 12]], is_int_above_8)
        == [9, 12, 11, 10])
assert (traverseNp([[0, 2, 3], [4, 5, 0, 12], [[7], [8], [9]], [10, 11, 12]], is_int_above_8)
        == [12, 9, 12, 11, 10])
assert (traverseNp([[0, 2, 3], [4, 5, 0], [7, 8, 9, 9.5], [10, 11, 12]], is_int_above_8)
        == [9, 12, 11, 10])
assert (traverseNp([[0, 2, 3], [4, 5, None], [7, 8, 9, 9.5], [10, 11, 12]], is_int_above_8)
        == [9, 12, 11, 10])
assert (traverseNp([[0, 2, 3], [4, None, 0], [7, 8, None, 9.5], [10, 11, None]], is_int_above_8)
        == [11, 10])
assert (traverseNp([[0, 2, 3, (1, 4, 8)], [4, 5, 0], [7, 8, 9], [10, 11, 12]], is_int_above_8)
        == [9, 12, 11, 10])
assert (traverseNp([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 1.5], [1, 1.5], [1, 1.5]], is_int_above_8)
        == [])
assert (traverseNp([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2], [1, 2], [1, 2]], is_int_above_8)
        == [])
assert (traverseNp([1, 2], is_int_divisible_by_3)
        == [])
assert (traverseNp([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], is_int_divisible_by_3)
        == [3, 6, 9])
assert (traverseNp([1, 2, 'hello', 'goodbye'], is_int_divisible_by_3)
        == [])
assert (traverseNp([(1, 2), (3, 4), (5, 6)], is_int_divisible_by_3)
        == [])
assert (traverseNp([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]],
                    [[0, 2, 3], [4, 5, 0], [7, 8, 9]]], is_int_divisible_by_3)
        == [9, 6, 3, 15, 12, 9, 6, 9, 0, 0, 3])
assert (traverseNp([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]],
                    [[0, 2, 3], [4, 5, 0], [7, 8, 9]],
                    [[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]]], is_int_divisible_by_3) ==
        [9, 6, 3, 15, 12, 9, 6, 9, 0, 0, 3])
assert (traverseNp([[[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]],
                     [[0, 2, 3], [4, 5, 0], [7, 8, 9]]],
                    [[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]]], is_int_divisible_by_3) ==
        [3, 0, 0, 9, 6, 9, 12, 15, 3, 6, 9])
assert (traverseNp([[[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]],
                    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]],
                     [[0, 2, 3], [4, 5, 0], [7, 8, 9]]],
                    [[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]]], is_int_divisible_by_3) ==
        [3, 0, 0, 9, 6, 9, 12, 15, 3, 6, 9])
assert (traverseNp([[[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]],
                    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                     [[[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]], [[0, 2, 3], [4, 5, 0], [7, 8, 9]]]],
                    [[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]]], is_int_divisible_by_3) ==
        [15, 12, 9, 6, 9, 0, 0, 3, 3, 6, 9])
assert (traverseNp([[[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]],
                    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                     [[[[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]], [[0, 2, 3], [4, 5, 0], [7, 8, 9]]]]],
                    [[1, 2, 'a', None, 'q'], [2.0, 'a', 'test'], ['tset'], [8989, 7]]], is_int_divisible_by_3) ==
        [3, 0, 0, 9, 6, 9, 12, 15, 3, 6, 9])
assert (traverseNp([[1, 2, 3], [4, 5, 6], [7, 8, 9]], is_int_divisible_by_3)
        == [3, 6, 9])
assert (traverseNp([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], is_int_divisible_by_3)
        == [3, 6, 9, 12])
assert (traverseNp([[1, 2, 3, 'a'], [4, 5, 6], [7, 8, 9], [10, 11, 12]], is_int_divisible_by_3)
        == [3, 6, 9, 12])
assert (traverseNp([[1, 2, 3], [4, 5, 6, 12], [[7], [8], [9]], [10, 11, 12]], is_int_divisible_by_3)
        == [3, 12, 6, 9, 12])
assert (traverseNp([[1, 2, 3], [4, 5, 6], [7, 8, 9, 9.5], [10, 11, 12]], is_int_divisible_by_3)
        == [3, 6, 9, 12])
assert (traverseNp([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]], is_int_divisible_by_3)
        == [3, 6, 9, 12, 15])
assert (traverseNp([[], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]], is_int_divisible_by_3)
        == [6, 9, 12, 15])
assert (traverseNp([[], [], [7, 8, 9], [10, 11, 12], [13, 14, 15, 16]], is_int_divisible_by_3)
        == [9, 12, 15])
assert (traverseNp([[], [], [7, 8, 9], [], [13, 14, 15, 16]], is_int_divisible_by_3)
        == [9, 15])
assert (traverseNp([[1, 2, 3, 4], [5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]], is_int_divisible_by_3)
        == [3, 6, 9, 12, 15])
assert (traverseNp([[0, 2, 3], [4, 5, 0], [7, 8, 9]], is_int_divisible_by_3)
        == [3, 0, 0, 9])
assert (traverseNp([[0, 2, 3], [4, 5, 0], [7, 8, 9], [10, 11, 12]], is_int_divisible_by_3)
        == [3, 0, 0, 9, 12])
assert (traverseNp([[0, 2, 3, 'a'], [4, 5, 0], [7, 8, 9], [10, 11, 12]], is_int_divisible_by_3)
        == [3, 0, 0, 9, 12])
assert (traverseNp([[0, 2, 3], [4, 5, 0, 12], [[7], [8], [9]], [10, 11, 12]], is_int_divisible_by_3)
        == [3, 0, 12, 0, 9, 12])
assert (traverseNp([[0, 2, 3], [4, 5, 0], [7, 8, 9, 9.5], [10, 11, 12]], is_int_divisible_by_3)
        == [3, 0, 0, 9, 12])
assert (traverseNp([[0, 2, 3], [4, 5, None], [7, 8, 9, 9.5], [10, 11, 12]], is_int_divisible_by_3)
        == [3, 0, 9, 12])
assert (traverseNp([[0, 2, 3], [4, None, 0], [7, 8, None, 9.5], [10, 11, None]], is_int_divisible_by_3)
        == [3, 0, 0])
assert (traverseNp([[0, 2, 3, (1, 4, 8)], [4, 5, 0], [7, 8, 9], [10, 11, 12]], is_int_divisible_by_3)
        == [3, 0, 0, 9, 12])
assert (traverseNp([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 1.5], [1, 1.5], [1, 1.5]], is_int_divisible_by_3)
        == [3, 3, 3])
assert (traverseNp([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2], [1, 2], [1, 2]], is_int_divisible_by_3)
        == [3, 3, 3, 3])

# ======================================================================
# Uppgift 5:  Testfall
# ======================================================================


# HÃ¤r kan det finnas flera olika lÃ¶sningar.  LÃ¶sningsfÃ¶rslaget ger
# en av de olika tÃ¤nkbara lÃ¶sningarna.

find_subseq([1, 2, 3], [1, 5, 1, 2, 7, 8, 9, 3])
find_subseq([1, 2, 3], [1, 1, 1, 2, 1, 3, 1, 2])
find_subseq([1, 2, 3], [1, 5, 3, 2, 1, 2])
find_subseq([1, 2, 3], [1, 2, 1, 5, 2, 3])
find_subseq([1, 2, 1], [1, 5, 2, 7, 1])
find_subseq([1, 1], [1])
find_subseq(['a', 'b'], ['a', 5, 'b'])
find_subseq([1, 7, 3], [1, 5, 1, 2, 7, 8, 9, 3, 3])
find_subseq([1, 1], [1, 1])
find_subseq([1, 2, 1], [1, 1])
find_subseq([1, 2, 1], [1, 2, 1])
find_subseq([1, 2, 1], [1, 2, 1])
find_subseq([1, 1], [99, 1, 1])
find_subseq([1, 2, 1], [99, 1, 1])
find_subseq([1, 2, 1], [99, 1, 2, 1])
find_subseq([1, 2, 1], [99, 1, 2, 1])
find_subseq([1, 2, 3], [1, 5, 1, 2, 7, 8, 9, 3])
find_subseq([1, 2, 3], [1, 1, 1, 2, 1, 3, 1, 2])
find_subseq([1, 7, 3], [99, 1, 5, 1, 2, 7, 8, 9, 3, 3])
find_subseq([1, 2, 3], [99, 1, 5, 1, 2, 7, 8, 9, 3])
find_subseq([1, 2, 3], [99, 1, 1, 1, 2, 1, 3, 1, 2])
find_subseq([1, 2, 3], [1, 5, 3, 2, 1, 2])
find_subseq([1, 2, 3], [1, 2, 1, 5, 2, 3])
find_subseq([1, 2, 1], [1, 5, 2, 7, 1])
find_subseq([1, 2, 2], [1, 5, 2, 7, 1])
find_subseq([1, 2, 2, 5, 5], [1, 5, 2, 7, 1])
find_subseq([1, 2, 5], [1, 5, 2, 7, 1])
find_subseq([1, 2, 2, 5, 7], [1, 5, 2, 7, 1])
find_subseq([1, 1, 2, 2, 5, 7], [1, 5, 2, 7])
find_subseq([99, 1, 2, 3], [1, 5, 3, 2, 1, 2])
find_subseq([1, 99, 2, 3], [1, 2, 1, 5, 2, 3])
find_subseq([1, 2, 99, 1], [1, 5, 2, 7, 1])
find_subseq([1, 2, 1, 99], [1, 5, 2, 7, 1])
find_subseq([1, 98, 2, 97, 1, 99], [1, 5, 2, 7, 1])
find_subseq([1, 1], [2, 1])
find_subseq([1, 1], [3, 2, 1])
find_subseq([1, 7, 3], [1, 5, 1, 2, 7, 8, 9, 3, 7, 3])
find_subseq([1, 7, 3], [9, 9, 9, 9, 9, 9, 9, 1, 5, 1, 2, 7, 8, 9, 3, 3])
find_subseq([1, 7, 3], [9, 9, 9, 9, 1, 1, 1, 9, 9, 9, 1, 5, 1, 2, 7, 8, 9, 3, 3])
find_subseq([1, 7, 3], [9, 9, 9, 9, 1, 1, 1, 9, 9, 9, 1, 5, 1, 2, 7, 8, 9, 3, 3, 1])
find_subseq((1, 1), (1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1))
find_subseq((1, 2, 1), (1, 5, 2, 7, 1))
find_subseq("abc", "asdbofc")

find_with_max_distance([1, 7, 3], [1, 5, 1, 2, 7, 8, 9, 3, 3], 3)
find_with_max_distance([1, 7, 3], [1, 5, 1, 2, 7, 8, 9, 3, 3], 10)
find_with_max_distance([1, 7, 3], [1, 5, 1, 2, 7, 8, 9, 3, 3], 2)
find_with_max_distance([], [1, 5, 1], 3)
find_with_max_distance(['a'], ['a', 5, 'a'], 3)
find_with_max_distance([1, 2], [2, 1], 3)
find_with_max_distance([1, 2, 3], [1, 9, 9, 9, 1, 2, 2, 9, 9, 3], 3)
find_with_max_distance([1, 7, 3], [1, 5, 1, 2, 7, 8, 9, 3, 3], 3)
find_with_max_distance([1, 7, 3], [1, 5, 1, 2, 7, 8, 9, 3, 3], 4)
find_with_max_distance([1, 7, 3], [1, 5, 1, 2, 7, 8, 9, 3, 3], 5)
find_with_max_distance([1, 7, 3], [9, 9, 9, 9, 9, 9, 9, 1, 5, 1, 2, 7, 8, 9, 3, 3], 3)
find_with_max_distance([1, 7, 3], [1, 5, 1, 2, 7, 8, 9, 3, 7, 3], 2)
find_with_max_distance([1, 2, 3], [1, 5, 1, 2, 7, 8, 9, 3], 2)
find_with_max_distance([1, 2, 3], [1, 5, 1, 2, 7, 8, 9, 3], 3)
find_with_max_distance([1, 2, 3], [1, 1, 1, 2, 1, 3, 1, 2], 1)
find_with_max_distance([1, 2, 3], [1, 1, 1, 2, 1, 3, 1, 2], 2)
find_with_max_distance([1, 2, 3], [1, 5, 3, 2, 1, 2], 10)
find_with_max_distance([1, 2, 3], [1, 2, 1, 5, 2, 3], 2)
find_with_max_distance([1, 2, 3], [1, 2, 1, 5, 2, 3], 3)
find_with_max_distance([1, 2, 3], [1, 2, 1, 5, 2, 3], 10)
find_with_max_distance([1, 2, 1], [1, 5, 2, 7, 1], 1)
find_with_max_distance([1, 2, 1], [1, 5, 2, 7, 1], 2)
find_with_max_distance([1, 2, 1], [1, 5, 2, 7, 1], 3)
find_with_max_distance([1, 1], [1], 0)
find_with_max_distance([1, 1], [1], 1)
find_with_max_distance([1, 1], [1], 33)
find_with_max_distance([1, 1], [2, 1], 1)
find_with_max_distance([1, 1], [3, 2, 1], 1)
find_with_max_distance([], [1], 0)
find_with_max_distance([], [1], 2)
find_with_max_distance([1, 7, 3], [9, 9, 9, 9, 9, 9, 9, 1, 5, 1, 2, 7, 8, 9, 3, 3], 25)
find_with_max_distance([1, 7, 3], [1, 5, 1, 2, 7, 8, 9, 3, 7, 3], 4)
find_with_max_distance([], [1, 5, 1], 3)
find_with_max_distance([1, 7, 3], [9, 9, 9, 9, 9, 9, 9, 1, 5, 1, 2, 7, 8, 9, 3, 3], 4)
find_with_max_distance([1, 7, 3], [9, 9, 9, 9, 9, 9, 9, 1, 5, 1, 2, 7, 8, 9, 3, 3], 2)
find_with_max_distance([1, 7, 3], [9, 9, 9, 9, 1, 1, 1, 9, 9, 9, 1, 5, 1, 2, 7, 8, 9, 3, 3], 3)
find_with_max_distance([1, 7, 3], [9, 9, 9, 9, 1, 1, 1, 9, 9, 9, 1, 5, 1, 2, 7, 8, 9, 3, 3, 1], 3)
find_with_max_distance([1, 7], [1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 7], 10)
find_with_max_distance([1, 7], [1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 7], 11)
find_with_max_distance([1, 1], [1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1], 10)
find_with_max_distance([1, 1], [1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1], 11)
find_with_max_distance((1, 1), (1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1), 11)
find_with_max_distance((1, 2, 1), (1, 5, 2, 7, 1), 1)
find_with_max_distance((1, 2, 1), (1, 5, 2, 7, 1), 2)
find_with_max_distance((1, 2, 1), (1, 5, 2, 7, 1), 3)
find_with_max_distance("abc", "asdbofc", 2)
find_with_max_distance("abc", "asdbofc", 3)
find_with_max_distance([1, 7, 3], [99, 99, 1, 99, 99, 7, 7, 99, 99, 99, 3, 99], 4)
find_with_max_distance([1, 7, 1, 3], [99, 99, 1, 99, 99, 7, 99, 99, 1, 1, 99, 99, 99, 3, 99], 4)
find_with_max_distance([1, 1], [1, 2, 1], 1)
find_with_max_distance([1, 1], [1, 2, 1], 2)
find_with_max_distance([1, 1], [1, 2, 1], 3)
find_with_max_distance([1, 1, 1], [1, 99, 1, 99, 1], 1)
find_with_max_distance([1, 1, 1], [1, 99, 1, 99, 1], 2)
find_with_max_distance([5, 5, 5], [5, 99, 5, 99, 5], 1)
find_with_max_distance([5, 5, 5], [5, 99, 5, 99, 5], 2)
find_with_max_distance([5, 5, 5], [99, 99, 5, 99, 5, 99, 5], 1)
find_with_max_distance([5, 5, 5], [99, 99, 5, 99, 5, 99, 5], 2)
find_with_max_distance([1, 1, 1], [1, '99', 1, '99', 1], 1)
find_with_max_distance([1, 1, 1], [1, '99', 1, '99', 1], 2)
find_with_max_distance([5.0, 5.0, 5.0], [5.0, '99', 5.0, '99', 5.0], 1)
find_with_max_distance([5.0, 5.0, 5.0], [5.0, '99', 5.0, '99', 5.0], 2)
find_with_max_distance([5.0, 5.0, 5.0], ['99', '99', 5.0, '99', 5.0, '99', 5.0], 1)
find_with_max_distance([5.0, 5.0, 5.0], ['99', '99', 5.0, '99', 5.0, '99', 5.0], 2)
find_with_max_distance([(12,), (12,), (12,)], ['99', '99', (12,), '99', (12,), '99', (12,)], 1)
find_with_max_distance([(12,), (12,), (12,)], ['99', '99', (12,), '99', (12,), '99', (12,)], 2)
find_with_max_distance([1, 2, 3], [1, 2, 99, 99, 99, 99, 99, 99, 99, 1, 2, 3], 2)
find_with_max_distance([1, 2, 3], [1, 2, 99, 99, 99, 99, 99, 99, 99, 1, 2, 3], 2)
find_with_max_distance([1, 2, 3], [1, 2, 1, 5, 2, 99, 99, 2, 99, 99, 2, 99, 99, 3], 3)
find_with_max_distance([1, 2, 3, 4, 5], [99, 1, 99, 99, 3, 2, 99, 1, 2, 99, 99, 3, 99, 99, 4, 99, 99, 5], 3)
find_with_max_distance([1, 2, 3, 4, 5], [99, 1, 99, 99, 2, 3, 99, 1, 2, 99, 99, 3, 99, 99, 4, 99, 99, 5], 3)
find_with_max_distance([1, 2, 3, 4, 5], [99, 1, 99, 99, 2, 3, 4, 99, 1, 2, 99, 99, 3, 99, 99, 4, 99, 99, 5], 3)
find_with_max_distance([1, 2, 3, 4, 5], [1, 99, 99, 2, 3, 4, 99, 1, 2, 99, 99, 3, 99, 99, 4, 99, 99, 5], 3)
find_with_max_distance([5, 5, 5], [5, 99, 99, 99, 5, 99, 5, 99, 5], 1)
find_with_max_distance([5, 5, 5], [5, 99, 99, 99, 5, 99, 5, 99, 5], 2)
find_with_max_distance([5.0, 5.0, 5.0], [5.0, '99', 5.0, '99', 5.0], 5)
find_with_max_distance([1, 3], [1, 2, 3, 1, 2], 3)
find_with_max_distance([1, 3], [1, 2, 3, 1, 2], 4)
find_with_max_distance([1, 3], [1, 2, 3, 1, 2], 5)
find_with_max_distance([1, 7, 12, 3], [99, 99, 1, 99, 99, 7, 99, 99, 12, 12, 99, 99, 99, 3, 99], 4)
find_with_max_distance([1, 7, 5, 12, 3], [99, 99, 1, 99, 99, 7, 99, 99, 5, 99, 99, 12, 12, 99, 99, 99, 3, 99], 4)
find_with_max_distance([1, 7, 5, 12, 3], [99, 99, 1, 99, 99, 7, 99, 99, 5, 99, 12, 12, 99, 99, 3, 99], 3)
find_with_max_distance([1, 7, 5, 12, 3], [99, 99, 1, 99, 99, 7, 99, 99, 5, 99, 12, 12, 99, 99, 3, 99], 2)
find_with_max_distance([1, 7, 5, 12, 13, 3], [99, 99, 1, 99, 99, 7, 99, 99, 5, 99, 12, 12, 99, 13, 13, 99, 3, 99], 3)
find_with_max_distance([1, 7, 5, 12, 13, 3], [99, 99, 1, 99, 99, 7, 99, 99, 5, 99, 12, 12, 99, 13, 5, 13, 99, 3, 99], 4)
find_with_max_distance([1, 2, 3], [1, 3, 2, 3], 4)
