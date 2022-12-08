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
    max_column_idx = len(data[0]) - 1
    max_row_idx = len(data) - 1
    visible_count = 0
    for i, row in enumerate(data):
        for j, tree in enumerate(row):
            if j in (0, max_column_idx) or i in (0, max_row_idx):
                visible_count += 1
                continue

            # check visibility to the left
            v_left = [x < tree for x in row[:j]]
            if all(v_left):
                visible_count += 1
                continue

            # check visibility to the right
            v_right = [x < tree for x in row[j+1:]]
            if all(v_right):
                visible_count += 1
                continue

            # check visibility up
            v_up = [x[j] < tree for x in data[:i]]
            if all(v_up):
                visible_count += 1
                continue

            # check visibility down
            v_down = [x[j] < tree for x in data[i+1:]]
            if all(v_down):
                visible_count += 1
                continue

    return visible_count


print(f'Part 1: {part1(f_input)}')



def part2(input):
    with open(input) as f:
        data = [[int(x) for x in line.strip()] for line in f]
    max_column_idx = len(data[0]) - 1
    max_row_idx = len(data) - 1
    max_scenic_score = 0
    for i, row in enumerate(data):
        for j, tree in enumerate(row):
            # left view_distance
            lvd = 0
            if j == 0:
                lvd = 0
            else:
                v_left = [x for x in row[:j]]
                while v_left:
                    tmp = v_left.pop()
                    if tmp < tree:
                        lvd += 1
                    else:
                        lvd += 1
                        break

            # right view_distance
            rvd = 0
            if j == max_column_idx:
                rvd = 0
            else:
                v_right = [x for x in row[j+1:]]
                while v_right:
                    tmp = v_right.pop(0)
                    if tmp < tree:
                        rvd += 1
                    else:
                        rvd += 1
                        break
            
            # up view_distance
            uvd = 0
            if i == 0:
                uvd = 0
            else:
                v_up = [x[j] for x in data[:i]]
                while v_up:
                    tmp = v_up.pop()
                    if tmp < tree:
                        uvd += 1
                    else:
                        uvd += 1
                        break
            
            # down view_distance
            dvd = 0
            if i == max_row_idx:
                dvd = 0
            else:
                v_down = [x[j] for x in data[i+1:]]
                while v_down:
                    tmp = v_down.pop(0)
                    if tmp < tree:
                        dvd += 1
                    else:
                        dvd += 1
                        break

            scenic_score = lvd * rvd * uvd * dvd
            max_scenic_score = max(scenic_score, max_scenic_score)

    return max_scenic_score


print(f'Part 2: {part2(f_input)}')
