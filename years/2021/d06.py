import os.path


testing = False
day = '06'
if testing:
    f_input = os.path.join('inputs', f'{day}-test.txt')
else:
    f_input = os.path.join('inputs', f'input{day}.txt')

def ans(days):
    d = {i:0 for i in range(9)}
    with open(f_input) as f:
        l = f.readline()
        for x in l.split(','):
            i = int(x)
            d[i] += 1
    
    for _ in range(days):
        e = d.copy()
        d.clear()
        d[0] = e[1]
        d[1] = e[2]
        d[2] = e[3]
        d[3] = e[4]
        d[4] = e[5]
        d[5] = e[6]
        d[6] = e[7] + e[0]
        d[7] = e[8]
        d[8] = e[0]
    print(sum(x for x in d.values()))


# part one
ans(80)

# part two
ans(256)
