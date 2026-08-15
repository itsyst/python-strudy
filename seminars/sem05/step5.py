"""
TDDE23 Seminarium 5 - En sak i taget
Funktionell programmering
"""

# =============================================================================
# UPPGIFT: PARADIGM
# =============================================================================

print("=" * 70)
print("PARADIGM - Sant eller Falskt")
print("=" * 70)

paradigm_questions = [
    ("1. Dynamisk typning är ett paradigm som Python stödjer.", 
     "SANT - Python använder dynamisk typning (variabler får typ vid körning)"),
    
    ("2. Pythonkod måste kompileras för att köras.", 
     "SANT/FALSKT (Tekniskt) - Python kompileras till bytecode, men detta sker automatiskt"),
    
    ("3. Om man programmerar funktionellt kan man ej använda listor då de är objekt.", 
     "FALSKT - Listor kan användas, men man ska inte mutera dem"),
    
    ("4. Python stödjer objektorienterad programmering.", 
     "SANT - Python har klasser, objekt, arv, etc."),
    
    ("5. I Python kan man ej programmera imperativt.", 
     "FALSKT - Python stödjer imperativ programmering (for-loopar, if-satser, etc.)"),
    
    ("6. Om man programmerar funktionellt får funktioner inte ha sidoeffekter.", 
     "SANT - Rena funktioner ska inte ha sidoeffekter"),
    
    ("7. Om en funktionellt programmerad funktion tar emot en lista får denna inte ändras, dock kan kopior av listan ändras.", 
     "SANT - Man får inte mutera input, men kan skapa och ändra kopior"),
    
    ("8. Funktionen print() kan användas i funktionell programmering.", 
     "FALSKT (Tekniskt) - print() har sidoeffekter (skriver till stdout)"),
    
    ("9. Funktionen range() kan användas i funktionell programmering.", 
     "SANT - range() är en ren funktion som returnerar en sekvens"),
    
    ("10. Funktionell programmering är generellt snabbare än annan programmering.", 
     "FALSKT - Det beror på implementationen och användningsfallet"),
    
    ("11. Inom funktionell programmering används ofta rekursion istället för for-loopar.", 
     "SANT - Rekursion är prefererat över imperativa loopar"),
    
    ("12. När man programmerar funktionellt måste all kod vara strikt funktionell.", 
     "FALSKT - Man kan blanda paradigm, särskilt i Python"),
]

for question, answer in paradigm_questions:
    print(f"\n{question}")
    print(f"   Svar: {answer}")


# =============================================================================
# UPPGIFT: HÖGRE ORDNINGENS FUNKTIONER, LAMBDAUTTRYCK OCH LISTBYGGARE
# =============================================================================

print("\n" + "=" * 70)
print("HÖGRE ORDNINGENS FUNKTIONER, LAMBDAUTTRYCK OCH LISTBYGGARE")
print("=" * 70)

print("\n#1: (lambda x: x + 2)(10)")
result1 = (lambda x: x + 2)(10)
print(f"Output: {result1}")
print("Förklaring: Lambda-funktion som lägger till 2 på 10 = 12")

print("\n#2: (lambda x, y: x * y)(2 + 3, 4 * 5)")
result2 = (lambda x, y: x * y)(2 + 3, 4 * 5)
print(f"Output: {result2}")
print("Förklaring: Lambda multiplicerar (2+3)=5 med (4*5)=20 = 100")

print("\n#3: (lambda x: x + 1)((lambda y: y + 2)(3))")
result3 = (lambda x: x + 1)((lambda y: y + 2)(3))
print(f"Output: {result3}")
print("Förklaring: Inre lambda: 3+2=5, yttre lambda: 5+1=6")

print("\n#4: seq = [[17, 4, 8], [9, 14, 2, 7], [33, 14]]")
print("    [sorted(x)[1] for x in seq]")
seq = [[17, 4, 8], [9, 14, 2, 7], [33, 14]]
result4 = [sorted(x)[1] for x in seq]
print(f"Output: {result4}")
print("Förklaring: Andra elementet (index 1) från varje sorterad underlista")
print("  [4,8,17][1]=8, [2,7,9,14][1]=7, [14,33][1]=33")

