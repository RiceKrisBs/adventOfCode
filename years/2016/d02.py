import os.path

instructions = []

with open(os.path.join('inputs', 'input02.txt'), 'r') as f:
    for line in f:
        instructions.append(line.strip())

class Position:
    def __init__(self):
        self.x = -2
        self.y = 0

    def move_position(self, dir):
        if dir == 'R':
            if abs(self.y) == 2 or (self.x == 1 and abs(self.y) == 1) or self.x == 2:
                pass
            else:
                self.x += 1
        elif dir == 'L':
            if abs(self.y) == 2 or (self.x == -1 and abs(self.y) == 1) or self.x == -2:
                pass
            else:
                self.x -= 1
        elif dir == 'U':
            if abs(self.x) == 2 or (self.y == 1 and abs(self.x) == 1) or self.y == 2:
                pass
            else:
                self.y += 1
        elif dir == 'D':
            if abs(self.x) == 2 or (self.y == -1 and abs(self.x) == 1) or self.y == -2:
                pass
            else:
                self.y -= 1

    def give_keypad_num(self):
        if self.x == -2:
            return 5
        if self.x == -1:
            if self.y == 1:
                return 2
            if self.y == 0:
                return 6
            return 'A'
        if self.x == 0:
            if self.y == 2:
                return 1
            if self.y == 1:
                return 3
            if self.y == 0:
                return 7
            if self.y == -1:
                return 'B'
            return 'D'
        if self.x == 1:
            if self.y == 1:
                return 4
            if self.y == 0:
                return 8
            return 'C'
        return 9

pos = Position()

for keypad_num in instructions:
    for d in keypad_num:
        pos.move_position(d)
    print(pos.give_keypad_num(),end='')
