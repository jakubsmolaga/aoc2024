import sys
import functools

nums = [ int(x) for x in sys.stdin.read().strip().split(' ')]

@functools.cache
def solve(stone: int, steps: int) -> int:
    if steps == 0:
        return 1
    if stone == 0:
        return solve(1, steps - 1)
    s = str(stone)
    if len(s) % 2 == 0:
        l = int(s[:len(s)//2])
        r = int(s[len(s)//2:])
        return solve(l, steps - 1) + solve(r, steps - 1)
    return solve(stone * 2024, steps - 1)

result1 = 0
result2 = 0
for num in nums:
    result1 += solve(num, 25)
    result2 += solve(num, 75)

print(result1)
print(result2)
