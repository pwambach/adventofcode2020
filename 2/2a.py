# docker run --rm -v $PWD:/workdir -w /workdir python:3.9-slim 2a.py

import re

with open("input") as f:
    count = 0

    for item in [re.split("-|:\s|\s", line) for line in f.readlines()]:
        min, max, char, word = item[0:4]
        i = word.count(char)
        if i >= int(min) and i <= int(max):
            count += 1

    print(count)
