#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid1 = [[0, 1, 0, 0, 0, 1],[1, 1, 0, 0, 0, 1],[1, 1, 0, 1, 1, 1],[0, 1, 1, 1, 0, 0],[0, 0, 1, 1, 0, 0]]
    grid9 = [[0, 0, 0, 0, 0, 0],[0, 1, 1, 0, 0, 0],[1, 1, 1, 0, 0, 0],[0, 1, 1, 1, 0, 0],[0, 0, 0, 1, 1, 1]]
    grid = [
        [0, 1, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [1, 1, 0, 1, 1, 1],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0]
    ]
    grid2 = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    grid7 = [[0, 0, 0, 0, 0, 0],
             [0, 1, 1, 1, 0, 0],
             [0, 1, 1, 1, 0, 0],
             [0, 1, 1, 1, 0, 0]]
    print(island_perimeter(grid))
    print("gird7", island_perimeter(grid7))
    print("grid9", island_perimeter(grid9))
    print(island_perimeter(grid1))
    print(island_perimeter(grid2))