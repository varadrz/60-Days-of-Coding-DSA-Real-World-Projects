# Day 28 - Search Engine Index
# Focus: Binary Search Tree
# Language: Python 3


class BSTNode:
    def __init__(self, keyword):
        self.keyword = keyword
        self.left = None
        self.right = None


class SearchEngineIndex:
    def __init__(self):
        self.root = None

    def insert(self, keyword):
        self.root = self._insert_recursive(self.root, keyword)

    def _insert_recursive(self, node, keyword):
        if not node:
            return BSTNode(keyword)

        if keyword < node.keyword:
            node.left = self._insert_recursive(node.left, keyword)
        elif keyword > node.keyword:
            node.right = self._insert_recursive(node.right, keyword)

        return node

    def search(self, keyword):
        return self._search_recursive(self.root, keyword)

    def _search_recursive(self, node, keyword):
        if not node:
            return False
        if node.keyword == keyword:
            return True
        if keyword < node.keyword:
            return self._search_recursive(node.left, keyword)
        return self._search_recursive(node.right, keyword)

    def inorder_traversal(self):
        result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.keyword)
            inorder(node.right)

        inorder(self.root)
        return result


def main():
    index = SearchEngineIndex()

    keywords = [
        "python", "algorithm", "binary", "tree",
        "search", "index", "data", "structure"
    ]

    for word in keywords:
        index.insert(word)

    print("\nIndexed Keywords (Sorted):")
    print(index.inorder_traversal())

    print("\nSearch Results:")
    print("python:", index.search("python"))
    print("java:", index.search("java"))


if __name__ == "__main__":
    main()
