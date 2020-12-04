# docker run --rm -v $PWD:/workdir -w /workdir python:3.9-slim python 4a.py

import re

with open("input") as f:
    list = [re.split(" |\\n", item) for item in f.read().strip().split("\n\n")]
    passports = [dict([pair.split(":") for pair in item]) for item in list]

    valid = 0

    for passport in passports:
        if len(passport) == 8 or (len(passport) == 7 and passport.get("cid") == None):
            byr = int(passport.get("byr"))
            byr = byr >= 1920 and byr <= 2002

            iyr = int(passport.get("iyr"))
            iyr = iyr >= 2010 and iyr <= 2020

            eyr = int(passport.get("eyr"))
            eyr = eyr >= 2020 and eyr <= 2030

            hgt = passport.get("hgt")
            hgt = (hgt[:-2], hgt[-2:])
            if (hgt[1] == "cm" and int(hgt[0]) >= 150 and int(hgt[0]) <= 193) or (
                hgt[1] == "in" and int(hgt[0]) >= 59 and int(hgt[0]) <= 76
            ):
                print(hgt)
                hgt = True
            else:
                hgt = False

            hcl = passport.get("hcl")
            hcl = (hcl[0:1], hcl[1:])
            hcl = hcl[0] == "#" and re.fullmatch("([a-f]|[0-9]){6}", hcl[1]) != None

            ecl = passport.get("ecl") in [
                "amb",
                "blu",
                "brn",
                "gry",
                "grn",
                "hzl",
                "oth",
            ]

            pid = passport.get("pid")
            pid = re.fullmatch("\d{9}", pid) != None

            if all([byr, iyr, eyr, hgt, hcl, ecl, pid]):
                valid += 1

    print(valid)
