# Day 21 - Meeting Room Booking System
# Focus: Merge Intervals
# Language: Python 3


def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]

        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged


def main():
    meetings = [
        [9, 10],
        [9.5, 11],
        [13, 14],
        [12, 13.5],
        [15, 16]
    ]

    print("\nOriginal Meetings:")
    for m in meetings:
        print(m)

    merged_meetings = merge_intervals(meetings)

    print("\nMerged Meeting Schedule:")
    for m in merged_meetings:
        print(m)


if __name__ == "__main__":
    main()
