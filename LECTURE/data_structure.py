# ========================
# Looping over lists
# ========================
from sys import getsizeof
from collections import deque
from array import array
from typing import Generator

print("="*70)
chars = ["o", "z", "a", "b", "c"]
matrix = [[0, 1], [2, 3], [4, 5]]
zeros = [0] * 6
combined = zeros + chars + [(2, 3, 4)]
print("Looping:", combined)

numbers = list(range(10))
print("Looping:", numbers)

word = list("Hello world")
print("Looping:", word, f"len: {len(word)}'")

first = matrix[0]
second = matrix[1]
third = matrix[2]
first.extend([2, 2])
print("Looping:", first)

one, *other, last = matrix  # list unpacking
print("Looping:", one, last)
print("Looping:", other)

for index, numbers in enumerate(matrix):
    print("Looping:", index, numbers)
print()

# ========================
# Adding and Removing items
# ========================
print("="*70)
# Add
matrix.append([6, 7])
matrix.insert(0, [99])
print("Adding:", matrix)
# Remove
matrix.remove([99])  # remove the first occurrence
print("Remove:", matrix)
matrix.pop(0)  # remove only one item at the given index otherwise from the last
print("Remove:", matrix)
del matrix[0][0:2]  # delete a range of items
print("Remove:", matrix)
matrix.clear()  # truncate list or remove all items in the list.
print("Remove:", matrix)
print()

# ========================
#  Finding items
# ========================
print("="*70)
letters = [(1, "a"), (2, "b"), (3, "c"), (1, "a"),]
print("Finding:", letters[::-1])
print("Finding:", letters[-2])
print("Finding:", letters.count((1, "a")))
# first occurrence, here we have two identical value but we get only the first one.
print("Finding:", "Found!", letters.index((1, "f"))) if (
    1, "f") in letters else print("Finding:", "Not found!")
letters = [(x, "f") if x == 1 else (x, y) for (x, y) in letters]
print("Finding:", letters)
print()

# ========================
#  Sorting items
# ========================
print("="*70)
chars.sort(reverse=True)
letters.sort()
print("Sorting", chars)
print("Sorting", sorted(chars))

products = [
    ("Fruits", 30),
    ("Books", 10),
    ("Flowers", 5),
    ("Pens", 10),
    ("Pens", 2)
]

# Nothing happens, python does not know how to sort this list
print("Sorting", products, "Does not sort!")

print("Sorted", sorted(products))


def sort_product(product: tuple) -> tuple:
    return product[1]


products.sort(key=sort_product)  # type error, must add key=
print("Sorting", products, "Works!")
print()

# ============================
#  Lambda function/expression
# ============================
print("="*70)
products.sort(key=lambda product: product[0], reverse=True)
print("lambda:", products)

products.sort(key=lambda product: (product[1], product[0]), reverse=True)
print("lambda:", products)
print()

# ============================
#  Map function
# ============================
print("="*70)
products = [(product[0], product[1]*2) for product in products]
print("Map:", products, "lambda")

prices = []
for p in products:
    prices.append(p[1]*5)
print("Map:", prices)


product_prices = map(lambda p: p[1], products)
print("Map", product_prices)  # iterable
print("Map", [price for price in product_prices])
print()


# ============================
#  Filter function
# ============================
print("="*70)
# get only products greater than 60 kr
filtered = filter(lambda p: p[1] >= 60, products)
print("Filter:", [p for p in filtered])
print("Filter:", list(filter(lambda p: 20 <= p[1] <= 60, products)))
print("Filter:", list(filtered))
print()


# ============================
#  Comprehension lists
# ============================
print("="*70)
comp = [item[0] for item in products]
comp_check = [item[1] >= 20 for item in products]
comp_filtered = [item for item in products if item[1] < 20]
print("Comprehension:", comp)  # comprehension expression
print("Comprehension:", comp_check)
print("Comprehension:", comp_filtered)
print()

# ============================
#  Zip functions
# ============================
print("="*70)
list1 = [1, 2, 3]
list2 = [10, 20, 30]
list3 = [100, 200, 300]
zipped = zip("abc", list1, list2, list3)  # iterable
print("Zip:", list(zipped))
print()

# ============================
#  Stack
# ============================
print("="*70)
stack = []
stack.append("a")
stack.append("b")
stack.append("c")

print("Stack", stack)
print("Stack", stack.pop(), "pop")
print("Stack", stack.pop(), "pop")
print("Stack", stack.pop(), "pop")
print("Stack", stack)

try:
    print("Redirect:", stack[-1])
except IndexError:
    print("Redirect: /home")

print()

# ============================
#  Stack LIFO: Last In First Out
# ============================
print("="*70)
stack = []
if not stack:
    print("Stack: Empty")
