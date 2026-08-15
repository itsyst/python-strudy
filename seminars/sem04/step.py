#  Moduler och import
import math
result = math.cos(math.pi)  # Returns -1.0

# Listbyggare (List comprehensions)
[i for i in range(0,10)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[i for i in range(0,10) if i % 2]  # [1, 3, 5, 7, 9] (odd numbers)
[[x for x in range(0,3)] for y in range(0,3)]  # [[0,1,2], [0,1,2], [0,1,2]]
[[x + y*3 for x in range(0,3)] for y in range(0,3)]  # [[0,1,2], [3,4,5], [6,7,8]]
[char for char in "banana" if char != "a"]  # ['b', 'n', 'n']

# Replace 'a' with '*' in strings containing 'a':
[s.replace('a', '*') for s in ['apelsin', 'banan', 'citron'] if 'a' in s]

# Numbers divisible by 3 or 5 but not by 15:
[i for i in range(0, 101) if (i % 3 == 0 or i % 5 == 0) and i % 15 != 0]

# 5x5 identity matrix:
[[1 if i == j else 0 for j in range(5)] for i in range(5)]