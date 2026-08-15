
# encoding: iso-8859-1

# -----------------------------------------------------------------------------
#  Datortentamen i kursen TDDD64 Programmering i Python
#  2012-12-18
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#  Uppgift 1
# -----------------------------------------------------------------------------

def echo(str):
	half = len(str) // 2
	quarter = len(str) // 4
	return str + " " + str[-half:] + " " + str[-quarter:]

def initials(name):
	result = name[0]
	previous = ""
	for char in name[1:]:
		if previous == " ":
			result += char
		previous = char
	return result

# -----------------------------------------------------------------------------
#  Uppgift 2
# -----------------------------------------------------------------------------

def add(x, y):
    if x == 'infinity' or y == 'infinity':
        return 'infinity'
    else:
        return x + y

def add_list_r(seq):
    if not seq:
        return 0
    else:
        return add(seq[0], add_list_r(seq[1:]))

def add_list_i(seq):
    res = 0
    for e in seq:
        res = add(res, e)
    return res

# -----------------------------------------------------------------------------
#  Uppgift 3
# -----------------------------------------------------------------------------

def add_for_each(seq, fn):
    if not seq:
        return 0
    else:
        return fn(seq[0]) + add_for_each(seq[1:], fn)

def average_max(seq):
    return add_for_each(seq, max) / len(seq)

# -----------------------------------------------------------------------------
#  Uppgift 4
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

# -----------------------------------------------------------------------------
#  Uppgift 5
# -----------------------------------------------------------------------------

def expert(db):
    node = 1
    content = []
    while True:
        content = db[node]
        if isinstance(content, str):
            print("Jag tror att det är {}.".format(content))
            break
        print(content[0])
        for i in range(len(content)-1):
            print("  {}. {}".format(i+1, content[i+1][0]))
        while True:
            answer = input("> ")
            j = int(answer)
            if 1 <= j <= len(content)-1:
                break
            else:
                print("Felaktigt alternativ! Försök igen!")
        node = content[j][1]

# -----------------------------------------------------------------------------
#  Uppgift 6
# -----------------------------------------------------------------------------

def count_r(seq):
	def count(seq, last, c):
		if not seq:
			if c > 0:
				return [(last, c)]
			else:
				return []
		elif seq[0] == last:
			return count(seq[1:], last, c+1)
		else:
			return [(last, c)] + count(seq[1:], seq[0], 1)
	return count(seq, seq[0], 0)
	
def count_i(seq):
	res = []
	last = seq[0]
	c = 0
	for e in seq:
		if e == last:
			c += 1
		else:
			res.append((last, c))
			last = e
			c = 1
	if c > 0:
		res.append((last, c))
	return res
