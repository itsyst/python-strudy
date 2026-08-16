import sys
import pprint
 
def create_trie():
    """Return a fresh empty trie"""
    return {"children":{}, "end": False}
 
def add_word(trie, word:str):
    """Insert word into trie and returns the same trie object"""
    node = trie
    for char in word:
        if char not in node["children"]:
            node["children"][char] = {"children": {}, "end": False}
        node = node["children"][char]
    node["end"] = True

    return trie

def word_in_trie(trie, word:str):
    node = trie
    for char in word:
        char_lower = f"{char.lower()}"
        if char_lower not in node["children"]:
            return False
        
        node = node["children"][char_lower]
 
    return True
 
def check_python_version():
    # ... färdig kod som kollar att du kör rätt version av Python ...
    print(
        f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

def run_tests():
    # De här testerna står uttryckligen som assertions på tentan.
    print("Kör uppgiftens tester...")
    trie = create_trie()
    for word in ["ace", "aced", "aces", "acre", "acres", "act","acted", "acting", "acts", "before"]:
        add_word(trie, word)
 
    for word in ["ace", "aced", "aces", "acre", "acres", "act","acted", "acting", "acts", "before"]:
        assert word_in_trie(trie, word) == True

    for word in "En Trie är en effektiv datastruktur".split(" "):
        assert not word_in_trie(trie, word) == True
 
    # Här lägger du dina egna tester. Du kan till exempel skapa egna
    # assertions, eller lägga till andra tester så som enkla utskrifter
    # av resultatet av en körning.
    print("*"*40)
    print("Kör egna tester...")

    # Här kan du lägga tester där du inte vet korrekta svar men
    # ändå kan skriva ut resultatet. Kanske det kraschar, kanske
    # det är uppenbart fel...
    print("*"*40)
    print("Kör utskriftstester...")
    pprint.pprint(trie)
    print("Har kört alla tester")

if __name__ == '__main__':
    check_python_version()
    run_tests()
