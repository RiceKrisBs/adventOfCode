import collections
import os.path


class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [['.' for x in range(self.width)] for y in range(self.height)]

    def __str__(self):
        picture = ''
        for row in self.grid:
            picture += ''.join(row) + '\n'
        return picture

    def rect(self, a, b):
        for row in self.grid[:b]:
            for i in range(a):
                row[i] = '#'

    def rotate_row(self, a, b):
        row_copy = collections.deque(self.grid[a])
        row_copy.rotate(b)
        self.grid[a] = [x for x in row_copy]

    def rotate_col(self, a, b):
        col_values = collections.deque([col[a] for col in self.grid])
        col_values.rotate(b)
        for row in self.grid:
            row[a] = col_values.popleft()

    def parse_directions(self, directions):
        direction = directions.strip().split()
        # print(direction)
        if direction[0] == 'rect':
            a, b = direction[1].split('x')
            self.rect(int(a), int(b))
        else:
            b = direction[-1]
            _, a = direction[2].split('=')
            if direction[1] == 'column':
                self.rotate_col(int(a), int(b))
            else:
                self.rotate_row(int(a), int(b))
        # print(self.__str__())

    def count_pixels(self):
        c = 0
        for row in self.grid:
            c += row.count('#')
        return c





width = 50
height = 6

# width = 7
# height = 3


# screen = Screen(width, height)
# print(screen)
# screen.rect(2,3)
# print(screen)
# screen.rotate_row(0,1)
# print(screen)
# screen.rotate_col(0,4)
# print(screen)

with open(os.path.join('inputs', 'input08.txt'), 'r') as f:
    screen = Screen(width, height)
    for line in f:
        screen.parse_directions(line)
    print(screen)
    print(screen.count_pixels())
