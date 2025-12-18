# Day 5 - Permission System using Bit Manipulation
# Focus: Bit Masking and Binary Operations
# Language: Python 3

READ = 4      # 100
WRITE = 2     # 010
EXECUTE = 1   # 001


class PermissionSystem:
    def __init__(self):
        self.permissions = {}

    def set_permission(self, user, permission):
        self.permissions[user] = permission

    def add_permission(self, user, permission):
        self.permissions[user] |= permission

    def remove_permission(self, user, permission):
        self.permissions[user] &= ~permission

    def has_permission(self, user, permission):
        return (self.permissions[user] & permission) != 0

    def show_permissions(self, user):
        perm = self.permissions[user]
        return {
            "read": bool(perm & READ),
            "write": bool(perm & WRITE),
            "execute": bool(perm & EXECUTE)
        }


def main():
    ps = PermissionSystem()

    ps.set_permission("alice", READ | WRITE)
    ps.set_permission("bob", READ)

    print("\n--- Permission System ---")

    print("Alice permissions:", ps.show_permissions("alice"))
    print("Bob permissions:", ps.show_permissions("bob"))

    print("\nAdding EXECUTE to Bob")
    ps.add_permission("bob", EXECUTE)
    print("Bob permissions:", ps.show_permissions("bob"))

    print("\nRemoving WRITE from Alice")
    ps.remove_permission("alice", WRITE)
    print("Alice permissions:", ps.show_permissions("alice"))

    print("\nPermission checks:")
    print("Alice can read:", ps.has_permission("alice", READ))
    print("Alice can write:", ps.has_permission("alice", WRITE))
    print("Bob can execute:", ps.has_permission("bob", EXECUTE))


if __name__ == "__main__":
    main()
