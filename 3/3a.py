# docker run --rm -v $PWD:/workdir -w /workdir python:3.9-slim python 3a.py

with open("input") as f:
    grid = f.readlines()

    x = 0
    y = 0
    trees = 0

    while y < len(grid) - 1:
        x = (x + 3) % (len(grid[0]) - 1)
        y += 1

        if grid[y][x] == "#":
            trees += 1

    print(trees)
