# Day 7 - Network Traffic Analyzer
# Focus: Sliding Window
# Language: Python 3

def peak_traffic_window(traffic, window_size):
    current_sum = sum(traffic[:window_size])
    max_sum = current_sum
    start_index = 0

    for i in range(window_size, len(traffic)):
        current_sum += traffic[i] - traffic[i - window_size]

        if current_sum > max_sum:
            max_sum = current_sum
            start_index = i - window_size + 1

    return max_sum, start_index


def main():
    print("\n--- Network Traffic Analyzer ---")

    traffic = list(map(int, input(
        "Enter traffic data (space separated): "
    ).split()))

    window_size = int(input("Enter window size: "))

    peak, index = peak_traffic_window(traffic, window_size)

    print("\nPeak Traffic:", peak)
    print("Peak Window Data:", traffic[index:index + window_size])
    print("Window Start Index:", index)


if __name__ == "__main__":
    main()
