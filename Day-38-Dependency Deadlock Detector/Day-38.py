# Day 38 - Dependency Deadlock Detector
# Focus: Graph Cycle Detection (DFS)
# Language: Python 3


class DeadlockDetector:
    def __init__(self):
        self.graph = {}

    def add_task(self, task):
        if task not in self.graph:
            self.graph[task] = []

    def add_dependency(self, task, depends_on):
        self.add_task(task)
        self.add_task(depends_on)
        self.graph[task].append(depends_on)

    def has_deadlock(self):
        visited = set()
        recursion_stack = set()

        def dfs(task):
            if task in recursion_stack:
                return True
            if task in visited:
                return False

            visited.add(task)
            recursion_stack.add(task)

            for dependency in self.graph[task]:
                if dfs(dependency):
                    return True

            recursion_stack.remove(task)
            return False

        for task in self.graph:
            if dfs(task):
                return True

        return False


def main():
    detector = DeadlockDetector()

    detector.add_dependency("Task-A", "Task-B")
    detector.add_dependency("Task-B", "Task-C")
    detector.add_dependency("Task-C", "Task-A")  # Creates a cycle

    if detector.has_deadlock():
        print("\nDeadlock detected in dependencies!")
    else:
        print("\nNo deadlock detected.")


if __name__ == "__main__":
    main()
