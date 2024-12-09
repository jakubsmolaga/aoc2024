import sys

disk_map = sys.stdin.read().strip()

disk = []

for i in range(0, len(disk_map), 2):
    file_id = str(i // 2)
    file_size = int(disk_map[i])
    for _ in range(file_size):
        disk.append(file_id)
    # disk += list(file_id * file_size)
    if i + 1 < len(disk_map):
        free_size = int(disk_map[i + 1])
        disk += list('.' * free_size)

l = 0
r = len(disk) - 1
while disk[l] != '.':
    l += 1
while disk[r] == '.':
    r -= 1
while l < r:
    disk[l] = disk[r]
    disk[r] = '.'
    while disk[l] != '.':
        l += 1
    while disk[r] == '.':
        r -= 1
while disk[len(disk) - 1] == '.':
    disk.pop()

checksum = 0

for i in range(len(disk)):
    checksum += i * int(disk[i])

print(checksum)

