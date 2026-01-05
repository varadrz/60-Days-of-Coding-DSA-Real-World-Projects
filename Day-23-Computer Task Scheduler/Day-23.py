# Day 23 - CPU Task Scheduler
# Focus: Greedy Scheduling
# Language: Python 3


def schedule_tasks(tasks):
    """
    tasks: list of tuples (task_name, execution_time)
    Goal: minimize total waiting time
    """
    # Sort tasks by execution time (Shortest Job First)
    tasks.sort(key=lambda x: x[1])

    current_time = 0
    total_waiting_time = 0

    schedule = []

    for task, time in tasks:
        schedule.append(task)
        total_waiting_time += current_time
        current_time += time

    return schedule, total_waiting_time


def main():
    tasks = [
        ("Task A", 6),
        ("Task B", 2),
        ("Task C", 8),
        ("Task D", 3)
    ]

    order, waiting_time = schedule_tasks(tasks)

    print("\nExecution Order:")
    for task in order:
        print(task)

    print("\nTotal Waiting Time:", waiting_time)


if __name__ == "__main__":
    main()
