import os.path

testing = False
day = '06'
if testing:
    f_input = os.path.join('inputs', f'input{day}-test.txt')
else:
    f_input = os.path.join('inputs', f'input{day}.txt')

def part1(input):
    with open(input) as f:
        data = [line.strip() for line in f]
    word = data[0]

    for i in range(4, len(word)+1):
        sub = word[i-4:i]
        s = set(x for x in sub)
        if len(s) == 4:
            return i

print(f'Part 1: {part1(f_input)}')


def part2(input):
    with open(input) as f:
        data = [line.strip() for line in f]
    word = data[0]

    for i in range(14, len(word)+1):
        sub = word[i-14:i]
        s = set(x for x in sub)
        if len(s) == 14:
            return i

print(f'Part 2: {part2(f_input)}')
