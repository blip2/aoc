import re

value = 0
sum = 0

limits = {
    "red": 12,
    "blue": 14,
    "green": 13,
}

with open("stones.in.txt") as f:
    for line in f:
        line_id = line.split(":")[0][4:]
        valid = True
        game = {"red": 0, "blue": 0, "green": 0}
        hands = line.split(":")[1].split(";")
        for hand in hands:
            stones = hand.split(",")
            for stone in stones:
                num = re.match(r"\s*([0-9]+)\s+([a-z]+)\s*", stone)
                if num:
                    count = int(num.groups()[0])
                    color = num.groups()[1]
                    if int(count) > limits[color]:
                        valid = False
                    if count > game[color]:
                        game[color] = count
        if valid:
            value += int(line_id)
        sum += game["red"] * game["blue"] * game["green"]

        # game[num.groups()[1]] += int(num.groups()[0])

        print(line_id, game)

print("part 1: ", value)
print("part 2: ", sum)
