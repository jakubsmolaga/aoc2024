import sys

grid = sys.stdin.read().strip().split('\n')
rows = len(grid)
cols = len(grid[0])

antennas = dict[str, list[tuple[int, int]]]()
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == '.':
            continue
        freq = grid[row][col]
        pos = (row, col)
        if freq not in antennas:
            antennas[freq] = []
        antennas[freq].append(pos)

antinodes = set[tuple[int, int]]()

for freq in antennas:
    positions = antennas[freq]
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            y1, x1 = positions[i]
            y2, x2 = positions[j]
            dy = y2 - y1
            dx = x2 - x1
            antinode1 = (y2 + dy, x2 + dx)
            antinode2 = (y1 - dy, x1 - dx)
            antinodes.add(antinode1)
            antinodes.add(antinode2)

valid_antinodes: list[tuple[int, int]] = []
for y, x in antinodes:
    if y < 0 or y >= rows:
        continue
    if x < 0 or x >= cols:
        continue
    valid_antinodes.append((y, x))

print(len(valid_antinodes))
    

antinodes = set[tuple[int, int]]()

for freq in antennas:
    positions = antennas[freq]
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            y1, x1 = positions[i]
            y2, x2 = positions[j]
            dy = y2 - y1
            dx = x2 - x1
            y, x = y2, x2
            while y >= 0 and y < rows and x >= 0 and x < cols:
                antinodes.add((y, x))
                y += dy
                x += dx
            y, x = y1, x1
            while y >= 0 and y < rows and x >= 0 and x < cols:
                antinodes.add((y, x))
                y -= dy
                x -= dx

print(len(antinodes))
