from rich.tree import Tree
from rich import print

def create_trie():
    return []


def add_word(trie, word: str):
    node = trie
    for i, char in enumerate(word):
        found_child = None

        for child in node:
            if child[0] == char:
                found_child = child
                node = child[1]
                break

        if found_child is None:
            is_end = (i == len(word) - 1)
            new_node = [char, [], is_end]
            node.append(new_node)
            node = new_node[1]
        else:
            if i == len(word) - 1:
                found_child[2] = True

def word_in_trie(trie, word: str):
    if not word:
        return False

    node = trie
    for char in word:
        for child in node:
            if child[0] == char:
                node = child[1]
                break
        else:
            return False

    return True

def show_trie(trie):
    tree = Tree("Trie")
    def add_nodes(node, parent):
        for char, children, is_end in node:
            label = f"[bold red]{char}[/]" if is_end else char
            child_branch = parent.add(label)
            add_nodes(children, child_branch)

    add_nodes(trie, tree)
    print(tree)

def find_all_matches(trie, prefix: str):
    node = trie
    path_node = None  # node corresponding to the last char of prefix

    # Traverse to the end of prefix
    for char in prefix:
        for child in node:
            if child[0] == char:
                node = child[1]
                path_node = child
                break
        else:
            return set()  # prefix not in trie

    matches = set()

    # If the prefix itself is a word, add it
    if path_node and path_node[2]:
        matches.add(prefix)

    # DFS to collect all words under prefix node
    def dfs(nodelist, current):
        for char, children, is_end in nodelist:
            new_word = current + char
            if is_end:
                matches.add(new_word)
            dfs(children, new_word)

    dfs(node, prefix)
    return matches



def run_tests():
    test_trie_cases = [
        ("ace", True),
        ("aced", True),
        ("aces", True),
        ("acre", True),
        ("acres", True),
        ("act", True),
        ("acted", True),
        ("acting", True),
        ("acts", True),
        ("actor", False),
        ("simple", False),
        ( "En Trie är en effektiv datastruktur", False)
    ]

    prefix_tests = [
        ("ac", {"ace","aced","aces","acre","acres","act","acted","acting","acts"}),
        ("act", {"act","acted","acting","acts"}),
        ("ace", {"ace","aced","aces"}),
        ("xyz", set())
    ]

    print("=" * 25, "word_in_trie", "="*25)
    my_trie = create_trie()
    for i, (testcase, expected) in enumerate(test_trie_cases):
        if expected:
            add_word(my_trie, testcase)
        result = word_in_trie(my_trie, testcase)
        assert result == expected, f"word_in_trie({testcase}) expected {expected}, got {result}"
        print(f"Test {i + 1}: word_in_trie({testcase}) -> {result}")

    # Test find_all_matches
    print("=" * 25, "find_all_matches", "="*25)
    for prefix, expected_matches in prefix_tests:
        result = find_all_matches(my_trie, prefix)
        assert result == expected_matches, f"find_all_matches({prefix}) expected {expected_matches}, got {result}"
        print(f"find_all_matches({prefix}) -> {result}")

    print("\nTrie Structure:")
    show_trie(my_trie)

if __name__ == "__main__":
    run_tests()

