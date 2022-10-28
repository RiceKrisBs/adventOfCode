import collections
import os.path
import re


class Room:
    def __init__(self, code):
        self.orig_encrypted_name = self._set_encrypted_name(code)
        self.encrypted_name = self.orig_encrypted_name.replace('-', '')
        self.sector_id = self._set_sector_id(code)
        self.checksum = self._set_checksum(code)
        self.real_room_name = self._decrypt_room_name(self.orig_encrypted_name)
        self.is_room_real = self.detect_fakes()

    def _set_encrypted_name(self, code):
        p = re.compile(r'([a-z]+|-)+')
        m = p.match(code)
        return m.group()[:-1]

    def _set_sector_id(self, code):
        p = re.compile(r'\d+')
        m = re.findall(p, code)
        return int(m[0])

    def _set_checksum(self, code):
        p = re.compile(r'.*?\[(.*)\]')
        m = re.search(p, code)
        return m.group(1)

    def detect_fakes(self):
        # get a counter for the pre-sorted encrypted name
        count = collections.Counter(''.join(sorted(list(self.encrypted_name))))
        encrypted_counter = count.most_common(len(count))

        # get a counter for the values in checksum
        checker = [(c, count[c]) for c in self.checksum]
        return encrypted_counter[:5] == checker

    def _decrypt_room_name(self, encrypted):
        decrypted = ''
        for c in encrypted:
            if c == '-':
                decrypted += ' '
            else:
                i = ord(c) + self.sector_id
                while i > 122:
                    i -= 26
                decrypted += chr(i)
        return decrypted


trials = (
    'aaaaa-bbb-z-y-x-123[abxyz]',
    'a-b-c-d-e-f-g-h-987[abcde]',
    'not-a-real-room-404[oarel]',
    'totally-real-room-200[decoy]',
    'qzmt-zixmtkozy-ivhz-343[abcde]'
)

# id_sums = 0
# for line in trials:
#     room = Room(line.strip())
#     print(room.orig_encrypted_name)
#     print(room.encrypted_name)
#     print('-'*10)
#     if room.is_room_real:
#         id_sums += room.sector_id


with open(os.path.join('inputs', 'input04.txt'), 'r') as f:
    id_sums = 0
    for line in f:
        room = Room(line.strip())
        if room.is_room_real and 'north' in room.real_room_name:
            print(f"{room.real_room_name} | sector_id: {room.sector_id}")
