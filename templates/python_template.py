import os.path

testing = True
day = '01'
if testing:
    f_input = os.path.join('inputs', f'input{day}-test.txt')
else:
    f_input = os.path.join('inputs', f'input{day}.txt')

def part1(input):
    with open(input) as f:
        data = [line.strip() for line in f]

print(f'Part 1: {part1(f_input)}')