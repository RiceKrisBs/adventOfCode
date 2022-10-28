from copy import copy
import os.path


def parse_input(file):
    passports = []
    with open(file, 'r') as f:
        passport = []
        for line in f:
            line = line.strip()
            if line == '':
                temp = copy(passport)
                passports.append(' '.join(temp))
                passport.clear()
                continue
            passport.append(line)
        # add last passport into list
        temp = copy(passport)
        passports.append(' '.join(temp))
        passport.clear()

    d_passport = {}
    for i in range(len(passports)):
        passports[i] = passports[i].split()
        for field in passports[i]:
            split_entry = field.split(':')
            d_passport[split_entry[0]] = split_entry[1]
        temp_passport = copy(d_passport)
        passports[i] = temp_passport
        d_passport.clear()
    return passports

def determine_candidate(d):
    if len(d) == 8:
        return True
    elif (len(d) == 7) and ('cid' not in d):
        return True
    return False

def validate_byr(byr):
    try:
        byr = int(byr)
        return 1920 <= byr <= 2002
    except:
        return False

def validate_iyr(iyr):
    try:
        iyr = int(iyr)
        return 2010 <= iyr <= 2020
    except:
        return False

def validate_eyr(eyr):
    try:
        eyr = int(eyr)
        return 2020 <= eyr <= 2030
    except:
        return False

def validate_hgt(hgt):
    ending = hgt[-2:]
    if ending == 'cm':
        try:
            cm = int(hgt[:-2])
            return 150 <= cm <= 193
        except:
            return False
    elif ending == 'in':
        try:
            inches = int(hgt[:-2])
            return 59 <= inches <= 76
        except:
            return False
    return False

def validate_hcl(hcl):
    valid_chars = '0123456789abcdef'
    if hcl[0] == '#' and len(hcl[1:]) == 6:
        return all(x in valid_chars for x in hcl[1:])
    return False

def validate_ecl(ecl):
    valid_colors = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    return ecl in valid_colors

def validate_pid(pid):
    valid_chars = '0123456789'
    if len(pid) == 9:
        return all (x in valid_chars for x in pid)
    return False

def validate_candidate(passport):
    return all(
        (validate_byr(passport['byr']),
         validate_iyr(passport['iyr']),
         validate_eyr(passport['eyr']),
         validate_hgt(passport['hgt']),
         validate_hcl(passport['hcl']),
         validate_ecl(passport['ecl']),
         validate_pid(passport['pid']),
         )
    )


if __name__ == '__main__':
    input_file = os.path.join('inputs', 'input04.txt')
    passports = parse_input(input_file)

    valid_candidates, valid_passports = 0, 0
    for p in passports:
        check = determine_candidate(p)
        valid_candidates += int(check)
        if check:
            # print(p)
            valid_passports += int(validate_candidate(p))

    print(f"Part one solution: {valid_candidates}")
    print(f"Part two solution: {valid_passports}")
