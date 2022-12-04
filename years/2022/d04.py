import os.path

testing = False
day = '04'
if testing:
    f_input = os.path.join('inputs', f'input{day}-test.txt')
else:
    f_input = os.path.join('inputs', f'input{day}.txt')

def part1(input):
    with open(input) as f:
        data = [line.split(',') for line in f]
    counter = 0
    for elf1, elf2 in data:
        e1a, e1b = map(int, elf1.split('-'))
        e2a, e2b = map(int, elf2.split('-'))
        if e1a >= e2a and e1b <= e2b:
            counter += 1
        elif e2a >= e1a and e2b <= e1b:
            counter += 1
    return counter

print('Part 1:', part1(f_input))

def part2(input):
    with open(input) as f:
        data = [line.split(',') for line in f]
    counter = 0
    for elf1, elf2 in data:
        e1a, e1b = map(int, elf1.split('-'))
        e2a, e2b = map(int, elf2.split('-'))
        if e2a <= e1a <= e2b or e2a <= e1b <= e2b:
            counter += 1
        elif e1a <= e2a <= e1b or e1a <= e2b <= e1b:
            counter += 1
    return counter

print('Part 2:', part2(f_input))
