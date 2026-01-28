# Day 45 - Org Restructuring Analyzer
# Focus: Dynamic Programming on Trees
# Language: Python 3


class EmployeeNode:
    def __init__(self, name, productivity):
        self.name = name
        self.productivity = productivity
        self.subordinates = []


def max_productivity(root):
    """
    Returns a tuple:
    (include_root, exclude_root)

    include_root: max productivity including this employee
    exclude_root: max productivity excluding this employee
    """

    if not root:
        return (0, 0)

    include_root = root.productivity
    exclude_root = 0

    for child in root.subordinates:
        child_include, child_exclude = max_productivity(child)

        include_root += child_exclude
        exclude_root += max(child_include, child_exclude)

    return include_root, exclude_root


def main():
    # Building organization tree
    ceo = EmployeeNode("CEO", 50)

    manager1 = EmployeeNode("Manager-1", 30)
    manager2 = EmployeeNode("Manager-2", 40)

    emp1 = EmployeeNode("Employee-1", 10)
    emp2 = EmployeeNode("Employee-2", 20)
    emp3 = EmployeeNode("Employee-3", 15)

    ceo.subordinates = [manager1, manager2]
    manager1.subordinates = [emp1, emp2]
    manager2.subordinates = [emp3]

    include, exclude = max_productivity(ceo)

    print("\nMaximum Organization Productivity:",
          max(include, exclude))


if __name__ == "__main__":
    main()
