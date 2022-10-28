import os.path


testing = False
day = '08'
if testing:
    f_input = os.path.join('inputs', f'{day}-test.txt')
else:
    f_input = os.path.join('inputs', f'input{day}.txt')


def part_one():
    display = {
        0: 6,
        1: 2,
        2: 5,
        3: 5,
        4: 4,
        5: 5,
        6: 6,
        7: 3,
        8: 7,
        9: 6
    }

    with open(f_input) as f:
        values = []
        for line in f:
            input_value, output_value = line.strip().split(' | ')
            values.append(
                {'input': input_value.strip().split(), 'output': output_value.strip().split()}
            )
    c = 0
    for value in values:
        for num in value['output']:
            if len(num) in (display[1], display[4], display[7], display[8]):
                c += 1
    print(c)

part_one()


def part_two():
    total = 0
    with open(f_input) as f:
        for line in f:
            old_input_values, old_output_values = line.strip().split(' | ')
            old_input_values = old_input_values.strip().split()
            old_output_values = old_output_values.strip().split()
            input_values = [''.join(sorted(x)) for x in old_input_values]
            output_values = [''.join(sorted(x)) for x in old_output_values]
            input_map = {i: None for i in range(10)}
            for val in input_values:
                if len(val) == 2:
                    input_map[1] = val
                elif len(val) == 4:
                    input_map[4] = val
                elif len(val) == 3:
                    input_map[7] = val
                elif len(val) == 7:
                    input_map[8] = val
            
            for i in input_map.values():
                if i in input_values:
                    input_values.remove(i)
            
            for val in input_values:
                if len(val) == 6:
                    if all([x in val for x in input_map[4]]):
                        input_map[9] = val
                    elif all([x in val for x in input_map[7]]):
                        input_map[0] = val
                    else:
                        input_map[6] = val

            for i in input_map.values():
                if i in input_values:
                    input_values.remove(i)

            for val in input_values:
                if len(val) == 5:
                    if all([x in val for x in input_map[1]]):
                        input_map[3] = val
                    elif all([x in input_map[9] for x in val]):
                        input_map[5] = val
                    else:
                        input_map[2] = val

            new_dict = {v:k for k,v in input_map.items()}
            num = ''.join(str(new_dict[k]) for k in output_values)
            total += int(num)
    print(total)

part_two()
