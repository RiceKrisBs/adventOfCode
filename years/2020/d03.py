import functools
import os.path


def parse_map(file):
    toboggan_map = []
    with open(file, 'r') as f:
        for line in f:
            toboggan_map.append(line.strip())
    return toboggan_map

class Sledder:
    def __init__(self, x_move, y_move):
        self.x_pos = 0
        self.y_pos = 0
        self.x_move = x_move
        self.y_move = y_move
        self.trees_hit = 0
        self.safe_moves = 0

    def take_next_move(self, next_row):
        next_x_pos = self.x_pos + self.x_move
        if next_x_pos >= len(next_row):
            next_x_pos = next_x_pos % len(next_row)
        self.x_pos = next_x_pos
        self.y_pos += self.y_move
        return next_row[self.x_pos]

    def check_result(self, spot):
        if spot == '#':
            self.trees_hit += 1
        else:
            self.safe_moves += 1

    def travel_through_map(self, toboggan_map):
        map_length = len(toboggan_map)
        for row in toboggan_map:
            if self.y_pos + self.y_move >= len(toboggan_map):
                break
            next_spot = self.take_next_move(toboggan_map[self.y_pos + 1])
            self.check_result(next_spot)


if __name__ == '__main__':
    input_file = os.path.join('inputs', 'input03.txt')
    toboggan_map = parse_map(input_file)
    total_trees_hit = []
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    for slope in slopes:
        sledder = Sledder(slope[0], slope[1])
        sledder.travel_through_map(toboggan_map)
        total_trees_hit.append(sledder.trees_hit)

    print(f"Part one solution: {total_trees_hit[1]}")

    product_trees_hit = functools.reduce((lambda x, y: x * y), total_trees_hit)
    print(f"Part two solution: {product_trees_hit}")
