import collections
import os.path


testing = False
day = '03'
if testing:
    f_input = os.path.join('inputs', f'{day}-test.txt')
    l = 5
else:
    f_input = os.path.join('inputs', f'input{day}.txt')
    l = 12


def part_one():
    digits = {i: '' for i in range(l)}

    with open(f_input) as f:
        for line in f:
            for i, v in enumerate(line.strip()):
                digits[i] += v

    gamma = ['_' for _ in range(l)]
    epsilon = ['_' for _ in range(l)]
    for k, v in digits.items():
        c = collections.Counter(v)
        gamma[k] = c.most_common(1)[0][0]
        epsilon[k] = c.most_common(len(c))[-1][0]

    g_int = int(''.join(gamma),2)
    e_int = int(''.join(epsilon),2)
    print(g_int*e_int)
part_one()


def part_two():
    oxygen = []
    c02 = []
    with open(f_input) as f:
        for line in f:
            oxygen.append(line.strip())
            c02.append(line.strip())
    
    i = 0
    while len(oxygen) > 1:
        oxygen_copy = oxygen[:]
        bits = [num[i] for num in oxygen]
        ones = bits.count('1')
        zeroes = bits.count('0')
        target = '1' if ones >= zeroes else '0'
        for num in oxygen_copy:
            if num[i] != target:
                oxygen.remove(num)
        i += 1
    ogr = oxygen[0]

    j = 0
    while len(c02) > 1:
        c02_copy = c02[:]
        bits = [num[j] for num in c02]
        ones = bits.count('1')
        zeroes = bits.count('0')
        target = '0' if zeroes <= ones else '1'
        for num in c02_copy:
            if num[j] != target:
                c02.remove(num)
        j += 1
    csr = c02[0]
    print(int(ogr,2)*int(csr,2))


part_two()
