# Day 8 - Ride-Sharing Pair Matcher
# Focus: Two Pointers
# Language: Python 3

def closest_pair(pickups, drops):
    pickups.sort()
    drops.sort()

    i = j = 0
    min_diff = float("inf")
    best_pair = None

    while i < len(pickups) and j < len(drops):
        diff = abs(pickups[i] - drops[j])

        if diff < min_diff:
            min_diff = diff
            best_pair = (pickups[i], drops[j])

        if pickups[i] < drops[j]:
            i += 1
        else:
            j += 1

    return best_pair, min_diff


def main():
    print("\n--- Ride-Sharing Pair Matcher ---")

    pickups = list(map(int, input(
        "Enter pickup locations (space separated): "
    ).split()))

    drops = list(map(int, input(
        "Enter drop locations (space separated): "
    ).split()))

    pair, distance = closest_pair(pickups, drops)

    print("\nBest Pickup-Drop Pair:", pair)
    print("Minimum Distance:", distance)


if __name__ == "__main__":
    main()
