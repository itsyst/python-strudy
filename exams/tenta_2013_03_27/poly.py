# Functions for polynomial handling

def plus_poly(p1, p2):
  "polynomial x polynomial -> polynomial"
  if is_same_variable(variable(p1), variable(p2)):
    return make_polynomial(variable(p1), plus_terms(termlist(p1), termlist(p2)))
  else:
    raise Error("Polynomials not in same variable!")
    
def plus_terms(l1, l2):
  "termlist x termlist -> termlist"
  if is_empty_termlist(l1):
    return l2
  elif is_empty_termlist(l2):
    return l1
  else:
    t1 = first_term(l1)
    t2 = first_term(l2)
    if integer(order(t1)) > integer(order(t2)):
      return insert_term(t1, plus_terms(rest_terms(l1), l2))
    elif integer(order(t1)) < integer(order(t2)):
      return insert_term(t2, plus_terms(l1, rest_terms(l2)))
    else:
      return insert_term(make_term(order(t1), add(coeff(t1), coeff(t2))),
                         plus_terms(rest_terms(l1), rest_terms(l2)))
                         
def print_poly(poly):
  "polynomial ->"
  tlist = termlist(poly)
  var = variable(poly)
  first = True
  while not is_empty_termlist(tlist):
    term = first_term(tlist)
    o = order(term)
    c = integer(coeff(term))
    if not first and c > 0:
      print("+", end='')
    first = False
    if o == 0:
      print("{}".format(c), end='')
    elif o == 1:
      print("{}{}".format(c, var), end='')
    else:
      print("{}{}^{}".format(integer(coeff(term)), var, order(term)), end='')
    tlist = rest_terms(tlist)
  print()
  
# Primitives fort the termlist datatype

def empty_termlist():
  "-> termlist"
  return []
  
def insert_term(term, tlist):
  "term x termlist -> termlist"
  return [term] + tlist
  
def first_term(tlist):
  "termlist -> term"
  return tlist[0]
  
def rest_terms(tlist):
  "termlist -> termlist"
  return tlist[1:]
  
def is_empty_termlist(tlist):
  "termlist -> truth value"
  return not tlist
  
# Primitives for the term datatype

def make_term(order, coeff):
  "order x coefficient -> term"
  return [order, coeff]
  
def coeff(term):
  "term -> coefficient"
  return term[1]
  
def order(term):
  "term -> order"
  return term[0]
    
# Primitives for the polynomial datatype

def make_polynomial(var, tlist):
  "variable x termlist -> polynomial"
  return [var, tlist]
  
def termlist(poly):
  "polynomial -> termlist"
  return poly[1]
  
def variable(poly):
  "polynomial -> variable"
  return poly[0]

# Primitive functions for the variable datatype

def is_same_variable(v1, v2):
  "variable x variable -> truth value"
  return v1 == v2

# Primitive functions for the coefficient datatype

def integer(coeff):
  "coefficient -> integer"
  return coeff
  
def make_coeff(int):
  "integer -> coefficient"
  return int
  
def add(x, y):
  "coefficient x coefficient -> coefficient"
  return make_coeff(integer(x) + integer(y))
  
# Tests

tlist = empty_termlist()
tlist = insert_term(make_term(2, make_coeff(5)), tlist)
tlist = insert_term(make_term(1, make_coeff(3)), tlist)
tlist = insert_term(make_term(0, make_coeff(-2)), tlist)
p1 = make_polynomial('x', tlist)

tlist = empty_termlist()
tlist = insert_term(make_term(3, make_coeff(3)), tlist)
tlist = insert_term(make_term(1, make_coeff(4)), tlist)
tlist = insert_term(make_term(0, make_coeff(6)), tlist)
p2 = make_polynomial('x', tlist)

