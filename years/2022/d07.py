import os.path

testing = False
day = '07'
if testing:
    f_input = os.path.join('inputs', f'input{day}-test.txt')
else:
    f_input = os.path.join('inputs', f'input{day}.txt')

def part1(input):
    with open(input) as f:
        data = [line.strip().split() for line in f]

    # parse the data and create a dict called
    # `computer` which has folders and their
    # _local_ folder size
    computer = {}
    current_location = ''
    for line_num, line in enumerate(data):
        if line[0] == '$':
            # it's a command
            if line[1] == 'cd':
                # change directory
                if line[2] == '..':
                    # go back
                    if current_location.count('/') == 1:
                        # catches the case where the `else` logic
                        current_location = '/'
                    else:
                        # strip off the last folder
                        last_sep = current_location.rfind('/')
                        current_location = current_location[:last_sep]
                else:
                    # go into the directory
                    if line[2] == '/':
                        # go directly to the / folder
                        current_location = '/'
                    else:
                        if current_location == '/':
                            # don't double up on the / at the beginning
                            current_location += line[2]
                        else:
                            # regular append the folder to the location
                            current_location = current_location + '/' + line[2]
                # adds / folder to the computer info
                if current_location not in computer:
                    computer[current_location] = {
                        'folders': [],
                        'files': [],
                        'local_size': 0
                    }
            else:
                # it's ls
                continue
            pass
        else:
            # it's a file or directory
            if line[0] == 'dir':
                # it's a directory
                d_name = line[1]
                if current_location == '/':
                    # avoids double // at the beginning of the directory
                    full_path = current_location + d_name
                else:
                    full_path = current_location + '/' + d_name

                # put the listed directory into it's parent's info
                computer[current_location]['folders'].append(full_path)
                # adds the directory itself into the computer info
                if full_path not in computer:
                    computer[full_path] = {
                        'folders': [],
                        'files': [],
                        'local_size': 0
                    }
            else:
                # it's a file
                f_info = (int(line[0]), line[1])
                computer[current_location]['files'].append(f_info)
                computer[current_location]['local_size'] += f_info[0]
    # done parsing files/directories into the computer info

    # start accumulating the total size of a directory, including all
    # of the children, children's children, etc.
    total_folder_sizes = {}
    for k,v in computer.items():
        # iterating through computer info
        if k not in total_folder_sizes:
            total_folder_sizes[k] = v['local_size']
        # start with direct children
        subfolders = [x for x in v['folders']]
        while subfolders:
            subfolder = subfolders.pop()
            info = computer[subfolder]
            total_folder_sizes[k] += info['local_size']
            # add the child's children into the subfolders to calculate total size
            subfolders.extend(info['folders'])

    return sum(v for k,v in total_folder_sizes.items() if v <= 100000)

print(f'Part 1: {part1(f_input)}')



def part2(input):
    with open(input) as f:
        data = [line.strip().split() for line in f]

    # parse the data and create a dict called
    # `computer` which has folders and their
    # _local_ folder size
    computer = {}
    current_location = ''
    for line_num, line in enumerate(data):
        if line[0] == '$':
            # it's a command
            if line[1] == 'cd':
                # change directory
                if line[2] == '..':
                    # go back
                    if current_location.count('/') == 1:
                        # catches the case where the `else` logic
                        current_location = '/'
                    else:
                        # strip off the last folder
                        last_sep = current_location.rfind('/')
                        current_location = current_location[:last_sep]
                else:
                    # go into the directory
                    if line[2] == '/':
                        # go directly to the / folder
                        current_location = '/'
                    else:
                        if current_location == '/':
                            # don't double up on the / at the beginning
                            current_location += line[2]
                        else:
                            # regular append the folder to the location
                            current_location = current_location + '/' + line[2]
                # adds / folder to the computer info
                if current_location not in computer:
                    computer[current_location] = {
                        'folders': [],
                        'files': [],
                        'local_size': 0
                    }
            else:
                # it's ls
                continue
            pass
        else:
            # it's a file or directory
            if line[0] == 'dir':
                # it's a directory
                d_name = line[1]
                if current_location == '/':
                    # avoids double // at the beginning of the directory
                    full_path = current_location + d_name
                else:
                    full_path = current_location + '/' + d_name

                # put the listed directory into it's parent's info
                computer[current_location]['folders'].append(full_path)
                # adds the directory itself into the computer info
                if full_path not in computer:
                    computer[full_path] = {
                        'folders': [],
                        'files': [],
                        'local_size': 0
                    }
            else:
                # it's a file
                f_info = (int(line[0]), line[1])
                computer[current_location]['files'].append(f_info)
                computer[current_location]['local_size'] += f_info[0]
    # done parsing files/directories into the computer info

    # start accumulating the total size of a directory, including all
    # of the children, children's children, etc.
    total_folder_sizes = {}
    for k,v in computer.items():
        # iterating through computer info
        if k not in total_folder_sizes:
            total_folder_sizes[k] = v['local_size']
        # start with direct children
        subfolders = [x for x in v['folders']]
        while subfolders:
            subfolder = subfolders.pop()
            info = computer[subfolder]
            total_folder_sizes[k] += info['local_size']
            # add the child's children into the subfolders to calculate total size
            subfolders.extend(info['folders'])

    total_disk_space = 70000000
    space_needed_for_update = 30000000
    space_used = total_folder_sizes['/']
    unused_space = total_disk_space - space_used
    space_to_delete = space_needed_for_update - unused_space
    options = [v for k,v in total_folder_sizes.items() if v >= space_to_delete]

    return min(options)


print(f'Part 2: {part2(f_input)}')
