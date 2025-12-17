# Day 4 - File Explorer using Recursion
# Focus: Recursion and Tree Traversal
# Language: Python 3

import os


def explore_directory(path, level=0):
    """
    Recursively explores directories and files
    """
    try:
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            print("  " * level + "- " + item)

            if os.path.isdir(full_path):
                explore_directory(full_path, level + 1)

    except PermissionError:
        print("  " * level + "- [Permission Denied]")


def search_file(path, target_file):
    """
    Recursively searches for a file in directory tree
    """
    try:
        for item in os.listdir(path):
            full_path = os.path.join(path, item)

            if item == target_file:
                return full_path

            if os.path.isdir(full_path):
                result = search_file(full_path, target_file)
                if result:
                    return result

    except PermissionError:
        return None

    return None


def main():
    print("\n===== Recursive File Explorer =====")
    root_path = input("Enter directory path to explore: ").strip()

    if not os.path.exists(root_path):
        print("Invalid path.")
        return

    print("\nDirectory Structure:")
    explore_directory(root_path)

    choice = input("\nDo you want to search for a file? (y/n): ").strip().lower()
    if choice == "y":
        filename = input("Enter file name to search: ").strip()
        result = search_file(root_path, filename)

        if result:
            print(f"\nFile found at: {result}")
        else:
            print("\nFile not found.")


if __name__ == "__main__":
    main()
