import os.path

testing = False
day = '03'
if testing:
    f_input = os.path.join('inputs', f'input{day}-test.txt')
else:
    f_input = os.path.join('inputs', f'input{day}.txt')

def part1(input):
    with open(input) as f:
        rucksacks = [line.strip() for line in f]
    priorities_sum = 0
    for rucksack in rucksacks:
        halfway = len(rucksack) // 2
        c1, c2 = rucksack[:halfway], rucksack[halfway:]
        for char in c1:
            if char in c2:
                shared_item = char
                break

        priorities_sum += calculate_letter_value(shared_item)

    return priorities_sum

def calculate_letter_value(char):
    if char.islower():
        return ord(char) - 96
    return ord(char) - 38

print('Part 1: ', part1(f_input))

def part2(input):
    with open(input) as f:
        data = [line.strip() for line in f]
    priorities_sum = 0
    index = 0
    while index < len(data):
        rucksacks = data[index:index+3]
        for char in rucksacks[0]:
            if sum(char in rucksack for rucksack in rucksacks) == 3:
                priorities_sum += calculate_letter_value(char)
                break
        index += 3

    return priorities_sum

print('Part 2: ', part2(f_input))
