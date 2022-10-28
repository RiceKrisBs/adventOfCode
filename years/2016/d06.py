import collections
import os.path

test = [
    'eedadn',
    'drvtee',
    'eandsr',
    'raavrd',
    'atevrs',
    'tsrnev',
    'sdttsa',
    'rasrtv',
    'nssdts',
    'ntnada',
    'svetve',
    'tesnvt',
    'vntsnd',
    'vrdear',
    'dvrsen',
    'enarar'
]

# letters = {i: '' for i in range(6)}


# for line in test:
#     for i in range(len(line)):
#         letters[i] += line[i]

# msg = ['_' for _ in range(6)]

# for k,v in letters.items():
#     c = collections.Counter(v)
#     # print(c.most_common(len(c)))
#     msg[k] = c.most_common(len(c))[-1][0]

# print(''.join(msg))

letters = {i: '' for i in range(8)}

with open(os.path.join('inputs', 'input06.txt'), 'r') as f:
    for line in f:
        line = line.strip()
        for i in range(len(line)):
            letters[i] += line[i]

msg = ['_' for _ in range(8)]

for k,v in letters.items():
    c = collections.Counter(v)
    msg[k] = c.most_common(len(c))[-1][0]

nb = ''.join(msg)
print(nb)
