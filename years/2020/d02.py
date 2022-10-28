import os.path


class Password:
    def __init__(self, limits, req_char, db_pw):
        self.low_val = int(limits.split('-')[0])
        self.high_val = int(limits.split('-')[1])
        self.req_char = req_char
        self.db_pw = db_pw
        self.rule_1_valid = self.check_rule_1()
        self.rule_2_valid = self.check_rule_2()

    def check_rule_1(self):
        char_count = self.db_pw.count(self.req_char)
        return self.low_val <= char_count <= self.high_val

    def check_rule_2(self):
        char_1 = self.db_pw[self.low_val - 1]
        char_2 = self.db_pw[self.high_val - 1]
        return (char_1 == self.req_char) ^ (char_2 == self.req_char)

def parse_password_database(database):
    db_passwords = []
    with open(database, 'r') as db:
        for line in db:
            line_parts = line.split()
            pw = Password(line_parts[0], line_parts[1][0], line_parts[2])
            db_passwords.append(pw)
    return db_passwords

def solutions(passwords):
    valid_passwords = {'rule 1': 0, 'rule 2': 0}
    for pw in passwords:
        if pw.rule_1_valid:
            valid_passwords['rule 1'] += 1
        if pw.rule_2_valid:
            valid_passwords['rule 2'] += 1
    return valid_passwords


if __name__ == '__main__':
    db_file = os.path.join('inputs', 'input02.txt')
    db_passwords = parse_password_database(db_file)
    counts = solutions(db_passwords)
    print(f"Part one solution: {counts['rule 1']}")
    print(f"Part two solution: {counts['rule 2']}")
