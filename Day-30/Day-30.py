# Day 30 - Auto-Complete Search Engine
# Focus: Trie (Prefix Tree)
# Language: Python 3


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class AutoComplete:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        word = word.lower().strip()
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.is_end = True

    def _dfs(self, node, prefix, results):
        if node.is_end:
            results.append(prefix)

        for ch, child in node.children.items():
            self._dfs(child, prefix + ch, results)

    def get_suggestions(self, prefix):
        prefix = prefix.lower().strip()
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return []

            node = node.children[ch]

        results = []
        self._dfs(node, prefix, results)
        return results


def main():
    engine = AutoComplete()

    # Dataset used for autocomplete
    words = [
        "python", "pytorch", "pycharm", "pytest",
        "java", "javascript", "json", "jupyter",
        "shoe", "shoes", "shoelace", "shoestore", "shorts"
    ]

    for word in words:
        engine.insert(word)

    while True:
        prefix = input("\nEnter search prefix (or type 'exit'): ").strip()
        if prefix.lower() == "exit":
            break

        suggestions = engine.get_suggestions(prefix)

        if suggestions:
            print("\nSuggestions:")
            for s in suggestions:
                print("-", s)
        else:
            print("\nNo suggestions found.")


if __name__ == "__main__":
    main()
