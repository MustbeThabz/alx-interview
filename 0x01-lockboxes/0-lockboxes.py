#!/usr/bin/python3
"""
Module for Lockboxes problem.

This module provides a function `canUnlockAll` to determine if all the boxes can be opened.

The function takes a list of lists `boxes`, where each sublist represents a box, and each element
in the sublist represents a key.

Example:
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Output: True
"""

def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
        boxes (list of lists): A list of lists where each sublist represents a box,
        and each element in the sublist represents a key.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = [False] * n
    stack = [0]  # Start with the first box (box 0).

    while stack:
        box = stack.pop()
        visited[box] = True

        for key in boxes[box]:
            if key < n and not visited[key]:
                stack.append(key)

    return all(visited)

if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))

