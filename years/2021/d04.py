import os.path


testing = False
day = '04'
if testing:
    f_input = os.path.join('inputs', f'{day}-test.txt')
else:
    f_input = os.path.join('inputs', f'input{day}.txt')

class BingoNumber:
    def __init__(self, number):
        self.number = number
        self.called = False

    def __repr__(self):
        return self.number

    def __int__(self):
        return self.number

    def check_number(self, num):
        if self.number == num:
            self.called = True

class BingoBoard:
    def __init__(self, rows):
        self.grid = [[BingoNumber(x) for x in row] for row in rows]
        self.row_lookup = self._set_row_lookups(rows)
        self.board_total = sum(int(x) for row in self.grid for x in row)
    
    def __repr__(self):
        s = ''
        for row in self.grid:
            s += ' '.join(str(x.number) for x in row) + '\n'
        return s.strip()

    def _set_row_lookups(self, rows):
        d = dict()
        for i, v in enumerate(rows):
            row_d = {k: i for k in v}
            d.update(row_d)
        return d

    def call_number(self, num):
        row = self.row_lookup.get(int(num))
        if row is not None:
            self.board_total -= int(num)
            for bingo_num in self.grid[row]:
                bingo_num.check_number(num)

    def check_bingo(self):
        row_sums = [sum(e.called for e in row) for row in self.grid]
        row_bingo = 5 in row_sums
        if row_bingo:
            return True
        column_sums = [sum(row[i].called for row in self.grid) for i in range(len(self.grid))]
        column_bingo = 5 in column_sums
        if column_bingo:
            return True
        return False


def part_one():
    with open(f_input) as f:
        called_numbers = f.readline().split(',')
        called_numbers = [int(x) for x in called_numbers]
        f.readline()
        bingo_boards = []
        board = []
        for line in f:
            if not line.strip():
                bingo_boards.append(BingoBoard(board))
                board.clear()
            else:
                line = line.strip().replace('  ', ' ').replace(' ',',').split(',')
                line = [int(x) for x in line]
                board.append(line)
        bingo_boards.append(BingoBoard(board))

    for called_number in called_numbers:
        bingo = False
        for b in bingo_boards:
            b.call_number(called_number)
            if b.check_bingo():
                bingo = True
                ans = called_number * b.board_total
                break
        if bingo:
            break
    print(ans)

part_one()

def part_two():
    with open(f_input) as f:
        called_numbers = f.readline().split(',')
        called_numbers = [int(x) for x in called_numbers]
        f.readline()
        bingo_boards = []
        board = []
        for line in f:
            if not line.strip():
                bingo_boards.append(BingoBoard(board))
                board.clear()
            else:
                line = line.strip().replace('  ', ' ').replace(' ',',').split(',')
                line = [int(x) for x in line]
                board.append(line)
        bingo_boards.append(BingoBoard(board))

    for called_number in called_numbers:
        bingo_copy = bingo_boards[:]
        skip = False
        for b in bingo_copy:
            b.call_number(called_number)
            if b.check_bingo():
                if len(bingo_boards) == 1:
                    print(called_number * bingo_boards[0].board_total)
                    skip = True
                else:
                    bingo_boards.remove(b)
        if skip:
            break

part_two()
