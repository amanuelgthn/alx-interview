#!/usr/bin/python3
"""
Function that returns the perimeter of the island described in grid
grid is a list of integers
    *0 represents water
    *1 represents land
    *Each cell is square, with a side length of 1
    *Cells are connected horizontally/vertically (not diagonally).
    *grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
There is only one island (or nothing).
The island doesn’t have “lakes” (water inside that isn’t
connected to the water surrounding the island).
"""


def island_perimeter(grid):
    """
    function that returns the perimeter of the island described in
    gird
    """
    count = 0
    length = len(grid)
    length_row = len(grid[0])
    for i in range(len(grid)):
        for j in range(length_row):
            if (grid[i][j] == 1):
                if i == 0 or j == 0 or j == length_row - 1 or i == length - 1:
                    count += 1
                if (grid[i-1][j] == 0):
                    count += 1
                if i + 1 < length and (grid[i+1][j] == 0):
                    count += 1
                if j + 1 < length_row and (grid[i][j+1] == 0):
                    count += 1
                if i + 1 < length and (grid[i][j-1] == 0):
                    count += 1
    return count

