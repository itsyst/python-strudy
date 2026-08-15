from cellular_automat import next_state

def pred_rule(a, b, c):
    """
    Regel 110 - Predikatfunktion baserad på sanningstabell
    
    ╔═══╦═══╦═══╦═══════╗
    ║ a ║ b ║ c ║ nästa ║
    ╠═══╬═══╬═══╬═══════╣
    ║ 0 ║ 0 ║ 0 ║   0   ║
    ║ 0 ║ 0 ║ 1 ║   1   ║
    ║ 0 ║ 1 ║ 0 ║   1   ║
    ║ 0 ║ 1 ║ 1 ║   1   ║
    ║ 1 ║ 0 ║ 0 ║   1   ║
    ║ 1 ║ 0 ║ 1 ║   1   ║
    ║ 1 ║ 1 ║ 0 ║   1   ║
    ║ 1 ║ 1 ║ 1 ║   0   ║
    ╚═══╩═══╩═══╩═══════╝
    
    Binärkod: 01101110 = 110 (Regel 110)
    Booleskt uttryck: (a OR b OR c) AND NOT (a AND b AND c)
    """
    return (a or b or c) and not (a and b and c)


def print_truth_table():
    """Skriv ut sanningstabell för pred_rule i vackert format"""
    print("\n╔═══════════════════════════════════════╗")
    print("║   REGEL 110 - SANNINGSTABELL          ║")
    print("╠═══╦═══╦═══╦═══════════════════════════╣")
    print("║ a ║ b ║ c ║ nästa b (output)          ║")
    print("╠═══╬═══╬═══╬═══════════════════════════╣")
    
    for i in range(8):
        a = bool(i & 4)
        b = bool(i & 2)
        c = bool(i & 1)
        result = pred_rule(a, b, c)
        
        a_str = "1" if a else "0"
        b_str = "1" if b else "0"
        c_str = "1" if c else "0"
        result_str = "1" if result else "0"
        symbol = "●" if result else "○"
        
        print(f"║ {a_str} ║ {b_str} ║ {c_str} ║   {result_str}   {symbol}                  ║")
    
    print("╚═══╩═══╩═══╩═══════════════════════════╝")
    print("\nLegend: ● = Levande (1)  ○ = Död (0)")
    print("Booleskt uttryck: (a OR b OR c) AND NOT (a AND b AND c)")

def show_compact_truth_table():
    """Kompakt sanningstabell med emojis"""
    print("\n┌─────────────────────────────────┐")
    print("│  Regel 110 Sanningstabell       │")
    print("├─────┬─────┬─────┬───────────────┤")
    print("│  a  │  b  │  c  │  nästa b      │")
    print("├─────┼─────┼─────┼───────────────┤")
    
    for a in [False, True]:
        for b in [False, True]:
            for c in [False, True]:
                result = pred_rule(a, b, c)
                a_sym = "■" if a else "□"
                b_sym = "■" if b else "□"
                c_sym = "■" if c else "□"
                r_sym = "■" if result else "□"
                print(f"│  {a_sym}  │  {b_sym}  │  {c_sym}  │     {r_sym}         │")
    
    print("└─────┴─────┴─────┴───────────────┘")
    print("\nLegend: ■ = True (1)  □ = False (0)")
 
def print_colored_truth_table():
    """Färgad sanningstabell (kräver terminal med färgstöd)"""
    
    # ANSI färgkoder
    RED = '\033'

## ✨ Komplett Körbar Kod
 
def print_state_fancy(seq, generation=0):
    """Vackert utskrift av cellulär automat"""
    alive_char = "█"
    dead_char = "░"
    
    state = ""
    for alive in seq:
        state += alive_char if alive else dead_char
    
    print(f"Gen {generation:2d}: {state}")


if __name__ == "__main__":
    # Visa sanningstabell
    print_truth_table()
    show_compact_truth_table()
 
    print("\n" + "="*80)
    print("SIMULERING AV CELLULÄR AUTOMAT (REGEL 110)")
    print("="*80 + "\n")
    
    # Skapa initial tillstånd
    seq = [i == 40 for i in range(80)]
    
    # Simulera automaten
    print_state_fancy(seq, 0)
    for i in range(39):
        seq = next_state(seq, pred_rule)
        print_state_fancy(seq, i+1)
    
    print("\n" + "="*80)
    print("STATISTIK")
    print("="*80)
    print(f"Antal generationer: 40")
    print(f"Bredd: 80 celler")
    print(f"Regel: 110 (Turing-komplett)")
    print("="*80)
