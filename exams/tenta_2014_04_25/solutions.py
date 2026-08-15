# encoding: iso-8859-1

# -----------------------------------------------------------------------------
#  Datortentamen i kursen TDDD73 Funktionell och imperativ programmering i Python
#  2014-04-25
# -----------------------------------------------------------------------------

# Dessa lösningsförslag ger inte nödvändigtvis full poäng. De ska endast
# ses som möjliga lösningar till problemen i uppgifterna.

# -----------------------------------------------------------------------------
#  Uppgift 1
# -----------------------------------------------------------------------------

def replace(str, old, new):
    res = ''
    for c in str:
      if c in old:
        res += new
      else:
        res += c
    return res

def title(str):
  res = ""
  up = True
  for c in str:
    if up:
      res += c.upper()
      up = False
    else:
      res += c.lower()
    up = not c.isalpha()
  return res

# -----------------------------------------------------------------------------
#  Uppgift 2
# -----------------------------------------------------------------------------

def intersect_r(set1, set2):
    if not set1:
        return []
    elif set1[0] in set2:
        return [set1[0]] + intersect_r(set1[1:], set2)
    else:
        return intersect_r(set1[1:], set2)

def intersect_i(set1, set2):
    res = []
    for e in set1:
        if e in set2:
            res.append(e)
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

def interleave_r(seq1, seq2):
	if not seq1:
		return seq2
	elif not seq2:
		return seq2
	else:
		return [seq1[0], seq2[0]] + interleave_r(seq1[1:], seq2[1:])
		
def interleave_i(seq1, seq2):
	res = []
	while seq1 and seq2:
		res.append(seq1[0])
		res.append(seq2[0])
		seq1 = seq1[1:]
		seq2 = seq2[1:]
	res = res + seq1 + seq2
	return res
	
# -----------------------------------------------------------------------------
#  Uppgift 5
# -----------------------------------------------------------------------------

def bubble_sort(seq):
  for i in range(len(seq)-1):
    for j in range(len(seq)-i-1):
      if seq[j]>seq[j+1]:
        seq[j], seq[j+1] = seq[j+1], seq[j]
  return seq

# -----------------------------------------------------------------------------
#  Uppgift 6
# -----------------------------------------------------------------------------

def make_wishlist():
  "-> wishlist"
  return ['WISHLIST']

def is_wishlist(obj):
  "object -> truth value"
  return isinstance(obj, list) and obj[0] == 'WISHLIST'

def empty_wishlist(wishlist):
  "wishlist -> truth value"
  return not wishlist[1:]
  
def extend_wishlist(wishlist, candy):
  "wishlist x candy -> wishlist"
  return wishlist + [candy]
  
def first_candy(wishlist):
  "wishlist -> candy"
  return wishlist[1]
  
def rest_wishlist(wishlist):
  "wishlist -> wishlist"
  return ['WISHLIST'] + wishlist[2:]
  
def in_wishlist(candy, wishlist):
  "candy x wishlist -> truth value"
  for c in wishlist[1:]:
    if c == candy:
      return True
  return False
  
def print_wishlist(wishlist):
  "wishlist ->"
  for c in wishlist[1:]:
    print_candy(c)

# No solutions for second assignment will be presented.

