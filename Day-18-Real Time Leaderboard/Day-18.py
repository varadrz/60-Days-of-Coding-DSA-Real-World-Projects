# Day 18 - Real-Time Leaderboard
# Focus: Heap Optimization
# Language: Python 3

import heapq


class Leaderboard:
    def __init__(self, k):
        self.k = k
        self.min_heap = []  # (score, user)

    def add_score(self, user, score):
        heapq.heappush(self.min_heap, (score, user))
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def get_top_players(self):
        # Return in descending order
        return sorted(self.min_heap, reverse=True)


def main():
    leaderboard = Leaderboard(k=3)

    leaderboard.add_score("Alice", 120)
    leaderboard.add_score("Bob", 300)
    leaderboard.add_score("Charlie", 180)
    leaderboard.add_score("David", 250)
    leaderboard.add_score("Eva", 200)

    print("\nTop Players:")
    for score, user in leaderboard.get_top_players():
        print(f"{user} | Score: {score}")


if __name__ == "__main__":
    main()
