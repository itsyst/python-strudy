"""
Lecture: Python Data Structures
Lists, Tuples, Sets, Dictionaries, Generators, map/filter, comprehension
"""

from sys import getsizeof
from collections import deque
from array import array

print("=" * 60)
print("LISTS")
print("=" * 60)

chars = ["o", "z", "a", "b", "c"]
matrix = [[0, 1], [2, 3], [4, 5]]
zeros = [0] * 6
combined = zeros + chars + [(2, 3, 4)]
print("Combined:", combined)

numbers = list(range(10))
print("Numbers:", numbers)

word = list("Hello world")
print("Word:", word, f"len={len(word)}")

# Unpacking
one, *other, last = matrix
print("Unpack:", one, other, last)

for index, row in enumerate(matrix):
    print(f"  [{index}]", row)

# Add / Remove
matrix.append([6, 7])
matrix.insert(0, [99])
print("After add:", matrix)
matrix.remove([99])
matrix.pop(0)
print("After remove:", matrix)

print("\n" + "=" * 60)
print("SORTING & LAMBDA")
print("=" * 60)

products = [
    ("Fruits", 30),
    ("Books", 10),
    ("Flowers", 5),
    ("Pens", 10),
    ("Pens", 2),
]

products.sort(key=lambda p: p[1])
print("Sorted by price:", products)

products.sort(key=lambda p: (p[1], p[0]), reverse=True)
print("Sorted by price then name:", products)

print("\n" + "=" * 60)
print("MAP / FILTER / COMPREHENSION")
print("=" * 60)

prices = list(map(lambda p: p[1], products))
print("Prices:", prices)

expensive = list(filter(lambda p: p[1] >= 20, products))
print("Expensive (>=20):", expensive)

names = [p[0] for p in products]
cheap = [p for p in products if p[1] < 20]
print("Names:", names)
print("Cheap:", cheap)

print("\n" + "=" * 60)
print("ZIP")
print("=" * 60)

list1 = [1, 2, 3]
list2 = [10, 20, 30]
list3 = [100, 200, 300]
print(list(zip("abc", list1, list2, list3)))

print("\n" + "=" * 60)
print("STACK (LIFO)")
print("=" * 60)

stack = []
stack.append("a")
stack.append("b")
stack.append("c")
print("Stack:", stack)
print("Pop:", stack.pop())
print("After pop:", stack)

print("\n" + "=" * 60)
print("QUEUE (FIFO)")
print("=" * 60)

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue:", queue)
print("Popleft:", queue.popleft())
print("After:", queue)

print("\n" + "=" * 60)
print("TUPLES")
print("=" * 60)

point = (3, 4) + (5, 6)
print("Point:", point)
x, y, *rest = point
print(f"x={x}, y={y}, rest={rest}")

print("\n" + "=" * 60)
print("SETS")
print("=" * 60)

nums = [1, 2, 2, 2, 4, 5, 6, 7, 7, 0, 1]
first = set(nums)
second = {0, 11, 14, 7}
print("Union:", first | second)
print("Intersection:", first & second)
print("Difference:", first - second)
print("Symmetric diff:", first ^ second)

print("\n" + "=" * 60)
print("DICTIONARIES")
print("=" * 60)

programs = dict(x=1, y=2)
programs["z"] = 30
print("Keys:", programs.keys())
print("Values:", programs.values())
for key, value in programs.items():
    print(f"  {key}: {value}")

print("Dict comprehension:", {x: x * 2 for x in range(5)})

print("\n" + "=" * 60)
print("GENERATORS")
print("=" * 60)

gen = (x * 2 for x in range(1000))
print("Generator size:", getsizeof(gen), "bytes")
print("List size:", getsizeof([x for x in range(1000)]), "bytes")

print("\nDone.")
