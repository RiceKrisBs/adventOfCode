import os.path

testing = False
day = '01'
if testing:
    f_input = os.path.join('inputs', f'input{day}-test.txt')
else:
    f_input = os.path.join('inputs', f'input{day}.txt')

def part_one(input):
    with open(input) as f:
        pass

print('Part one: ', part_one(f_input))


def part_two(input):
    with open(input) as f:
        pass

print('Part two: ', part_one(f_input))
