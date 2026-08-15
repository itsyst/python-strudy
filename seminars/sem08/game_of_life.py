import time
import os

class GameOfLife:
    """
    Conway's Game of Life implementation
    """
    
    def __init__(self, width, height):
        """Skapa ett tomt spelbräde"""
        self.width = width
        self.height = height
        self.grid = [[False for _ in range(width)] for _ in range(height)]
    
    def set_cell(self, row, col, alive=True):
        """Sätt en cells tillstånd"""
        if 0 <= row < self.height and 0 <= col < self.width:
            self.grid[row][col] = alive
    
    def get_cell(self, row, col):
        """Hämta en cells tillstånd"""
        if 0 <= row < self.height and 0 <= col < self.width:
            return self.grid[row][col]
        return False  # Celler utanför är döda
    
    def count_neighbors(self, row, col):
        """
        Räkna levande grannar för en cell.
        En cell har 8 grannar (diagonaler inkluderade).
        """
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue  # Räkna inte cellen själv
                if self.get_cell(row + dr, col + dc):
                    count += 1
        return count
    
    def next_generation(self):
        """
        Beräkna och returnera nästa generation enligt reglerna:
        - Levande cell med 0-1 grannar dör (ensamhet)
        - Levande cell med 4-8 grannar dör (trängsel)
        - Död cell med exakt 3 grannar återföds
        - Levande cell med 2-3 grannar överlever
        """
        new_grid = [[False for _ in range(self.width)] for _ in range(self.height)]
        
        for row in range(self.height):
            for col in range(self.width):
                neighbors = self.count_neighbors(row, col)
                current = self.grid[row][col]
                
                if current:  # Cell är levande
                    # Överlever med 2 eller 3 grannar
                    if neighbors == 2 or neighbors == 3:
                        new_grid[row][col] = True
                    # Annars dör den (0-1 eller 4-8 grannar)
                else:  # Cell är död
                    # Återföds med exakt 3 grannar
                    if neighbors == 3:
                        new_grid[row][col] = True
        
        self.grid = new_grid
    
    def print_grid(self, alive_char="█", dead_char="░"):
        """Skriv ut spelbrädet"""
        for row in self.grid:
            line = ""
            for cell in row:
                line += alive_char if cell else dead_char
            print(line)
    
    def clear_screen(self):
        """Rensa terminalen (plattformsoberoende)"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def add_pattern(self, pattern, start_row, start_col):
        """
        Lägg till ett mönster på spelbrädet.
        pattern är en lista av (rad, kolumn) tupler relativt start-position.
        """
        for dr, dc in pattern:
            self.set_cell(start_row + dr, start_col + dc, True)


# ============================================================================
# KLASSISKA MÖNSTER
# ============================================================================

# Stabila mönster
BLOCK = [(0, 0), (0, 1), (1, 0), (1, 1)]

BEEHIVE = [(0, 1), (0, 2), (1, 0), (1, 3), (2, 1), (2, 2)]

# Oscillerande mönster
BLINKER = [(0, 0), (0, 1), (0, 2)]  # Period 2

TOAD = [(1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2)]  # Period 2

BEACON = [(0, 0), (0, 1), (1, 0), (2, 3), (3, 2), (3, 3)]  # Period 2

PULSAR = [
    (2, 4), (2, 5), (2, 6), (2, 10), (2, 11), (2, 12),
    (4, 2), (4, 7), (4, 9), (4, 14),
    (5, 2), (5, 7), (5, 9), (5, 14),
    (6, 2), (6, 7), (6, 9), (6, 14),
    (7, 4), (7, 5), (7, 6), (7, 10), (7, 11), (7, 12),
    (9, 4), (9, 5), (9, 6), (9, 10), (9, 11), (9, 12),
    (10, 2), (10, 7), (10, 9), (10, 14),
    (11, 2), (11, 7), (11, 9), (11, 14),
    (12, 2), (12, 7), (12, 9), (12, 14),
    (14, 4), (14, 5), (14, 6), (14, 10), (14, 11), (14, 12),
]  # Period 3

# Rymdskepp (rör sig över spelbrädet)
GLIDER = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

LWSS = [  # Lightweight spaceship
    (0, 1), (0, 4),
    (1, 0),
    (2, 0), (2, 4),
    (3, 0), (3, 1), (3, 2), (3, 3)
]


# ============================================================================
# DEMO-FUNKTIONER
# ============================================================================

def demo_stable_patterns():
    """Demo av stabila mönster"""
    game = GameOfLife(20, 10)
    
    # Lägg till block
    game.add_pattern(BLOCK, 3, 3)
    
    # Lägg till bikupa
    game.add_pattern(BEEHIVE, 3, 10)
    
    print("STABILA MÖNSTER (Block och Bikupa)")
    print("Dessa förändras aldrig.\n")
    
    for gen in range(5):
        print(f"Generation {gen}:")
        game.print_grid()
        print()
        if gen < 4:
            game.next_generation()
            time.sleep(1)


def demo_oscillators():
    """Demo av oscillerande mönster"""
    game = GameOfLife(30, 20)
    
    # Lägg till blinker
    game.add_pattern(BLINKER, 5, 5)
    
    # Lägg till toad
    game.add_pattern(TOAD, 5, 15)
    
    # Lägg till beacon
    game.add_pattern(BEACON, 12, 5)
    
    print("OSCILLERANDE MÖNSTER")
    print("Blinker (vänster), Toad (mitten), Beacon (nedre vänster)\n")
    
    for gen in range(20):
        print(f"Generation {gen}:")
        game.print_grid()
        print()
        game.next_generation()
        time.sleep(0.3)


def demo_glider():
    """Demo av seglare (glider)"""
    game = GameOfLife(40, 20)
    
    # Lägg till glider i övre vänstra hörnet
    game.add_pattern(GLIDER, 2, 2)
    
    print("GLIDER (Seglare)")
    print("Rör sig diagonalt över spelbrädet\n")
    
    for gen in range(50):
        # game.clear_screen()  # Avkommentera för animering
        print(f"Generation {gen}:")
        game.print_grid()
        print()
        game.next_generation()
        time.sleep(0.2)


def demo_pulsar():
    """Demo av pulsar"""
    game = GameOfLife(20, 20)
    
    game.add_pattern(PULSAR, 2, 2)
    
    print("PULSAR")
    print("Oscillerar med period 3\n")
    
    for gen in range(20):
        print(f"Generation {gen}:")
        game.print_grid()
        print()
        game.next_generation()
        time.sleep(0.5)


def interactive_game():
    """Interaktiv Game of Life"""
    print("="*60)
    print("CONWAY'S GAME OF LIFE - INTERAKTIV")
    print("="*60)
    
    width = int(input("Bredd (t.ex. 50): ") or "50")
    height = int(input("Höjd (t.ex. 30): ") or "30")
    
    game = GameOfLife(width, height)
    
    print("\nVälj startmönster:")
    print("1. Glider")
    print("2. Blinker")
    print("3. Pulsar")
    print("4. Slumpmässigt")
    choice = input("Val (1-4): ") or "1"
    
    if choice == "1":
        game.add_pattern(GLIDER, 5, 5)
    elif choice == "2":
        game.add_pattern(BLINKER, height//2, width//2)
    elif choice == "3":
        if width >= 20 and height >= 20:
            game.add_pattern(PULSAR, 2, 2)
        else:
            print("För litet för pulsar, använder glider istället")
            game.add_pattern(GLIDER, 5, 5)
    else:
        import random
        for _ in range(width * height // 5):
            r = random.randint(0, height-1)
            c = random.randint(0, width-1)
            game.set_cell(r, c, True)
    
    generations = int(input("\nAntal generationer (t.ex. 100): ") or "100")
    delay = float(input("Fördröjning mellan generationer i sekunder (t.ex. 0.1): ") or "0.1")
    
    print("\nStartar simulering...\n")
    
    for gen in range(generations):
        print(f"\nGeneration {gen}:")
        game.print_grid()
        game.next_generation()
        time.sleep(delay)


# ============================================================================
# HUVUDPROGRAM
# ============================================================================

if __name__ == "__main__":
    print("="*60)
    print("CONWAY'S GAME OF LIFE")
    print("="*60)
    print()
    
    print("Välj demo:")
    print("1. Stabila mönster (Block, Bikupa)")
    print("2. Oscillerande mönster (Blinker, Toad, Beacon)")
    print("3. Glider (Seglare)")
    print("4. Pulsar")
    print("5. Interaktivt läge")
    print("6. Kör alla demos")
    
    choice = input("\nVälj (1-6): ") or "1"
    print()
    
    if choice == "1":
        demo_stable_patterns()
    elif choice == "2":
        demo_oscillators()
    elif choice == "3":
        demo_glider()
    elif choice == "4":
        demo_pulsar()
    elif choice == "5":
        interactive_game()
    elif choice == "6":
        print("\n" + "="*60)
        print("DEMO 1: STABILA MÖNSTER")
        print("="*60 + "\n")
        demo_stable_patterns()
        
        input("\nTryck Enter för nästa demo...")
        
        print("\n" + "="*60)
        print("DEMO 2: OSCILLERANDE MÖNSTER")
        print("="*60 + "\n")
        demo_oscillators()
        
        input("\nTryck Enter för nästa demo...")
        
        print("\n" + "="*60)
        print("DEMO 3: GLIDER")
        print("="*60 + "\n")
        demo_glider()
    else:
        print("Ogiltigt val. Kör glider-demo.")
        demo_glider()
