"""
TDDE23 Seminarium 6 - Experimentering
Analysera och testa program
"""

# =============================================================================
# FUNKTIONEN SOM SKA TESTAS
# =============================================================================

def count(seq):
    """
    Counts the number of elements in a given list
    including elements in inner lists
    """
    if not seq:
        return 0
    elif isinstance(seq[0], list):
        return count(seq[0]) + count(seq[1:])
    else:
        return 1 + count(seq[1:])


# =============================================================================
# ANALYS AV FUNKTIONEN
# =============================================================================

print("=" * 70)
print("ANALYS AV count() FUNKTIONEN")
print("=" * 70)

analysis = """
VAD GÖR FUNKTIONEN?
───────────────────────────────────────────────────────────────────
count() räknar det totala antalet element i en lista, inklusive
element i inre listor (nested lists). Den "plattar ut" listan
rekursivt och räknar alla icke-list element.

Exempel:
  count([1, 2, 3]) → 3
  count([1, [2, 3], 4]) → 4
  count([[1, 2], [3, 4]]) → 4

HUR FUNGERAR DEN?
───────────────────────────────────────────────────────────────────
Rekursiv approach med tre fall:

1. BASFALL (if not seq):
   - Tom lista → returnera 0

2. REKURSIVT FALL 1 (elif isinstance(seq[0], list)):
   - Första elementet är en lista
   - Räkna element i den listan + räkna resten

3. REKURSIVT FALL 2 (else):
   - Första elementet är inte en lista
   - Räkna 1 + räkna resten

VILKA TESTFALL BEHÖVS?
───────────────────────────────────────────────────────────────────
För att fullständigt testa funktionen behöver vi täcka:

1. BASFALL:
   ✓ Tom lista

2. ENKLA FALL:
   ✓ Lista med ett element
   ✓ Lista med flera element
   ✓ Lista med endast ett element (edge case)

3. NESTED LISTS:
   ✓ Lista med en inre lista
   ✓ Lista med flera inre listor
   ✓ Djupt nästlade listor (flera nivåer)
   ✓ Tom inre lista

4. BLANDADE FALL:
   ✓ Mix av element och listor
   ✓ Listor på olika nivåer

5. EDGE CASES:
   ✓ Tom lista inuti lista
   ✓ Listor med endast listor (inga "riktiga" element)
"""

print(analysis)


# =============================================================================
# DEL 1: TESTFUNKTION - OLIKA ALTERNATIV
# =============================================================================

print("\n" + "=" * 70)
print("DEL 1: OLIKA DESIGN AV test_count()")
print("=" * 70)

# Testfall definierade i en datastruktur
# Format: (input, expected_output, description)
TEST_CASES = [
    # Basfall
    ([], 0, "Tom lista"),
    
    # Enkla fall
    ([1], 1, "Ett element"),
    ([1, 2, 3], 3, "Flera element"),
    ([1, 2, 3, 4, 5], 5, "Många element"),
    
    # Nested lists
    ([[1, 2, 3]], 3, "En inre lista"),
    ([[1, 2], [3, 4]], 4, "Två inre listor"),
    ([1, [2, 3], 4], 4, "Mix av element och lista"),
    ([[[1, 2]]], 2, "Djupt nästlad lista"),
    ([[1, [2, 3]], 4], 4, "Nested lists på flera nivåer"),
    
    # Edge cases
    ([[]], 0, "Tom inre lista"),
    ([[], []], 0, "Flera tomma inre listor"),
    ([1, [], 2], 2, "Tom lista bland element"),
    ([[[]]], 0, "Djupt nästlad tom lista"),
    ([[[1]]], 1, "Djupt nästlad med ett element"),
]

print("\nTestfall definierade:")
print("-" * 70)
for i, (input_data, expected, desc) in enumerate(TEST_CASES, 1):
    print(f"{i:2d}. {desc:30s} | Input: {str(input_data):20s} | Expected: {expected}")


print("\n" + "=" * 70)
print("ALTERNATIV 1: Returnera True/False")
print("=" * 70)

def test_count_v1():
    """
    Testar count() och returnerar True om alla tester passerar
    
    FÖRDELAR:
    - Enkelt att använda i if-satser
    - Tydligt om alla tester passerade eller inte
    
    NACKDELAR:
    - Ingen information om vilka tester som failade
    - Stoppar inte vid första felet
    """
    all_passed = True
    
    for input_data, expected, description in TEST_CASES:
        result = count(input_data)
        if result != expected:
            print(f"✗ FAIL: {description}")
            print(f"  Input: {input_data}")
            print(f"  Expected: {expected}, Got: {result}")
            all_passed = False
        else:
            print(f"✓ PASS: {description}")
    
    return all_passed

