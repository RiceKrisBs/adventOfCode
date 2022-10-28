import os.path

def parse_directions(directions):
    values = []
    with open(directions, 'r') as d:
        for value in d:
            values.append(value)
    return values[0]

def part_one_solution(directions):
    return directions.count('(') - directions.count(')')

def part_two_solution(directions):
    total = 0
    for floor, direction in enumerate(directions, start=1):
        if direction == '(':
            total += 1
        else:
            total -= 1

        if total < 0:
            return floor


if __name__ == '__main__':
    directions = os.path.join('inputs', 'input01.txt')
    values = parse_directions(directions)
    print(f"Part one solution: {part_one_solution(values)}")
    print(f"Part two solution: {part_two_solution(values)}")
