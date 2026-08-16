from re import M, match
import sys
import pprint
 
def create_trie():
    return {"children":{}, "end":False}

def add_word(trie, word:str):
    node = trie
    for char in word:
        if char not in node["children"]:
            node["children"][char] = {"children":{}, "end": False}
        node = node["children"][char]

    node["end"] = True
    return trie

def word_in_trie(trie, word: str):
    node = trie
    for char in word:
        if char not in node["children"]:
            return False

        node = node["children"][char]
    return node["end"]

def find_all_matches(trie, prefix: str):
    node = trie
    for char in prefix:
        if char not in node["children"]:
            return set()

        node = node["children"][char]

    matches = set()

    def collect(current_node, current_word):
        if current_node["end"]:
            matches.add(current_word)
        for ch, child in current_node["children"].items():
            collect(child, current_word + ch)

    collect(node, prefix)
    
    return matches
 
def check_python_version():
    # ... färdig kod som kollar att du kör rätt version av Python ...
    print(
        f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

def run_tests():
    # De här testerna står uttryckligen som assertions på tentan.
    print("Kör uppgiftens tester...")
    trie = create_trie()
    words = ["ace", "aced", "aces", "acre", "acres", "act","acted", "acting", "acts", "before"]
    for word in words:
        add_word(trie, word)
        assert word_in_trie(trie, word) is True
 
    absent = "En Trie är en effektiv datastruktur Before".split()
    for word in absent:
        assert  word_in_trie(trie, word) is False

    # prefixes alone are not complete words
    assert word_in_trie(trie, "ac") is False
    assert word_in_trie(trie, "acti") is False

    # assert find_all_matches(trie, "ace") == {"ace", "aced", "aces"}

    # Här kan du lägga tester där du inte vet korrekta svar men
    # ändå kan skriva ut resultatet. Kanske det kraschar, kanske
    # det är uppenbart fel...
    print("*"*40)
    print("Kör utskriftstester...")
    # pprint.pp(trie)
    print(word_in_trie(trie, "ace"))
    print(word_in_trie(trie, absent[-1]))
    pprint.pprint(find_all_matches(trie, "ac"))
    print("Har kört alla tester")

if __name__ == '__main__':
    check_python_version()
    run_tests()





























