# Day 34 - Course Prerequisite Planner
# Focus: Topological Sort (Kahn's Algorithm)
# Language: Python 3

from collections import deque, defaultdict


class CoursePlanner:
    def __init__(self):
        self.graph = defaultdict(list)
        self.indegree = defaultdict(int)

    def add_course(self, course):
        if course not in self.graph:
            self.graph[course] = []

    def add_prerequisite(self, course, prerequisite):
        # prerequisite -> course
        self.graph[prerequisite].append(course)
        self.indegree[course] += 1
        if prerequisite not in self.indegree:
            self.indegree[prerequisite] = 0

    def plan_courses(self):
        queue = deque()
        order = []

        for course in self.indegree:
            if self.indegree[course] == 0:
                queue.append(course)

        while queue:
            current = queue.popleft()
            order.append(current)

            for neighbor in self.graph[current]:
                self.indegree[neighbor] -= 1
                if self.indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) != len(self.indegree):
            return []  # Cycle detected

        return order


def main():
    planner = CoursePlanner()

    planner.add_prerequisite("Data Structures", "Programming Basics")
    planner.add_prerequisite("Algorithms", "Data Structures")
    planner.add_prerequisite("Databases", "Programming Basics")
    planner.add_prerequisite("System Design", "Algorithms")

    order = planner.plan_courses()

    if order:
        print("\nCourse Completion Order:")
        for course in order:
            print(course)
    else:
        print("Cycle detected. Course plan not possible.")


if __name__ == "__main__":
    main()
