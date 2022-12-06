import os.path

testing = False
day = '05'
if testing:
    f_input = os.path.join('inputs', f'input{day}-test.txt')
else:
    f_input = os.path.join('inputs', f'input{day}.txt')

def part1(input):
    stacks = {1: ['B', 'Q', 'C'],
              2: ['R', 'Q', 'W', 'Z'],
              3: ['B', 'M', 'R', 'L', 'V'],
              4: ['C', 'Z', 'H', 'V', 'T', 'W'],
              5: ['D', 'Z', 'H', 'B', 'N', 'V', 'G'],
              6: ['H', 'N', 'P', 'C', 'J', 'F', 'V', 'Q'],
              7: ['D', 'G', 'T', 'R', 'W', 'Z', 'S'],
              8: ['C', 'G', 'M', 'N', 'B', 'W', 'Z', 'P'],
              9: ['N', 'J', 'B', 'M', 'W', 'Q', 'F', 'P']}
    with open(input) as f:
        for line in f:
            if 'move' not in line:
                continue

            h1, h2 = line.strip().split(' from ')
            num = int(h1.split()[-1])
            temp = h2.split(' to ')
            start_stack = int(temp[0])
            end_stack = int(temp[1])

            for _ in range(num):
                tmp = stacks[start_stack].pop()
                stacks[end_stack].append(tmp)

    return ''.join(stacks[i][-1] for i in range(1, 10))

print(f'Part 1: {part1(f_input)}')


def part2(input):
    stacks = {1: ['B', 'Q', 'C'],
              2: ['R', 'Q', 'W', 'Z'],
              3: ['B', 'M', 'R', 'L', 'V'],
              4: ['C', 'Z', 'H', 'V', 'T', 'W'],
              5: ['D', 'Z', 'H', 'B', 'N', 'V', 'G'],
              6: ['H', 'N', 'P', 'C', 'J', 'F', 'V', 'Q'],
              7: ['D', 'G', 'T', 'R', 'W', 'Z', 'S'],
              8: ['C', 'G', 'M', 'N', 'B', 'W', 'Z', 'P'],
              9: ['N', 'J', 'B', 'M', 'W', 'Q', 'F', 'P']}
    with open(input) as f:
        for line in f:
            if 'move' not in line:
                continue
            h1, h2 = line.strip().split(' from ')
            num = int(h1.split()[-1])
            temp = h2.split(' to ')
            start_stack = int(temp[0])
            end_stack = int(temp[1])

            placeholder = []
            for _ in range(num):
                tmp = stacks[start_stack].pop()
                placeholder.append(tmp)

            placeholder.reverse()
            stacks[end_stack].extend(placeholder)

    return ''.join(stacks[i][-1] for i in range(1, 10))

print(f'Part 2: {part2(f_input)}')
