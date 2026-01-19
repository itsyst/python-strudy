from rich import print
from rich.tree import Tree


def create_node():
    return {"end": False, "children": {}}


class Trie:
    def __init__(self):
        self.root = create_node()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node["children"]:
                node["children"][char] = create_node()
            node = node["children"][char]
        node["end"] = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node["children"]:
                return False
            node = node["children"][char]
        return node["end"]

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node["children"]:
                return False
            node = node["children"][char]
        return True


    def visualize(self):
        tree = Tree("🌳 [bold green]TRIE ROOT[/bold green]")
        self._build_tree(self.root, tree)
        print(tree)

    def _build_tree(self, node, tree):
        for char, child in node["children"].items():
            label = f"[cyan]{char}[/cyan]"
            if child["end"]:
                label += " [bold yellow](word end)[/bold yellow]"
            branch = tree.add(label)
            self._build_tree(child, branch)


if __name__ == "__main__":
    trie = Trie()

    words = ["car", "cat", "dog", "door", "doom"]
    for w in words:
        trie.insert(w)

    print("[bold green]Search Tests[/bold green]")
    print("car:", trie.search("car"))
    print("cat:", trie.search("cat"))
    print("cap:", trie.search("cap"))

    print("\n[bold blue]Prefix Tests[/bold blue]")
    print("do ->", trie.starts_with("do"))
    print("ca ->", trie.starts_with("ca"))
    print("za ->", trie.starts_with("za"))

    print("\n[bold magenta]Visualization[/bold magenta]")
    trie.visualize()
