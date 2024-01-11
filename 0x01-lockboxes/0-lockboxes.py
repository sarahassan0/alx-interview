#!/usr/bin/python3

""" You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1
    and each box may contain keys to the other boxes. """


def canUnlockAll(boxes):
    """ Return True if all boxes can be opened, else return False """

    visited = set()

    def dfs(box):
        visited.add(box)

        for key in boxes[box]:
            if key not in visited:
                dfs(key)

    dfs(0)

    return len(visited) == len(rooms)
