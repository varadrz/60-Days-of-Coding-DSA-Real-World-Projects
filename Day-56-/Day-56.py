# Day 56 - Smart Campus System
# Focus: Capstone Project (Queues + Graphs + HashMaps)
# Language: Python 3

from collections import deque


class SmartCampusSystem:
    def __init__(self):
        self.buildings = {}        # Graph: building -> connected buildings
        self.student_queue = deque()  # Queue for service requests
        self.student_records = {}  # HashMap: student_id -> details

    # -------- GRAPH OPERATIONS --------
    def add_building(self, building):
        if building not in self.buildings:
            self.buildings[building] = []

    def connect_buildings(self, b1, b2):
        self.add_building(b1)
        self.add_building(b2)
        self.buildings[b1].append(b2)
        self.buildings[b2].append(b1)

    def show_campus_map(self):
        print("\nCampus Connectivity Map:")
        for b, connections in self.buildings.items():
            print(f"{b} -> {connections}")

    # -------- QUEUE OPERATIONS --------
    def request_service(self, student_id):
        self.student_queue.append(student_id)
        print(f"Service requested by Student {student_id}")

    def process_service(self):
        if self.student_queue:
            student_id = self.student_queue.popleft()
            print(f"Processing service for Student {student_id}")
        else:
            print("No pending service requests.")

    # -------- HASHMAP OPERATIONS --------
    def add_student(self, student_id, name, department):
        self.student_records[student_id] = {
            "name": name,
            "department": department
        }

    def show_students(self):
        print("\nStudent Records:")
        for sid, info in self.student_records.items():
            print(sid, "->", info)


def main():
    campus = SmartCampusSystem()

    # Add buildings and connections (Graph)
    campus.connect_buildings("Library", "Hostel")
    campus.connect_buildings("Library", "Academic Block")
    campus.connect_buildings("Cafeteria", "Hostel")

    # Add students (HashMap)
    campus.add_student(101, "Aarav", "CSE")
    campus.add_student(102, "Isha", "ECE")

    # Student service requests (Queue)
    campus.request_service(101)
    campus.request_service(102)

    campus.show_students()
    campus.show_campus_map()

    campus.process_service()
    campus.process_service()
    campus.process_service()


if __name__ == "__main__":
    main()
