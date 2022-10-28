import os.path
import re

possible = 0
triangles = []

with open(os.path.join('inputs', 'input03.txt'), 'r') as f:
    for line in f:
        line = re.sub(r'\s+', ',', line.strip())
        line = [int(x) for x in line.split(',')]
        triangles.append(line)

for i in range(0, len(triangles), 3):
    for t in range(3):
        triangle = [triangles[i][t], triangles[i+1][t], triangles[i+2][t]]
        triangle.sort()
        if triangle[0] + triangle[1] > triangle[2]:
            possible += 1

print(possible)
