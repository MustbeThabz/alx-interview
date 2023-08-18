#!/usr/bin/python3
import sys

def print_statistics(total_size, status_counts):
    print("File size: {}".format(total_size))
    for status_code, count in sorted(status_counts.items()):
        print("{}: {}".format(status_code, count))

def main():
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            parts = line.split(" ")
            if len(parts) < 9:
                continue

            ip, _, _, _, status_code, file_size = parts[0], parts[8], parts[-2], parts[-1]

            if not ip or not status_code.isdigit() or not file_size.isdigit():
                continue

            total_size += int(file_size)

            if status_code in status_counts:
                status_counts[status_code] += 1
            else:
                status_counts[status_code] = 1

            if i % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)

main()

