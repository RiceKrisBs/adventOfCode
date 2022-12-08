import os.path

testing = False
day = '08'
if not day:
    raise OSError('Set the day!')

if testing:
    f_input = os.path.join('inputs', f'input{day}-test.txt')
else:
    f_input = os.path.join('inputs', f'input{day}.txt')

def part1(input):
    with open(input) as f:
        data = [[int(x) for x in line.strip()] for line in f]
    visible_count = 0
    for i, row in enumerate(data):
        for j, tree in enumerate(row):
            v_left = [x < tree for x in row[:j]]
            v_right = [x < tree for x in row[j+1:]]
            v_up = [x[j] < tree for x in data[:i]]
            v_down = [x[j] < tree for x in data[i+1:]]

            if all(v_left) or all(v_right) or all(v_up) or all(v_down):
                visible_count += 1

    return visible_count

print(f'Part 1: {part1(f_input)}')



def part2(input):
    with open(input) as f:
        data = [[int(x) for x in line.strip()] for line in f]
    max_column_idx = len(data[0]) - 1
    max_row_idx = len(data) - 1
    max_scenic_score = 0
    for i, row in enumerate(data):
        if i in (0, max_row_idx):
            continue
        for j, tree in enumerate(row):
            if j in (0, max_column_idx):
                continue

            lvd = rvd = uvd = dvd = 0

            # left view_distance
            v_left = [x for x in row[:j]]
            while v_left:
                lvd += 1
                tmp = v_left.pop()
                if tmp >= tree:
                    break

            # right view_distance
            v_right = [x for x in row[j+1:]]
            v_right.reverse()
            while v_right:
                rvd += 1
                tmp = v_right.pop()
                if tmp >= tree:
                    break
            
            # up view_distance
            v_up = [x[j] for x in data[:i]]
            while v_up:
                uvd += 1
                tmp = v_up.pop()
                if tmp >= tree:
                    break
            
            # down view_distance
            v_down = [x[j] for x in data[i+1:]]
            v_down.reverse()
            while v_down:
                dvd += 1
                tmp = v_down.pop()
                if tmp >= tree:
                    break

            scenic_score = lvd * rvd * uvd * dvd
            max_scenic_score = max(scenic_score, max_scenic_score)

    return max_scenic_score

print(f'Part 2: {part2(f_input)}')