stack.append("a")
stack.append("b")
stack.append("c")

print("Stack", stack)
print("Stack", stack.pop(), "pop")
print("Stack", stack.pop(), "pop")
print("Stack", stack.pop(), "pop")
print("Stack", stack)

try:
    print("Redirect:", stack[-1])
except IndexError:
    print("Redirect: /home")

print()

# ============================
#  Queue FIFO: First In First Out
# ============================
print("="*70)
queue = deque([])
if not queue:
    print("Queue: Empty")
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print("Queue:", queue)
print("Queue:", queue.popleft())
print("Queue:", queue)
print("Queue:", queue.pop())
print("Queue:", queue)
print()

# =======================================
#  Tuples (read only list, can not modify)
# =======================================
print("="*70)
point_1 = 1, 2
point_2 = ()
point_3 = (3, 4) + (5, 6)
print("Tuple:", type(point_1), type(point_2))
print("Tuple:", point_1 + point_2)
print("Tuple:", tuple([3, 4]))  # Convert list to a tuple
print("Tuple:", point_3, point_3[0])
x, y, *rest = point_3
print(f"Tuple: x: {x}, y: {y}, rest: {rest}")
if 6 in point_3:
    print("Tuple: exists")
print()

# =======================================
#  Swapping Variables
# =======================================
print("="*70)
x = 0
y = 11
print(f"Swap: x: {x}, y: {y}")
z = x
x = y
y = z
print(f"Swap: x: {x}, y: {y}")
# In python simply use:
x, y = y, x
print(f"Swap: x: {x}, y: {y}")
print()

# ====================================================================================
#  Arrays (dealing with large seq of numbers or encountering a performance problems )
# ====================================================================================
print("="*70)
numbers = array("i", [1, 2, 3])
print("Array", numbers)
numbers.append(6)
print("Array", numbers)
numbers.insert(0, 9)
print("Array", numbers)
print("Array", numbers.pop())
print("Array", numbers[0])
print("Array", numbers)


# =================================================
# Sets
# =================================================
print("="*70)
list_of_numbers = [1, 2, 2, 2, 2, 2, 4, 5, 6, 7, 7, 7, 0, 1]
print("Set: ", list_of_numbers)
first = set(list_of_numbers)
print("Set: ", first)
second = {0, 11, 14, 7}
print("Set: ", second)
second.add(15)
print("Set: ", second)
second.remove(11)
print("Set: ", second, f"len: {len(second)}")
print("Set: ", first | second)  # Union of two sets
print("Set: ", first & second)  # Intersection
print("Set: ", first - second)
print("Set: ", first ^ second)  # Symmetric difference
print()


# =================================================
# Dictionaries: key value pairs (map)
# =================================================
print("="*70)
courses = {"course1": 1, "course2": 2}
print("Dic:", courses)
programs = dict(x=1, y=2)
print("Dic:", programs["x"])
programs["x"] = 10
print("Dic:", programs["x"])
programs["z"] = 30
print("Dic:", programs.get("x"))
print("Dic:", programs.keys())
print("Dic:", programs.values())
del programs["z"]
for key, value in programs.items():
    print("Dic: ", key, value)
print()


# =================================================
# Dictionaries: Comprehension
# =================================================
print("="*70)
values = []
for x in range(5):
    values.append(x * 2)
print("Dic_Comp:", values)
print("List_Comp:", [x * 2 for x in range(5)])
print("Dic_Comp:", {x: x * 2 for x in range(5)})
print("Set_Comp:", set(x * 2 for x in {1, 2, 3, 3, 4, 4, 0}))
print()


# =================================================
# Generator
# =================================================
print("="*70)
gen1 = (x * 2 for x in {1, 2, 3, 3, 4, 4, 0})
gen2 = (x for x in range(1000))
list_values = [x for x in range(1000)]
print("Generator:", gen1)
print("Generator:", [x for x in gen1])
print("Generator:", getsizeof(gen1))  # bytes of memory
print("Generator:", getsizeof(gen2))  # bytes of memory
print("Generator:", getsizeof(list_values))  # bytes of memory
print()


# =================================================
# Unpacking operator
# =================================================
print("="*70)
list_numbers = [1, 2, 3]
print("Unpack:", list_numbers)
print("Unpack:", *list_numbers)  # Unpack the list
list_num = list(range(6))
print("Unpack:", *list_numbers)  # Unpack the list
unpacked_list = [*range(6), *"this is a string"]
print("Unpack:", *unpacked_list)  # Unpack the list
unpack_dic1 = dict(x=1, y=2)
unpack_dic2 = dict(z=3, t=4)
print("Unpack:", {**unpack_dic1, **unpack_dic2, "t":5})  # Unpack the list last value t will be used

print()
