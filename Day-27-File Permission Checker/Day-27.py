# Day 27 - File Permission Checker
# Focus: Tree Traversals
# Language: Python 3


class FileNode:
    def __init__(self, name, permission):
        self.name = name
        self.permission = permission  # e.g., "r", "rw", "rwx"
        self.children = []


def dfs_permission_check(root, required_permission):
    """
    Depth-First Search to find files with required permission
    """
    result = []

    def dfs(node):
        if not node:
            return
        if required_permission in node.permission:
            result.append(node.name)
        for child in node.children:
            dfs(child)

    dfs(root)
    return result


def bfs_permission_check(root, required_permission):
    """
    Breadth-First Search to find files with required permission
    """
    from collections import deque

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if required_permission in node.permission:
            result.append(node.name)
        for child in node.children:
            queue.append(child)

    return result


def main():
    # Building file system tree
    root = FileNode("root", "rwx")

    home = FileNode("home", "rw")
    var = FileNode("var", "r")
    root.children.extend([home, var])

    docs = FileNode("documents", "rw")
    pics = FileNode("pictures", "r")
    home.children.extend([docs, pics])

    log = FileNode("log", "r")
    var.children.append(log)

    print("\nDFS - Files with read permission:")
    print(dfs_permission_check(root, "r"))

    print("\nBFS - Files with read permission:")
    print(bfs_permission_check(root, "r"))


if __name__ == "__main__":
    main()
