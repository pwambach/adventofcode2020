# docker run --rm -v $PWD:/workdir -w /workdir python:3.9-slim python 2b.py

import re

with open("input") as f:
    count = 0

    for item in [re.split("-|:\s|\s", line) for line in f.readlines()]:
        pos1, pos2, char, word = item[0:4]
        c1 = word[int(pos1) - 1]
        c2 = word[int(pos2) - 1]
        if [c1, c2].count(char) == 1:
            count += 1

    print(count)
