import os.path


def parse_expense_report(report):
    report_values = []
    with open(report, 'r') as r:
        for num in r:
            report_values.append(int(num))
    return report_values

def part_one_solution(report_values):
    for i1, v1 in enumerate(report_values):
        for v2 in report_values[i1 + 1:]:
            if v1 + v2 == 2020:
                return v1 * v2

def part_two_solution(report_values):
    for i1, v1 in enumerate(report_values):
        for i2, v2 in enumerate(report_values[i1 + 1:]):
            if v1 + v2 >= 2020:
                continue
            for v3 in report_values[i2 + 1:]:
                if sum((v1, v2, v3)) == 2020:
                    return v1 * v2 * v3


if __name__ == '__main__':
    expense_report = os.path.join('inputs', 'input01.txt')
    report_values = parse_expense_report(expense_report)
    print(f"Part one solution: {part_one_solution(report_values)}")
    print(f"Part two solution: {part_two_solution(report_values)}")
