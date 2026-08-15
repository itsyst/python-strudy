
# -----------------------------------------------------------------------------
#  TDDD73 Funktionell och imperativ programmering i Python
#  2015-04-10
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#  Uppgift 1
# -----------------------------------------------------------------------------

def print_calendar(days, start):
    i = 1 - start
    c = 0
    while i <= days:
        if i <= 0:
            print('   ', end='')
        else:
            print(' {:2}'.format(i), end='')
        i += 1
        c += 1
        if c % 7 == 0:
            print()
    if c % 7 != 0:
        print()

# -----------------------------------------------------------------------------
#  Uppgift 2
# -----------------------------------------------------------------------------

def merge_r(seq1, seq2):
	if not seq1:
		return seq2
	elif not seq2:
		return seq1
	elif seq1[0] < seq2[0]:
		return [seq1[0]] + merge_r(seq1[1:], seq2)
	else:
		return [seq2[0]] + merge_r(seq1, seq2[1:])
		
def merge_i(seq1, seq2):
	res = []
	while seq1 and seq2:
		if seq1[0] < seq2[0]:
			res.append(seq1[0])
			seq1 = seq1[1:]
		else:
			res.append(seq2[0])
			seq2 = seq2[1:]
	res = res + seq1 + seq2
	return res

# -----------------------------------------------------------------------------
#  Uppgift 3
# -----------------------------------------------------------------------------

def each_pair(seq, fn):
  if not seq[1:]:
    return []
  else:
    return [fn(seq[0], seq[1])] + each_pair(seq[1:], fn)
    
def combine_pairs(seq, fn_pair, fn_combine, base):
  if not seq[1:]:
    return base
  else:
    return fn_combine(fn_pair(seq[0], seq[1]), combine_pairs(seq[1:], fn_pair, fn_combine, base))

# -----------------------------------------------------------------------------
#  Uppgift 4
# -----------------------------------------------------------------------------

# Notering 2022-01-02, av nuvarande examinator (som inte skapade denna
# tenta eller lösningsförslagen):
# 
# Detta lösningsförslag använder remove() på ett sätt som modifierar
# indata.  Denna del är alltså felaktig och man skulle behöva
# t.ex. göra en kopia av seq2 eller undvika borttagningen på annat
# sätt.
#
# Dessutom skulle man kunna tolka remove() som en metod som behandlar
# hela listor.  Tanken var troligen att remove() tar bort *ett
# element* och därför var tillåten, men detta kunde i så fall ha varit
# tydligare i tentan (alternativt kunde lösningsförslaget ha tagit
# bort element på andra sätt).


def is_anagram_r(seq1, seq2):
	if not seq1:
		return not seq2
	elif seq1[0] in seq2:
		seq2.remove(seq1[0])
		return is_anagram_r(seq1[1:], seq2)
	else:
		return False
		
def is_anagram_i(seq1, seq2):
	for e in seq1:
		if e in seq2:
			seq2.remove(e)
		else:
			return False
	return not seq2

# -----------------------------------------------------------------------------
#  Uppgift 5
# -----------------------------------------------------------------------------

svensson = ['Erik', ['Olle', ['Eva', 'Karin', 'Anna'],
                             ['Lars', 'Maria'],
                             ['PÃ¤r', 'Sofia']],
                    'Lisa',
                    ['Stina', ['Gunnar', 'Lasse'],
                              'Lennart']]

def ancestors(person, tree):
    if isinstance(tree, str):
        if person == tree:
            return [person]
        else:
            return []
    elif person == tree[0]:
        return [person]
    else:
        for child_tree in tree[1:]:
            result = ancestors(person, child_tree)
            if result:
                return [tree[0]] + result
        return []

# -----------------------------------------------------------------------------
#  Uppgift 6
# -----------------------------------------------------------------------------

def make_ring(elements):
    "list of elements -> ring"
    return ('RING', elements)
  
def is_ring(object):
    "any object -> truth value"
    return isinstance(object, tuple) and len(object) == 2 and object[0] == 'RING'
    
def top(ring):
    "ring -> element"
    return ring[1][0]
    
def left_rotate(ring):
    "ring -> ring"
    elements = ring[1]
    rotated = elements[1:] + [elements[0]]
    return ('RING', rotated)
    
def right_rotate(ring):
    "ring -> ring"
    elements = ring[1]
    rotated = [elements[-1]] + elements[:1]
    return ('RING', rotated)
    
def left_rotate_in(ring):
    "ring ->"
    elements = ring[1]
    first = elements.pop(0)
    elements.append(first)
    
def right_rotate_in(ring):
    "ring ->"
    elements = ring[1]
    last = elements.pop()
    elements.insert(0, last)
