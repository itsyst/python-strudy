#%%
"""
          Datortentamen i kursen TDDD64 Programmering i Python

                     tisdag 18 december kl 8-13

"""
"""-----------------------------------------------------------------------------
 Uppgift 1
-----------------------------------------------------------------------------"""

#*** Deluppgift 1A (2,5p) ***

def echo(string: str):
    lngth = len(string)
    return string + " " + string[round(lngth/2):] + " " + string[lngth - int(lngth/4):]

#*** Deluppgift 1B (2,5p) ***

def initials(name: str):
    new = ""
    for ini in name.split(" "):
        new += ini[0]
    return new

"""-----------------------------------------------------------------------------
 Uppgift 2
-----------------------------------------------------------------------------"""
#Klarade extremt fult xxx

def add(val1, val2):
    if "infinity" in (val1, val2):
        return "infinity"
    return val1 + val2

def add_list_i(seq: list): #fixd
    summ = 0
    for val in seq:
        summ = add(summ, val)
    return summ

def add_list_r(seq: list): #fixd
    if not seq:
        return 0
    return add(seq[0], add_list_r(seq[1:]))

"""-----------------------------------------------------------------------------
 Uppgift 3
-----------------------------------------------------------------------------"""

#*** Deluppgift 3A (3p) ***

def add_for_each(seq: list, fn: "function") -> int:
    if not seq:
        return 0
    if isinstance(seq, list):
        return fn(seq[0]) + add_for_each(seq[1:], fn)
    return fn(seq[0])

#*** Deluppgift 3B (2p) ***

def average_max(seq: list) -> int:
    return add_for_each(seq, lambda val: max(val))/len(seq)

"""-----------------------------------------------------------------------------
 Uppgift 4
-----------------------------------------------------------------------------"""

def make_ring(seq: list) -> "ring":
    """make_ring : list of elements -> ring"""
    """Skapar och returnerar en ny ring från en lista med element där första
    elementet i listan är toppelement i ringen."""
    return seq

def is_ring(obj) -> bool:
    """Kontrollerar om det givna objektet är en ring."""
    return isinstance(obj, list)

def top(obj: "ring") -> "top_ring":
    """Returnerar toppelementet i ringen."""
    if is_ring(obj):
        return obj[0]

def left_rotate(ring) -> "ring":
    """Returnerar en ny ring genom att elementen roteras ett steg åt vänster."""
    if is_ring(ring):
        seq = ring[1:] + [ring[0]]
        return make_ring(seq)

def right_rotate(ring) -> "ring":
    """Returnerar en ny ring genom att elementen roteras ett steg åt höger."""
    if is_ring(ring):
        seq = [ring[-1]] + ring[:-1]
        return make_ring(seq)

def left_rotate_in(ring):
    """Roterar elementen i den aktuella ringen ett steg åt vänster. Inga
    nya objekt ska skapas eller returneras, utan ringen ska modifieras
    på plats."""
    if is_ring(ring):
        last = ring.pop(0)
        ring.append(last)

def right_rotate_in(ring):
    """Roterar elementen i den aktuella ringen ett steg åt höger. Inga
    nya objekt ska skapas eller returneras, utan ringen ska modifieras
    på plats."""
    if is_ring(ring):
        first = ring.pop(len(ring) - 1)
        ring.insert(0, first)
"""-----------------------------------------------------------------------------
 Uppgift 5
-----------------------------------------------------------------------------"""
animals = {
    1: ("Var lever djuret?", ("på land", 2), ("i vatten", 3), ("i luften", 4)),
    2: ("Hur många ben har djuret?", ("två", 5), ("fyra", 6), ("många", 7)),
    3: "en fisk",
    4: ("Ungefär hur stort är det?", ("litet", 8), ("stort", 9)),
    5: "en apa",
    6: ("Hur ser djuret ut utanpå?", ("taggar", 10), ("päls", 11)),
    7: "en insekt av något slag",
    8: ("Hur ser djuret ut?", ("grått", 12), ("rött bröst", 13), ("blå och gul", 14)),
    9: ("Hur beter sig djuret?", ("glidflyger", 15), ("hoar om natten", 16)),
    10: "en igelkott",
    11: ("Hur låter djuret?", ("miau", 17), ("vov", 18)),
    12: "en gråsparv",
    13: "en domherre",
    14: "en blåmes",
    15: "en örn",
    16: "en uggla",
    17: "en katt",
    18: "en hund"}

def expert(data):
    key = 1
    while True:
        values = data[key]
        if isinstance(values, tuple):
            for line_vals in enumerate(values):
                line = line_vals[1]
                if isinstance(line, tuple):
                    print(f"  {line_vals[0]}. {line[0]}")
                else:
                    print(line)
        else:
            print(f"Jag tror att det är {values}.")
            break
        choice = int(input())
        key = values[choice][1]

"""-----------------------------------------------------------------------------
 Uppgift 6
-----------------------------------------------------------------------------"""

def count_i(seq):
    result = []
    amount = 1
    prev = seq[0]
    for vals in enumerate(seq[1:]):
        val = vals[1]
        if val == prev:
            amount += 1
            if vals[0] == len(seq) - 2: #if last
                result.append((val, amount))
        else:
            result.append((prev, amount))
            amount = 1
            prev = val
    return result

def count_r(seq):
    def inner(seq, prev, amount):
        if not seq:
            if amount > 0:
                return [(prev, amount)]
            return []
            #if amount > 0
        if seq[0] == prev:
            return inner(seq[1:], prev, amount+1)
        else:
            return [((prev), amount)] + inner(seq[1:], seq[0], 1)
        
    return inner(seq[1:], seq[0], 1)
        

if __name__ == '__main__':
    assert echo("Korvbröd") == 'Korvbröd bröd öd'
    assert echo("Hejsan") == 'Hejsan san n'
    assert echo("Julgran") == 'Julgran ran n'

    assert initials("Kalle Anka") == "KA"
    assert initials("Per Anders Fogelström") == "PAF"

    assert add_list_i([1, 2, 3, 4]) == 10
    assert add_list_i([1, 2, 'infinity', 4]) == "infinity"

    assert add_for_each([1, 2, 3, 4], lambda x: x**2) == 30
    assert add_for_each([[1, 2, 3], [1], [1, 2, 3, 4]], lambda x: len(x)) == 8

    assert average_max([[12,13,15,11],[8,9,10],[5,7,6],[8,9,11,10],[3,5,5,2]]) == 9.6

    #
#%%
##abstrakt datatyp, högordning funktion etc..