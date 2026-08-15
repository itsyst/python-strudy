
# -----------------------------------------------------------------------------
#  Datortentamen i kursen TDDD73 Funktionell och imperativ programmering i Python
#  2015-01-13 8-13
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#  Uppgift 1
# -----------------------------------------------------------------------------

# Count the number of characters in str1 that are similar to corresponding
# characters in str2, which has to be at least as long as str1.

def count_similar(str1, str2):
  count = 0
  for i in range(len(str1)):
    if str1[i] == str2[i]:
      count += 1
  return count

# Check if the shorter string is equal to a part of the longer string where
# one character is removed. The shorter string should be one character shorter
# than the longer one.

def check_alike(short, long):
  for i in range(len(long)):
    if short == long[0:i]+long[i+1:]:
      return True
  return False

# Check if two strings are 'close enough', i.e. either are of the same length
# with maximum one character differing, or one string equal to the other one
# with one character removed.

def close_enough(str1, str2):
  if len(str1) == len(str2):
    return count_similar(str1, str2) >= len(str1)-1
  elif len(str1) == len(str2)-1:
    return check_alike(str1, str2)
  elif len(str1)-1 == len(str2):
    return check_alike(str2, str1)
  else:
    return False

# -----------------------------------------------------------------------------
#  Uppgift 2
# -----------------------------------------------------------------------------

# Note: These solutions treat the first element differently, but it is ok
# to initiate the 'last' variable to some predefined value assumed never to
# be in the list, e.g. None, in order to avoid an if statement.

def uniq_r(seq):
  def uniq_help(seq, last):
    if not seq:
      return []
    elif seq[0] == last:
      return uniq_help(seq[1:], last)
    else:
      return [seq[0]] + uniq_help(seq[1:], seq[0])
  if not seq[1:]:
    return seq
  else:
    return [seq[0]] + uniq_help(seq[1:], seq[0])
  
def uniq_i(seq):
  if not seq[1:]:
    return seq
  else:
    res = [seq[0]]
    last = seq[0]
    for e in seq[1:]:
      if e != last:
        res.append(e)
        last = e
    return res

# -----------------------------------------------------------------------------
#  Uppgift 3
# -----------------------------------------------------------------------------

def gen_find(seq, fn, deep):
  if not seq:
    return False
  elif fn(seq[0]):
    return True
  elif deep and isinstance(seq[0], list):
    return gen_find(seq[0], fn, deep) or gen_find(seq[1:], fn, deep)
  else:
    return gen_find(seq[1:], fn, deep)

def where(seq, e):
  if gen_find(seq, (lambda x: x == e), False):
    return 'top'
  elif gen_find(seq, (lambda x: x == e), True):
    return 'deep'
  else:
    return 'no'

# -----------------------------------------------------------------------------
#  Uppgift 4
# -----------------------------------------------------------------------------

def combos(word):
  n = len(word)
  res = []
  for left in range(1,n-2+1):
    for right in range(1,n-left-1+1):
      res.append(word[:left]+word[-right:])
  return res

# -----------------------------------------------------------------------------
#  Uppgift 5
# -----------------------------------------------------------------------------

g = {'a':('d'), 'b':('a'), 'c':('b', 'd', 'f'), 'd':('h'), 'e':(),
     'f':('e', 'g'), 'g':('h'), 'h':('f', 'i'), 'i':('j'), 'j':('h')}
     
def locations(g, start, steps):
  if start not in g:
    return []
  elif steps <= 0:
    return [start]
  elif steps == 1:
    return list(g[start])
  else:
    res = []
    for d in g[start]:
      new = locations(g, d, steps-1)
      for e in new:
        if e not in res:
          res.append(e)
    return res

# -----------------------------------------------------------------------------
#  Uppgift 6
# -----------------------------------------------------------------------------

# No solutions will be presented.
