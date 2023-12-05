import re

inputs = []
input_pairs = []
maps = {}
section = None


def do_map(input, custom_mappings):
    for mapping in custom_mappings:
        if input >= mapping["src"] and input <= mapping["src"] + mapping["range"]:
            offset = input - mapping["src"]
            input = mapping["dest"] + offset
            break
    return input


with open("seeds.in.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        elif "seeds:" in line:
            inputs = [int(x) for x in line.split(":")[1].strip().split(" ")]
            input_pairs = [(int(x.split(' ')[0]), int(x.split(' ')[1])) for x in re.findall(r"(\d+ \d+)", line.split(":")[1].strip())]
        elif "map:" in line:
            if section:
                maps[section["from"]] = section
            sections = re.match(r"^(.*)-to-(.*) map:$", line)
            section = {
                "from": sections.groups()[0],
                "to": sections.groups()[1],
                "custom_mappings": [],
            }
        else:
            values = [int(x) for x in line.split(" ")]
            section["custom_mappings"].append(
                {
                    "src": values[1],
                    "dest": values[0],
                    "range": values[2],
                }
            )
    maps[section["from"]] = section

def map_inputs(inputs):
    output = []
    for input in inputs:
        mapped_value = input
        map_type = "seed"
        while True:
            mapped_value = do_map(mapped_value, maps[map_type]["custom_mappings"])
            map_type = maps[map_type]["to"]
            if map_type == "location":
                break
        output.append(mapped_value)
    return output

out1 = min(map_inputs(inputs))

input_list = []
for pair in input_pairs:
    input_list = input_list + list(range(pair[0], pair[0]+pair[1]))

out2 = min(map_inputs(input_list))


print("part 1: ", out1)
print("part 2: ", out2)