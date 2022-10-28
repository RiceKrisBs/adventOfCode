import copy
import os.path


def parse_input(file):
    intcodes = []
    with open(file, 'r') as f:
        line = f.readline().split(',')
    return [int(i) for i in line]

def opcode_1(intcode, pos_x, pos_y, pos_sum):
    intcode[pos_sum] = intcode[pos_x] + intcode[pos_y]

def opcode_2(intcode, pos_x, pos_y, pos_prod):
    intcode[pos_prod] = intcode[pos_x] * intcode[pos_y]

def insert_arguments(intcode, noun, verb):
    intcode[1] = noun
    intcode[2] = verb

def solve(intcode):
    for i in range(0, len(intcode), 4):
        if intcode[i] == 99:
            break
        if intcode[i] == 1:
            opcode_1(intcode, intcode[i+1], intcode[i+2], intcode[i+3])
        if intcode[i] == 2:
            opcode_2(intcode, intcode[i+1], intcode[i+2], intcode[i+3])
    return intcode[0]


if __name__ == '__main__':
    input_file = os.path.join('inputs', 'input02.txt')
    intcodes = parse_input(input_file)

    part_1_intcodes = copy.copy(intcodes)
    insert_arguments(part_1_intcodes, 12, 2)
    part_1_answer = solve(part_1_intcodes)
    print(f"Part one solution: {part_1_answer}")

    target = 19690720
    combinations = ((x, y) for x in range(100) for y in range(100))
    for noun, verb in combinations:
        part_2_intcodes = copy.copy(intcodes)
        insert_arguments(part_2_intcodes, noun, verb)
        output = solve(part_2_intcodes)
        if output == target:
            break
    part_2_answer = 100 * noun + verb
    print(f"Part two solution: {part_2_answer}")
