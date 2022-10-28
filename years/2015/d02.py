import os.path

def parse_input(file):
    with open(file, 'r') as f:
        return [Box(line.strip()) for line in f]


class Box:
    def __init__(self, input):
        dims = input.split('x')
        self.l = int(dims[0])
        self.w = int(dims[1])
        self.h = int(dims[2])
        self.sides = sorted([self.l, self.w, self.h])
        self.box_paper = self._calc_paper()
        self.box_ribbon = self._calc_ribbon()

    def _calc_paper(self):
        paper_for_sides = ((2 * self.l * self.w)
                          + (2 * self.l * self.h)
                          + (2 * self.w * self.h))
        slack = self.sides[0] * self.sides[1]
        return paper_for_sides + slack

    def _calc_ribbon(self):
        ribbon_wrapping = (2 * self.sides[0]) + (2 * self.sides[1])
        ribbon_bow = self.l * self.w * self.h
        return ribbon_wrapping + ribbon_bow



if __name__ == '__main__':
    input_file = os.path.join('inputs', 'input02.txt')
    boxes = parse_input(input_file)

    total_paper, total_ribbon = 0, 0
    for box in boxes:
        total_paper += box.box_paper
        total_ribbon += box.box_ribbon

    print(f"Part one solution: {total_paper}")
    print(f"Part two solution: {total_ribbon}")
