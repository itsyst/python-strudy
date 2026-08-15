
# -----------------------------------------------------------------------------
#  Datortentamen i kursen TDDD73 Funktionell och imperativ programmering i Python
#  2015-01-13 14-19
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#  Uppgift 1
# -----------------------------------------------------------------------------

def split(s, l):
  res = []
  while len(s)>0:
    res.append(s[0:l])
    s = s[l:]
  return res

def column(s, l):
  res = []
  separators = ' .,:;!?'
  i = l-1
  while True:
    if len(s)<=l:
      res.append(s)
      break
    elif i<=0:
      res.append(s[0:l])
      s = s[l:]
      i = l-1
    elif s[i] in separators:
      res.append(s[0:i+1])
      s = s[i+1:]
      i = l-1
    else:
      i -= 1
  return res

# -----------------------------------------------------------------------------
#  Uppgift 2
# -----------------------------------------------------------------------------

def find_r(seq, e):
  def find_help(seq, e, i):
    if not seq:
      return -1
    elif seq[0] == e:
      return i
    else:
      return find_help(seq[1:], e, i+1)
  return find_help(seq, e, 0)
  
def find_i(seq, e):
  for i in range(len(seq)):
    if seq[i] == e:
      return i
  return -1

# -----------------------------------------------------------------------------
#  Uppgift 3
# -----------------------------------------------------------------------------

def insert_after(seq, fn, e):
  if not seq:
    return []
  elif fn(seq[0]):
    return [seq[0], e] + insert_after(seq[1:], fn, e)
  else:
    return [seq[0]] + insert_after(seq[1:], fn, e)

def mark_interval(seq, a, b, e):
  return insert_after(seq, (lambda x: isinstance(x, int) and a <= x <= b), e)

# -----------------------------------------------------------------------------
#  Uppgift 4
# -----------------------------------------------------------------------------

def contain_i(small,large):
  for e in large:
    if small and e == small[0]:
      small = small[1:]
  return not small
  
def contain_r(small,large):
  if not large:
    return not small
  elif not small:
    return True
  elif large[0] == small[0]:
    return contain_r(small[1:], large[1:])
  else:
    return contain_r(small, large[1:])

# -----------------------------------------------------------------------------
#  Uppgift 5
# -----------------------------------------------------------------------------

t = {'a': (('b', 4), ('c', 7), ('d', 3)),
     'b': (('e', 2), ('f', 9)),
     'c': (('g', 5), ),
     'd': (('h', 4), ('i', 3)),
     'e': (),
     'f': (),
     'g': (('j', 2), ('k', 1), ('l', 8)),
     'h': (),
     'i': (('m', 6), ),
     'j': (),
     'k': (),
     'l': (),
     'm': ()}
        
def distance(tree, start, goal):
  def walk(pos, d):
    if pos == goal:
      return d
    else:
      children = tree[pos]
      if not children:
        return -1
      else:
        for pair in children:
          res = walk(pair[0], d+pair[1])
          if res > 0:
            return res
        return -1
  return walk(start, 0)

# -----------------------------------------------------------------------------
#  Uppgift 6
# -----------------------------------------------------------------------------

# No solutions will be presented.
