
''' 
Uppgift 2:

S = 'a', S, 'a' | 'b', S, 'b' | 'a' | 'b' | '' ;
'''

import random

def generate_S_recursive(depth=0, max_depth=3):
    """S = 'a', S, 'a' | 'b', S, 'b' | 'a' | 'b' | ''"""
    if depth >= max_depth:
        return random.choice(['a', 'b', ''])
    
    choice = random.choice([1, 2, 3, 4, 5])
    
    if choice == 1:
        return 'a' + generate_S_recursive(depth + 1, max_depth) + 'a'
    elif choice == 2 :
        return 'b' + generate_S_recursive(depth +1, max_depth) + 'b'
    elif choice == 3:
        return 'a'
    elif choice == 4:
        return 'b'
    else:
        return ''
    
if __name__ == "__main__":
    print("Uppgift 2 - Genererade ord:")
    for i in range(10):
        word = generate_S_recursive()
        print(f" {i + 1}. {word}")