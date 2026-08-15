# encoding: iso-8859-1

# --------------------------------------------------------------------------
#  Primitives for the 'Candy' data type
# --------------------------------------------------------------------------

# 'Candy' is our basic data type containing the name of the candy, the
# price and the weight. 

def make_candy(name, price, weight):
  "string x integer x integer -> candy"
  return ['CANDY', name, price, weight]
  
def is_candy(obj):
  "object -> truth value"
  return isinstance(obj, list) and obj[0] == 'CANDY'
  
def candy_name(candy):
  "candy -> string"
  return candy[1]
  
def candy_price(candy):
  "candy -> integer"
  return candy[2]
  
def candy_weight(candy):
  "candy -> integer"
  return candy[3]
  
def print_candy(candy):
  "candy ->"
  print(candy_name(candy) + " " + str(candy_price(candy)))
  
# --------------------------------------------------------------------------
#  Primitives for the 'Wishlist' data type
# --------------------------------------------------------------------------

# 'Wishlist' is a sequential datatype which is basically a list of objects
# of the 'Candy' data type.

# Create an empty wishlist

def make_wishlist():
  "-> wishlist"
  return "ERROR"

# Check if an object is a wishlist

def is_wishlist(obj):
  "object -> truth value"
  return "ERROR"

# Check if a wishlist is empty

def empty_wishlist(wishlist):
  "wishlist -> truth value"
  return "ERROR"

# Extend an existing wishlist with one candy object
  
def extend_wishlist(wishlist, candy):
  "wishlist x candy -> wishlist"
  return "ERROR"

# Get the fist candy object
  
def first_candy(wishlist):
  "wishlist -> candy"
  return "ERROR"
  
# Get the rest of a wishlist, without the first candy object

def rest_wishlist(wishlist):
  "wishlist -> wishlist"
  return "ERROR"
  
# Check if a candy is contained in a wishlist

def in_wishlist(candy, wishlist):
  "candy x wishlist -> truth value"
  return "ERROR"

# Give a nice printout of a wishlist
  
def print_wishlist(wishlist):
  "wishlist ->"
  print("ERROR")
  
# --------------------------------------------------------------------------
#  Working with wishlists
# --------------------------------------------------------------------------

# These are some auxilliary functions for working with wishlists.

# Create all possible wishlists from a set of wishlists

def possible_wishlists(wishlist):
  "wishlist -> list of wishlists"
  return "ERROR"

# Check if a wishlist is a subset of another wishlist

def wishlist_subset(small, large):
  "wishlist x wishlist -> truth value"
  for candy in small:
    if not in_wishlist(candy, large):
      return False
  return True

# Calculate the total cost of a wishlist

def total_cost(wishlist):
  "wishlist -> integer"
  if empty_wishlist(wishlist):
    return 0
  else:
    return candy_price(first_candy(wishlist)) + total_cost(rest_wishlist(wishlist))
    
# --------------------------------------------------------------------------
#  Primitives for the 'Candylist' data type
# --------------------------------------------------------------------------

# 'Candylist' is a pair of objects, the first one being an integer denoting
# the total cost and the second one being a wishlist. We don't have a full
# set of primitives, and we mostly work with lists of 'Candylist' objects.

# Create candylists from a wishlist

def make_candylists(wishlist):
  result = []
  for wishlist in possible_wishlists(wishlist):
    result += [[total_cost(wishlist), wishlist]]
  return result
    
# Selectors for candylists

def candylist_price(candylist):
  return candylist[0]
  
def candylist_wishlist(candylist):
  return candylist[1]
  
# --------------------------------------------------------------------------
#  Working with candylists
# --------------------------------------------------------------------------

# Removes too expensive candylists

def filter_expensive_candylists(candylists, highest_price):
  if not candylists:
    return []
  elif candylist_price(candylists[0]) <= highest_price:
    return [candylists[0]] + filter_expensive_candylists(candylists[1:], highest_price)
  else:
    return filter_expensive_candylists(candylists[1:], highest_price)
    
# Checks if a candylist is redundant, i.e. if it is a subset of
# another candylist

def redundant_candylist(candylist, candylists):
  "candylist x list of candylists -> truth value"
  if not candylists:
    return False
  elif wishlist_subset(candylist_wishlist(candylist), candylist_wishlist(candylists[0])):
    return True
  else:
    return redundant_candylist(candylists, candylists[1:])

# Removes redundant candylists

def filter_unnecessary_candylists(candylists):
  if not candylists:
    return []
  elif redundant_candylist(candylists[0], candylists[1:]):
    return filter_unnecessary_candylists(candylists[1:])
  else:
    return [candylists[0]] + filter_unnecessary_candylists(candylists[1:])

# Print all candylists

def print_candylists(candylists):
  "list of candylists ->"
  for candylist in candylists:
    print('-' * 40)
    print_wishlist(candylist_wishlist(candylist))
    print('*** TOTAL ' + str(candylist_price(candylist)))
    
# This is the main function

def egginator(wishlist, highest_price):
  "wishlist x integer -> list of candylists"
  result = make_candylists(wishlist)
  result = filter_expensive_candylists(result, highest_price)
  result = filter_unnecessary_candylists(result)
  return result

# --------------------------------------------------------------------------
#  Testing
# --------------------------------------------------------------------------

def make_testlist():
  w = make_wishlist()
  w = extend_wishlist(w, make_candy('Aladdin', 79, 300))
  w = extend_wishlist(w, make_candy('Lyxchoklad', 139, 350))
  w = extend_wishlist(w, make_candy('Storpaket', 189, 500))
  return w

#print_candylists(egginator(make_testlist(), 220))
