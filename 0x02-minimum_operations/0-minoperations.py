#!/usr/bin/python3

def minOperations(n):
    if n <= 1:
        return n

    operations = [float('inf')] * (n + 1)
    operations[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                operations[i] = min(operations[i], operations[j] + (i // j))

    return operations[n]

# Test cases
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

