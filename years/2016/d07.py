import os.path

f = [
    'aba[bab]xyz',
    'xyx[xyx]xyx',
    'aaa[kek]eke',
    'zazbz[bzb]cdb'
]


def split_string(s):
    s += '['
    bracket_positions = [0]
    d = {
        'outside': [],
        'inside': []
    }
    for i, c in enumerate(s):
        if c not in ('[', ']'):
            continue
        
        # even means '['
        if len(bracket_positions) % 2:
            d['outside'].append(s[bracket_positions[-1]:i].replace(']',''))
        else:
            d['inside'].append(s[bracket_positions[-1]:i].replace('[',''))
        bracket_positions.append(i)
    return d


def has_aba(s):
    options = []
    if len(s) < 3:
        return options
    for i in range(len(s)-2):
        phrase = s[i:i+3]
        if phrase.count(phrase[0]) == 3:
            continue
        if phrase == phrase[::-1]:
            options.append(phrase)
    return options

def has_bab(s, aba):
    if len(s) < 3:
        return False
    for i in range(len(s)-2):
        phrase = s[i:i+3]
        if phrase.count(phrase[0]) == 3:
            continue
        target = aba[1]+aba[0]+aba[1]
        if phrase == target:
            return True
    return False


support_count = 0


with open(os.path.join('inputs', 'input07.txt'), 'r') as f:
    for line in f:
        count_it = False
        phrases = split_string(line.strip())
        insides = []
        for phrase in phrases['inside']:
            x = has_aba(phrase)
            insides.extend(x)
        for phrase in phrases['outside']:
            for x in insides:
                if has_bab(phrase, x):
                    count_it = True
                    break
            if count_it:
                break
        support_count += int(count_it)

if False:
    for line in f:
        count_it = False
        phrases = split_string(line.strip())
        insides = []
        for phrase in phrases['inside']:
            x = has_aba(phrase)
            insides.extend(x)
        for phrase in phrases['outside']:
            for x in insides:
                if has_bab(phrase, x):
                    count_it = True
                    break
            if count_it:
                break
        support_count += int(count_it)



print(support_count)
