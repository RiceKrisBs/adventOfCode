import os.path
from collections import deque

testing = False
day = '11'
if not day:
    raise OSError('Set the day!')

if testing:
    f_input = os.path.join('inputs', f'input{day}-test.txt')
else:
    f_input = os.path.join('inputs', f'input{day}.txt')

def part1(input):
    with open(input) as f:
        contents = f.read().strip()
    data = contents.split('\n\n')
    monkeys = {}
    for chunk in data:
        monkey = [line.strip() for line in chunk.split('\n')]
        monkey_num = int(monkey[0][:-1].split()[-1])
        items = list(map(int, monkey[1].replace(',', '').split('Starting items: ')[1].split()))
        # need to set tmp and operation like this to avoid namespace/scoping issues
        tmp = monkey[2].split(' = ')[1]
        operation = lambda old, tmp=tmp: eval(tmp)
        div_test = int(monkey[3].split('by ')[1])
        div_true = int(monkey[4].split('monkey ')[1])
        div_false = int(monkey[5].split('monkey ')[1])
        monkeys[monkey_num] = {
            'items': deque(items),
            'operation': operation,
            'div_test': div_test,
            'div_true': div_true,
            'div_false': div_false
        }

    inspected_items = [0 for _ in range(len(monkeys))]

    rounds = 20
    for round in range(rounds):
        # if round == 1: break # temp to inspect
        for m_num, m_dict in monkeys.items():
            # print(f'Monkey {m_num}')
            while m_dict['items']:
                inspected_items[m_num] += 1
                worry = m_dict['items'].popleft()
                # print(f'  Monkey inspects an item with a worry level of {worry}')
                worry = m_dict['operation'](worry)
                # print(f'    Worry level is set to {worry}')
                worry = worry // 3
                # print(f'    Monkey gets board. Worry is set to {worry}')
                if worry % m_dict['div_test']:
                    target_monkey = m_dict['div_false']
                else:
                    target_monkey = m_dict['div_true']
                # print(f'    Item with worry level {worry} is thrown to monkey {target_monkey}')
                monkeys[target_monkey]['items'].append(worry)

    # for k, v in monkeys.items():
    #     print(k, v)
    inspected_items.sort()
    return inspected_items[-1] * inspected_items[-2]

p1_ans = part1(f_input)
print(f'Part 1: {p1_ans}')



def part2(input):
    with open(input) as f:
        contents = f.read().strip()
    data = contents.split('\n\n')
    monkeys = {}
    for chunk in data:
        monkey = [line.strip() for line in chunk.split('\n')]
        monkey_num = int(monkey[0][:-1].split()[-1])
        items = list(map(int, monkey[1].replace(',', '').split('Starting items: ')[1].split()))
        # need to set tmp and operation like this to avoid namespace/scoping issues
        tmp = monkey[2].split(' = ')[1]
        operation = lambda old, tmp=tmp: eval(tmp)
        div_test = int(monkey[3].split('by ')[1])
        div_true = int(monkey[4].split('monkey ')[1])
        div_false = int(monkey[5].split('monkey ')[1])
        monkeys[monkey_num] = {
            'items': deque(items),
            'operation': operation,
            'div_test': div_test,
            'div_true': div_true,
            'div_false': div_false
        }

    maybe = [monkeys[i]['div_test'] for i in range(len(monkeys))]
    divisor = 1
    for num in maybe:
        divisor *= num

    inspected_items = [0 for _ in range(len(monkeys))]

    rounds = 10000
    for round in range(rounds):
        # if round == 1: break # temp to inspect
        for m_num, m_dict in monkeys.items():
            # print(f'Monkey {m_num}')
            while m_dict['items']:
                inspected_items[m_num] += 1
                worry = m_dict['items'].popleft()
                # print(f'  Monkey inspects an item with a worry level of {worry}')
                worry = m_dict['operation'](worry)
                # print(f'    Worry level is set to {worry}')
                # worry = worry // 3
                worry = worry % divisor
                # print(f'    Monkey gets board. Worry is set to {worry}')
                if worry % m_dict['div_test']:
                    target_monkey = m_dict['div_false']
                else:
                    target_monkey = m_dict['div_true']
                # print(f'    Item with worry level {worry} is thrown to monkey {target_monkey}')
                monkeys[target_monkey]['items'].append(worry)

    # for k, v in monkeys.items():
    #     print(k, v)
    inspected_items.sort()
    return inspected_items[-1] * inspected_items[-2]

p2_ans = part2(f_input)
print(f'Part 2: {p2_ans}')
