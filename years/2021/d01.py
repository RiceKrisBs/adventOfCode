import os.path


testing = False
day = '01'
if testing:
    f_input = os.path.join('inputs', f'{day}-test.txt')
else:
    f_input = os.path.join('inputs', f'input{day}.txt')

# part one
a_count = 0
previous = None
with open(f_input) as f:
    for line in f:
        if previous:
            current = int(line.strip())
            a_count += int(current > previous)
            previous = current
        else:
            previous = int(line.strip())
print(f"part one: {a_count}")

# part two
l = []
with open(f_input) as f:
    for line in f:
        l.append(int(line.strip()))

b_count = 0
previous = None
for i in range(len(l) - 2):
    if previous is not None:
        current = sum(l[i:i+3])
        b_count += int(current > previous)
        previous = current
    else:
        previous = sum(l[i:i+3])

print(f"part two: {b_count}")
