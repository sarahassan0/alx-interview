#!/usr/bin/python3

""" You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1
    and each box may contain keys to the other boxes. """

# this sloution is valid but it has stack overflow when the size of input is 1000 boxes
def canUnlockAll(boxes):
    """ Return True if all boxes can be opened, else return False """
    if boxes is None:
        return False

    visited = set()

    def dfs(box):

        visited.add(box)

        for key in boxes[box]:
            if key < len(boxes) and key not in visited:
                dfs(key)

    dfs(0)

    return len(visited) == len(boxes)
