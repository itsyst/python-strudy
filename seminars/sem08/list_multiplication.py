def create_grid(width, height):
    """ 
    Returns a two dimensional list with given width and height 
    Skapar helt separata listobjekt för varje rad
    Varje False är en separat instans
    SÄKER - inga delade referenser
    """
    grid = []
    for row in range(height):
        grid.append([])
        for col in range(width):
            grid[row].append(False)
    return grid


def create_grid2(width, height):
    """ 
    Returns a two dimensional list with given width and height 
    Använder [False] * width för varje rad
    Skapar nya listor för varje rad
    SÄKER - raderna är separata
    """
    grid = []
    for i in range(height):
        grid.append([False] * width)
    return grid


def create_grid3(width, height):
    """ 
    Returns a two dimensional list with given width and height 
    [[False] * width] * height
    FARLIG! - Alla rader pekar på SAMMA lista
    Problem: ändring i en rad ändrar ALLA rader
    """
    return [[False] * width] * height


def create_grid4(width, height):
    """ 
    Returns a two dimensional list with given width and height 
    List comprehension med nästlade loopar
    Skapar helt separata objekt
    SÄKER - mest Pythonic
    """
    return [[False for i in range(width)] for i in range(height)]


def create_grid5(width, height):
    """ 
    Returns a two dimensional list with given width and height 
    [[False] * width for i in range(height)]
    Skapar nya listor för varje rad
    SÄKER och koncis
    """
    return [[False] * width for i in range(height)]

grid = create_grid3(2, 2)
grid[0][0] = True
print(grid)
# Output: [[True, False], [True, False]]
# But we expected only the first element of the first row to be True.


def show_problem():
    grid = [[False] * 3] * 3  # create_grid3-stil
    
    # Försök ändra bara en cell
    grid[0][0] = True
    
    print("\nFörväntad:")
    print("[[True, False, False],")
    print(" [False, False, False],")
    print(" [False, False, False]]")
    
    print("Faktisk:")
    print(grid)
    # [[True, False, False],
    #  [True, False, False],  <- Oops!
    #  [True, False, False]]  <- Oops!

print(show_problem())