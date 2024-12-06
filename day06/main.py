import sys

grid = [ list(line) for line in sys.stdin.read().strip().split('\n') ]
rows = len(grid)
cols = len(grid[0])

guard_y = -1
guard_x = -1

for row in range(rows):
    for col in range(cols):
        if grid[row][col] == '^':
            guard_y = row
            guard_x = col

start_x = guard_x
start_y = guard_y

grid[guard_y][guard_x] = '.'

move_y = -1
move_x = 0

visited = set[tuple[int, int]]()
visited.add((guard_x, guard_y))

while True:
    next_y = guard_y + move_y
    next_x = guard_x + move_x
    if next_y < 0 or next_y >= rows or next_x < 0 or next_x >= cols:
        break
    if grid[next_y][next_x] == '.':
        guard_y = next_y
        guard_x = next_x
        visited.add((guard_x, guard_y))
        continue
    # turn 90deg clockwise
    move_y, move_x = (move_x, -move_y)

print(len(visited))

def is_grid_looping(grid: list[list[str]], guard_x: int, guard_y: int) -> bool:
    move_y = -1
    move_x = 0

    seen_states = set[tuple[int, int, int, int]]()

    while True:
        next_y = guard_y + move_y
        next_x = guard_x + move_x
        if next_y < 0 or next_y >= rows or next_x < 0 or next_x >= cols:
            return False
        state = (guard_x, guard_y, move_x, move_y)
        if state in seen_states:
            return True
        seen_states.add(state)
        if grid[next_y][next_x] == '.':
            guard_y = next_y
            guard_x = next_x
            continue
        # turn 90deg clockwise
        move_y, move_x = (move_x, -move_y)

looped_count = 0
for x, y in visited:
    grid[y][x] = '#'
    if is_grid_looping(grid, start_x, start_y):
        looped_count += 1
    grid[y][x] = '.'

print(looped_count)
