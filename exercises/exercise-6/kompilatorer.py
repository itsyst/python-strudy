
'''
Kompilator
En kompilator översätter hela programmet på en gång från källkod till maskinkod innan programmet körs.
Hur det fungerar:

Du skriver kod (t.ex. C, C++, Rust)
Kompilatorn översätter all kod till en körbar fil (exe, binär fil)
Du kör den färdiga filen direkt på datorn

Fördelar:

Mycket snabbare körning
Hittar många fel innan programmet körs
Programmet kan köras utan kompilatorn installerad

Nackdelar:

Tar tid att kompilera (speciellt stora program)
Måste kompilera om vid varje ändring
Plattformsberoende (Windows-version fungerar inte på Mac)

'''

def the_program():
    print("Hej på dej")
    print("Hej på dej")
    exit()
    print("Hej på dej")

if __name__ == "__main__":
    the_program()
