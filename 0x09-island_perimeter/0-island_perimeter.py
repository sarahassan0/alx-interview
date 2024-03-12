#!/usr/bin/python3
""" Island_perimeter problem module """


def island_perimeter(grid):
    """
        Returns the perimeter of the island described in grid where:
        grid is a list of list of integers:
        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally)
    """
    perimeter = 0

    for r in range(len(grid)):
        perimeter += sum(grid[r]) * 4

        for c in range(len(grid[r])):

            if c > 0 and grid[r][c-1] == 1 == grid[r][c]:
                perimeter -= 2

            if r > 0 and grid[r-1][c] == 1 == grid[r][c]:
                perimeter -= 2

    return perimeter
