import os.path


def parse_input(file):
    with open(file, 'r') as f:
        return [BoardingPass(line.strip()) for line in f]


class BoardingPass:
    def __init__(self, info: str):
        self.row_info: str = info[:7]
        self.column_info: str = info[7:]
        self.row_number: int = self._find_position(self.row_info)
        self.column_number: int = self._find_position(self.column_info)
        self.seat_id: int = self._calc_seat_id()

    def _find_position(self, sequence: str):
        binary = [0 if x in ('F', 'L') else 1 for x in sequence]
        l = len(binary)
        zipper = zip(range(l), range(l-1, -1, -1))
        return sum([binary[x] * 2 ** y for x, y in zipper])

    def _calc_seat_id(self):
        return self.row_number * 8 + self.column_number

def solve(x, y):
    return x * 8 + y


if __name__ == '__main__':
    input_file = os.path.join('inputs', 'input05.txt')
    boarding_passes = parse_input(input_file)

    seat_ids = set(x.seat_id for x in boarding_passes)
    print(f"Part one solution: {max(seat_ids)}")

    seat_exists = False
    combinations = ((x, y) for x in range(128) for y in range(8))
    for x, y in combinations:
        check = solve(x, y)
        if check in seat_ids:
            seat_exists = True
            continue
        if seat_exists and check not in seat_ids:
            print(f"Part two solution: {check}")
            break
