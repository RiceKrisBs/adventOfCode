import os.path
from collections import deque

testing = False
day = '12'
if not day:
    raise OSError('Set the day!')

if testing:
    f_input = os.path.join('inputs', f'input{day}-test.txt')
else:
    f_input = os.path.join('inputs', f'input{day}.txt')

def custom_ord(char):
    if char == 'S':
        return ord('a') - 1 # 96
    if char == 'E':
        return ord('z') + 1 # 123
    return ord(char)

def search(start_pos, end_pos, graph, starting_options=None):
    visited = set()
    queue = deque()
    parent = {}

    if starting_options:
        for option in starting_options:
            queue.append(option)
            visited.add(option)
            parent[option] = None
    else:
        queue.append(start_pos)
        visited.add(start_pos)
        parent[start_pos] = None

    path_found = False
    while queue:
        current_pos = queue.popleft()
        if current_pos == end_pos:
            path_found = True
            break
        for next_pos in graph[current_pos]:
            if next_pos not in visited:
                queue.append(next_pos)
                parent[next_pos] = current_pos
                visited.add(next_pos)
    path = []
    if path_found:
        path.append(end_pos)
        while parent[end_pos] is not None:
            path.append(parent[end_pos])
            end_pos = parent[end_pos]
        path.reverse()
        # print(' -> '.join(str(x) for x in path))
    return len(path) - 1

def part1(input):
    with open(input) as f:
        data = [list(map(custom_ord, line.strip())) for line in f]

    row_limit = len(data) - 1
    column_limit = len(data[0]) - 1
    graph = {}
    S = ord('a') - 1
    E = ord('z') + 1
    for row_num, row in enumerate(data):
        for col_num, col_val in enumerate(row):
            position = (row_num, col_num)
            graph[position] = []
            if col_val == S:
                starting = position
            if col_val == E:
                ending = position

            # look left
            if col_num > 0:
                left_val = data[row_num][col_num-1]
                if left_val <= col_val + 1:
                    graph[position].append((row_num, col_num-1))

            # look right
            if col_num < column_limit:
                right_val = data[row_num][col_num+1]
                if right_val <= col_val + 1:
                    graph[position].append((row_num,col_num+1))

            # look up
            if row_num > 0:
                up_val = data[row_num-1][col_num]
                if up_val <= col_val + 1:
                    graph[position].append((row_num-1,col_num))

            # look down
            if row_num < row_limit:
                down_val = data[row_num+1][col_num]
                if down_val <= col_val + 1:
                    graph[position].append((row_num+1,col_num))

    dist = search(starting, ending, graph)
    return dist

p1_ans = part1(f_input)
print(f'Part 1: {p1_ans}')


def part2(input):
    with open(input) as f:
        data = [list(map(custom_ord, line.strip())) for line in f]

    starting_options = []
    row_limit = len(data) - 1
    column_limit = len(data[0]) - 1
    graph = {}
    S = ord('a') - 1
    E = ord('z') + 1
    for row_num, row in enumerate(data):
        for col_num, col_val in enumerate(row):
            position = (row_num, col_num)
            graph[position] = []
            if col_val == S or col_val == ord('a'):
                starting_options.append(position)
            if col_val == E:
                ending = position

            # look left
            if col_num > 0:
                left_val = data[row_num][col_num-1]
                if left_val <= col_val + 1:
                    graph[position].append((row_num, col_num-1))

            # look right
            if col_num < column_limit:
                right_val = data[row_num][col_num+1]
                if right_val <= col_val + 1:
                    graph[position].append((row_num,col_num+1))

            # look up
            if row_num > 0:
                up_val = data[row_num-1][col_num]
                if up_val <= col_val + 1:
                    graph[position].append((row_num-1,col_num))

            # look down
            if row_num < row_limit:
                down_val = data[row_num+1][col_num]
                if down_val <= col_val + 1:
                    graph[position].append((row_num+1,col_num))

    dist = search(None, ending, graph, starting_options)
    return dist

p2_ans = part2(f_input)
print(f'Part 2: {p2_ans}')
