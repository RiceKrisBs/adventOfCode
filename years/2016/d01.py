import os.path

def parse_directions(directions):
    with open(directions, 'r') as d:
        line1 = d.readline().strip()
        dirs = line1.split(', ')
    return dirs

class Position:
    orientations = ('N', 'E', 'S', 'W')
    def __init__(self):
        self.orientation_index = 0
        self.x_cord = 0
        self.y_cord = 0
        self.visited = [(0, 0)]

    def parse_direction(self, d):
        return (d[0], int(d[1:]))

    def _get_orientation(self):
        return Position.orientations[self.orientation_index]

    def _get_current_position(self):
        return (self.x_cord, self.y_cord)

    def turn(self, side):
        if side == "R":
            self.orientation_index = (self.orientation_index + 1) % 4
        elif side == "L":
            self.orientation_index = (self.orientation_index - 1) % 4

    def move_part1(self, distance):
        if self._get_orientation() == 'N':
            self.y_cord += distance
        elif self._get_orientation() == 'S':
            self.y_cord -= distance
        elif self._get_orientation() == 'E':
            self.x_cord += distance
        elif self._get_orientation() == 'W':
            self.x_cord -= distance

    def move_part2(self, distance):
        if self._get_orientation() == 'N':
            for _ in range(distance):
                self.y_cord += 1
                stop = self.check_visited()
                if stop:
                    break
        elif self._get_orientation() == 'S':
            for _ in range(distance):
                self.y_cord -= 1
                stop = self.check_visited()
                if stop:
                    break
        elif self._get_orientation() == 'E':
            for _ in range(distance):
                self.x_cord += 1
                stop = self.check_visited()
                if stop:
                    break
        elif self._get_orientation() == 'W':
            for _ in range(distance):
                self.x_cord -= 1
                stop = self.check_visited()
                if stop:
                    break
        if stop:
            return True

    def check_visited(self):
        current_position = self._get_current_position()
        if current_position in self.visited:
            return True
        else:
            self.visited.append(current_position)
            return False


    def distance_from_start(self):
        return abs(self.x_cord) + abs(self.y_cord)

if __name__ == '__main__':
    directions_file = os.path.join('inputs', 'input01.txt')
    directions = parse_directions(directions_file)

    # part one
    elf1 = Position()
    for d in directions:
        side, distance = elf1.parse_direction(d)
        elf1.turn(side)
        elf1.move_part1(distance)
    print(f"Part one solution: {elf1.distance_from_start()}")

    # part two
    elf2 = Position()
    for d in directions:
        side, distance = elf2.parse_direction(d)
        elf2.turn(side)
        stop = elf2.move_part2(distance)
        if stop:
            break
    print(f"Part two solution: {elf2.distance_from_start()}")