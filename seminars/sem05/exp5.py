"""
TDDE23 Seminarium 5 - Experimentering
Högre ordningens funktioner och lambda-uttryck
"""

# =============================================================================
# UPPGIFT: HÖGRE ORDNINGENS FUNKTIONER
# =============================================================================

print("=" * 70)
print("HÖGRE ORDNINGENS FUNKTIONER - count() funktion")
print("=" * 70)

# Predikatfunktioner
def is_number(x):
    """
    Returnerar True om x är ett tal (int eller float)
    """
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def is_positive(x):
    """
    Returnerar True om x är ett positivt tal
    """
    return isinstance(x, (int, float)) and x > 0


# Iterativ implementation
def count_iterative(lst, predicate):
    """
    Räknar antal element i lst som uppfyller predicate-funktionen
    
    Args:
        lst: Lista med element
        predicate: Funktion som tar ett element och returnerar True/False
    
    Returns:
        int: Antal element som uppfyller predikatet
    """
    counter = 0
    for elem in lst:
        if predicate(elem):
            counter += 1
    return counter


# Rekursiv implementation
def count_recursive(lst, predicate):
    """
    Räknar antal element i lst som uppfyller predicate-funktionen (rekursivt)
    
    Args:
        lst: Lista med element
        predicate: Funktion som tar ett element och returnerar True/False
    
    Returns:
        int: Antal element som uppfyller predikatet
    """
    if not lst:
        return 0
    
    # Första elementet uppfyller predikatet: 1 + resten
    if predicate(lst[0]):
        return 1 + count_recursive(lst[1:], predicate)
    # Första elementet uppfyller inte predikatet: 0 + resten
    else:
        return count_recursive(lst[1:], predicate)


# Vi använder den iterativa versionen som standard
count = count_iterative

print("\nPredikatfunktioner definierade:")
print("  - is_number(x): Returnerar True om x är ett tal")
print("  - is_positive(x): Returnerar True om x är ett positivt tal")

print("\nTest av count() med predikatfunktioner:")
print("-" * 70)

# Test 1: Räkna antal tal
test1 = [17, 3.14, "banan"]
result1 = count(test1, is_number)
print(f"\nTest 1: count({test1}, is_number)")
print(f"Resultat: {result1}")
print(f"Förklaring: 17 och 3.14 är tal, 'banan' är inte ett tal → 2 tal")

# Test 2: Räkna antal positiva tal
test2 = [1, -1, 45.3, 4711, -273.15]
result2 = count(test2, is_positive)
print(f"\nTest 2: count({test2}, is_positive)")
print(f"Resultat: {result2}")
print(f"Förklaring: 1, 45.3 och 4711 är positiva → 3 positiva tal")

# Extra test: Jämför iterativ och rekursiv
print("\n" + "-" * 70)
print("Jämförelse av iterativ och rekursiv implementation:")
test3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
iter_result = count_iterative(test3, lambda x: x % 2 == 0)
rec_result = count_recursive(test3, lambda x: x % 2 == 0)
print(f"Lista: {test3}")
print(f"Predikat: Jämna tal")
print(f"Iterativ: {iter_result}")
print(f"Rekursiv: {rec_result}")
print(f"Samma resultat: {iter_result == rec_result}")


# =============================================================================
# UPPGIFT: LAMBDA-UTTRYCK
# =============================================================================

print("\n" + "=" * 70)
print("LAMBDA-UTTRYCK med count()")
print("=" * 70)

print("\nLambda-uttryck kombinerar anonyma funktioner med count()")
print("Syntax: lambda parametrar: uttryck")

# Test 1: Räkna antalet förekomster av strängen "a"
print("\n" + "-" * 70)
print("1. Räkna antalet förekomster av strängen 'a'")
test_lambda1 = ["a", "B", "c", "a", "d"]
lambda1 = lambda x: x == "a"
result_lambda1 = count(test_lambda1, lambda1)
print(f"   count({test_lambda1}, lambda x: x == 'a')")
print(f"   Resultat: {result_lambda1}")
print(f"   Förklaring: Två stycken 'a' i listan")

# Test 2: Räkna antalet listor som är två element långa
print("\n" + "-" * 70)
print("2. Räkna antalet listor som är två element långa")
test_lambda2 = [["a"], [1, 2], ["b", "c"]]
lambda2 = lambda x: isinstance(x, list) and len(x) == 2
result_lambda2 = count(test_lambda2, lambda2)
print(f"   count({test_lambda2}, lambda x: isinstance(x, list) and len(x) == 2)")
print(f"   Resultat: {result_lambda2}")
print(f"   Förklaring: [1, 2] och ['b', 'c'] har längd 2 → 2 listor")

