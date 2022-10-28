import os.path


def parse_input(file):
    values = []
    with open(file, 'r') as f:
        for value in f:
            values.append(int(value))
    return values

def calc_fuel_requirement(mass):
    return (mass // 3) - 2

if __name__ == '__main__':
    input_file = os.path.join('inputs', 'input01.txt')
    values = parse_input(input_file)
    fuel_for_gifts = 0
    fuel_for_fuel = 0

    for mass in values:
        fuel_for_mass = calc_fuel_requirement(mass)
        fuel_for_gifts += fuel_for_mass
        extra_fuel = calc_fuel_requirement(fuel_for_mass)
        while extra_fuel >= 0:
            fuel_for_fuel += extra_fuel
            extra_fuel = calc_fuel_requirement(extra_fuel)
    print(f"Part one solution: {fuel_for_gifts}")
    print(f"Part two solution: {fuel_for_gifts + fuel_for_fuel}")
