"""
TDDE23 Seminarium 4 - Experimentering Solutions
All exercises in executable Python code
"""

# =============================================================================
# UPPGIFT: LISTBYGGARE
# =============================================================================

print("=" * 70)
print("LISTBYGGARE")
print("=" * 70)

# 1. Givet en lista med tal, bygg en ny lista av alla icke-negativa tal
print("\n1. Icke-negativa tal:")
numbers = [1, -1, 45.3, 4711, -273.15]
non_negative = [x for x in numbers if x >= 0]
print(f"Input:  {numbers}")
print(f"Output: {non_negative}")

# 2. Givet en lista med strängar, bygg en ny lista av teckenkoden 
#    för första bokstaven i varje sträng
print("\n2. Teckenkoder för första bokstaven:")
words = ["Apa", "Banan", "Citron"]
char_codes = [ord(word[0]) for word in words]
print(f"Input:  {words}")
print(f"Output: {char_codes}")

# 3. Bygg en lista av alla näst minsta tal i underlistorna i en given lista
print("\n3. Näst minsta tal i underlistor:")
nested_lists = [[17, 4, 8], [9, 14, 2, 7], [33, 14]]
second_smallest = [sorted(sublist)[1] for sublist in nested_lists]
print(f"Input:  {nested_lists}")
print(f"Output: {second_smallest}")

# 4. Bygg en lista av strängar som endast innehåller 'a' i given lista 
#    men byt ut alla 'a':n mot '*'
print("\n4. Strängar med 'a', ersätt med '*':")
fruits = ['apelsin', 'banan', 'citron']
filtered_replaced = [word.replace('a', '*') for word in fruits if 'a' in word]
print(f"Input:  {fruits}")
print(f"Output: {filtered_replaced}")

# 5. Skapa en lista med alla tal mellan 0 och 100 som är delbara med 3 
#    eller 5 men ej delbara med 15
print("\n5. Tal 0-100 delbara med 3 eller 5, men ej 15:")
special_numbers = [x for x in range(101) if (x % 3 == 0 or x % 5 == 0) and x % 15 != 0]
print(f"Output: {special_numbers}")
print(f"Antal tal: {len(special_numbers)}")

# 6. Skapa en 5x5 identitetsmatris
print("\n6. 5x5 Identitetsmatris:")
identity_matrix = [[1 if i == j else 0 for j in range(5)] for i in range(5)]
print("Output:")
for row in identity_matrix:
    print(" ".join(str(x) for x in row))


# =============================================================================
# UPPGIFT: GIT (Endast dokumentation i kommentarer)
# =============================================================================

print("\n" + "=" * 70)
print("GIT OPERATIONS (Dokumentation)")
print("=" * 70)

git_operations = """
1. Skapa en commit som ångrar en tidigare commit:
   git revert <commit-hash>

2. Ångra en commit som inte har pushats:
   git reset --soft HEAD~1   # Behåll ändringarna
   git reset --hard HEAD~1   # Ta bort ändringarna helt

3. Ändra commit-meddelandet eller lägg till fler ändringar:
   git commit --amend -m "Nytt meddelande"
   git add <files>
   git commit --amend --no-edit

4. Ångra git add:
   git reset              # Ångra alla filer
   git reset <filename>   # Ångra specifik fil

5. Ta bort alla ändringar sedan senaste committen:
   git checkout .         # Gammal syntax
   git restore .          # Ny syntax
   git reset --hard HEAD  # Även staged ändringar

6. Spara undan och återställa ändringar:
   git stash             # Spara undan
   git stash list        # Lista sparade
   git stash pop         # Återställ och ta bort
   git stash apply       # Återställ utan att ta bort

7. Se ändringarna från 3 commits sedan:
   git show HEAD~3       # Se ändringar i specifik commit
   git diff HEAD~3 HEAD  # Se diff mellan commits
   git log -1 HEAD~3     # Se commit-information
"""

print(git_operations)


# =============================================================================
# UPPGIFT: PROGRAMUTVECKLINGSPROCESSEN - Peters Golfresultat
# =============================================================================

print("=" * 70)
print("PROGRAMUTVECKLINGSPROCESSEN - Peters Golfresultat")
print("=" * 70)

def initialize_results():
    """
    Skapa en tom resultatlista
    
    Returns:
        list: En tom lista för att lagra resultat
    """
    return []


def add_result(results, distance):
    """
    Lägg till ett enskilt resultat och sortera listan
    
    Args:
        results (list): Lista med befintliga resultat
        distance (float/int): Avståndet i meter
    
    Returns:
        list: Den uppdaterade, sorterade listan
    """
    results.append(distance)
    results.sort()
    return results


def add_multiple_results(results, distances):
    """
    Lägg till flera resultat samtidigt och sortera listan
    
    Args:
        results (list): Lista med befintliga resultat
        distances (list): En lista av tal som ska läggas till
    
    Returns:
        list: Den uppdaterade, sorterade listan
    """
    results.extend(distances)
    results.sort()
    return results


def get_results(results):
    """
    Hämta alla resultat
    
    Args:
        results (list): Listan med resultat
    
    Returns:
        list: En kopia av den sorterade listan
    """
    return results.copy()


# Demonstration av Peters golfresultatsystem
print("\nDemonstration av golfresultatsystemet:")
print("-" * 70)

# Initialisera systemet
results = initialize_results()
print(f"Initialiserad lista: {results}")

# Lägg till enskilda resultat
results = add_result(results, 245.5)
print(f"Efter att ha lagt till 245.5: {results}")

results = add_result(results, 198.3)
print(f"Efter att ha lagt till 198.3: {results}")

# Lägg till flera resultat samtidigt
results = add_multiple_results(results, [267.1, 203.4, 189.2])
print(f"Efter att ha lagt till [267.1, 203.4, 189.2]: {results}")

# Hämta resultat
final_results = get_results(results)
print(f"\nSlutliga resultat: {final_results}")
print(f"Antal slag: {len(final_results)}")
print(f"Bästa slag: {min(final_results)} meter")
print(f"Sämsta slag: {max(final_results)} meter")
print(f"Genomsnitt: {sum(final_results) / len(final_results):.2f} meter")


# =============================================================================
# BONUS: Effektivare implementation med bisect (för stora dataset)
# =============================================================================

print("\n" + "=" * 70)
print("BONUS: Effektivare implementation med bisect")
print("=" * 70)

import bisect

def add_result_efficient(results, distance):
    """
    Effektivare version som använder bisect för att hitta rätt position
    Komplexitet: O(log n) för sökning + O(n) för insättning
    
    Args:
        results (list): Sorterad lista med befintliga resultat
        distance (float/int): Avståndet i meter
    
    Returns:
        list: Den uppdaterade, sorterade listan
    """
    bisect.insort(results, distance)
    return results


# Demonstration
print("\nDemonstration med bisect:")
efficient_results = []
efficient_results = add_result_efficient(efficient_results, 245.5)
efficient_results = add_result_efficient(efficient_results, 198.3)
efficient_results = add_result_efficient(efficient_results, 267.1)
efficient_results = add_result_efficient(efficient_results, 203.4)
efficient_results = add_result_efficient(efficient_results, 189.2)
print(f"Resultat: {efficient_results}")

print("\n" + "=" * 70)
print("ALLA UPPGIFTER SLUTFÖRDA!")
print("=" * 70)