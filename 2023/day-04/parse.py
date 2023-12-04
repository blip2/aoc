import re

value = 0
total = 0

cards = {}

with open("cards.in.txt") as f:
    for line in f:
        line_id = int(line.split(":")[0][4:])
        numbers = line.split(":")[1].split("|")
        cards[line_id] = {'winning': re.split(r"\s+", numbers[0].strip()), 'numbers': re.split(r"\s+", numbers[1].strip()), 'value': 0, 'matches': 0, 'count': 1}       
        for num in cards[line_id]['numbers']:
            if num in cards[line_id]['winning']:
                cards[line_id]['matches'] += 1
                if cards[line_id]['value']:
                    cards[line_id]['value'] = cards[line_id]['value'] * 2
                else:
                    cards[line_id]['value'] = 1
        value += cards[line_id]['value']
    
for card in cards:
    for match in range(cards[card]['matches']):
        cards[int(card)+int(match)+1]['count'] += cards[card]['count']
    total += cards[card]['count']

print("part 1: ", value)
print("part 2: ", total)
