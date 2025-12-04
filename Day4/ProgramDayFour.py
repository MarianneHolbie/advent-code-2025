# Advent of Code 2025 - Day4

#####################
#     Part One      #
#####################

import numpy as np

def process_file(path='input'):
    accessible = 0
    # all adjacent positions
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    with open(path, 'r') as f:
        # transform in grid
        grid = [list(line.strip()) for line in f]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '@':
                    adj_arobase = 0
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                            if grid[ni][nj] == '@':
                                adj_arobase += 1
                    if adj_arobase < 4:
                        accessible += 1
    return accessible


#####################
#     Part Two      #
#####################




def process_file_part2(path='input'):
    remove = True
    accessible = 0
    # all adjacent positions
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    with open(path, 'r') as f:
        # transform in grid
        grid = [list(line.strip()) for line in f]
        while remove:
            remove = False
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == '@':
                        adj_arobase = 0
                        for di, dj in directions:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                                if grid[ni][nj] == '@':
                                    adj_arobase += 1
                        if adj_arobase < 4:
                            accessible += 1
                            grid[i][j] = '.'
                            remove = True
    return accessible


if __name__ == '__main__':
    print(process_file('input'))
    print(process_file_part2('input'))


