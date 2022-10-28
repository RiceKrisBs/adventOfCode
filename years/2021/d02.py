import os.path


testing = False
day = '02'
if testing:
    f_input = os.path.join('inputs', f'{day}-test.txt')
else:
    f_input = os.path.join('inputs', f'input{day}.txt')


dirs = []
with open(f_input) as f:
    for line in f:
        d, v = line.strip().split()
        dirs.append((d, int(v)))

# part one
horizontal, vertical = 0, 0
for d, v in dirs:
    if d == 'forward':
        horizontal += v
    elif d == 'down':
        vertical += v
    elif d == 'up':
        vertical -= v
print(f"part one: {horizontal * vertical}")

# part two
horizontal, vertical, aim = 0, 0, 0
for d, v in dirs:
    if d == 'forward':
        horizontal += v
        vertical += aim * v
    elif d == 'down':
        aim += v
    elif d == 'up':
        aim -= v

print(f"part two: {horizontal * vertical}")