# Test 3: Räkna antalet tal som är delbara med tre
print("\n" + "-" * 70)
print("3. Räkna antalet tal som är delbara med tre")
test_lambda3 = [1, 2, 3, 4, 5, 6, 9]
lambda3 = lambda x: x % 3 == 0
result_lambda3 = count(test_lambda3, lambda3)
print(f"   count({test_lambda3}, lambda x: x % 3 == 0)")
print(f"   Resultat: {result_lambda3}")
print(f"   Förklaring: 3, 6 och 9 är delbara med 3 → 3 tal")


# =============================================================================
# EXTRA: FLER EXEMPEL MED LAMBDA OCH count()
# =============================================================================

print("\n" + "=" * 70)
print("EXTRA EXEMPEL - Lambda med count()")
print("=" * 70)

extra_examples = [
    (
        "Strängar längre än 5 tecken",
        ["hej", "världen", "python", "kod", "programmering"],
        lambda x: isinstance(x, str) and len(x) > 5,
        "världen, python och programmering är längre än 5 tecken"
    ),
    (
        "Negativa tal",
        [10, -5, 3, -8, 0, -1, 7],
        lambda x: x < 0,
        "-5, -8 och -1 är negativa"
    ),
    (
        "Strängar som börjar med 'p'",
        ["python", "java", "perl", "ruby", "php"],
        lambda x: isinstance(x, str) and x.lower().startswith('p'),
        "python, perl och php börjar med 'p'"
    ),
    (
        "Tal mellan 10 och 20",
        [5, 12, 18, 25, 15, 8, 20, 30],
        lambda x: 10 <= x <= 20,
        "12, 18, 15 och 20 är mellan 10 och 20"
    ),
]

for title, test_list, predicate, explanation in extra_examples:
    result = count(test_list, predicate)
    print(f"\n{title}:")
    print(f"  Lista: {test_list}")
    print(f"  Resultat: {result}")
    print(f"  Förklaring: {explanation}")


# =============================================================================
# SAMMANFATTNING
# =============================================================================

print("\n" + "=" * 70)
print("SAMMANFATTNING")
print("=" * 70)

summary = """
HÖGRE ORDNINGENS FUNKTIONER:
  • Funktioner som tar andra funktioner som parametrar
  • count() är en högre ordningens funktion
  • Tar en lista och en predikatfunktion som parameter
  • Returnerar antal element som uppfyller predikatet

PREDIKATFUNKTIONER:
  • Funktioner som returnerar True eller False
  • Används för att testa villkor på element
  • Exempel: is_number(), is_positive()

LAMBDA-UTTRYCK:
  • Anonyma funktioner (funktioner utan namn)
  • Syntax: lambda parametrar: uttryck
  • Perfekt för enkla, engångsfunktioner
  • Kan användas direkt som argument till högre ordningens funktioner
  
EXEMPEL PÅ LAMBDA:
  • lambda x: x == "a"           → Testar om x är "a"
  • lambda x: len(x) == 2        → Testar om längden är 2
  • lambda x: x % 3 == 0         → Testar om x är delbart med 3
  • lambda x: x > 0 and x < 10   → Testar om x är mellan 0 och 10

FUNKTIONELL PROGRAMMERING:
  • Undvik sidoeffekter
  • Använd rena funktioner
  • Funktioner som värden (first-class functions)
  • Högre ordningens funktioner för abstraktion
"""

print(summary)

# =============================================================================
# KOMPLETT LÖSNING - Alla svar på ett ställe
# =============================================================================

print("=" * 70)
print("KOMPLETTA SVAR PÅ UPPGIFTERNA")
print("=" * 70)

print("\nUPPGIFT: Högre ordningens funktioner")
print("Svar:")
print(f"  count([17, 3.14, 'banan'], is_number) = {count([17, 3.14, 'banan'], is_number)}")
print(f"  count([1, -1, 45.3, 4711, -273.15], is_positive) = {count([1, -1, 45.3, 4711, -273.15], is_positive)}")

print("\nUPPGIFT: Lambda-uttryck")
print("Svar:")
print(f"  count(['a', 'B', 'c', 'a', 'd'], lambda x: x == 'a') = {count(['a', 'B', 'c', 'a', 'd'], lambda x: x == 'a')}")
print(f"  count([['a'], [1, 2], ['b', 'c']], lambda x: isinstance(x, list) and len(x) == 2) = {count([['a'], [1, 2], ['b', 'c']], lambda x: isinstance(x, list) and len(x) == 2)}")
print(f"  count([1, 2, 3, 4, 5, 6, 9], lambda x: x % 3 == 0) = {count([1, 2, 3, 4, 5, 6, 9], lambda x: x % 3 == 0)}")

print("\n" + "=" * 70)
print("ALLA UPPGIFTER SLUTFÖRDA!")
print("=" * 70)