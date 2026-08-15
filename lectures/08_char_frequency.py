"""
Lecture: Character Frequency
"""

from pprint import pprint

sentence = "This is a common interview question"

char_frequency = {}
for char in sentence:
    char_frequency[char] = char_frequency.get(char, 0) + 1

print("Frequency map:")
pprint(char_frequency, width=1)

max_freq = max(char_frequency.values())
most_common = [k for k, v in char_frequency.items() if v == max_freq]
print("Most frequent char(s):", most_common)

sorted_freq = sorted(char_frequency.items(), key=lambda kv: kv[1], reverse=True)
print("Top item:", sorted_freq[0])
