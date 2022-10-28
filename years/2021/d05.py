import os.path


testing = False
day = '05'
if testing:
    f_input = os.path.join('inputs', f'{day}-test.txt')
else:
    f_input = os.path.join('inputs', f'input{day}.txt')

def main(part):
    all_points = dict()
    with open(f_input) as f:
        for line in f:
            line = line.strip().split(' -> ')
            a = tuple(int(x) for x in line[0].split(','))
            b = tuple(int(x) for x in line[1].split(','))
            if part == 1:
                if a[0] != b[0] and a[1] != b[1]:
                    continue
            segment_points = []
            if a[0] == b[0]:
                min_y = min(a[1], b[1])
                max_y = max(a[1], b[1])
                for y in range(min_y, max_y+1):
                    segment_points.append((a[0],y))
            elif a[1] == b[1]:
                min_x = min(a[0], b[0])
                max_x = max(a[0], b[0])
                for x in range(min_x, max_x+1):
                    segment_points.append((x,a[1]))
            else:
                min_x = min(a[0], b[0])
                max_x = max(a[0], b[0])
                if min_x == a[0]:
                    p1, p2 = a, b
                else:
                    p1, p2 = b, a
                x = p1[0]
                y = p1[1]
                if p2[1] > p1[1]:
                    while y <= p2[1]:
                        segment_points.append((x,y))
                        x += 1
                        y += 1
                else:
                    while y >= p2[1]:
                        segment_points.append((x,y))
                        x += 1
                        y -= 1

            for p in segment_points:
                if p in all_points:
                    all_points[p] += 1
                else:
                    all_points[p] = 1

    c = 0
    for _, v in all_points.items():
        if v > 1:
            c += 1
    print(c)

# part one
main(1)

# part two
main(2)
