''' 
Uppgift 1:

S = 'a', A | 'b', B ;
A = 'a', B | '' ;
B = 'a' | 'b'
'''
import random

def generate_B():
    """B = 'a' | 'b'"""
    return random.choice(['a', 'b'])

def generate_A():
    """A = 'a', B | ''"""
    choice = random.choice([1, 2])
    if choice == 1:
        return 'a' + generate_B()  # 'a', B
    else:
        return ''  # tom sträng

def generate_S():
    """S = 'a', A | 'b', B"""
    choice = random.choice([1, 2])
    if choice == 1:
        return 'a' + generate_A()  # 'a', A
    else:
        return 'b' + generate_B()  # 'b', B

# Testa genom att generera ord
if __name__ == "__main__":
    print("Uppgift 1 - Genererade ord:")
    for i in range(10):
        word = generate_S()
        print(f"  {i+1}. {word}")