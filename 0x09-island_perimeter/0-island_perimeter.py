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
    count = 0
    length = len(grid)
    length_row = len(grid[0])
    for i in range(len(grid)):
        for j in range(length_row):
            if (grid[i][j] == 1):
                try:
                    if (grid[i-1][j] == 0):
                        count += 1
                except IndexError:
                    count += 1
                try:
                    if (grid[i+1][j] == 0):
                        count += 1
                except IndexError:
                    count += 1
                try:
                    if (grid[i][j+1] == 0):
                        count += 1
                except IndexError:
                    count += 1
                try:
                    if (grid[i][j-1] == 0):
                        count += 1
                except IndexError:
                    count += 1
    return count