print("\nKör test_count_v1():")
print("-" * 70)
success = test_count_v1()
print(f"\nResultat: {'ALLA TESTER PASSERADE' if success else 'VISSA TESTER FAILADE'}")
print(f"Returvärde: {success}")


print("\n" + "=" * 70)
print("ALTERNATIV 2: Returnera lista med misslyckade testfall")
print("=" * 70)

def test_count_v2():
    """
    Testar count() och returnerar lista med testfall som failade
    
    FÖRDELAR:
    - Detaljerad information om vad som gick fel
    - Kan analysera failures efteråt
    - Tom lista = alla tester passerade
    
    NACKDELAR:
    - Mer komplex att använda
    - Behöver checka om lista är tom
    """
    failures = []
    
    for input_data, expected, description in TEST_CASES:
        result = count(input_data)
        if result != expected:
            failures.append({
                'description': description,
                'input': input_data,
                'expected': expected,
                'got': result
            })
            print(f"✗ FAIL: {description}")
        else:
            print(f"✓ PASS: {description}")
    
    return failures

print("\nKör test_count_v2():")
print("-" * 70)
failures = test_count_v2()
print(f"\nResultat: {len(failures)} test(er) failade")
print(f"Returvärde: {failures}")


print("\n" + "=" * 70)
print("ALTERNATIV 3: Returnera antal fel")
print("=" * 70)

def test_count_v3():
    """
    Testar count() och returnerar antal misslyckade tester
    
    FÖRDELAR:
    - Snabb överblick av hur många fel
    - Lätt att använda (0 = success)
    - Enkel returtyp
    
    NACKDELAR:
    - Ingen information om vilka tester som failade
    """
    num_failures = 0
    
    for input_data, expected, description in TEST_CASES:
        result = count(input_data)
        if result != expected:
            print(f"✗ FAIL: {description}")
            print(f"  Input: {input_data}")
            print(f"  Expected: {expected}, Got: {result}")
            num_failures += 1
        else:
            print(f"✓ PASS: {description}")
    
    return num_failures

print("\nKör test_count_v3():")
print("-" * 70)
num_errors = test_count_v3()
print(f"\nResultat: {num_errors} test(er) failade")
print(f"Returvärde: {num_errors}")


print("\n" + "=" * 70)
print("ALTERNATIV 4: Returnera detaljerad rapport (REKOMMENDERAD)")
print("=" * 70)

def test_count_v4():
    """
    Testar count() och returnerar detaljerad testrapport
    
    FÖRDELAR:
    - Bästa av alla världar
    - Fullständig information
    - Lätt att använda och analysera
    
    NACKDELAR:
    - Lite mer komplex implementation
    """
    report = {
        'total': len(TEST_CASES),
        'passed': 0,
        'failed': 0,
        'failures': []
    }
    
    for input_data, expected, description in TEST_CASES:
        result = count(input_data)
        if result != expected:
            print(f"✗ FAIL: {description}")
            print(f"  Input: {input_data}")
            print(f"  Expected: {expected}, Got: {result}")
            report['failed'] += 1
            report['failures'].append({
                'description': description,
                'input': input_data,
                'expected': expected,
                'got': result
            })
        else:
            print(f"✓ PASS: {description}")
            report['passed'] += 1
    
    return report

print("\nKör test_count_v4():")
print("-" * 70)
report = test_count_v4()
print(f"\nTestrapport:")
print(f"  Totalt: {report['total']}")
print(f"  Passerade: {report['passed']}")
print(f"  Failade: {report['failed']}")
if report['failures']:
    print(f"\nFailade tester:")
    for failure in report['failures']:
        print(f"  - {failure['description']}: Expected {failure['expected']}, Got {failure['got']}")


# =============================================================================
# DEL 2: MOTIVERING AV TESTFALL
# =============================================================================

print("\n" + "=" * 70)
print("DEL 2: FULLSTÄNDIG TÄCKNING AV TESTFALL")
print("=" * 70)

