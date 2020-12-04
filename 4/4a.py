# docker run --rm -v $PWD:/workdir -w /workdir python:3.9-slim python 4a.py

import re

with open("input") as f:
    list = [re.split(" |\\n", item) for item in f.read().strip().split("\n\n")]
    passports = [dict([pair.split(":") for pair in item]) for item in list]

    valid = 0

    for passport in passports:
        if len(passport) == 8 or (len(passport) == 7 and passport.get("cid") == None):
            valid += 1

    print(valid)
