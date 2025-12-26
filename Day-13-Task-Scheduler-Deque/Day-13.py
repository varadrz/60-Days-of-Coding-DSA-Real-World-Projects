# Day 13 - Task Scheduler using Deque
# Focus: Deque (Double-Ended Queue)
# Language: Python 3

from collections import deque


class TaskScheduler:
    def __init__(self):
        self.tasks = deque()

    def add_high_priority_task(self, task):
        self.tasks.appendleft(task)
        print(f"High priority task added: {task}")

    def add_low_priority_task(self, task):
        self.tasks.append(task)
        print(f"Low priority task added: {task}")

    def execute_task(self):
        if not self.tasks:
            print("No tasks to execute.")
            return None

        task = self.tasks.popleft()
        print(f"Executing task: {task}")
        return task

    def view_tasks(self):
        if not self.tasks:
            print("No pending tasks.")
            return

        print("\nPending Tasks:")
        for task in self.tasks:
            print(task)


def main():
    scheduler = TaskScheduler()

    scheduler.add_low_priority_task("Send report")
    scheduler.add_low_priority_task("Clean logs")
    scheduler.add_high_priority_task("Fix production bug")
    scheduler.add_high_priority_task("Restart server")

    scheduler.view_tasks()

    scheduler.execute_task()
    scheduler.execute_task()

    scheduler.view_tasks()


if __name__ == "__main__":
    main()
