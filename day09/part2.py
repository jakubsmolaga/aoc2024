import sys

disk_map = sys.stdin.read().strip()

files = []
spaces = []
pos = 0
for i in range(len(disk_map)):
    if i % 2 == 0:
        file_id = i // 2
        file_size = int(disk_map[i])
        files.append((pos, file_id, file_size))
        pos += file_size
    else:
        space_size = int(disk_map[i])
        spaces.append((pos, space_size))
        pos += space_size

updated_files = []

for pos, file_id, file_size in reversed(files):
    space_index = -1
    for i in range(len(spaces)):
        space_pos, space_size = spaces[i]
        if space_pos >= pos:
            break
        if space_size >= file_size:
            space_index = i
            break
    if space_index < 0:
        updated_files.append((pos, file_id, file_size))
        continue
    old_space_pos, old_space_size = spaces[space_index]
    new_space_pos, new_space_size = old_space_pos + file_size, old_space_size - file_size
    spaces[space_index] = (new_space_pos, new_space_size)
    updated_files.append((old_space_pos, file_id, file_size))

files = updated_files

files.sort()

checksum = 0
for pos, file_id, file_size in files:
    for i in range(pos, pos + file_size):
        checksum += i * file_id

print(checksum)

