from pprint import pprint

sentence = "This is a common interview question"


char_frequency = dict()

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

max_freq = max(char_frequency.values())
pprint(char_frequency, width=1)
items = [key for key, value in char_frequency.items() if value == max_freq]
print(items)


char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)
print(char_frequency_sorted[0])
