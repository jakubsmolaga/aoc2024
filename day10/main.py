import sys

grid = [[int(x) for x in line] for line in sys.stdin.read().strip().split('\n')]
rows = len(grid)
cols = len(grid[0])

def get_score(y: int, x: int, visited: set[tuple[int, int]], unique_endpoints_only: bool) -> int:
    if unique_endpoints_only:
        if (y,x) in visited:
            return 0
        visited.add((y, x))
    if grid[y][x] == 9:
        return 1
    num = grid[y][x]
    score = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if abs(dy) + abs(dx) >= 2:
                continue
            yy = y + dy
            xx = x + dx
            if yy < 0 or yy >= rows:
                continue
            if xx < 0 or xx >= cols:
                continue
            if grid[yy][xx] != num + 1:
                continue
            score += get_score(yy, xx, visited, unique_endpoints_only)
    return score



result1 = 0
result2 = 0
for y in range(rows):
    for x in range(cols):
        if grid[y][x] != 0:
            continue
        result1 += get_score(y, x, set(), True)
        result2 += get_score(y, x, set(), False)

print(result1)
print(result2)

