from rich.tree import Tree
from rich import print


def create_trie():
    return ()


def add_word(trie, word):
    return add_word_recursive(trie, word, 0)


def add_word_recursive(node_list, word, index):
    if index == len(word):
        return node_list

    char = word[index]
    new_nodes = []
    found = False

    for (c, children, is_end) in node_list:
        if c == char:
            found = True
            new_child = add_word_recursive(children, word, index + 1)
            if index == len(word) - 1:
                is_end = True
            new_nodes.append((c, new_child, is_end))
        else:
            new_nodes.append((c, children, is_end))

    if not found:
        if index == len(word) - 1:
            new_nodes.append((char, (), True))
        else:
            new_nodes.append((char,
                              add_word_recursive((), word, index + 1),
                              False))

    return tuple(new_nodes)

def word_in_trie(trie, word):
    if not word:
        return False

    node_list = trie
    for char in word:
        for (c, children, is_end) in node_list:
            if c == char:
                node_list = children
                break
        else:
            return False

    return True

def show_trie(trie):
    tree = Tree("Trie")

    def add_nodes(node_list, parent):
        for char, children, is_end in node_list:
            label = f"[bold red]{char}[/]" if is_end else char
            branch = parent.add(label)
            add_nodes(children, branch)

    add_nodes(trie, tree)
    print(tree)

def find_all_matches(trie, prefix):
    node_list = trie
    path_node = None

    for char in prefix:
        for child in node_list:
            if child[0] == char:
                node_list = child[1]
                path_node = child
                break
        else:
            return set()

    matches = set()

    if path_node and path_node[2]:
        matches.add(prefix)

    def dfs(nodes, current):
        for char, children, is_end in nodes:
            new = current + char
            if is_end:
                matches.add(new)
            dfs(children, new)

    dfs(node_list, prefix)
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
            my_trie = add_word(my_trie, testcase)
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

