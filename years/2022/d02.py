import os.path

testing = False
day = '02'
if testing:
    f_input = os.path.join('inputs', f'input{day}-test.txt')
else:
    f_input = os.path.join('inputs', f'input{day}.txt')

def part1(input):
    with open(input) as f:
        data = [line.strip().split() for line in f]
    score = 0
    i_win = {'X': 'C', 'Y': 'A', 'Z': 'B'}
    tie = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    score_map = {'X': 1, 'Y': 2, 'Z': 3}
    
    for opp, me in data:
        if opp == tie[me]:
            score += 3
        elif opp == i_win[me]:
            score += 6
        score += score_map[me]

    return score

print('Part one: ', part1(f_input))



def part2(input):
    with open(input) as f:
        data = [line.strip().split() for line in f]
    score = 0
    i_win = {'C': 'X', 'A': 'Y', 'B': 'Z'}
    they_win = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    tie = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    score_map = {'X': 1, 'Y': 2, 'Z': 3}
    
    for opp, res in data:
        if res == 'X':
            me = they_win[opp]
        elif res == 'Y':
            score += 3
            me = tie[opp]
        else:
            score += 6
            me = i_win[opp]
        score += score_map[me]

    return score

print('Part two: ', part2(f_input))
