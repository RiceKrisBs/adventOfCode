import os.path

testing = False
day = '10'
if not day:
    raise OSError('Set the day!')

if testing:
    f_input = os.path.join('inputs', f'input{day}-test.txt')
else:
    f_input = os.path.join('inputs', f'input{day}.txt')

def part1(input):
    with open(input) as f:
        data = [line.strip() for line in f]
    
    cycle = 1
    X = 1
    x_history = []

    for num, line in enumerate(data):
        # start of cycle
        l = line.split()

        if l[0] == 'noop':
            # during cycle
            x_history.append(X)
            # end of cycle
            cycle += 1
        else:
            # during cycle
            x_history.append(X)
            cycle += 1
            x_history.append(X)
            X += int(l[1])
            cycle += 1


    targets = [x for x in range(20, cycle, 40)]
    interests = [x_history[x-1] for x in targets]
    # print(interests)
    vals = [x*y for x,y in zip(targets, interests)]
    # print(vals)
    return sum(vals)


p1_ans = part1(f_input)
print(f'Part 1: {p1_ans}')


def part2(input):
    with open(input) as f:
        data = [line.strip() for line in f]
    
    cycle = 1
    X = 1
    board = ''
    lit = '█'
    unlit = '.'

    for num, line in enumerate(data):
        # start of cycle
        l = line.split()

        if l[0] == 'noop':
            # during cycle
            sprite = (X-1, X, X+1)
            if (cycle-1) % 40 in sprite:
                board += lit
            else:
                board += unlit
            # end of cycle
            cycle += 1
        else:


            sprite = (X-1, X, X+1)
            if (cycle-1) % 40 in sprite:
                board += lit
            else:
                board += unlit
            cycle += 1

            sprite = (X-1, X, X+1)
            if (cycle-1) % 40 in sprite:
                board += lit
            else:
                board += unlit
            X += int(l[1])
            cycle += 1

    return '\n' + '\n'.join(board[i:i+40] for i in range(0, 240, 40))

p2_ans = part2(f_input)
print(f'Part 2: {p2_ans}')
