total = 0
matrix = []
numbers = []
gears = []
gear_total = 0

non_symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]

with open("engine.in.txt") as f:
    for line in f:
        matrix.append(line)

for row in range(len(matrix)):
    start = None
    text = ""

    for char in range(len(matrix[row])):
        value = matrix[row][char]
        if value.isdigit():
            if not start:
                start = char
            text = text + value
        else:
            if start:
                special_char = False
                x_range = range(max(0,start-1), min(char+1,len(matrix)))
                #print(max(0,start-1), min(char+1,len(matrix)), list(x_range))
                
                y_range = range(max(0,row-1), min(row+2,len(matrix[row])))
                #print(max(0,row-1), min(row+2,len(matrix[row])), list(y_range))

                for y in y_range:
                    for x in x_range:
                        check = matrix[y][x]
                        #print(x, y, check)
                        if check not in non_symbols:
                            special_char = True

                        if check == "*":
                            gears.append({"x": row, "y": char, "x*": x, "y*": y, "value": int(text)})


                if special_char:
                    total +=  int(text)

                start = None
                text = ""

confirmed_gears = {}

for poss_gear in gears:
    for check in gears:
        if (poss_gear['x*'] == check['x*'] and poss_gear['y*'] == check['y*'] and (poss_gear['x'], poss_gear['y']) != (check['x'], check['y'])):
            confirmed_gears[str(poss_gear['x*']) + '/' + str(poss_gear['y*'])] = int(poss_gear['value']) * int(check['value'])

gear_total = sum(confirmed_gears.values())

print("part 1: ", total)
print("part 2: ", gear_total)