print("\n#5: seq = ['apelsin', 'banan', 'citron']")
print("    [x.replace('a', '*') for x in seq if 'a' in x]")
seq = ['apelsin', 'banan', 'citron']
result5 = [x.replace('a', '*') for x in seq if 'a' in x]
print(f"Output: {result5}")
print("Förklaring: Endast ord med 'a', ersätt alla 'a' med '*'")

print("\n#6: Jämföra listbyggare med map/filter")
a = [i + 2 for i in range(10) if i % 2 == 0]
b = list(map(lambda i: i + 2, filter(lambda i: i % 2 == 0, list(range(10)))))
result6 = a == b
print(f"a = {a}")
print(f"b = {b}")
print(f"a == b: {result6}")
print("Förklaring: Båda ger jämna tal från 0-9, adderat med 2: [2,4,6,8,10]")

print("\n#7: list(filter(lambda x: x % 3 == 0, list(range(0, 20, 2))))[2]")
result7 = list(filter(lambda x: x % 3 == 0, list(range(0, 20, 2))))[2]
print(f"Output: {result7}")
print("Förklaring: Jämna tal 0-20 som är delbara med 3: [0,6,12,18], index 2 = 12")

print("\n#8: ''.join([chr(ord(c) - 1) for c in \"Helloworld\"])")
result8 = ''.join([chr(ord(c) - 1) for c in "Helloworld"])
print(f"Output: {result8}")
print("Förklaring: Varje tecken ersätts med föregående tecken i ASCII")

print("\n#9: Palindromiska tal 100-130")
def pal_num(n):
    s = str(n)
    return s == s[::-1]

result9 = [i for i in range(100, 130) if pal_num(i)]
print(f"Output: {result9}")
print("Förklaring: Tal som är samma framlänges och baklänges: 101, 111, 121")

print("\n#10: Fibonacci-sekvens med jämna tal")
def fib_maker():
    a, b = 0, 1
    def next_fib():
        nonlocal a, b
        a, b = b, a + b
        return b - a
    return next_fib

fib = fib_maker()
result10 = list(filter(lambda x: x % 2 == 0, [fib() for i in range(7)]))
print(f"Output: {result10}")
print("Förklaring: Första 7 Fibonacci-tal: [0,1,1,2,3,5,8], jämna: [0,2,8]")


# =============================================================================
# UPPGIFT 1: ITERATOR OCH INDEX
# =============================================================================

print("\n" + "=" * 70)
print("UPPGIFT 1: ITERATOR OCH INDEX")
print("=" * 70)

def func1(seq):
    """Iterera med for-each (iterator)"""
    res = []
    for elem in seq:
        if elem % 2 == 0:
            res.append(elem)
    return res

def func2(seq):
    """Iterera med range och index"""
    res = []
    for i in range(len(seq)):
        if seq[i] % 2 == 0:
            res.append(seq[i])
    return res

def func3(seq):
    """Iterera med while-loop och index"""
    res = []
    i = 0
    while i < len(seq):
        if seq[i] % 2 == 0:
            res.append(seq[i])
        i += 1
    return res

# Testa funktionerna
test_seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"\nTestsekvens: {test_seq}")
print(f"func1 (for-each):    {func1(test_seq)}")
print(f"func2 (for-range):   {func2(test_seq)}")
print(f"func3 (while-loop):  {func3(test_seq)}")

print("\nAnalys:")
print("-" * 70)
print("1. Vad gör funktionerna?")
print("   Alla tre returnerar en lista med jämna tal från input-sekvensen")

print("\n2. Vad är skillnaden mellan funktionerna?")
print("   func1: Använder FOR-EACH iteration (elementbaserad)")
print("   func2: Använder FOR-RANGE iteration (indexbaserad)")
print("   func3: Använder WHILE-LOOP iteration (manuell indexhantering)")

print("\n3. Vilken funktion är lättast att läsa? Vilken borde användas?")
print("   func1 är lättast - direktaccess till element utan indexhantering")
print("   func1 borde användas för detta syfte (filtrering utan indexbehov)")

