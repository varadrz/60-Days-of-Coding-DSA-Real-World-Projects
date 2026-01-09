# Day 26 - Organization Hierarchy Viewer
# Focus: Binary Trees
# Language: Python 3


class EmployeeNode:
    def __init__(self, name):
        self.name = name
        self.left = None    # Direct report 1
        self.right = None   # Direct report 2


def display_hierarchy(root, level=0):
    if not root:
        return

    print("  " * level + "- " + root.name)
    display_hierarchy(root.left, level + 1)
    display_hierarchy(root.right, level + 1)


def main():
    # Building organization hierarchy
    ceo = EmployeeNode("CEO")

    ceo.left = EmployeeNode("CTO")
    ceo.right = EmployeeNode("CFO")

    ceo.left.left = EmployeeNode("Engineering Manager")
    ceo.left.right = EmployeeNode("QA Manager")

    ceo.right.left = EmployeeNode("Finance Manager")
    ceo.right.right = EmployeeNode("Accounts Manager")

    print("\nOrganization Hierarchy:\n")
    display_hierarchy(ceo)


if __name__ == "__main__":
    main()
