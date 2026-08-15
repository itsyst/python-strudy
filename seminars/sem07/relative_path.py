def relative_path(from_path, to_path):
    """
    Skapar en relativ sökväg från from_path till to_path.
    Fungerar för Unix-sökvägar.
    """
    # Ta bort avslutande /
    from_path = from_path.rstrip('/')
    to_path = to_path.rstrip('/')
    
    # Dela upp sökvägarna
    from_parts = from_path.split('/')
    to_parts = to_path.split('/')
    
    # Hitta gemensam prefix (hur långt sökvägarna är lika)
    common_length = 0
    for i in range(min(len(from_parts), len(to_parts))):
        if from_parts[i] == to_parts[i]:
            common_length += 1
        else:
            break
    
    # Antal nivåer upp vi måste gå (..)
    levels_up = len(from_parts) - common_length
    
    # Sökväg nedåt från gemensam punkt
    path_down = to_parts[common_length:]
    
    # Bygg relativ sökväg
    result_parts = ['..'] * levels_up + path_down
    return '/'.join(result_parts)


if __name__ == "__main__":
    path = relative_path('/Users/Ingegerd/python/work', '/Users/Ingegerd/haskell/work')
    print(f"{path}")

# >>> relative_path('/Users/Ingegerd/python/work', '/Users/Ingegerd/haskell/work')
# '../../haskell/work'

# >>> relative_path('/Users/Ingegerd/', '/Users/Ingegerd/haskell/work')
# 'haskell/work'

# >>> relative_path('/a/b/c', '/a/d/e')
# '../../d/e'
