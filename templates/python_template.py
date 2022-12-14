import os.path

testing = True
day = ''
if not day:
    raise OSError('Set the day!')

if testing:
    f_input = os.path.join('inputs', f'input{day}-test.txt')
else:
    f_input = os.path.join('inputs', f'input{day}.txt')

def part1(input):
    with open(input) as f:
        data = [line.strip() for line in f]

p1_ans = part1(f_input)
print(f'Part 1: {p1_ans}')
