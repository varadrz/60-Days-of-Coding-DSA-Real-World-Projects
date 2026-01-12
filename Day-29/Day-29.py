# Day 29 - Role-Based Access Control
# Focus: Lowest Common Ancestor (LCA)
# Language: Python 3


class RoleNode:
    def __init__(self, role):
        self.role = role
        self.left = None
        self.right = None


def lowest_common_ancestor(root, role1, role2):
    if not root:
        return None

    if root.role == role1 or root.role == role2:
        return root

    left_lca = lowest_common_ancestor(root.left, role1, role2)
    right_lca = lowest_common_ancestor(root.right, role1, role2)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca else right_lca


def main():
    # Building role hierarchy
    ceo = RoleNode("CEO")

    ceo.left = RoleNode("CTO")
    ceo.right = RoleNode("CFO")

    ceo.left.left = RoleNode("Engineering Manager")
    ceo.left.right = RoleNode("QA Manager")

    ceo.right.left = RoleNode("Finance Manager")
    ceo.right.right = RoleNode("Accounts Manager")

    role1 = "Engineering Manager"
    role2 = "QA Manager"

    lca = lowest_common_ancestor(ceo, role1, role2)

    if lca:
        print(f"\nLowest Common Role for '{role1}' and '{role2}': {lca.role}")
    else:
        print("No common role found")


if __name__ == "__main__":
    main()
