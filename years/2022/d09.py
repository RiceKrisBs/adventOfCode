import os.path

testing = False
day = '09'
if not day:
    raise OSError('Set the day!')

if testing:
    f_input = os.path.join('inputs', f'input{day}-test.txt')
else:
    f_input = os.path.join('inputs', f'input{day}.txt')


def follow_x(x, y):
    ok = set()
    ok.add((y[0]-1,y[1]+1))
    ok.add((y[0],y[1]+1))
    ok.add((y[0]+1,y[1]+1))
    ok.add((y[0]-1,y[1]))
    ok.add((y[0],y[1]))
    ok.add((y[0]+1,y[1]))
    ok.add((y[0]-1,y[1]-1))
    ok.add((y[0],y[1]-1))
    ok.add((y[0]+1,y[1]-1))
    # ok now contains all of the spaces 1 
    # away from y

    if tuple(x) in ok:
        # y doesn't need to move
        return
    if x[0] == y[0] and x[1] > y[1]:
        y[1] += 1
    elif x[0] == y[0] and x[1] < y[1]:
        y[1] -= 1
    elif x[1] == y[1] and x[0] > y[0]:
        y[0] += 1
    elif x[1] == y[1] and x[0] < y[0]:
        y[0] -= 1
    elif x[0] > y[0] and x[1] > y[1]:
        y[0] += 1
        y[1] += 1
    elif x[0] < y[0] and x[1] > y[1]:
        y[0] -= 1
        y[1] += 1
    elif x[0] < y[0] and x[1] < y[1]:
        y[0] -= 1
        y[1] -= 1
    elif x[0] > y[0] and x[1] < y[1]:
        y[0] += 1
        y[1] -= 1


def part1(input):
    with open(input) as f:
        data = [line.strip().split() for line in f]

    visited = set()
    head = [0, 0]
    tail = [0, 0]

    for direction, dist in data:
        dist = int(dist)
        if direction == 'R':
            for _ in range(dist):
                head[0] += 1
                follow_x(head, tail)
                visited.add(tuple(tail))
        
        elif direction == 'L':
            for _ in range(dist):
                head[0] -= 1
                follow_x(head, tail)
                visited.add(tuple(tail))

        elif direction == 'U':
            for _ in range(dist):
                head[1] += 1
                follow_x(head, tail)
                visited.add(tuple(tail))
        
        elif direction == 'D':
            for _ in range(dist):
                head[1] -= 1
                follow_x(head, tail)
                visited.add(tuple(tail))

    return len(visited)

p1_ans = part1(f_input)
print(f'Part 1: {p1_ans}')


def part2(input):
    with open(input) as f:
        data = [line.strip().split() for line in f]

    visited = set()
    head = [0,0]
    s1 = [0,0]
    s2 = [0,0]
    s3 = [0,0]
    s4 = [0,0]
    s5 = [0,0]
    s6 = [0,0]
    s7 = [0,0]
    s8 = [0,0]
    tail = [0,0]
    items = (head, s1, s2, s3, s4, s5, s6, s7, s8, tail)


    for direction, dist in data:
        dist = int(dist)
        if direction == 'R':
            for _ in range(dist):
                head[0] += 1
                for i in range(9):
                    x, y = items[i], items[i+1]
                    follow_x(x,y)
                visited.add(tuple(tail))
        
        elif direction == 'L':
            for _ in range(dist):
                head[0] -= 1
                for i in range(9):
                    x, y = items[i], items[i+1]
                    follow_x(x,y)
                visited.add(tuple(tail))

        elif direction == 'U':
            for _ in range(dist):
                head[1] += 1
                for i in range(9):
                    x, y = items[i], items[i+1]
                    follow_x(x,y)
                visited.add(tuple(tail))
        
        elif direction == 'D':
            for _ in range(dist):
                head[1] -= 1
                for i in range(9):
                    x, y = items[i], items[i+1]
                    follow_x(x,y)
                visited.add(tuple(tail))

    return len(visited)

p2_ans = part2(f_input)
print(f'Part 2: {p2_ans}')