print("\n4. Vid vilka tillfällen ska de olika sätten användas?")
print("   FOR-EACH (func1):")
print("     - När man bara behöver elementvärdena")
print("     - För enkel iteration över alla element")
print("     - Mest pythonisk och lättläst")
print("   ")
print("   FOR-RANGE (func2):")
print("     - När man behöver index samtidigt som värde")
print("     - För att modifiera element på plats")
print("     - För att jämföra med närliggande element")
print("   ")
print("   WHILE-LOOP (func3):")
print("     - När man behöver dynamisk kontroll över iteration")
print("     - För att hoppa över element eller ändra steg")
print("     - För komplexa iterationsmönster")


# =============================================================================
# UPPGIFT 2: ITERATOR OCH INDEX - ANVÄNDNINGSFALL
# =============================================================================

print("\n" + "=" * 70)
print("UPPGIFT 2: ITERATOR OCH INDEX - ANVÄNDNINGSFALL")
print("=" * 70)

print("\n1. Hitta första förekomsten och lagra dess index:")
print("   Använd: FOR-RANGE med break")
print("   Exempel:")

def find_first_index(seq, target):
    for i in range(len(seq)):
        if seq[i] == target:
            return i
    return -1

test_list = [10, 20, 30, 40, 30, 50]
index = find_first_index(test_list, 30)
print(f"   Lista: {test_list}")
print(f"   Första index av 30: {index}")

print("\n2. Returnera antal förekomster av ett element:")
print("   Använd: FOR-EACH (ingen indexbehov)")
print("   Exempel:")

def count_occurrences(seq, target):
    count = 0
    for elem in seq:
        if elem == target:
            count += 1
    return count

count = count_occurrences(test_list, 30)
print(f"   Lista: {test_list}")
print(f"   Antal förekomster av 30: {count}")
print(f"   (Alternativt: test_list.count(30) = {test_list.count(30)})")

print("\n3. Returnera det minsta elementet i en lista:")
print("   Använd: FOR-EACH (ingen indexbehov)")
print("   Exempel:")

def find_minimum(seq):
    if not seq:
        return None
    min_val = seq[0]
    for elem in seq:
        if elem < min_val:
            min_val = elem
    return min_val

minimum = find_minimum(test_list)
print(f"   Lista: {test_list}")
print(f"   Minsta element: {minimum}")
print(f"   (Alternativt: min(test_list) = {min(test_list)})")

print("\n4. Bubble sort - jämför element med efterföljare:")
print("   Använd: WHILE-LOOP + FOR-RANGE (behöver index för swap)")
print("   Exempel:")

def bubble_sort(seq):
    seq = seq.copy()  # Kopiera för att inte mutera input
    changed = True
    while changed:
        changed = False
        for i in range(len(seq) - 1):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                changed = True
    return seq

unsorted = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(unsorted)
print(f"   Osorterad: {unsorted}")
print(f"   Sorterad:  {sorted_list}")


# =============================================================================
# SAMMANFATTNING
# =============================================================================

print("\n" + "=" * 70)
print("SAMMANFATTNING AV ITERATIONSMETODER")
print("=" * 70)

summary = """
FOR-EACH (for elem in seq):
  ✓ Använd när du bara behöver värden
  ✓ Enklast och mest pythonisk
  ✓ Exempel: filtrering, counting, summering
  
FOR-RANGE (for i in range(len(seq))):
  ✓ Använd när du behöver index
  ✓ För att modifiera element på plats
  ✓ För att jämföra med närliggande element
  ✓ Exempel: swap, jämförelser med grannar
  
WHILE-LOOP (while condition):
  ✓ Använd för komplex iterationskontroll
  ✓ När antalet iterationer är okänt
  ✓ För att hoppa över eller upprepa steg
  ✓ Exempel: bubble sort, sökalgoritmer

ENUMERATE (for i, elem in enumerate(seq)):
  ✓ Bäst av båda världar - både index och värde
  ✓ Använd istället för FOR-RANGE när möjligt
"""

print(summary)

print("=" * 70)
print("ALLA UPPGIFTER SLUTFÖRDA!")
print("=" * 70)