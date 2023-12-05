import re

inputs = []
input_pairs = []
maps = []
section = None


def is_overlap(r1, r2):
    if r1["range"][0] <= r2["range"][0] <= r1["range"][1]:
        return True
    if r2["range"][0] <= r1["range"][0] <= r2["range"][1]:
        return True
    return False


def split_ranges(r1, r2):
    middle = {}
    if r1["range"][0] <= r2["range"][0]:
        start = r1
        end = r2
    else:
        start = r2
        end = r1

    if start["range"][0] == end["range"][0] and start["range"][1] == end["range"][1]:
        start["offset"] = start["offset"] + end["offset"]
        return [start]

    if start["range"][0] == end["range"][0]:
        if (start["range"][1] < end["range"][1]):
            end["range"] = (start["range"][1] + 1, end["range"][1])
            start["offset"] = start["offset"] + end["offset"]
        else:
            start["range"] = (end["range"][1] + 1, start["range"][1])
            end["offset"] = start["offset"] + end["offset"]
        return [start, end]

    if start["range"][1] == end["range"][1]:
        start["range"] = (start["range"][0], end["range"][0] - 1)
        end["range"] = (end["range"][0], end["range"][1])
        end["offset"] = start["offset"] + end["offset"]
        return [start, end]

    if start["range"][1] > end["range"][1]:
        middle["range"] = (end["range"][0], end["range"][1])
        middle["offset"] = start["offset"] + end["offset"]
        end["range"] = (end["range"][1] + 1, start["range"][1])
        start["range"] = (start["range"][0], middle["range"][0] - 1)
        end["offset"] = start["offset"]
    else:
        middle["range"] = (end["range"][0], start["range"][1])
        start["range"] = (start["range"][0], middle["range"][0] - 1)
        end["range"] = (middle["range"][1] + 1, end["range"][1])
        middle["offset"] = start["offset"] + end["offset"]

    return [start, middle, end]


def do_map(map, value):
    for range in map:
        if range["range"][0] <= value <= range["range"][1]:
            return value + range["offset"]
    return value


with open("seeds.in.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        elif "seeds:" in line:
            inputs = [int(x) for x in line.split(":")[1].strip().split(" ")]
            input_pairs = [
                (int(x.split(" ")[0]), int(x.split(" ")[1]))
                for x in re.findall(r"(\d+ \d+)", line.split(":")[1].strip())
            ]
        elif "map:" in line:
            if section:
                maps.append(section)
            sections = re.match(r"^(.*)-to-(.*) map:$", line)
            section = {
                "from": sections.groups()[0],
                "to": sections.groups()[1],
                "ranges": [],
            }
        else:
            values = [int(x) for x in line.split(" ")]
            section["ranges"].append(
                {
                    "range": (values[1], values[1] + values[2]),
                    "offset": values[0] - values[1],
                }
            )
    maps.append(section)

master_range = []
for section in maps:
    for range in section["ranges"]:
        concat = []
        for mrange in master_range:
            #print(is_overlap(range, mrange), range, mrange)
            if is_overlap(range, mrange):
                #print("removing", mrange, range)
                master_range.remove(mrange)
                adds = split_ranges(range, mrange)
                concat = concat + adds
                #print("adding", adds)
        if not len(concat):
            concat = [range]
        master_range = master_range + concat
        #print("master", master_range)
    print("new map")

print(master_range)


output = []
for input in inputs:
    #print(input, do_map(master_range, input))
    output.append(do_map(master_range, input))
out1 = min(output)

print("part 1: ", out1)
