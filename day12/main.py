import sys
import math

grid: list[str] = sys.stdin.read().strip().split('\n')
rows = len(grid)
cols = len(grid[0])

def get_area(x: int, y: int, plant: str, visited: set[tuple[int, int]]) -> int:
    if x < 0 or x >= cols:
        return 0
    if y < 0 or y >= rows:
        return 0
    if grid[y][x] != plant:
        return 0
    if (x, y) in visited:
        return 0
    visited.add((x, y))
    area = 1
    area += get_area(x - 1, y, plant, visited)
    area += get_area(x + 1, y, plant, visited)
    area += get_area(x, y - 1, plant, visited)
    area += get_area(x, y + 1, plant, visited)
    return area

def get_perimeter(x: int, y: int, plant: str, visited: set[tuple[int, int]]) -> int:
    if x < 0 or x >= cols:
        return 1
    if y < 0 or y >= rows:
        return 1
    if grid[y][x] != plant:
        return 1
    if (x, y) in visited:
        return 0
    visited.add((x, y))
    perimeter = 0
    perimeter += get_perimeter(x - 1, y, plant, visited)
    perimeter += get_perimeter(x + 1, y, plant, visited)
    perimeter += get_perimeter(x, y - 1, plant, visited)
    perimeter += get_perimeter(x, y + 1, plant, visited)
    return perimeter

def is_plant(x: int, y: int, plant: str) -> bool:
    if x < 0 or x >= cols:
        return False
    if y < 0 or y >= rows:
        return False
    if grid[y][x] != plant:
        return False
    return True

def count_corners(x: int, y: int, plant: str, visited: set[tuple[int, int]]) -> int:
    if not is_plant(x, y, plant):
        return 0
    if (x, y) in visited:
        return 0
    visited.add((x, y))
    corners = 0
    # out corners
    if (not is_plant(x - 1, y, plant)) and (not is_plant(x, y - 1, plant)):
        corners += 1
    if (not is_plant(x - 1, y, plant)) and (not is_plant(x, y + 1, plant)):
        corners += 1
    if (not is_plant(x + 1, y, plant)) and (not is_plant(x, y - 1, plant)):
        corners += 1
    if (not is_plant(x + 1, y, plant)) and (not is_plant(x, y + 1, plant)):
        corners += 1
    # in corners
    if is_plant(x - 1, y, plant) and is_plant(x, y - 1, plant) and (not is_plant(x - 1, y - 1, plant)):
        corners += 1
    if is_plant(x - 1, y, plant) and is_plant(x, y + 1, plant) and (not is_plant(x - 1, y + 1, plant)):
        corners += 1
    if is_plant(x + 1, y, plant) and is_plant(x, y - 1, plant) and (not is_plant(x + 1, y - 1, plant)):
        corners += 1
    if is_plant(x + 1, y, plant) and is_plant(x, y + 1, plant) and (not is_plant(x + 1, y + 1, plant)):
        corners += 1
    corners += count_corners(x - 1, y, plant, visited)
    corners += count_corners(x + 1, y, plant, visited)
    corners += count_corners(x, y - 1, plant, visited)
    corners += count_corners(x, y + 1, plant, visited)
    return corners

total_price = 0
total_discount_price = 0
visited = set[tuple[int, int]]()
for y in range(rows):
    for x in range(cols):
        if (x, y) in visited:
            continue
        area = get_area(x, y, grid[y][x], set())
        perimeter = get_perimeter(x, y, grid[y][x], visited)
        price = area * perimeter
        total_price += price
        corners = count_corners(x, y, grid[y][x], set())
        discount_price = area * corners
        total_discount_price += discount_price

print(total_price)
print(total_discount_price)