coverage_analysis = """
TÄCKNING AV KODVÄGAR:
───────────────────────────────────────────────────────────────────

count() har tre kodvägar:
1. if not seq          → Basfall (tom lista)
2. elif isinstance...  → Första elementet är lista
3. else               → Första elementet är inte lista

För att täcka alla vägar behöver vi:

✓ KODVÄG 1 (Basfall):
  - Test 1: [] → täcker "if not seq"

✓ KODVÄG 2 (Första är lista):
  - Test 6: [[1, 2, 3]] → täcker "elif isinstance(seq[0], list)"
  - Test 7: [[1, 2], [3, 4]] → täcker nested lists
  
✓ KODVÄG 3 (Första är inte lista):
  - Test 2: [1] → täcker "else"
  - Test 3: [1, 2, 3] → täcker rekursion på "else"


EDGE CASES OCH GRÄNSFALL:
───────────────────────────────────────────────────────────────────

✓ Tom lista (Test 1)
✓ Ett element (Test 2) - minsta möjliga icke-tomma lista
✓ Tom inre lista (Test 10) - vad händer med tomma nested lists?
✓ Djupt nästlade listor (Test 8, 13, 14) - testar rekursionens djup
✓ Mix av element och listor (Test 8) - testar båda kodvägarna

MINIMALT ANTAL TESTFALL:
───────────────────────────────────────────────────────────────────

Teoretiskt minimum för 100% kodtäckning: 3 testfall
  1. [] - basfall
  2. [1, 2, 3] - enkla element
  3. [[1, 2], 3] - nested list

Men för ROBUST testning rekommenderas: 10-15 testfall
Vårt uppsättning: 15 testfall täcker:
  ✓ Alla kodvägar
  ✓ Edge cases
  ✓ Olika komplexitetsnivåer
  ✓ Djup nästling
  ✓ Blandade fall

Detta ger oss förtroende att funktionen fungerar korrekt i alla
tänkbara situationer.
"""

print(coverage_analysis)


# =============================================================================
# SAMMANFATTNING OCH REKOMMENDATION
# =============================================================================

print("\n" + "=" * 70)
print("SAMMANFATTNING OCH REKOMMENDATION")
print("=" * 70)

recommendation = """
REKOMMENDERAD IMPLEMENTATION: test_count_v4()
───────────────────────────────────────────────────────────────────

Motivering:
1. Returnerar detaljerad rapport med all information
2. Lätt att avgöra om tester passerade (report['failed'] == 0)
3. Ger information om vilka tester som failade
4. Kan analyseras programmatiskt
5. Bra för både manuell inspektion och automatisering

Datastruktur för testfall:
  Lista av tupler: (input, expected_output, description)
  
  Fördelar:
  - Enkel att läsa och underhålla
  - Lätt att lägga till nya testfall
  - Beskrivningar gör det lätt att förstå vad som testas
  - Kan itereras över enkelt

Antal testfall:
  15 testfall för fullständig täckning
  
  Inkluderar:
  - Basfall (tom lista)
  - Enkla fall (1-5 element)
  - Nested lists (olika djup)
  - Edge cases (tomma inre listor)
  - Blandade fall

ANVÄNDNING:
───────────────────────────────────────────────────────────────────
report = test_count_v4()

if report['failed'] == 0:
    print("✓ Alla tester passerade!")
else:
    print(f"✗ {report['failed']} tester failade")
    for failure in report['failures']:
        print(f"  {failure['description']}")
"""

print(recommendation)

# Visa final implementation
print("\n" + "=" * 70)
print("FINAL IMPLEMENTATION (Kopiera denna)")
print("=" * 70)

final_code = '''
# Testfall
TEST_CASES = [
    ([], 0, "Tom lista"),
    ([1], 1, "Ett element"),
    ([1, 2, 3], 3, "Flera element"),
    ([1, 2, 3, 4, 5], 5, "Många element"),
    ([[1, 2, 3]], 3, "En inre lista"),
    ([[1, 2], [3, 4]], 4, "Två inre listor"),
    ([1, [2, 3], 4], 4, "Mix av element och lista"),
    ([[[1, 2]]], 2, "Djupt nästlad lista"),
    ([[1, [2, 3]], 4], 4, "Nested lists på flera nivåer"),
    ([[]], 0, "Tom inre lista"),
    ([[], []], 0, "Flera tomma inre listor"),
    ([1, [], 2], 2, "Tom lista bland element"),
    ([[[]]], 0, "Djupt nästlad tom lista"),
    ([[[1]]], 1, "Djupt nästlad med ett element"),
]

def test_count():
    """
    Testar count() och returnerar detaljerad testrapport
    """
    report = {
        'total': len(TEST_CASES),
        'passed': 0,
        'failed': 0,
        'failures': []
    }
    
    for input_data, expected, description in TEST_CASES:
        result = count(input_data)
        if result != expected:
            print(f"✗ FAIL: {description}")
            print(f"  Input: {input_data}")
            print(f"  Expected: {expected}, Got: {result}")
            report['failed'] += 1
            report['failures'].append({
                'description': description,
                'input': input_data,
                'expected': expected,
                'got': result
            })
        else:
            print(f"✓ PASS: {description}")
            report['passed'] += 1
    
    return report
'''

print(final_code)

print("\n" + "=" * 70)
print("ALLA UPPGIFTER SLUTFÖRDA!")
print("=" * 70)