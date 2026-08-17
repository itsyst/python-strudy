import sys
from turtle import pos
 
def crosses_own_path_set(moves: str) :
    x = 0 
    y = 0
    visited = {(0,0)}

    for move in moves:
        if move == "N":
            y += 1
        elif move == "E":
            x += 1
        elif move == "S":
            y -= 1
        elif move == "W":
            x -= 1

        position = (x,y)

        if position in visited:
            return True

        visited.add(position)
        
    return False

def crosses_own_path(moves: str) -> bool:
    position: list[int] = [0, 0]
    visited: dict[tuple[int, int], bool] = {(0, 0): True}

    steps: dict[str, tuple[int, int]] = {
        "N": (0, 1),
        "S": (0, -1),
        "E": (1, 0),
        "W": (-1, 0)
    }

    for move in moves:
        dx: int
        dy: int
        dx, dy = steps[move]

        position[0] += dx
        position[1] += dy

        coordinate: tuple[int, int] = tuple(position)

        if coordinate in visited:
            return True

        visited[coordinate] = True

    return False

def test_method(method):
    # Startar (0,0) -> (0,1) -> (1,1) -> (1,0) -> (0,0). Tillbaka till start!
    assert method("NESW") is True
    # (0,0) -> (0,1) -> (0,2) -> (0,3). Korsar aldrig sin väg.
    assert method("NNN") is False
    assert method("NESEN") is False
    # (0,0) -> (1,0) -> (0,0). Tillbaka till start.
    assert method("EW") is True
    # Roboten rör sig inte -- har alltså inte korsat sin egen väg.
    assert method("") is False
     
def check_python_version():
    print(
        f"Python {sys.version_info.major}."
        f"{sys.version_info.minor}."
        f"{sys.version_info.micro}"
    )

def run_tests():
    print("Testar crosses_own_path_set...")
    test_method(crosses_own_path_set)
    print("crosses_own_path_set klarade alla tester.")

    print("*" * 40)

    print("Testar crosses_own_path...")
    test_method(crosses_own_path)
    print("crosses_own_path klarade alla tester.")
 
    print("*" * 40)
 
    print("Har kört alla tester.")
    print(crosses_own_path("NESW"))
 
if __name__ == '__main__':
    check_python_version()
    run_tests()
