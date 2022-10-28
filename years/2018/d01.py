import os.path


def parse_frequency_changes(file):
    frequency_changes = []
    with open(file, 'r') as f:
        for change in f:
            if change[0] == '+':
                frequency_changes.append(int(change[1:]))
            else:
                frequency_changes.append(int(change))
    return frequency_changes


if __name__ == '__main__':
    input_file = os.path.join('inputs', 'input01.txt')
    frequency_changes = parse_frequency_changes(input_file)
    print(f"Part one solution: {sum(frequency_changes)}")

    current_frequency, index = 0, 0
    past_frequencies = set()
    while current_frequency not in past_frequencies:
        past_frequencies.add(current_frequency)
        if index >= len(frequency_changes):
            index = index % len(frequency_changes)
        current_frequency += frequency_changes[index]
        index += 1
    print(f"Part two solution: {current_frequency}")
