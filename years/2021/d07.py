import os.path
import statistics

testing = False
day = '07'
if testing:
    f_input = os.path.join('inputs', f'{day}-test.txt')
else:
    f_input = os.path.join('inputs', f'input{day}.txt')

def part_one():
    with open(f_input) as f:
        line = f.readline()
        line = [int(x) for x in line.split(',')]
    m = int(statistics.median(line))
    s = 0
    for i in line:
        s += abs(i - m)
    print(s)

part_one()


def part_two():
    with open(f_input) as f:
        line = f.readline()
        line = [int(x) for x in line.split(',')]
    m = int(statistics.mean(line))
    s = 0
    for i in line:
        n = abs(i - m)
        s += (n*(n+1))/2
    print(int(s))

part_two()
