import os.path


def parse_captcha(file):
    values = []
    with open(file, 'r') as f:
        line = f.readline().strip()
    for char in line:
        values.append(int(char))
    values.append(values[0])
    return values


if __name__ == '__main__':
    input_file = os.path.join('inputs', 'input01.txt')
    captcha_values = parse_captcha(input_file)

    part_1_total = 0
    for i in range(len(captcha_values) - 1):
        if captcha_values[i] == captcha_values[i + 1]:
            part_1_total += captcha_values[i]
    print(f"Part one solution: {part_1_total}")

    part_2_total = 0
    captcha_values = captcha_values[:-1]
    offset = len(captcha_values) // 2
    for i in range(len(captcha_values)):
        target_index = i + offset
        if target_index >= (len(captcha_values)):
            target_index = target_index % (len(captcha_values))
        if captcha_values[i] == captcha_values[target_index]:
            part_2_total += captcha_values[i]
    print(f"Part two solution: {part_2_total}")
