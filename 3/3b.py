# docker run --rm -v $PWD:/workdir -w /workdir python:3.9-slim python 3b.py

from functools import reduce


def countTrees(grid, slope):
    x_s, y_s = slope
    x = 0
    y = 0
    trees = 0

    while y < len(grid) - 1:
        x = (x + x_s) % (len(grid[0]) - 1)
        y += y_s

        if grid[y][x] == "#":
            trees += 1

    return trees


with open("input") as f:
    grid = f.readlines()
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    trees = [countTrees(grid, slope) for slope in slopes]
    result = reduce((lambda x, y: x * y), trees)
    print(result)
