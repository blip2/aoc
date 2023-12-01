import re

value = 0
count = 0
lines = 0

replace = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e"
}

with open("input.txt") as f:
    for line in f:
        lines += 1
        repline = line
        for r in replace:
            repline = repline.replace(r, replace[r])
        z = re.match(r"^[a-z]*([0-9])?.*?([0-9])?[a-z]*$", repline)
        if z:
            if z.groups()[1]:
                add = int(z.groups()[0] + z.groups()[1])
            else:
                add = int(z.groups()[0] + z.groups()[0])
            value = value + add
            if add:
                count += 1
            print(line, repline, z.groups(), add, value)

print(value, lines, count)
