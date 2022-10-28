import os.path


testing = False
day = '09'
if testing:
    f_input = os.path.join('inputs', f'{day}-test.txt')
else:
    f_input = os.path.join('inputs', f'input{day}.txt')

def part_one():
    rows = []
    with open(f_input) as f:
        for line in f:
            rows.append([int(x) for x in line.strip()])

    risk_level = 0

    num_rows = len(rows)
    row_length = len(rows[0])
    for i, row in enumerate(rows):
        for j, h in enumerate(row):
            if h == 9:
                continue
            if j > 0:
                if row[j] >= row[j-1]:
                    continue
            if j < row_length - 1:
                if row[j] >= row[j+1]:
                    continue
            if i > 0:
                if row[j] >= rows[i-1][j]:
                    continue
            if i < num_rows - 1:
                if row[j] >= rows[i+1][j]:
                    continue
            risk_level += 1+h
    print(risk_level)

part_one()


def part_two():
    pass