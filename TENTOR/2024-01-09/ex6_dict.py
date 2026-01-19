from rich.tree import Tree
from rich import print

def create_trie():
    return {'children':{}, 'is_end': False}

def add_word(trie: dict, word: str):
    if not word or not isinstance(word, str):
        return

    current = trie
    for ch in word:
        if ch not in current["children"]:
            current["children"][ch] = {"children": {}, "is_end": False}
        current = current["children"][ch]

    current["is_end"] = True


def word_in_trie(trie: dict, word:str) -> bool:
    if not word or not isinstance(word, str):
        return False
    current = trie
    for char in word:
        if char in current['children']:
            current = current['children'][char]
        else:
            return False

    return current['is_end']

def show_trie(trie):
    tree = Tree("Trie")

    def add_nodes(node, branch):
        children = node.get("children", {})
        if not isinstance(children, dict):
            return

        for ch, child in children.items():
            is_end = child.get("is_end", False)
            label = f"[bold red]{ch}[/]" if is_end else ch
            sub = branch.add(label)
            add_nodes(child, sub)

    add_nodes(trie, tree)
    print(tree)

def run_tests():
    test_cases = [
        ( "ace", True),
        ("aced", True),
        ("aces", True),
        ("acre", True),
        ("acres", True),
        ("act", True),
        ("acted", True),
        ("acting", False),
        ("acts", False),
        ("En Trie är en effektiv datastruktu", False)
    ]

    my_trie = create_trie()
    print("="*25, "word_in_trie", "="*25)
    for i,  (testcase, expected) in enumerate(test_cases):
       if expected:
           add_word(my_trie, testcase)
       result = word_in_trie(my_trie, testcase)
       assert result == expected, f"Test{i + 1 }: expected: {expected}, get: {result}"
       print(f"Test{i + 1 }: word_in_trie({testcase}) -> {result}")
    print()
    show_trie(my_trie)

if __name__ == "__main__"   :
    run_tests()



