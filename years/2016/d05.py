import hashlib
import os.path

test_door_id = 'abc'
with open(os.path.join('inputs', 'input05.txt'), 'r') as f:
    puzzle_door_id = f.readline().strip()

password = ['_' for _ in range(8)]
print(f"     Initialized: {password}")
i = 1

door_id = puzzle_door_id

def check_position(val):
    if not position.isnumeric():
        return False
    return int(val) < 8

while True:
    test_id = door_id + str(i)
    hashed = hashlib.md5(test_id.encode())
    hex_val = hashed.hexdigest()

    if hex_val[:5] == '00000':
        # print(hex_val)
        position = hex_val[5]
        if check_position(position) and password[int(position)] == '_':
            password[int(position)] = hex_val[6]
            print(f"Found a new item: {password}")

    i += 1
    if '_' not in password:
        break


print(''.join(password))
