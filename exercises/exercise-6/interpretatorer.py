'''
Interpretator
En interpretator läser och kör koden rad för rad i realtid.
Hur det fungerar:

Du skriver kod (t.ex. Python, JavaScript)
Interpretatorn läser och kör varje rad direkt
Inget mellansteg med körbar fil

Fördelar:

Snabbare utveckling (testa direkt utan att kompilera)
Plattformsoberoende (samma kod fungerar överallt)
Lättare att debugga

Nackdelar:

Långsammare körning
Behöver interpretatorn installerad för att köra programmet
Vissa fel upptäcks först när koden körs

Exempel:

Kompilerade språk: C, C++, Rust, Go
Interpreterade språk: Python, JavaScript, Ruby, PHP

'''

def interpret_hg(the_program):
    for statement in the_program:
        if statement == 'hello':
            interpret_hello()
        elif statement == 'goodbye':
            interpret_exit()
        else:
            print("Syntax error: I don't understand " + statement)

def interpret_hello():
    print("Hej på dej")

def interpret_exit():
    print("Goodbye")
    exit()

# if __name__ == "__main__":
#     my_program = ['hello', 'hello', 'goodbye', 'hello']
#     interpret_hg(my_program)

if __name__ == "__main__":
    # Läs program från fil
    with open('program.hg', 'r') as f:
        my_program = [line.strip() for line in f.readlines()]
    interpret_hg(my_program)