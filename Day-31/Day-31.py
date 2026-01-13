# Day 31 - Social Network Connections
# Focus: Graph Basics
# Language: Python 3


class SocialNetwork:
    def __init__(self):
        self.graph = {}  # adjacency list

    def add_user(self, user):
        if user not in self.graph:
            self.graph[user] = []

    def add_connection(self, user1, user2):
        self.add_user(user1)
        self.add_user(user2)

        # Undirected graph (mutual connection)
        self.graph[user1].append(user2)
        self.graph[user2].append(user1)

    def show_connections(self):
        for user in self.graph:
            print(f"{user} -> {self.graph[user]}")


def main():
    network = SocialNetwork()

    network.add_connection("Alice", "Bob")
    network.add_connection("Alice", "Charlie")
    network.add_connection("Bob", "David")
    network.add_connection("Charlie", "Eva")

    print("\nSocial Network Connections:\n")
    network.show_connections()


if __name__ == "__main__":
    main()
